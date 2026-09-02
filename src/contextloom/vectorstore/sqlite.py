"""SQLite FTS 关键词 + NumPy 向量后端。"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path

import numpy as np

from contextloom.core.models import Chunk, SearchResult
from contextloom.vectorstore.base import BaseVectorStore


class SQLiteStore(BaseVectorStore):
    name = "sqlite"

    def __init__(self, index_dir: str | Path, dim: int = 512) -> None:
        self._db_path = Path(index_dir) / "contextloom.sqlite3"
        self._db_path.parent.mkdir(parents=True, exist_ok=True)
        self._dim = dim
        self._init_db()

    def _conn(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self._db_path)
        conn.execute("PRAGMA journal_mode=WAL;")
        return conn

    def _init_db(self) -> None:
        with self._conn() as conn:
            conn.executescript(
                """
                CREATE TABLE IF NOT EXISTS chunks (
                    id TEXT PRIMARY KEY,
                    document_id TEXT NOT NULL,
                    collection TEXT NOT NULL,
                    text TEXT NOT NULL,
                    idx INTEGER NOT NULL,
                    heading TEXT DEFAULT '',
                    embedding TEXT DEFAULT '',
                    metadata TEXT DEFAULT '{}'
                );
                CREATE INDEX IF NOT EXISTS idx_chunks_collection ON chunks(collection);
                CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts USING fts5(
                    text, collection, content='chunks', content_rowid='rowid'
                );
                """
            )

    async def add(self, chunks: list[Chunk], collection: str) -> int:
        rows = [(c.id, c.document_id, collection, c.text, c.index, c.heading,
                 json.dumps(c.embedding) if c.embedding is not None else "",
                 json.dumps(c.metadata, ensure_ascii=False)) for c in chunks]
        with self._conn() as conn:
            conn.executemany("INSERT OR REPLACE INTO chunks VALUES (?,?,?,?,?,?,?,?)", rows)
            conn.execute("INSERT INTO chunks_fts(chunks_fts) VALUES('rebuild')")
        return len(rows)

    async def search(self, query_embedding, query_text, collection, top_k):
        with self._conn() as conn:
            fts_rows = conn.execute(
                "SELECT rowid FROM chunks_fts WHERE chunks_fts MATCH ? AND collection = ? LIMIT ?",
                (_fts_query(query_text), collection, top_k * 4),
            ).fetchall()
            fts_ids = {r[0] for r in fts_rows}
            rows = conn.execute(
                "SELECT rowid, id, document_id, text, heading, metadata, embedding "
                "FROM chunks WHERE collection = ?", (collection,),
            ).fetchall()

        qvec = np.asarray(query_embedding, dtype=np.float32)
        qnorm = float(np.linalg.norm(qvec)) or 1.0
        results: list[tuple[float, SearchResult]] = []
        for row in rows:
            rowid, cid, did, text, heading, meta, emb = row
            keyword_bonus = 0.2 if rowid in fts_ids else 0.0
            sim = 0.0
            if emb:
                try:
                    vec = np.asarray(json.loads(emb), dtype=np.float32)
                    if vec.shape[0] == qvec.shape[0]:
                        sim = float(np.dot(qvec, vec) / (qnorm * (np.linalg.norm(vec) or 1.0)))
                except Exception:
                    sim = 0.0
            score = sim + keyword_bonus
            results.append((score, SearchResult(
                chunk_id=cid, document_id=did, text=text, score=score,
                heading=heading, metadata=json.loads(meta or "{}"),
            )))
        results.sort(key=lambda x: x[0], reverse=True)
        return [r for _, r in results[:top_k]]

    async def delete_collection(self, collection: str) -> int:
        with self._conn() as conn:
            cur = conn.execute("DELETE FROM chunks WHERE collection = ?", (collection,))
            conn.execute("INSERT INTO chunks_fts(chunks_fts) VALUES('rebuild')")
            return cur.rowcount

    async def count(self, collection: str) -> int:
        with self._conn() as conn:
            return int(conn.execute(
                "SELECT COUNT(*) FROM chunks WHERE collection = ?", (collection,)).fetchone()[0])


def _fts_query(text: str) -> str:
    tokens = [t for t in text.replace("/", " ").replace("-", " ").split() if len(t) > 1]
    return " OR ".join(f'"{t}"' for t in tokens[:8]) or '" "'
