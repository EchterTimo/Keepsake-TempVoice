# Keepsake TempVoice

Custom-made temporary voice bot for Jump Space Discord.

## Environment Variables

- `DISCORD_BOT_TOKEN` — Your Discord bot token.
- `MAX_CHANNELS_PER_CATEGORY` — Maximum number of channels allowed per category. Discord has a limit of 50 channels per category. To avoid hitting this limit, it's recommended to set this value below 50.
- `GENERATOR_CHANNEL_ID` — Channel ID where users can generate temp voice channels.
- `CATEGORIES` — Comma-separated list of category IDs to use (e.g., `111, 222, 333, 444`). The bot will create temp voice channels in these categories, distributing them evenly.
- `IGNORED_CHANNELS` — Comma-separated list of channel IDs to ignore (e.g., `555, 666`). They will not be deleted when empty.
- `GUILD_ID` — Your Discord server (guild) ID. This is required for the bot to function properly.
