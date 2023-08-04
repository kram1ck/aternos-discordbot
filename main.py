import os

import discord
from loguru import logger

from backend.configs_control import get_configs
from backend.aternosbot import Aternos
from backend.exceptions import NoAnyTokenFound


if __name__ == "__main__":
    TOKEN = os.getenv('BOT_TOKEN')
    
    if not TOKEN:
        logger.debug('BOT_TOKEN was not found in environment. Trying to get it from configs...')
        try:
            configs = get_configs()
            TOKEN = configs['BOT_TOKEN']
        except:
            raise NoAnyTokenFound

    intents = discord.Intents.default()
    intents.message_content = True

    bot = Aternos(intents=intents)
    bot.run(token=TOKEN)
