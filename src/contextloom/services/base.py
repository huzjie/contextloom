"""服务基类。"""

from __future__ import annotations

from contextloom.config.settings import Settings
from contextloom.embedding.factory import get_embedder
from contextloom.vectorstore.factory import create_store


class BaseService:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.store = create_store(settings)
        self.embedder = get_embedder(settings)
