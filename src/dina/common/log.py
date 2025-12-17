import logging as lg
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path

import colorlog
from pydantic import BaseModel

CRITICAL = lg.CRITICAL  # type: ignore
FATAL = lg.FATAL  # type: ignore
ERROR = lg.ERROR  # type: ignore
WARNING = lg.WARNING  # type: ignore
WARN = lg.WARN  # type: ignore
INFO = lg.INFO  # type: ignore
DEBUG = lg.DEBUG  # type: ignore
NOTSET = lg.NOTSET  # type: ignore


class LoggingConfig(BaseModel):
    level: str = "INFO"
    file: Path
    max_bytes: int = 10_000_000
    backup_count: int = 5


def configure_logging(
    config: LoggingConfig | None = None,
):
    """
    Configure logging with colors and optional rotating file handler.

    Behavior:
    - Console handler level is controlled by the LOG_LEVEL environment variable (default: INFO).
    - File handler level is controlled by the `level` parameter (e.g., from matcher.toml).

    Args:
        config (LoggingConfig): Logging configuration.
    """
    # Define custom TRACE level
    TRACE_LEVEL = 5
    if not hasattr(lg, "TRACE"):
        lg.addLevelName(TRACE_LEVEL, "TRACE")
        lg.TRACE = TRACE_LEVEL  # type: ignore[attr-defined]

        # Add trace method to all loggers
        def trace(self, message, *args, **kwargs):
            if self.isEnabledFor(TRACE_LEVEL):
                self._log(TRACE_LEVEL, message, args, **kwargs)

        lg.Logger.trace = trace  # type: ignore[attr-defined]

    # Resolve console level from environment (default INFO)
    console_level_name = os.getenv("LOG_LEVEL", "INFO").upper()
    console_level = getattr(lg, console_level_name, lg.INFO)

    # Configure root logger
    lg.root.handlers.clear()

    # Console handler with colors
    console_handler = colorlog.StreamHandler()
    console_handler.setLevel(console_level)
    console_handler.setFormatter(
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
    lg.root.addHandler(console_handler)

    # Optional rotating file handler

    if config is not None:
        # Resolve file handler level from parameter (default INFO)
        if config.level is None:
            file_level = lg.INFO
        elif isinstance(config.level, str):
            file_level = getattr(lg, config.level.upper(), lg.INFO)
        else:
            file_level = int(config.level)
        path = config.file
        try:
            if path.parent and not path.parent.exists():
                path.parent.mkdir(parents=True, exist_ok=True)
        except Exception:
            # If directory creation fails, still proceed with console logging
            pass
        file_handler = RotatingFileHandler(
            path, maxBytes=config.max_bytes, backupCount=config.backup_count
        )
        file_handler.setLevel(file_level)
        file_formatter = lg.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(file_formatter)
        lg.root.addHandler(file_handler)

    # Let handlers decide what to emit
    lg.root.setLevel(lg.NOTSET)


def get_logger(name):
    """
    Get a logger with the specified name.

    Args:
        name (str): The name of the logger, typically __name__

    Returns:
        logging.Logger: A configured logger instance
    """
    return lg.getLogger(name)
