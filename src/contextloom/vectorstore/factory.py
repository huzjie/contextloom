"""向量后端工厂（带共享实例缓存）。"""

from __future__ import annotations

from functools import lru_cache

from contextloom.config.settings import Settings
from contextloom.vectorstore.base import BaseVectorStore


def _build_store(settings: Settings) -> BaseVectorStore:
    backend = settings.vector_backend
    if backend == "sqlite":
        from contextloom.vectorstore.sqlite import SQLiteStore
        return SQLiteStore(settings.index_dir, dim=settings.embed_dim)
    if backend == "faiss":
        from contextloom.vectorstore.faiss import FaissStore
        return FaissStore(dim=settings.embed_dim)
    if backend == "memory":
        from contextloom.vectorstore.memory import MemoryStore
        return MemoryStore()
    raise ValueError(f"未知向量后端: {backend}")


@lru_cache(maxsize=32)
def create_store_cached(backend: str, index_dir: str, dim: int) -> BaseVectorStore:
    """按 (backend, index_dir, dim) 缓存，保证内存/FAISS 后端跨服务共享同一实例。"""
    from contextloom.config.settings import Settings

    s = Settings(vector_backend=backend, data_dir=index_dir, embed_dim=dim, _env_file=None)
    return _build_store(s)


def create_store(settings: Settings) -> BaseVectorStore:
    """创建向量后端；内存/FAISS 后端返回共享实例，SQLite 按路径实例化。"""
    if settings.vector_backend in ("memory", "faiss"):
        return create_store_cached(settings.vector_backend, str(settings.data_dir),
                                   settings.embed_dim)
    return _build_store(settings)
