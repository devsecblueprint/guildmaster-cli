import logging


class Logger:
    @staticmethod
    def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
        """
        Set up a logger with the specified name, log file, and logging level.

        Args:
            name (str): The name of the logger.
            level (int): The logging level (default: logging.INFO).

        Returns:
            logging.Logger: Configured logger instance.
        """
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(console_handler)

        return logger
