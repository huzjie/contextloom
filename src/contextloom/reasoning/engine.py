"""跨章节推理引擎：检索 -> 装配 -> 本地 LLM -> 答案。"""

from __future__ import annotations

import time

from contextloom.config.settings import Settings
from contextloom.core.models import Answer
from contextloom.embedding.factory import get_embedder
from contextloom.llm.factory import create_backend
from contextloom.logging import get_logger
from contextloom.reasoning.assembler import ContextAssembler
from contextloom.vectorstore.factory import create_store

logger = get_logger(__name__)


class ReasoningEngine:
    def __init__(self, settings: Settings, *, store=None, embedder=None,
                 backend=None) -> None:
        self.settings = settings
        self.store = store or create_store(settings)
        self.embedder = embedder or get_embedder(settings)
        self.backend = backend or create_backend(settings)
        self.assembler = ContextAssembler(context_window=settings.llm_context_window)

    async def answer(self, question: str, collection: str,
                     top_k: int | None = None) -> Answer:
        start = time.perf_counter()
        top_k = top_k or self.settings.top_k
        qvec = (await self.embedder.embed([question]))[0]
        results = await self.store.search(qvec, question, collection, top_k)
        logger.info("检索到 %d 条相关片段", len(results))
        system, prompt = self.assembler.build_prompt(question, results)
        llm_result = await self.backend.complete(prompt, system=system)
        elapsed = int((time.perf_counter() - start) * 1000)
        return Answer(question=question, answer=llm_result.text, collection=collection,
                      sources=results, backend=self.backend.name, model=llm_result.model,
                      token_usage=llm_result.token_usage, elapsed_ms=elapsed)
