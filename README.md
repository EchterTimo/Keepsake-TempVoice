<!-- markdownlint-disable MD041 -->
![Jump Space](./images/jump_space.jpeg)

# Keepsake TempVoice

temp voice bot for the [Jump Space](https://store.steampowered.com/app/1757300) Discord. ([discord.gg/jumpspace](https://discord.gg/jumpspace))

> If you like this project, consider giving it a star ⭐ on GitHub!

## Features

- Create temporary voice channels by joining a "generator" voice channel.
- Automatically delete empty temporary voice channels.
- Distribute temporary voice channels across multiple categories to avoid hitting Discord's category channel limit.
- Per-user cooldown for creating new temporary voice channels, preventing spam.

## Prerequisites / Requirements / Dependencies / Requirements

- Python 3.12 or higher installed on your machine.
- A Discord Bot User

## Create and configure your bot

- Create a new application in the [Discord Developer Portal](https://discord.com/developers/applications).
- Switch to the **Installation** tab and set **Install Link** to `None`
- Switch to **Bot** tab and uncheck **Public Bot**

## Invite your bot to your server

- Go to the **OAuth2** tab and use the **URL Generator** like described below:
  - Under **SCOPES** select `bot` and `applications.commands`
  - Under **BOT PERMISSIONS** select `Manage Channels`, `View Channels` and `Move Members`
  - Copy the generated URL and open it in your browser
  - Select your server and authorize the bot

## Getting Started / Installation / Usage / Deployment / How to Run

- Copy `example.env` to `.env` and configure it.

    | Variable                    | Description                                                                                                  |
    |-----------------------------|--------------------------------------------------------------------------------------------------------------|
    | `DISCORD_BOT_TOKEN`         | Your Discord bot token.                                                                                      |
    | `MAX_CHANNELS_PER_CATEGORY` | Maximum number of channels allowed per category. Set below 50 to avoid Discord's limit.                      |
    | `CREATION_COOLDOWN`         | Cooldown time in seconds between creating new temp voice channels for the same user. Helps prevent spam.     |
    | `GUILD_ID`                  | Your Discord server (guild) ID. Required for the bot to function.                                            |
    | `GENERATOR_CHANNEL_ID`      | Channel ID where users generate temp voice channels.                                                         |
    | `CATEGORIES`                | Comma-separated list of category IDs to use. Temp voice channels are distributed among these.                |
    | `IGNORED_CHANNELS`          | Comma-separated list of channel IDs to ignore. These will not be deleted when empty.                         |

- Create a virtual environment (optional but recommended):

    ```bash
    python -m venv .venv
    ```

- Activate the virtual environment (if using one):

    ```bash
    .venv/Scripts/activate  # On Windows
    source .venv/bin/activate  # On macOS/Linux
    ```

- Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

- Run the bot:

    ```bash
    python src/main.py
    ```
