from loguru import logger
import config

logger.remove()
logger.add(config.LOGFILE,
           format='{time:YYYY-MM-DD HH:mm:ss} | {level} - {message} (function = {function})')
