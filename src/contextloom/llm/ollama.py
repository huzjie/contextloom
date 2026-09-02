"""Ollama 专用后端（/api/chat）。"""

from __future__ import annotations

import httpx

from contextloom.llm.base import BaseLLMBackend, LLMResult


class OllamaBackend(BaseLLMBackend):
    name = "ollama"

    async def complete(self, prompt, system=None, stop=None):
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        payload = {"model": self.model, "messages": messages, "stream": False,
                   "options": {"temperature": self.temperature,
                               "num_predict": self.max_tokens}}
        if stop:
            payload["options"]["stop"] = stop
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            resp = await client.post(f"{self.base_url}/api/chat", json=payload)
            resp.raise_for_status()
            data = resp.json()
        return LLMResult(text=data.get("message", {}).get("content", ""),
                         model=self.model,
                         token_usage={"prompt_tokens": data.get("prompt_eval_count", 0),
                                      "completion_tokens": data.get("eval_count", 0)},
                         raw=data)
