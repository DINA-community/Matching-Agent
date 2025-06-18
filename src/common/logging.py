import logging
import os

import colorlog


def configure_logging():
    """
    Configure logging with colors and environment variable-based log level.

    This function sets up logging with colored output and reads the log level
    from the LOG_LEVEL environment variable (defaults to INFO if not set).
    """
    # Get log level from environment variable, default to INFO
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()

    # Configure logging with colors
    handler = colorlog.StreamHandler()
    handler.setFormatter(
        colorlog.ColoredFormatter(
            "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            log_colors={
                "DEBUG": "cyan",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "red,bg_white",
            },
        )
    )
    logging.root.handlers.clear()
    logging.root.addHandler(handler)
    logging.root.setLevel(getattr(logging, log_level))


def get_logger(name):
    """
    Get a logger with the specified name.

    Args:
        name (str): The name of the logger, typically __name__

    Returns:
        logging.Logger: A configured logger instance
    """
    return logging.getLogger(name)
