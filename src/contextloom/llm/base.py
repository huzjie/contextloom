"""LLM 后端基类。"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, AsyncIterator


@dataclass
class LLMResult:
    text: str
    model: str = ""
    token_usage: dict[str, int] = field(default_factory=dict)
    raw: dict[str, Any] = field(default_factory=dict)


class BaseLLMBackend(ABC):
    name = "base"

    def __init__(self, base_url: str, model: str, *, temperature: float = 0.2,
                 max_tokens: int = 8192, timeout: float = 300.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.timeout = timeout

    @abstractmethod
    async def complete(self, prompt: str, system: str | None = None,
                       stop: list[str] | None = None) -> LLMResult:
        ...

    async def stream(self, prompt: str, system: str | None = None) -> AsyncIterator[str]:
        result = await self.complete(prompt, system)
        yield result.text
