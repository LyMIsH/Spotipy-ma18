import logging
from pathlib import Path


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, filename=f"{Path().absolute()}\\logs.log", filemode='a',
                    format='%(levelname)s: %(name)s - %(asctime)s - %(message)s')


def debug(msg):
    logger.debug(msg)


def info(msg):
    logger.info(msg)


def warning(msg):
    logger.warning(msg)


def error(msg):
    logger.error(msg)


def fatal(msg):
    logger.fatal(msg)
