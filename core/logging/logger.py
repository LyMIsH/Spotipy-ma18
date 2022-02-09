import logging
import config


logging.basicConfig(handlers=[logging.FileHandler(config.settings['log_path'], 'w', 'utf-8')],
                    level=logging.DEBUG, format='%(levelname)s: %(name)s - %(asctime)s - %(message)s')


def debug(msg):
    logging.debug(msg)


def info(msg):
    logging.info(msg)


def warning(msg):
    logging.warning(msg)


def error(msg):
    logging.error(msg)


def fatal(msg):
    logging.fatal(msg)
