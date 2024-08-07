import logging
import os
import time

import colorlog

from app.core.config import Setting
from utils.util import generate_filepath

log_colors_config = {
    "DEBUG": "white",
    "INFO": "green",
    "WARNING": "yellow",
    "ERROR": "red",
    "CRITICAL": "bold_red",
}


def configure_logger(logger: logging.Logger, filename: str, setting: Setting):
    fmt_file = logging.Formatter(
        fmt="[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s " "line:%(lineno)d [%(levelname)s] :  %(message)s",
        datefmt="%Y-%m-%d  %H:%M:%S",
    )

    fh = logging.FileHandler(filename=filename, encoding=setting.LOG_FILE_ENCODING)
    fh.setFormatter(fmt_file)
    fh.setLevel(setting.LOG_FILE_LEVEL)
    logger.addHandler(fh)

    if setting.LOG_CONSOLE_OUTPUT:
        fmt_sh = colorlog.ColoredFormatter(
            fmt="%(log_color)s[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s "
            "line:%(lineno)d [%(levelname)s] :  %(message)s",
            datefmt="%Y-%m-%d  %H:%M:%S",
            log_colors=setting.LOG_CONSOLE_COLOR,
        )

        sh = logging.StreamHandler()
        sh.setFormatter(fmt_sh)
        sh.setLevel(setting.LOG_STREAM_LEVEL)
        logger.addHandler(sh)
    return logger


def get_logger(setting: Setting) -> logging.Logger:
    filename = generate_filepath(
        filename=f'{setting.PROJECT_NAME.replace(" ", "")}-{time.strftime("%Y-%m-%d", time.localtime())}.log',
        filepath=os.path.join(os.getcwd(), setting.LOG_PATH),
    )
    logger = logging.getLogger(setting.LOG_NAME)
    logger.setLevel("DEBUG")
    return configure_logger(logger=logger, filename=filename, setting=setting)
