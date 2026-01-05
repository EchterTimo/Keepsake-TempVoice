from environs import Env

env = Env()
env.read_env()

GENERATOR_CHANNEL_ID = env.int("GENERATOR_CHANNEL_ID")
MAX_CHANNELS_PER_CATEGORY = env.int("MAX_CHANNELS_PER_CATEGORY")
CATEGORIES = env.list("CATEGORIES", subcast=int)
IGNORED_CHANNELS = env.list("IGNORED_CHANNELS", subcast=int)
GUILD_ID = env.int("GUILD_ID")
CREATION_COOLDOWN = env.int("CREATION_COOLDOWN")
_BOT_TOKEN = env.str("BOT_TOKEN")

if MAX_CHANNELS_PER_CATEGORY > 50:
    raise ValueError(
        "MAX_CHANNELS_PER_CATEGORY should stay within Discord's 50-channel limit"
    )
