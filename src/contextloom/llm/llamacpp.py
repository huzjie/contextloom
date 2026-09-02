"""llama.cpp server 后端。"""

from contextloom.llm.openai_compat import OpenAICompatBackend


class LlamaCppBackend(OpenAICompatBackend):
    name = "llamacpp"
