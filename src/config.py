from os import getenv
from dotenv import load_dotenv


def getenv_int_list(key: str) -> list[int]:
    string = getenv(key)
    categories = []
    for cat in string.split(','):
        cat = cat.strip()
        if cat.isdigit():
            categories.append(int(cat))
    return categories


def getenv_int(key: str):
    return int(getenv(key))


load_dotenv()
_BOT_TOKEN = getenv('BOT_TOKEN')
GENERATOR_CHANNEL_ID = getenv_int('GENERATOR_CHANNEL_ID')
MAX_CHANNELS_PER_CATEGORY = getenv_int('MAX_CHANNELS_PER_CATEGORY')
CATEGORIES = getenv_int_list('CATEGORIES')
IGNORED_CHANNELS = getenv_int_list('IGNORED_CHANNELS')
GUILD_ID = getenv_int('GUILD_ID')
