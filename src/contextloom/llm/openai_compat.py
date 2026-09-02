"""OpenAI 兼容后端（Ollama / vLLM / SGLang / 星火 MaaS 统一协议）。"""

from __future__ import annotations

import httpx

from contextloom.llm.base import BaseLLMBackend, LLMResult


class OpenAICompatBackend(BaseLLMBackend):
    name = "openai"

    def __init__(self, base_url, model, *, api_key: str = "", **kwargs) -> None:
        super().__init__(base_url, model, **kwargs)
        self.api_key = api_key

    async def complete(self, prompt, system=None, stop=None):
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        payload = {"model": self.model, "messages": messages,
                   "temperature": self.temperature, "max_tokens": self.max_tokens,
                   "stream": False}
        if stop:
            payload["stop"] = stop
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            resp = await client.post(f"{self.base_url}/v1/chat/completions",
                                     headers=headers, json=payload)
            resp.raise_for_status()
            data = resp.json()
        choice = data["choices"][0]
        return LLMResult(text=choice["message"]["content"],
                         model=data.get("model", self.model),
                         token_usage=data.get("usage", {}), raw=data)
