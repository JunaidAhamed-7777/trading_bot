from bot.logging_config import setup_logger

logger = setup_logger()

logger.info("Application started")
logger.warning("Test warning")
logger.error("Test error")

print("Logs written")