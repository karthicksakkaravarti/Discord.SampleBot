import logging
import sys

import discord
from django.core.management import BaseCommand
from bot.bot import BasicCommandBot
from bot.cogs.SimpleCog import SimpleCog
from simplebot.settings.base import DISCORD_TOKEN_SIMPLE


def get_logger():
    logger = logging.getLogger('')
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


logger = get_logger()


class Command(BaseCommand):
    def handle(self, *args, **options):
        logger.info('Starting Simple Discord Bot ...')
        intents = discord.Intents(messages=True, guilds=True, members=True)
        bot = BasicCommandBot(command_prefix='!simplebot ', intents=intents, description='SimpleBot to showcase how bot works!',logger=logger)
        bot.add_cog(SimpleCog(bot, logger=logger))
        bot.run(DISCORD_TOKEN_SIMPLE)


