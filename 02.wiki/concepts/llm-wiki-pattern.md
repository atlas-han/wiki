---
title: LLM Wiki Pattern
type: concept
category: pattern
tags: [knowledge-base, workflow, llm-tooling]
related: [agent-harness-design, memex, code-knowledge-graph, obsidian-cli-workflow]
first-seen: karpathy-llm-wiki-gist
sources: [karpathy-llm-wiki-gist, xda-obsidian-cli-terminal-workflow]
created: 2026-05-25
updated: 2026-07-07
---

# LLM Wiki Pattern

LLM이 점진적으로 유지·확장하는 마크다운 기반 개인 지식 베이스 패턴. 단발성 RAG와 달리 **누적되는 인공물(persistent, compounding artifact)** 을 만든다는 점이 핵심. [[andrej-karpathy|Karpathy]]의 [[karpathy-llm-wiki-gist|2026 gist]]에서 제시. *Knowledge base 형태의 [[agent-harness-design|agent harness]]*로 해석할 수 있다 — schema 문서가 LLM에 운영 규칙을 인코딩한다는 점에서.

## 기본 구조

세 레이어:

1. **Raw sources** — 큐레이션된 원본 문서. LLM은 읽기만 함.
2. **Wiki** — LLM이 작성하는 마크다운 파일들. 요약·개체 페이지·개념 페이지·교차 참조 포함.
3. **Schema** — `CLAUDE.md` 또는 `AGENTS.md` 같은 운영 규칙서. LLM이 위키를 어떻게 다룰지 정의.

## 주요 작업

| 작업 | 설명 | 보통 영향 받는 페이지 수 |
|------|------|------|
| Ingest | 새 소스를 흡수, 관련 페이지 모두 업데이트 | 10~15 |
| Query | 질문에 답하고, 가치 있는 답은 위키로 환원 | 1~3 (필요시 신규 페이지) |
| Lint | 모순·고아·누락 점검 | 가변 |

## 왜 작동하는가

- LLM은 지치지 않고 교차 참조 업데이트를 잊지 않음
- 한 번에 15개 파일을 동시에 다룰 수 있어 "북키핑" 비용이 사실상 0
- 사람의 시간은 큐레이션·방향 설정에 집중

## 다른 접근과의 비교

- **RAG (Retrieval-Augmented Generation)**: 매 질의마다 raw 문서에서 chunk를 retrieve하여 답 생성. 누적 없음.
- **NotebookLM, ChatGPT 파일 업로드**: RAG 변형. wiki 구축 안 함.
- **LLM Wiki**: raw + LLM이 유지하는 중간 wiki 레이어. 질문할수록 자산이 쌓임.

## 도구 스택 (참조)

- [[obsidian|Obsidian]]: 위키 뷰어, 그래프, 위키링크, 플러그인 생태계. [[obsidian-cli-workflow]] 관점에서는 quick capture·search·daily note append를 terminal command로 노출하는 app-aware command surface이기도 하다.
- [[claude-code|Claude Code]] / Codex: 위키를 유지하는 LLM 에이전트
- **qmd**: 마크다운용 로컬 검색 엔진 (BM25 + 벡터 + LLM 재정렬). MCP 서버도 제공.
- **Obsidian Web Clipper**: 웹 기사를 마크다운으로 변환해 `raw/`에 저장
- **Marp / Dataview**: 위키 콘텐츠로부터 슬라이드·동적 테이블 생성

## 이 위키에서의 구현

이 vault 자체가 이 패턴의 인스턴스. 운영 규칙은 [[CLAUDE]]에 정의. 진화 로그는 [[log]] 참조.

## 그래프화: /understand-knowledge

[[understand-anything|Understand-Anything]]의 `/understand-knowledge` 명령은 **Karpathy-pattern wiki를 직접 입력으로 받아** force-directed [[code-knowledge-graph|지식 그래프]] + community clustering을 생성한다. `index.md`에서 wikilink·카테고리를 결정론적으로 파싱한 뒤, LLM(`article-analyzer`)이 암묵 관계·엔티티·claim을 발굴 — [[tree-sitter-llm-hybrid|결정론+의미 하이브리드]]를 wiki에 적용한 형태. 즉 이 LLM-WIKI는 그 도구의 입력이 될 수 있고, `index.md`의 위키링크 밀도가 그래프 품질의 1차 신호가 된다.

## References

- [[karpathy-llm-wiki-gist]]
- [[understand-anything]] · [[code-knowledge-graph]] (LLM Wiki의 그래프 대응물)
