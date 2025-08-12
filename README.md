# 🧙 GuildMaster CLI

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=for-the-badge)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg?style=for-the-badge)](https://makeapullrequest.com)
![Status](https://img.shields.io/badge/status-in--progress-yellow?style=for-the-badge)
[![Join Our Discord](https://img.shields.io/discord/1269864144903864381?label=Join%20Discord\&logo=discord\&style=for-the-badge)](discord.gg/enMmUNq8jc)

> ⚔️ **GuildMaster CLI** is an administrative command-line interface built for managing the [DSB Discord](https://discord.gg/devsecblueprint) server. Automate tedious tasks like role synchronization and more as this tool evolves.

## 🚧 Project Status

GuildMaster CLI is currently under active development. Right now, it includes core functionality to update all Discord roles via a single command.

Stay tuned as new features (like event management, audit logging, and quest assignments 👀) are rolled out!

## 🧰 Features

- ✅ Update all Discord roles with a single command
- 🚧 Built with [Python Fire](https://github.com/google/python-fire) for rapid CLI development
- ✨ Designed for server maintainers, moderators, and admins in the DSB community


## 📦 Installation

1. **Clone the repo**:
   ```bash
   git clone https://github.com/The-DevSec-Blueprint/guildmaster-cli.git
   cd guildmaster-cli
   ```

2. **(Optional) Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

You must have your Discord bot token and configuration ready in a `.env` file or exported as environment variables.

```bash
python guildmaster.py update_roles
```

This command will trigger a role sync across the DSB Discord server using your preconfigured bot permissions.


## 🛠 Version Management

This project uses [bumpver](https://github.com/mbarkhau/bumpver) for consistent versioning.

```bash
# Patch bump (e.g., 1.0.0 → 1.0.1)
bumpver update --patch

# Minor bump (e.g., 1.0.1 → 1.1.0)
bumpver update --minor

# Major bump (e.g., 1.1.0 → 2.0.0)
bumpver update --major
```


## 🧪 Contributing

We welcome pull requests! If you'd like to contribute:

1. Fork the repo
2. Create a new branch (`git checkout -b feat/add-feature`)
3. Commit your changes (`git commit -m 'add cool feature'`)
4. Push to your branch (`git push origin feat/add-feature`)
5. Open a PR!

## 📜 License

Licensed under the [MIT License](https://opensource.org/licenses/MIT).

> Made with ❤️ for the builders who shift left and secure everything—code, cloud, and community.