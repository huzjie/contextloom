"""任务队列测试。"""
import asyncio

import pytest

from contextloom.workers.queue import Job, TaskQueue


@pytest.mark.asyncio
async def test_execute():
    q = TaskQueue(max_concurrency=2)
    done = []
    async def task(x):
        done.append(x)
    await q.start(1)
    q.submit(Job(id="1", fn=task, args=(42,)))
    await asyncio.sleep(0.3)
    await q.stop()
    assert 42 in done
