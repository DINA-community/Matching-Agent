import logging as lg
import multiprocessing
import os
from contextlib import contextmanager
from contextvars import ContextVar, Token
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Iterator, Optional

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

_MATCH_UUID_CONTEXT: ContextVar[str] = ContextVar("match_uuid", default="-")
_LOG_RECORD_FACTORY_ENRICHED_ATTR = "_dina_enriched_with_match_uuid"


class LoggingConfig(BaseModel):
    level: str = Field("INFO", description="Log level for file logging.")
    file: Path = Field(..., description="Path to the log file.")
    max_bytes: int = Field(
        10_000_000, description="Maximum size of a log file before rotation."
    )
    backup_count: int = Field(5, description="Number of rotated log files to keep.")


class _ConditionalMatchUuidFormatter(lg.Formatter):
    """
    Formatter that appends match UUID only for non-main-process records.
    """

    def format(self, record: lg.LogRecord) -> str:
        match_uuid = getattr(record, "match_uuid", "-")
        process_name = getattr(record, "processName", "")
        include_match_uuid = (
            process_name != "MainProcess" and bool(match_uuid) and match_uuid != "-"
        )
        record.match_uuid_segment = (
            f"[match_uuid={match_uuid}] - " if include_match_uuid else ""
        )
        return super().format(record)


class _ConditionalMatchUuidColoredFormatter(colorlog.ColoredFormatter):
    """
    Colored formatter variant that appends match UUID only for worker records.
    """

    def format(self, record: lg.LogRecord) -> str:
        match_uuid = getattr(record, "match_uuid", "-")
        process_name = getattr(record, "processName", "")
        include_match_uuid = (
            process_name != "MainProcess" and bool(match_uuid) and match_uuid != "-"
        )
        record.match_uuid_segment = (
            f"[match_uuid={match_uuid}] - " if include_match_uuid else ""
        )
        return super().format(record)


@contextmanager
def match_uuid_context(match_uuid: str) -> Iterator[None]:
    """
    Bind a match UUID to all log records emitted in the current context.

    Args:
        match_uuid: Match trace UUID to inject into log records.
    """
    token: Token[str] = _MATCH_UUID_CONTEXT.set(match_uuid)
    try:
        yield
    finally:
        _MATCH_UUID_CONTEXT.reset(token)


def clear_match_uuid_context() -> None:
    """
    Reset the match UUID logging context to the default placeholder.
    """
    _MATCH_UUID_CONTEXT.set("-")


def _install_match_uuid_log_record_factory() -> None:
    """
    Ensure every log record carries a ``match_uuid`` field for formatting.
    """
    current_factory = lg.getLogRecordFactory()
    if getattr(current_factory, _LOG_RECORD_FACTORY_ENRICHED_ATTR, False):
        return

    def record_factory(*args, **kwargs):
        record = current_factory(*args, **kwargs)
        if not hasattr(record, "match_uuid"):
            record.match_uuid = _MATCH_UUID_CONTEXT.get()
        return record

    setattr(record_factory, _LOG_RECORD_FACTORY_ENRICHED_ATTR, True)
    lg.setLogRecordFactory(record_factory)


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
    _install_match_uuid_log_record_factory()

    # Configure root logger
    lg.root.handlers.clear()

    if multiprocessing.current_process().name == "MainProcess":
        # Console handler with colors
        console_handler = colorlog.StreamHandler()
        console_handler.setLevel(console_level)
        console_handler.setFormatter(
            _ConditionalMatchUuidColoredFormatter(
                "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(match_uuid_segment)s%(message)s",
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
            file_formatter = _ConditionalMatchUuidFormatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(match_uuid_segment)s%(message)s"
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
