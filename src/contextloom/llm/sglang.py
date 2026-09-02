"""SGLang 后端。"""

from contextloom.llm.openai_compat import OpenAICompatBackend


class SGLangBackend(OpenAICompatBackend):
    name = "sglang"
