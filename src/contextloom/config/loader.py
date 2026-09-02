"""YAML/JSON 配置加载与合并。"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from contextloom.config.settings import Settings


def load_yaml(path: str | Path) -> dict[str, Any]:
    p = Path(path)
    if not p.exists():
        return {}
    with p.open("r", encoding="utf-8") as fp:
        return yaml.safe_load(fp) or {}


def merge_settings(settings: Settings, overrides: dict[str, Any]) -> Settings:
    for key, value in overrides.items():
        if hasattr(settings, key):
            setattr(settings, key, value)
    return settings
