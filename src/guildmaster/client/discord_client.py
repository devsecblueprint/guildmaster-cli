import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")


class DiscordClient:
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        self.bot = commands.Bot(command_prefix="!", intents=intents)

    def run(self):
        self.bot.run(TOKEN)

    def close(self):
        self.bot.close()
