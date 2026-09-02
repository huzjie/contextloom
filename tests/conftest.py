"""pytest 全局 fixture。"""
from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest

SRC = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC))

os.environ.setdefault("CLOOM_LLM_BACKEND", "mock")
os.environ.setdefault("CLOOM_VECTOR_BACKEND", "memory")
os.environ.setdefault("CLOOM_EMBED_ALLOW_HASH_FALLBACK", "true")


@pytest.fixture
def settings():
    from contextloom.config.settings import Settings
    return Settings(
        llm_backend="mock",
        vector_backend="memory",
        embed_allow_hash_fallback=True,
        data_dir=Path("./data-test"),
        _env_file=None,
    )


@pytest.fixture
def sample_text() -> str:
    return ("这是第一段。用于测试分块逻辑。\n" * 20)
