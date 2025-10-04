from interactions import (
    Client,
    Intents,
    Activity,
    ActivityType
)
from config import _BOT_TOKEN
import logging
from logging.handlers import RotatingFileHandler
import sys
import colorlog
from pathlib import Path


def make_logger(name: str) -> logging.Logger:
    '''Create a logger with a file handler and a console handler.'''

    # ensure logs directory exists
    logs_dir = Path("logs")
    try:
        logs_dir.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        logging.error(f"Failed to create logs directory '{logs_dir}': {e}. Falling back to current directory.")
        logs_dir = Path(".")

    # file handler (rotating)
    file_path = logs_dir / "bot.log"
    file_handler = RotatingFileHandler(
        filename=str(file_path),
        maxBytes=20 * 1024 * 1024,  # 20 MB
        backupCount=5,
        encoding="utf-8",
    )
    file_handler.setLevel(logging.DEBUG)

    # console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)

    # formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    # color formatter for console handler with timestamps
    color_formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(asctime)s - %(levelname)s:%(reset)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        }
    )
    # set formatters
    console_handler.setFormatter(color_formatter)
    file_handler.setFormatter(formatter)

    # Configure the logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger


__VERSION__ = "0.3.7"

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
    logger=make_logger("bot"),
    token=_BOT_TOKEN
)
client.version = __VERSION__
