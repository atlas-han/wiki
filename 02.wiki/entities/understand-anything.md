---
title: Understand-Anything
type: entity
category: tool
tags: [knowledge-graph, code-understanding, multi-agent, claude-code-plugin, developer-tooling]
links:
  - https://github.com/Lum1104/Understand-Anything
  - https://understand-anything.com/
sources: [lum1104-understand-anything, james-ai-explorer-understand-anything]
created: 2026-05-30
updated: 2026-06-01
---

# Understand-Anything

[[lum1104|Lum1104]]가 만든 오픈소스 [[claude-code|Claude Code]] 플러그인. 임의의 코드베이스·지식 베이스·문서를 탐색·검색·질의 가능한 [[code-knowledge-graph|인터랙티브 지식 그래프]]로 변환한다. 슬로건: *"Graphs that teach > graphs that impress."* 출처: [[lum1104-understand-anything]].

## 무엇을 하는가

- 멀티 에이전트 파이프라인이 프로젝트를 스캔 → 모든 파일·함수·클래스·의존성을 노드로 하는 그래프(`.understand-anything/knowledge-graph.json`) 생성
- 웹 대시보드에서 레이어별 색상·검색·클릭으로 시각적 탐색; 노드 선택 시 코드·관계·평문 설명
- 자연어 질의(`/understand-chat`), diff 영향 분석(`/understand-diff`), 온보딩 가이드(`/understand-onboard`), 비즈니스 도메인 추출(`/understand-domain`)
- **그래프는 JSON** — 한 번 커밋하면 팀원은 파이프라인 스킵 (온보딩·PR 리뷰·docs-as-code)

## 핵심 설계

- **[[tree-sitter-llm-hybrid|Tree-sitter + LLM 하이브리드]]**: 구조는 [[tree-sitter|Tree-sitter]]로 결정론적(reproducible + 증분), 의미는 LLM이 담당
- **멀티 에이전트 (5+2)**: `project-scanner` → `file-analyzer`(병렬) → `architecture-analyzer` → `tour-builder` → `graph-reviewer`; `domain-analyzer`·`article-analyzer`는 옵션. → [[generator-evaluator-pattern]]·[[agent-harness-design]] 계열의 응용
- **증분 업데이트**: fingerprint 기반 변경 감지, 바뀐 파일만 재분석, `--auto-update`로 post-commit hook

## LLM wiki 분석 기능

`/understand-knowledge`는 [[llm-wiki-pattern|Karpathy-pattern LLM wiki]]를 force-directed 그래프 + community clustering으로 분석한다. `index.md`에서 wikilink·카테고리를 결정론적으로 파싱한 뒤 `article-analyzer`가 암묵 관계·엔티티·claim을 발굴. → **이 LLM-WIKI 자체가 입력이 될 수 있다.**

## 멀티 플랫폼

[[claude-code|Claude Code]] 네이티브 + Cursor·VS Code+Copilot(auto-discovery), Copilot CLI, Codex·OpenCode·OpenClaw·Antigravity·Gemini CLI·Pi·Vibe·Hermes·Cline·KIMI·Trae (총 15종). `--language`로 en/zh/zh-TW/ja/ko/ru 출력.

## 설치 (Claude Code)

```
/plugin marketplace add Lum1104/Understand-Anything
/plugin install understand-anything
```

## 위키 내 위치

이 환경에는 `understand-anything` 플러그인이 실제로 설치되어 있다 (`/understand`, `/understand-knowledge` 등 스킬 사용 가능). [[llm-wiki-pattern]]을 코드가 아닌 *지식 그래프* 측면에서 보완하는 도구.

## 2차 소스 시각 (사용자 평가)

[[james-ai-explorer-understand-anything|한국어 블로그(James AI Explorer, 2026-05-28)]] 는 같은 도구를 *"1시간 → 5분"* 시간 절감 프레임과 IDE / Sourcegraph 대비 비교표로 재포지셔닝한다. 한국어 사용자에게는 `--language ko` 와 MIT 무료가 결정적 진입 신호. README 가 다루지 않는 *경쟁 도구 포지셔닝* 정보가 추가됨.

## References

- [[lum1104-understand-anything]] (1차, GitHub README)
- [[james-ai-explorer-understand-anything]] (2차, 한국어 블로그)
- [[code-knowledge-graph]] · [[tree-sitter-llm-hybrid]] · [[llm-wiki-pattern]]
