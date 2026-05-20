from loguru import logger
import sys
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

def configure_logging():
    logger.remove()

    logger.add(
        sys.stdout,
        level="INFO",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
    )

    logger.add(
        LOG_DIR / "edge_ai.log",
        rotation="10 MB",
        retention="7 days",
        level="INFO"
    )

    return logger
