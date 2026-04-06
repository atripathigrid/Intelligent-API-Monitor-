from loguru import logger

logger.add(
    "server.log",
    rotation="1 MB",
    retention="10 days",
    level="INFO",
    format="{time} | {level} | {message}"
)