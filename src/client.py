from interactions import (
    Client,
    Intents,
    Activity,
    ActivityType
)
from config import _BOT_TOKEN

__VERSION__ = "0.1.0"

client = Client(
    disable_dm_commands=True,
    send_command_tracebacks=True,  # todo: remove in production
    activity=Activity(
        name="Jump Space",
        state=f"Bot v{__VERSION__}",
        type=ActivityType.PLAYING
    ),
    intents=Intents.new(
        default=True
    ),
    token=_BOT_TOKEN
)
