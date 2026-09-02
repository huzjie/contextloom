"""服务健康检查。"""
import sys

import httpx


def main() -> int:
    try:
        r = httpx.get("http://localhost:8000/health", timeout=5)
        ok = r.status_code == 200 and r.json().get("status") == "ok"
        print("healthy" if ok else "unhealthy")
        return 0 if ok else 1
    except Exception as exc:
        print("unreachable:", exc)
        return 1


if __name__ == "__main__":
    sys.exit(main())
