"""
# guildmaster.tasks.role_manager
A module for managing roles in a Discord server.
This module provides functionality to assign a specific role to all members of a Discord server.
"""

import asyncio
import discord
from tqdm.asyncio import tqdm

from config.logger import Logger
from client.discord_client import DiscordClient


class DiscordRoleManager:
    """
    A class for managing a role to every member in a Discord server.
    """

    def __init__(self):
        self.logger = Logger.setup_logger(__name__)

    def assign_to_all(self, guild: int, role: str, delay: float = 3.0):
        """
        Assign a role to every member in a Discord server.

        Args:
            guild (int): The Discord server's guild ID.
            role (str): The name of the role to assign.
            token (str): Your Discord bot token.
            delay (float, optional): Delay in seconds between role assignments (default: 3.0).
        """
        client = DiscordClient()

        @client.bot.event
        async def on_ready():
            self.logger.info("Logged in as %s", client.bot.user)

            # Fetch the guild using the provided guild ID
            guild_obj = client.bot.get_guild(guild)
            if not guild_obj:
                self.logger.error("Guild not found. Please check your guild ID.")
                await client.bot.close()
                return

            # Retrieve the role by name
            role_obj = discord.utils.get(guild_obj.roles, name=role)
            if not role_obj:
                self.logger.error("Role not found. Please check the role name.")
                await client.bot.close()
                return

            self.logger.debug(
                "Assigning role '%s' to all members of '%s'...", role, guild_obj.name
            )

            # Iterate through each member and add the role if they don't have it
            members = guild_obj.members
            async for member in tqdm(members, desc="Assigning roles", unit="member"):
                if role_obj not in member.roles:
                    try:
                        await member.add_roles(role_obj)
                        self.logger.debug(
                            "Added role to %s#%s", member.name, member.discriminator
                        )
                        await asyncio.sleep(delay)
                    except Exception as e:
                        self.logger.error(
                            "Failed to add role to %s#%s: %s",
                            member.name,
                            member.discriminator,
                            e,
                        )

            self.logger.debug("Finished processing all members.")
            await client.bot.close()

        client.run()
