"""LLM 后端工厂。"""

from __future__ import annotations

from contextloom.config.settings import Settings
from contextloom.llm.base import BaseLLMBackend


def create_backend(settings: Settings) -> BaseLLMBackend:
    common = dict(temperature=settings.llm_temperature, max_tokens=settings.llm_max_tokens,
                  timeout=settings.llm_timeout_seconds)
    backend = settings.llm_backend
    if backend == "ollama":
        from contextloom.llm.ollama import OllamaBackend
        return OllamaBackend(settings.llm_base_url, settings.llm_model, **common)
    if backend == "llamacpp":
        from contextloom.llm.llamacpp import LlamaCppBackend
        return LlamaCppBackend(settings.llm_base_url, settings.llm_model, **common)
    if backend == "vllm":
        from contextloom.llm.vllm import VllmBackend
        return VllmBackend(settings.llm_base_url, settings.llm_model, **common)
    if backend == "sglang":
        from contextloom.llm.sglang import SGLangBackend
        return SGLangBackend(settings.llm_base_url, settings.llm_model, **common)
    if backend == "openai":
        from contextloom.llm.openai_compat import OpenAICompatBackend
        return OpenAICompatBackend(settings.llm_base_url, settings.llm_model,
                                   api_key=settings.llm_api_key, **common)
    if backend == "mock":
        from contextloom.llm.mock import MockBackend
        return MockBackend(settings.llm_base_url, settings.llm_model, **common)
    raise ValueError(f"未知 LLM 后端: {backend}")
