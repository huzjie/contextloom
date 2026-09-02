"""Mock 后端（无模型时的确定性回显）。"""

from __future__ import annotations

from contextloom.llm.base import BaseLLMBackend, LLMResult


class MockBackend(BaseLLMBackend):
    name = "mock"

    async def complete(self, prompt, system=None, stop=None):
        summary = prompt.strip().replace("\n", " ")
        if len(summary) > 200:
            summary = summary[:200] + "..."
        return LLMResult(
            text=f"[mock:{self.model}] 基于 {len(prompt)} 字符上下文的回答：{summary}",
            model=self.model,
            token_usage={"prompt_tokens": max(1, len(prompt) // 4), "completion_tokens": 32},
        )
