import asyncio
import discord
from client.discord_client import DiscordClient, TOKEN

class DiscordRoleAssigner:
    """
    A class for assigning a role to every member in a Discord server.
    """
    
    def assign(self, guild: int, role: str, delay: float = 3.0):
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
            print(f"Logged in as {client.bot.user}")

            # Fetch the guild using the provided guild ID
            guild_obj = client.bot.get_guild(guild)
            if not guild_obj:
                print("Guild not found. Please check your guild ID.")
                await client.bot.close()
                return

            # Retrieve the role by name
            role_obj = discord.utils.get(guild_obj.roles, name=role)
            if not role_obj:
                print("Role not found. Please check the role name.")
                await client.bot.close()
                return

            print(f"Assigning role '{role_obj.name}' to all members of '{guild_obj.name}'...")

            # Iterate through each member and add the role if they don't have it
            for member in guild_obj.members:
                if role_obj not in member.roles:
                    try:
                        await member.add_roles(role_obj)
                        print(f"Added role to {member.name}#{member.discriminator}")
                        await asyncio.sleep(delay)
                    except Exception as e:
                        print(f"Failed to add role to {member.name}#{member.discriminator}: {e}")

            print("Finished processing all members.")
            await client.close()

        client.run()