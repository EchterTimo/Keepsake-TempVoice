from os import getenv
from dotenv import load_dotenv
import sys


def getenv_int_list(key: str) -> list[int]:
    string = getenv(key)
    if string is None:
        print(f"[ERROR] Environment variable '{key}' is not set!")
        print(f"[ERROR] Please copy .env.example to .env and configure all required variables.")
        sys.exit(1)
    
    categories = []
    for cat in string.split(','):
        cat = cat.strip()
        if cat.isdigit():
            categories.append(int(cat))
    return categories


def getenv_int(key: str):
    value = getenv(key)
    if value is None:
        print(f"[ERROR] Environment variable '{key}' is not set!")
        print(f"[ERROR] Please copy .env.example to .env and configure all required variables.")
        sys.exit(1)
    
    try:
        return int(value)
    except ValueError:
        print(f"[ERROR] Environment variable '{key}' must be a valid integer, got: '{value}'")
        print(f"[ERROR] Please check your .env file and fix the configuration.")
        sys.exit(1)


def getenv_required(key: str) -> str:
    value = getenv(key)
    if value is None:
        print(f"[ERROR] Environment variable '{key}' is not set!")
        print(f"[ERROR] Please copy .env.example to .env and configure all required variables.")
        sys.exit(1)
    return value


load_dotenv()
_BOT_TOKEN = getenv_required('BOT_TOKEN')

GENERATOR_CHANNEL_ID = getenv_int('GENERATOR_CHANNEL_ID')
MAX_CHANNELS_PER_CATEGORY = getenv_int('MAX_CHANNELS_PER_CATEGORY')
CATEGORIES = getenv_int_list('CATEGORIES')
IGNORED_CHANNELS = getenv_int_list('IGNORED_CHANNELS')
GUILD_ID = getenv_int('GUILD_ID')
CREATION_COOLDOWN = getenv_int('CREATION_COOLDOWN')

if MAX_CHANNELS_PER_CATEGORY > 50:
    raise ValueError(
        "MAX_CHANNELS_PER_CATEGORY should stay within Discord's 50-channel limit")
