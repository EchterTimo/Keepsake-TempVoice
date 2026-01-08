<!-- markdownlint-disable MD041 -->
![Jump Space](./images/jump_space.jpeg)

# Keepsake TempVoice

temp voice bot for the [Jump Space](https://store.steampowered.com/app/1757300) Discord. ([discord.gg/jumpspace](https://discord.gg/jumpspace))

> [!IMPORTANT]
> This Bot is meant to be run on one discord server (guild) only. If you want to run it on multiple servers, you need to run multiple instances of the bot.

## Support this project

If you find this project helpful, please consider starring ⭐ the repository on GitHub.

## Features

- Create temporary voice channels by joining a "generator" voice channel.
- Automatically delete empty temporary voice channels.
- The channel owner can ban members from his channel.
- Distribute temporary voice channels across multiple categories to avoid hitting Discord's category channel limit.
- Per-user cooldown for creating new temporary voice channels, preventing spam.

## Dependencies

- Python 3.12 or higher installed on your machine.
- A Discord Bot User

## Create and configure your bot

- Create a new application in the [Discord Developer Portal](https://discord.com/developers/applications).
- Switch to the **Installation** tab and set **Install Link** to `None`
- Switch to **Bot** tab and uncheck **Public Bot**

## Invite your bot to your server

- Go to the **OAuth2** tab and use the **URL Generator** like described below:
  - Under **SCOPES** select `bot` and `applications.commands`
  - Under **BOT PERMISSIONS** enable...
    - `Manage Roles`
    - `Manage Channels`
    - `View Channels`
    - `Send Messages`
    - `Send Messages in Threads`
    - `Move Members`
  - Copy the generated URL and open it in your browser
  - Select your server and authorize the bot

## Usage

- Copy `example.env` to `.env` and configure it.

> [!NOTE]
> To obtain your Discord bot token, go to the [Discord Developer Portal](https://discord.com/developers/applications), select your application, navigate to the **Bot** tab, and click **Reset Token** to get your bot token. Paste this value as `BOT_TOKEN` in your `.env` file.

> [!CAUTION]
> Setting `MAX_CHANNELS_PER_CATEGORY` above 50 will lead to issues due to Discord's limit of 50 channels per category.

    | Variable                    | Description                                                                                                  |
    |-----------------------------|--------------------------------------------------------------------------------------------------------------|
    | BOT_TOKEN                   | Your Discord bot token.                                                                                      |
    | MAX_CHANNELS_PER_CATEGORY   | Maximum number of channels allowed per category.                                                             |
    | CREATION_COOLDOWN           | Cooldown time in seconds between creating new temp voice channels for the same user. Helps prevent spam.     |
    | GUILD_ID                    | Your Discord server (guild) ID. Required for the bot to function.                                            |
    | GENERATOR_CHANNEL_ID        | Channel ID where users generate temp voice channels.                                                         |
    | CATEGORIES                  | Comma-separated list of category IDs to use. Temp voice channels are distributed among these.                |
    | IGNORED_CHANNELS            | Comma-separated list of channel IDs to ignore. These channels will not be deleted when empty.                |

- Create a virtual environment (optional but recommended):

    ```bash
    # Windows
    python -m venv .venv

    # macOS/Linux
    python3 -m venv .venv
    ```

- Activate the virtual environment (if using one):

    ```bash
    # Windows
    .venv/Scripts/activate
    
    # macOS/Linux
    source .venv/bin/activate
    ```

- Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

- Run the bot:

    ```bash
    python src/main.py
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.
