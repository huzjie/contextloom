"""示例：通过 REST API 调用。"""
import httpx

BASE = "http://localhost:8000"


def ask(question: str, collection: str = "default"):
    with httpx.Client(timeout=60) as c:
        return c.post(f"{BASE}/queries/ask",
                      json={"question": question, "collection": collection}).json()


if __name__ == "__main__":
    print(ask("你的问题？"))
