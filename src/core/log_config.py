"""Sets up the logging configuration for the application."""

import logging
import os
import sys


def setup_logging():
    """
    Configure the logging settings for the application.

    This function sets the logging level based on the environment variable.

    How to use:
    1. Call `setup_logging()` at the start of your application.
    2. Set the environment variable `LOG_LEVEL` to control the logging level.
    Supported levels: DEBUG, INFO, WARNING, ERROR, CRITICAL.
    3. The default level is INFO if `LOG_LEVEL` is not set.

    Example:
        import logging
        from your_module import setup_logging

        setup_logging()
        logger = logging.getLogger(__name__)
        logger.info("This is an info message.")

    """
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    logger = logging.getLogger()
    logger.setLevel(log_level)
    handler = logging.StreamHandler(sys.stdout)
    log_message_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(log_message_format)
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)
