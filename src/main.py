import fire

from tasks.role_assigner import DiscordRoleAssigner

def main():
    fire.Fire(DiscordRoleAssigner)

if __name__ == '__main__':
    main()
