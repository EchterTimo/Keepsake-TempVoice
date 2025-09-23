# Keepsake TempVoice

Custom-made temporary voice bot for Jump Space Discord.

## Features

- Create temporary voice channels by joining a "generator" voice channel.
- Automatically delete empty temporary voice channels.
- Distribute temporary voice channels across multiple categories to avoid hitting Discord's category channel limit.
- Ignore specific channels from being deleted when empty.

## Environment Variables

| Variable                    | Description                                                                                                  |
|-----------------------------|--------------------------------------------------------------------------------------------------------------|
| `DISCORD_BOT_TOKEN`         | Your Discord bot token.                                                                                      |
| `MAX_CHANNELS_PER_CATEGORY` | Maximum number of channels allowed per category. Set below 50 to avoid Discord's limit.                      |
| `CREATION_COOLDOWN`         | Cooldown time in seconds between creating new temp voice channels for the same user. Helps prevent spam.      |
| `GUILD_ID`                  | Your Discord server (guild) ID. Required for the bot to function.                                            |
| `GENERATOR_CHANNEL_ID`      | Channel ID where users generate temp voice channels.                                                         |
| `CATEGORIES`                | Comma-separated list of category IDs to use. Temp voice channels are distributed among these.                |
| `IGNORED_CHANNELS`          | Comma-separated list of channel IDs to ignore. These will not be deleted when empty.                         |
