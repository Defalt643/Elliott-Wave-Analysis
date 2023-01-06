#import library
import  logging
import time

levelToName = {
    50:"fatal",
    40:"error",
    30:"warn",
    20:"info",
    10:"debug"
}

logLevels = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warn':logging.WARN,
    'error':logging.ERROR,
    'fatal':logging.FATAL
}

def set_level_log(level):
    if isinstance(level, str):
        log_level = logLevels[level]
    elif isinstance(level, int):
        log_level = level
    else:
        raise ValueError("log level must be string ot integer")
    logging.basicConfig(level=log_level, format='time="%(asctime)s" level=%(levelname)s msg="%(message)s"')

def set_format():
    logging.basicConfig(format='time="%(asctime)s" level=%(levelname)s msg="%(message)s"')

def debug(message):
    # logging.debug(f"DEBUG: \n{message}")
    logging.debug(str(time.ctime(time.time()))+" [DEBUG] "+message)

def info(message):
    # logging.info(message)
    logging.info(str(time.ctime(time.time()))+" [INFO] "+message)

def warning(message):
    logging.warning(str(time.ctime(time.time()))+" [WARN] "+message)

def error(message):
    logging.error(str(time.ctime(time.time()))+" [ERROR] "+message)

def critical(message):
    logging.critical(str(time.ctime(time.time()))+" [CRITICAL] "+message)
