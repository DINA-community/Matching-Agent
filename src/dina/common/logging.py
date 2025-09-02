import logging as lg
import os

import colorlog

CRITICAL = lg.CRITICAL  # type: ignore
FATAL = lg.FATAL  # type: ignore
ERROR = lg.ERROR  # type: ignore
WARNING = lg.WARNING  # type: ignore
WARN = lg.WARN  # type: ignore
INFO = lg.INFO  # type: ignore
DEBUG = lg.DEBUG  # type: ignore
NOTSET = lg.NOTSET  # type: ignore


def configure_logging():
    """
    Configure logging with colors and environment variable-based log level.

    This function sets up logging with colored output and reads the log level
    from the LOG_LEVEL environment variable (defaults to INFO if not set).
    """
    # Get log level from environment variable, default to INFO
    TRACE_LEVEL = 5
    lg.addLevelName(TRACE_LEVEL, "TRACE")
    lg.TRACE = TRACE_LEVEL

    # Add trace method to all loggers
    def trace(self, message, *args, **kwargs):
        if self.isEnabledFor(TRACE_LEVEL):
            self._log(TRACE_LEVEL, message, args, **kwargs)

    lg.Logger.trace = trace

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
    lg.root.handlers.clear()
    lg.root.addHandler(handler)
    lg.root.setLevel(getattr(lg, log_level))


def get_logger(name):
    """
    Get a logger with the specified name.

    Args:
        name (str): The name of the logger, typically __name__

    Returns:
        logging.Logger: A configured logger instance
    """
    return lg.getLogger(name)
