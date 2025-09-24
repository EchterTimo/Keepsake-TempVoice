from interactions import (
    Client,
    Intents,
    Activity,
    ActivityType
)
from config import _BOT_TOKEN

__VERSION__ = "0.3.3"

client = Client(
    disable_dm_commands=True,
    send_command_tracebacks=False,
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
client.version = __VERSION__
