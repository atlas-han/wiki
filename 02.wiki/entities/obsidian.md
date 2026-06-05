---
title: Obsidian
type: entity
category: tool
tags: [knowledge-base, markdown, viewer, wiki]
aliases: [옵시디언]
sources: [karpathy-llm-wiki-gist]
links:
  - https://obsidian.md
created: 2026-05-25
updated: 2026-05-25
---

# Obsidian

로컬 마크다운 vault를 기반으로 한 노트 앱. 백링크·그래프 뷰·플러그인 생태계가 강점. 본 위키의 **사용자 측 뷰어** — 본 vault가 곧 Obsidian vault.

## 위키에서 알려진 사실

- [[llm-wiki-pattern]]에서 사용자가 vault를 읽고, LLM은 옆에서 마크다운을 편집하는 워크플로의 디폴트 뷰어
- 핵심 기능들 ([[karpathy-llm-wiki-gist]]에서 언급):
  - **Graph view** — 허브 페이지, 고아 페이지 시각적 확인
  - **Web Clipper** — 웹 기사를 마크다운으로 변환해 `raw/`로 저장 (본 위키의 `01.raw/articles/`도 이 클리퍼 결과물)
  - **Attachment 다운로드** 핫키 — 이미지를 `raw/assets/` 등에 로컬 저장
  - **Dataview** 플러그인 — frontmatter 기반 동적 테이블
  - **Marp** 플러그인 — 마크다운으로 슬라이드 생성

## Karpathy의 비유

> Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.

## References

- [[karpathy-llm-wiki-gist]]
- [[llm-wiki-pattern]]
