import sys
import fire
from guildmaster.tasks.role_manager import DiscordRoleManager

class GuildMasterCommands:
    """
    A CLI tool for managing Discord server tasks and settings.
    """
    def __init__(self):
        self.role = DiscordRoleManager()

def main():
    try:
        fire.Fire(name="guildmaster", component=GuildMasterCommands)
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()