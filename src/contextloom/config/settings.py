"""配置系统：环境变量（CLOOM_ 前缀）+ .env + 默认值。"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="CLOOM_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    env: str = "dev"
    log_level: str = "INFO"
    host: str = "0.0.0.0"
    port: int = 8000
    workers: int = 1
    data_dir: Path = Path("./data")

    llm_backend: Literal["ollama", "llamacpp", "vllm", "sglang", "openai", "mock"] = "ollama"
    llm_model: str = "qwen3:8b"
    llm_base_url: str = "http://localhost:11434"
    llm_api_key: str = ""
    llm_temperature: float = 0.2
    llm_max_tokens: int = 8192
    llm_context_window: int = 131072
    llm_timeout_seconds: float = 300.0

    vector_backend: Literal["sqlite", "faiss", "memory"] = "sqlite"
    embed_model: str = "BAAI/bge-small-zh-v1.5"
    embed_dim: int = 512
    embed_allow_hash_fallback: bool = True
    embed_batch_size: int = 32

    chunk_size: int = 1024
    chunk_overlap: int = 128
    chunk_strategy: Literal["recursive", "semantic", "code", "sliding"] = "recursive"
    top_k: int = 8
    rerank_enabled: bool = False

    queue_max_concurrency: int = 2

    @field_validator("port", "workers", "llm_context_window", "llm_max_tokens",
                     "chunk_size", "chunk_overlap", "top_k", "queue_max_concurrency")
    @classmethod
    def _positive(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("必须为正整数")
        return v

    @field_validator("chunk_overlap")
    @classmethod
    def _overlap_lt_size(cls, v: int, info) -> int:
        size = info.data.get("chunk_size")
        if size is not None and v >= size:
            raise ValueError("chunk_overlap 必须小于 chunk_size")
        return v

    @property
    def index_dir(self) -> Path:
        return self.data_dir / "index"

    @property
    def ingest_dir(self) -> Path:
        return self.data_dir / "ingest"

    @property
    def collections_dir(self) -> Path:
        return self.data_dir / "collections"

    def ensure_dirs(self) -> None:
        for d in (self.data_dir, self.index_dir, self.ingest_dir, self.collections_dir):
            d.mkdir(parents=True, exist_ok=True)


@lru_cache
def load_settings() -> Settings:
    s = Settings()
    s.ensure_dirs()
    return s
