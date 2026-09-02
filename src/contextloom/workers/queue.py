"""基于 asyncio 的轻量后台任务队列。"""

from __future__ import annotations

import asyncio
from collections import deque
from dataclasses import dataclass, field
from typing import Any, Awaitable, Callable

from contextloom.logging import get_logger

logger = get_logger(__name__)


@dataclass
class Job:
    id: str
    fn: Callable[..., Awaitable[Any]]
    args: tuple = field(default_factory=tuple)
    kwargs: dict = field(default_factory=dict)


class TaskQueue:
    def __init__(self, max_concurrency: int = 2) -> None:
        self._queue: deque[Job] = deque()
        self._sem = asyncio.Semaphore(max_concurrency)
        self._workers: list[asyncio.Task] = []
        self._running = False

    async def start(self, worker_count: int = 1) -> None:
        self._running = True
        self._workers = [asyncio.create_task(self._worker()) for _ in range(worker_count)]

    async def stop(self) -> None:
        self._running = False
        for w in self._workers:
            w.cancel()
        await asyncio.gather(*self._workers, return_exceptions=True)

    def submit(self, job: Job) -> None:
        self._queue.append(job)

    async def _worker(self) -> None:
        while self._running:
            if not self._queue:
                await asyncio.sleep(0.1)
                continue
            job = self._queue.popleft()
            async with self._sem:
                try:
                    await job.fn(*job.args, **job.kwargs)
                except Exception:
                    logger.exception("任务 %s 执行失败", job.id)
