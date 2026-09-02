"""异步工具。"""

from __future__ import annotations

import asyncio
from typing import Awaitable, TypeVar

T = TypeVar("T")


async def run_with_semaphore(sem: asyncio.Semaphore, coro: Awaitable[T]) -> T:
    async with sem:
        return await coro
