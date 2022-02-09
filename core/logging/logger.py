import logging
import config


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, filename=config.settings['log_path'], filemode='a',
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
