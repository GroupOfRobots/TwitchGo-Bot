import logging


class Logger:
    def __init__(self, filename="logfile.log"):
        self.filename = filename
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        try:
            file_handler = logging.FileHandler(filename)
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
        except Exception as e:
            print(f"Error while setting up file logger: {e}")

    def log_info(self, message: str):
        try:
            self.logger.info(message)
        except Exception as e:
            print(f"Error while logging info: {e}")

    def log_warning(self, message: str):
        try:
            self.logger.warning(message)
        except Exception as e:
            print(f"Error while logging warning: {e}")

    def log_error(self, message: str):
        try:
            self.logger.error(message)
        except Exception as e:
            print(f"Error while logging error: {e}")

    def log_critical(self, message: str):
        try:
            self.logger.critical(message)
        except Exception as e:
            print(f"Error while logging critical: {e}")
