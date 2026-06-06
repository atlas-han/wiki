#!/usr/bin/env python3
"""Graphify chris's LLM-WIKI and retrieve graph-grounded context for a query.

This is intentionally dependency-free: it parses Obsidian wikilinks, builds a
page graph, ranks matching pages, then expands across graph neighbors so an
answering agent sees both direct hits and related context.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, cast

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
TOKEN_RE = re.compile(r"[A-Za-z0-9가-힣][A-Za-z0-9가-힣_+.#/-]*")

STOPWORDS = {
    "the", "a", "an", "and", "or", "of", "to", "in", "for", "on", "with",
    "is", "are", "was", "were", "what", "how", "why", "when", "where",
    "이", "그", "저", "것", "수", "등", "및", "에", "의", "를", "을", "은", "는",
    "이야", "뭐야", "어떻게", "알려줘", "설명", "정리", "위키", "wiki",
}

@dataclass
class Page:
    slug: str
    path: str
    title: str
    type: str
    tags: list[str]
    links: list[str]
    summary: str
    text: str


def wiki_root() -> Path:
    return Path(os.environ.get("WIKI_PATH", "/opt/data/wiki")).resolve()


def page_dirs(root: Path) -> list[Path]:
    candidates = [root / "02.wiki"]
    return [p for p in candidates if p.exists()]


def slug_for(path: Path) -> str:
    return path.stem


def parse_frontmatter(text: str) -> dict[str, object]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    data: dict[str, object] = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        k, v = k.strip(), v.strip()
        if v.startswith("[") and v.endswith("]"):
            items = [x.strip().strip('"\'') for x in v[1:-1].split(",") if x.strip()]
            data[k] = items
        else:
            data[k] = v.strip('"\'')
    return data


def body_without_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1)


def first_summary(body: str) -> str:
    lines: list[str] = []
    for raw in body.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("---"):
            if lines:
                break
            continue
        if line.startswith("-") and not lines:
            continue
        lines.append(line)
        if len(" ".join(lines)) > 280:
            break
    return " ".join(lines)[:400]


def load_pages(root: Path) -> dict[str, Page]:
    pages: dict[str, Page] = {}
    for base in page_dirs(root):
        for path in base.rglob("*.md"):
            rel = path.relative_to(root)
            # Keep meta pages available but rank them lower later.
            text = path.read_text(encoding="utf-8", errors="replace")
            fm = parse_frontmatter(text)
            body = body_without_frontmatter(text)
            slug = slug_for(path)
            links = [normalize_link(x) for x in WIKILINK_RE.findall(body)]
            tags_obj = fm.get("tags", [])
            tags: list[str]
            if isinstance(tags_obj, list):
                tags = [str(x) for x in tags_obj]
            elif isinstance(tags_obj, str):
                tags = [tags_obj]
            else:
                tags = []
            pages[slug] = Page(
                slug=slug,
                path=str(rel),
                title=str(fm.get("title") or slug.replace("-", " ")),
                type=str(fm.get("type") or "unknown"),
                tags=tags,
                links=links,
                summary=first_summary(body),
                text=body,
            )
    return pages


def normalize_link(link: str) -> str:
    # Obsidian links may include paths like 02.wiki/engineering/index; use basename.
    return Path(link.strip()).stem


def tokenize(s: str) -> list[str]:
    return [t.lower() for t in TOKEN_RE.findall(s) if t.lower() not in STOPWORDS and len(t) > 1]


def build_graph(pages: dict[str, Page]) -> dict[str, set[str]]:
    graph: dict[str, set[str]] = defaultdict(set)
    aliases = {slug: slug for slug in pages}
    for slug, page in pages.items():
        for link in page.links:
            target = aliases.get(link)
            if target:
                graph[slug].add(target)
                graph[target].add(slug)
    return graph


def score_pages(query: str, pages: dict[str, Page]) -> list[tuple[float, str]]:
    q_tokens = tokenize(query)
    q_counter = Counter(q_tokens)
    scored: list[tuple[float, str]] = []
    for slug, page in pages.items():
        hay_title = f"{page.slug} {page.title} {' '.join(page.tags)}".lower()
        hay_text = page.text.lower()
        score = 0.0
        for tok, weight in q_counter.items():
            if tok in hay_title:
                score += 8.0 * weight
            count = hay_text.count(tok)
            if count:
                score += min(count, 12) * weight
        if page.path.endswith(("index.md", "log.md", "overview.md")):
            score *= 0.55
        if score > 0:
            scored.append((score, slug))
    scored.sort(reverse=True)
    return scored


def expand(seeds: Iterable[str], graph: dict[str, set[str]], depth: int, limit: int) -> tuple[list[str], list[dict[str, object]]]:
    seen: set[str] = set()
    order: list[str] = []
    edges: list[dict[str, object]] = []
    q: deque[tuple[str, int, str | None]] = deque((s, 0, None) for s in seeds)
    while q and len(order) < limit:
        node, d, parent = q.popleft()
        if node in seen:
            continue
        seen.add(node)
        order.append(node)
        if parent:
            edges.append({"source": parent, "target": node, "distance": d})
        if d >= depth:
            continue
        for nb in sorted(graph.get(node, [])):
            if nb not in seen:
                q.append((nb, d + 1, node))
    return order, edges


def make_result(query: str, max_seeds: int, depth: int, limit: int) -> dict[str, object]:
    root = wiki_root()
    pages = load_pages(root)
    graph = build_graph(pages)
    scored = score_pages(query, pages)
    seeds = [slug for _, slug in scored[:max_seeds]]
    selected, traversal_edges = expand(seeds, graph, depth=depth, limit=limit)
    node_payload = []
    score_map = {slug: score for score, slug in scored}
    for slug in selected:
        page = pages[slug]
        node_payload.append({
            "slug": slug,
            "path": page.path,
            "title": page.title,
            "type": page.type,
            "tags": page.tags,
            "score": round(score_map.get(slug, 0.0), 2),
            "summary": page.summary,
            "out_links": [x for x in page.links if x in pages][:20],
        })
    return {
        "query": query,
        "wiki_root": str(root),
        "graphify": {
            "method": "wikilink graph + keyword seed ranking + neighbor expansion",
            "total_nodes": len(pages),
            "total_edges_undirected": sum(len(v) for v in graph.values()) // 2,
            "seed_nodes": seeds,
            "depth": depth,
        },
        "nodes": node_payload,
        "traversal_edges": traversal_edges,
    }


def render_markdown(result: dict[str, object]) -> str:
    gf = cast(dict[str, Any], result["graphify"])
    nodes = cast(list[dict[str, Any]], result["nodes"])
    traversal_edges = cast(list[dict[str, Any]], result["traversal_edges"])
    lines = [
        f"# Graphified LLM-WIKI Query Context",
        f"",
        f"Query: {result['query']}",
        f"Wiki: {result['wiki_root']}",
        f"Graph: {gf['total_nodes']} nodes / {gf['total_edges_undirected']} undirected edges; seeds={', '.join(gf['seed_nodes']) or '(none)'}; depth={gf['depth']}",
        "",
        "## Relevant graph nodes",
    ]
    for node in nodes:
        tags = ", ".join(node["tags"])
        links = ", ".join(f"[[{x}]]" for x in node["out_links"][:8])
        lines.extend([
            f"### [[{node['slug']}]] — {node['title']} (score={node['score']})",
            f"- Path: `{node['path']}`",
            f"- Type/tags: `{node['type']}` / {tags or '(none)'}",
            f"- Summary: {node['summary'] or '(no summary extracted)'}",
            f"- Links: {links or '(none)'}",
            "",
        ])
    lines.append("## Graph traversal edges")
    for edge in traversal_edges[:40]:
        lines.append(f"- [[{edge['source']}]] → [[{edge['target']}]] (distance {edge['distance']})")
    return "\n".join(lines).strip() + "\n"


def render_prompt(result: dict[str, object]) -> str:
    context = render_markdown(result)
    return f"""You are Mnemosyne Query Agent for chris's LLM-WIKI.
Answer in Korean, conclusion-first, using English technical terms where useful.
Use ONLY the graphified wiki context below for claims about chris's wiki. If the context does not contain the answer, say that the LLM-WIKI has no grounded entry for it, then optionally add a clearly labeled general-knowledge note.
Cite wiki pages with [[slug]] links.

{context}

User question: {result['query']}
"""


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description="Graphify LLM-WIKI and retrieve query context")
    p.add_argument("query", help="Question or search terms")
    p.add_argument("--format", choices=["markdown", "json", "prompt"], default="markdown")
    p.add_argument("--max-seeds", type=int, default=6)
    p.add_argument("--depth", type=int, default=1)
    p.add_argument("--limit", type=int, default=18)
    args = p.parse_args(argv)
    result = make_result(args.query, args.max_seeds, args.depth, args.limit)
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif args.format == "prompt":
        print(render_prompt(result))
    else:
        print(render_markdown(result))
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
