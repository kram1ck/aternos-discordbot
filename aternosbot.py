import discord
import sl_commands
import sys
import os
from loguru import logger
from exceptions import NoAnyRoleAttribute



class Aternos(discord.Client):
    driver = sl_commands.get_driver()
    SERVER_IP = ''
    SERVER_VERSION = ''
    _CONFIGS = sl_commands.get_configs()
    _SERVER_NUMBER = _CONFIGS['SERVER_NUMBER']
    _AUTH_NAME = _CONFIGS['AUTH_NAME']
    _AUTH_PASSWORD = _CONFIGS['AUTH_PASSWORD']
    _EXPECT_ROLE_NAME = _CONFIGS['ROLE_NAME']
    _EXPECT_ROLE_ID = _CONFIGS['ROLE_ID']

    if not _EXPECT_ROLE_ID and not _EXPECT_ROLE_NAME:
        logger.critical('Raise the exception...')
        raise NoAnyRoleAttribute


    async def on_ready(self):
        sl_commands.select_server(self.driver, auth_name=self._AUTH_NAME, auth_pass=self._AUTH_PASSWORD, server_num=self._SERVER_NUMBER)

        self.SERVER_IP = await sl_commands.get_ip(self.driver)
        self.SERVER_VERSION = await sl_commands.get_version(self.driver)

        logger.info(f'{self.user} Bot has authorized and is ready!')
        logger.info(f'Current server: {self.SERVER_IP}')


    async def on_message(self, message):
        if message.author == self.user:
                return

        has_role = False
        roles = message.author.roles

        """If user has not needed role, bot will not perform command"""
        for role in roles:
            if role.id == int(self._EXPECT_ROLE_ID) or role.name == str(self._EXPECT_ROLE_NAME):
                has_role = True
                break
        
        # return if user has no role
        if not has_role:
            return
        
        logger.info(f'User {message.author} tried to run command {message.content}')

        sl_commands.go_over_block(self.driver)
        status = await sl_commands.get_status(self.driver)


        if message.content.startswith('.запус') or message.content.startswith('.откр'):
            if status.startswith("Оффл"):
                await message.channel.send('🎉 Запускаю сервер для вас...')
                await sl_commands.launch_server(self.driver)

                await message.channel.send('⏳ Сервер готовится к запуску! Ждём его загрузки...')
                await sl_commands.timer(self.driver)

                await message.reply('✅ Сервер запущен и готов к работе!')
            else:
                logger.error(f'Пользователь не смог запустить сервер\nСтатус сервера был: {status}')
                await message.channel.send(f'❌ Извините, в данный момент статус сервера **{status.lower()}**.\nВы не можете его запустить!')


        if message.content.startswith('.закр'):
            if status.startswith("Онла"):
                await message.channel.send('😞 Уже уходите? Как жаль. Закрываю сервер...')
                await sl_commands.stop_server(self.driver)

                await sl_commands.timer(self.driver, condition="Оффлайн")

                await message.reply('✅ Сервер успешно отключен!')
            else:
                logger.error(f'Пользователь не смог закрыть сервер\nСтатус сервера был: {status}')
                await message.channel.send(f'❌ Извините, в данный момент статус сервера **{status.lower()}**.\nВы не можете его закрыть!')


        if message.content.startswith('.статус'):
            left_time = await sl_commands.get_left_time(self.driver)
            if status.startswith('Онла') and left_time:
                await message.reply(f'✨ Статус сервера: {status.lower()}!\n🕒 Времени до закрытия: {left_time}')
                return
            await message.reply(f'Статус сервера: {status.lower()}!')


        if message.content.startswith('.инфо'):
            players = await sl_commands.get_players(self.driver)
            tps = await sl_commands.get_tps(self.driver)

            await message.channel.send(f'**Информация о выбранном сервере:**\n\n✨ Статус Сервера: {status}\n👥 Игроков на Сервере: {players}\n⏲ TPS Сервера: {tps}\n💎 IP Сервера: {self.SERVER_IP}\n🎫 Версия Сервера: {self.SERVER_VERSION}')


        if message.content.startswith('.хелп') or message.content.startswith('.помо'):
            await message.reply(f'**Вот какие команды ты можешь использовать:**\n\n.запуск / .запусти / .запустить --> Запустить сервер\n.закрой / .закрыть --> Закрыть сервер\n.статус --> Получить статус и время до закрытия сервера\n.инфо --> Получить информацию о сервере\n.хелп / .помощь / .помоги --> Получить полный список доступных команд.')


        if message.content.startswith('.cl'):
            """Close the driver if it needs"""
            self.driver.close()
            sys.exit()


if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True

    TOKEN = str(os.getenv('BOT_TOKEN'))

    bot = Aternos(intents=intents)
    bot.run(token=TOKEN)
