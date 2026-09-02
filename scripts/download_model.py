"""辅助：提示如何下载端侧模型（不直接下载权重）。"""

MODEL_HINTS = {
    "spark-x2.5": "在 HuggingFace 搜索 iFlytek/Spark-X2.5，按 vLLM/SGLang/llama.cpp 部署",
    "qwen3": "ollama pull qwen3:8b",
    "llama": "ollama pull llama3.2",
}


def main() -> None:
    for k, v in MODEL_HINTS.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
