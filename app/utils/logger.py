# app/core/utils/logger.py

import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logging(log_file: str):
    """
    Configure logging with a rotating file handler and console output.

    Args:
        log_file (str): Path to the log file.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Formatter for log messages
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

    # Rotating file handler
    file_handler = RotatingFileHandler(log_file, maxBytes=10**6, backupCount=5)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
