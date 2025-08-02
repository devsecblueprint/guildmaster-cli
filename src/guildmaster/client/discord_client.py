"""
# guildmaster.client.discord_client
A module for managing the Discord client connection.
This module provides functionality to connect to Discord using a bot token.
"""
import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")


class DiscordClient:
    """
    A class for managing the Discord client connection.
    """
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        self.bot = commands.Bot(command_prefix="!", intents=intents)

    def run(self):
        """
        Run the Discord bot using the provided token.
        """
        self.bot.run(TOKEN)

    def close(self):
        """
        Close the Discord bot connection.
        """
        self.bot.close()
