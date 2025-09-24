from interactions.api.events import Ready
from client import client
from utils import blank_line

client.load_extension('temp_voice')


@client.listen(Ready)
async def on_ready(event: Ready):
    print(
        f"Bot is ready! Logged in as {event.bot.user.username}. v{client.version}")

if __name__ == "__main__":
    blank_line()
    print("Running bot...")
    client.start()
