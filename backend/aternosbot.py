import sys
import asyncio

import discord
from loguru import logger

import backend.control as control
from backend.configs_control import get_configs
from backend.exceptions import NoAnyRoleAttribute



class Aternos(discord.Client):
    _CONFIGS = get_configs()
    _SERVER_NUMBER = _CONFIGS['SERVER_NUMBER']
    _AUTH_NAME = _CONFIGS['AUTH_NAME']
    _AUTH_PASSWORD = _CONFIGS['AUTH_PASSWORD']
    _EXPECT_ROLE_NAME = _CONFIGS['ROLE_NAME']
    _EXPECT_ROLE_ID = _CONFIGS['ROLE_ID']
    if _CONFIGS['HEADLESS_MODE'] == "False" or not _CONFIGS['HEADLESS_MODE']:
        _IS_HEADLESS = False
    else:
        _IS_HEADLESS = True


    SERVER_IP = ''
    SERVER_VERSION = ''
    driver = control.get_driver(headless=_IS_HEADLESS)

    if not _EXPECT_ROLE_ID and not _EXPECT_ROLE_NAME:
        logger.critical('Raise the exception...')
        raise NoAnyRoleAttribute


    async def on_ready(self):
        control.select_server(self.driver, auth_name=self._AUTH_NAME, auth_pass=self._AUTH_PASSWORD, server_num=self._SERVER_NUMBER)

        self.SERVER_IP = await control.get_ip(self.driver)
        self.SERVER_VERSION = await control.get_version(self.driver)

        logger.info(f'{self.user} Bot has authorized and is ready!')
        logger.info(f'Current server: {self.SERVER_IP}')


    async def on_message(self, message):

        if message.author == self.user:
                return

        has_role = False
        roles = message.author.roles

        # If user has not needed role, bot will not perform command
        for role in roles:
            if role.id == int(self._EXPECT_ROLE_ID) or role.name == str(self._EXPECT_ROLE_NAME):
                has_role = True
                break
        
        # return if user has no role
        if not has_role:
            return
        

        if message.content.startswith('.'):
            self.driver.refresh()

            logger.info(f'User {message.author} tried to run command {message.content}')
            control.go_over_block(self.driver)
            status = await control.get_status(self.driver)


        if message.content.startswith('.запус') or message.content.startswith('.откр'):
            if status.startswith("Оффл") or status.startswith("Оши"):
                await message.channel.send('🎉 Запускаю сервер для вас...')
                await control.launch_server(self.driver)

                await message.channel.send('⏳ Сервер готовится к запуску! Ждём его загрузки...')
                await control.timer(self.driver)

                await message.reply('✅ Сервер запущен и готов к работе!')
                logger.info(f'Server was successful launched by user {message.author}')
            else:
                logger.error(f'User could not start server\nStatus was: {status}')
                await message.channel.send(f'❌ Извините, в данный момент статус сервера **{status.lower()}**.\nВы не можете его запустить!')


        elif message.content.startswith('.закр'):
            if status.startswith("Онла"):
                await message.channel.send('😞 Уже уходите? Как жаль. Закрываю сервер...')
                await control.stop_server(self.driver)

                await control.timer(self.driver, condition="Оффлайн")

                await message.reply('✅ Сервер успешно отключен!')
                logger.info(f'Server was successful closed by user {message.author}')
            else:
                logger.error(f'User could not stop server\nStatus was: {status}')
                await message.channel.send(f'❌ Извините, в данный момент статус сервера **{status.lower()}**.\nВы не можете его закрыть!')

        
        elif message.content.startswith('.перез'):
            if status.startswith('Онла'):
                await message.channel.send('🔄 Перезагружаю сервер...')
                await control.restart_server(self.driver)

                await control.timer(self.driver)

                await message.reply('✅ Сервер успешно перезагружен!')
                logger.info(f'Server was successful restarted by used {message.author}')
            else:
                logger.error(f'User could not restart server\nStatus was: {status}')
                await message.channel.send(f'❌ Извините, в данный момент статус сервера **{status.lower()}**.\nВы не можете его перезапустить!')


        elif message.content.startswith('.статус'):
            left_time = await control.get_left_time(self.driver)
            if status.startswith('Онла') and left_time:
                await message.reply(f'✨ Статус сервера: {status.lower()}!\n🕒 Времени до закрытия: {left_time}')
                return
            await message.reply(f'Статус сервера: {status.lower()}!')


        elif message.content.startswith('.инфо'):
            players = await control.get_players(self.driver)
            tps = await control.get_tps(self.driver)

            await message.channel.send(f'**Информация о выбранном сервере:**\n\n✨ Статус Сервера: {status}\n👥 Игроков на Сервере: {players}\n⏲ TPS Сервера: {tps}\n💎 IP Сервера: {self.SERVER_IP}\n🎫 Версия Сервера: {self.SERVER_VERSION}')


        elif message.content.startswith('.хелп') or message.content.startswith('.помо'):
            await message.reply(f'**Вот какие команды ты можешь использовать:**\n\n.запуск / .запусти / .запустить --> Запустить сервер\n.закрой / .закрыть --> Закрыть сервер\n.статус --> Получить статус и время до закрытия сервера\n.инфо --> Получить информацию о сервере\n.хелп / .помощь / .помоги --> Получить полный список доступных команд.')


        elif message.content.startswith('.cl'):
            """Close the driver if it needs"""
            self.driver.close()
            sys.exit()