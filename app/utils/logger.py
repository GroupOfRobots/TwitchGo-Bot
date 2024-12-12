# app/utils/logger.py

import logging

def setup_logging(log_file: str) -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime)s] %(levelname)s: %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
