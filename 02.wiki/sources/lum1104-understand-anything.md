---
title: "Lum1104/Understand-Anything — README"
type: source
tags: [knowledge-graph, code-understanding, multi-agent, claude-code-plugin, tooling]
source-url: https://github.com/Lum1104/Understand-Anything
source-type: docs
date-published: 2026-03-15
ingested: 2026-05-30
created: 2026-05-30
updated: 2026-07-08
---

# Lum1104/Understand-Anything — README

[[understand-anything|Understand-Anything]]의 GitHub README. 임의의 코드베이스·지식 베이스·문서를 **탐색·검색·질의 가능한 인터랙티브 지식 그래프**로 바꾸는 [[claude-code|Claude Code]] 플러그인(및 멀티 플랫폼 도구). 제작자 [[lum1104|Lum1104]]. 슬로건: *"Graphs that teach > graphs that impress."*

## 한 줄 요약

> "You just joined a new team. The codebase is 200,000 lines of code. Where do you even start?"

멀티 에이전트 파이프라인이 프로젝트를 분석해 모든 파일·함수·클래스·의존성의 [[code-knowledge-graph|지식 그래프]]를 만들고, 시각적으로 탐색하는 대시보드를 제공한다. *"Stop reading code blind. Start seeing the big picture."*

## 핵심 인용

> **The goal isn't a graph that wows you with how complex your codebase is — it's a graph that quietly teaches you how every piece fits together.**

> Static analysis and LLMs do what each does best. ([[tree-sitter-llm-hybrid]])

> The graph is just JSON — **commit it once, and teammates skip the pipeline.** Good for onboarding, PR reviews, and docs-as-code.

## 주요 takeaway

1. **코드 → 지식 그래프**: 파일·함수·클래스가 각각 노드. 클릭하면 평문(plain-English) 요약·관계·guided tour를 보여줌. → [[code-knowledge-graph]]
2. **[[tree-sitter-llm-hybrid|Tree-sitter + LLM 하이브리드]]**: 구조적 사실(import/export/정의/call site/상속)은 [[tree-sitter|Tree-sitter]]로 결정론적 추출 → reproducible + fingerprint 기반 증분. 의미적 내용(요약·태그·레이어·도메인·투어)은 LLM 담당.
3. **멀티 에이전트 파이프라인**: `/understand`가 5개 에이전트 오케스트레이션, `/understand-domain`이 6번째 추가. file-analyzer는 병렬(최대 5 동시, 배치당 20-30파일). → [[generator-evaluator-pattern]]·[[agent-harness-design]] 계열.
4. **[[llm-wiki-pattern|Karpathy LLM wiki]] 직접 지원**: `/understand-knowledge`가 이 위키 같은 wiki를 force-directed 그래프 + community clustering으로 분석. `index.md`에서 wikilink/카테고리를 결정론적 파싱 후 LLM이 암묵 관계·엔티티·claim 발굴.
5. **그래프 = 커밋 가능한 JSON**: `.understand-anything/knowledge-graph.json`. 한 번 커밋하면 팀원은 파이프라인 스킵. `intermediate/`·`diff-overlay.json`은 로컬 scratch(커밋 제외). 10MB+는 git-lfs.

## 명령어(slash commands)

| 명령 | 역할 |
|------|------|
| `/understand` | 멀티 에이전트 스캔 → `knowledge-graph.json` 생성 (증분 default, `--language`로 다국어, `--auto-update`로 post-commit hook, 디렉토리 scope 지정) |
| `/understand-dashboard` | 레이어별 색상·검색·클릭 가능한 웹 대시보드 |
| `/understand-chat <q>` | 코드베이스에 자연어 질의 |
| `/understand-diff` | 현재 변경의 영향(ripple) 분석 |
| `/understand-explain <file>` | 특정 파일·함수 deep-dive |
| `/understand-onboard` | 신규 팀원용 온보딩 가이드 |
| `/understand-domain` | 비즈니스 도메인·flow·step 추출 (domain view) |
| `/understand-knowledge <wiki>` | [[llm-wiki-pattern|Karpathy-pattern wiki]] 분석 |

## 멀티 에이전트 (Under the Hood)

| Agent | 역할 |
|-------|------|
| `project-scanner` | 파일 발견, 언어·프레임워크 탐지 |
| `file-analyzer` | 함수·클래스·import 추출, 그래프 노드·엣지 생성 (병렬) |
| `architecture-analyzer` | 아키텍처 레이어 식별 (API/Service/Data/UI/Utility) |
| `tour-builder` | guided learning tour 생성 |
| `graph-reviewer` | 그래프 완전성·참조 무결성 검증 (inline default, `--review`로 full LLM) |
| `domain-analyzer` | 비즈니스 도메인·flow·step 추출 (`/understand-domain`) |
| `article-analyzer` | wiki 글에서 엔티티·claim·암묵 관계 추출 (`/understand-knowledge`) |

## 기능 하이라이트

- **Guided Tours** — 의존성 순서로 정렬된 아키텍처 walkthrough
- **Fuzzy & Semantic Search** — 이름·의미로 검색 ("which parts handle auth?")
- **Diff Impact Analysis** — 커밋 전 변경 파급 효과 확인
- **Persona-Adaptive UI** — junior dev / PM / power user에 따라 상세도 조정
- **Layer Visualization** — 아키텍처 레이어별 색상 그룹핑
- **Language Concepts** — 12개 프로그래밍 패턴(generics, closures, decorators 등) 맥락 설명

## 멀티 플랫폼

[[claude-code|Claude Code]] 네이티브(플러그인 마켓플레이스) 외 14종 지원: Cursor·VS Code+Copilot(auto-discovery), Copilot CLI, Codex·OpenCode·OpenClaw·Antigravity·Gemini CLI·Pi·Vibe·Hermes·Cline·KIMI·Trae (`install.sh <platform>`). `~/.understand-anything/repo`에 클론 + 심링크.

## 등장 개체

- **Person/Org**: [[lum1104|Lum1104]] (제작자), Better Stack (커뮤니티 walkthrough 제작)
- **Tool**: [[understand-anything|Understand-Anything]], [[tree-sitter|Tree-sitter]], [[claude-code|Claude Code]], Codex, Cursor, GitHub Copilot, Gemini CLI, git-lfs
- **Concept**: [[code-knowledge-graph]], [[tree-sitter-llm-hybrid]], [[llm-wiki-pattern]], [[generator-evaluator-pattern]], [[agent-harness-design]], [[model-context-protocol]]

## 이 위키와의 관계

`/understand-knowledge`는 정확히 **이 LLM-WIKI 같은 [[llm-wiki-pattern|Karpathy-pattern wiki]]** 를 그래프화하는 명령이다. 즉 이 vault는 Understand-Anything의 입력이 될 수 있다 — `index.md`의 위키링크가 결정론적 파서의 1차 신호. 이 환경에는 `understand-anything` 플러그인이 실제로 설치되어 있어, 본 위키를 `/understand-knowledge`로 그래프화하는 것이 자연스러운 다음 실험.

## References

- [Understand-Anything (GitHub)](https://github.com/Lum1104/Understand-Anything)
- [Homepage + live demo](https://understand-anything.com/)
- [Karpathy LLM wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) → [[karpathy-llm-wiki-gist]]
- [[understand-anything]] · [[lum1104]] · [[code-knowledge-graph]] · [[tree-sitter-llm-hybrid]]
