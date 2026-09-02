"""vLLM 后端。"""

from contextloom.llm.openai_compat import OpenAICompatBackend


class VllmBackend(OpenAICompatBackend):
    name = "vllm"
