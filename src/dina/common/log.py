import logging as lg
import multiprocessing
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional

import colorlog
from pydantic import BaseModel, Field

CRITICAL = lg.CRITICAL  # type: ignore
FATAL = lg.FATAL  # type: ignore
ERROR = lg.ERROR  # type: ignore
WARNING = lg.WARNING  # type: ignore
WARN = lg.WARN  # type: ignore
INFO = lg.INFO  # type: ignore
DEBUG = lg.DEBUG  # type: ignore
NOTSET = lg.NOTSET  # type: ignore


class LoggingConfig(BaseModel):
    level: str = Field("INFO", description="Log level for file logging.")
    file: Path = Field(..., description="Path to the log file.")
    max_bytes: int = Field(
        10_000_000, description="Maximum size of a log file before rotation."
    )
    backup_count: int = Field(5, description="Number of rotated log files to keep.")


def configure_logging(
    config: LoggingConfig | None = None,
    queue: Optional[multiprocessing.Queue] = None,
):
    """
    Configure logging with colors and optional rotating file handler.

    Behavior:
    - Console handler level is controlled by the LOG_LEVEL environment variable (default: INFO).
    - File handler level is controlled by the `level` parameter (e.g., from matcher.toml).

    Args:
        :param config:
        :param queue:
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

    if multiprocessing.current_process().name == "MainProcess":
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
    elif queue is not None:
        queue_handler = lg.handlers.QueueHandler(queue)
        lg.root.addHandler(queue_handler)

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
