"""统一日志配置。"""

from __future__ import annotations

import logging
import sys
from typing import Any


def setup_logging(level: str = "INFO") -> None:
    fmt = "%(asctime)s | %(levelname)-7s | %(name)s | %(message)s"
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format=fmt,
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
    )


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)


def log_config(config: Any) -> None:
    logger = get_logger(__name__)
    logger.info("ContextLoom 配置: backend=%s model=%s vector=%s window=%s",
                getattr(config, "llm_backend", "?"), getattr(config, "llm_model", "?"),
                getattr(config, "vector_backend", "?"), getattr(config, "llm_context_window", "?"))
