"""问答与检索服务。"""

from __future__ import annotations

from contextloom.core.models import Answer, SearchResult
from contextloom.reasoning.engine import ReasoningEngine
from contextloom.services.base import BaseService


class QueryService(BaseService):
    def __init__(self, settings) -> None:
        super().__init__(settings)
        # 复用本服务的 store / embedder，避免多实例导致内存后端检索为空
        self.engine = ReasoningEngine(settings, store=self.store, embedder=self.embedder)

    async def search(self, query: str, collection: str, top_k: int | None = None
                     ) -> list[SearchResult]:
        qvec = (await self.embedder.embed([query]))[0]
        return await self.store.search(qvec, query, collection, top_k or self.settings.top_k)

    async def ask(self, question: str, collection: str) -> Answer:
        return await self.engine.answer(question, collection)
