---
title: LLM Wiki Pattern
type: concept
category: pattern
tags: [knowledge-base, workflow, llm-tooling]
related: [agent-harness-design, memex, code-knowledge-graph, obsidian-cli-workflow, company-brain, sweeper-agent, no-silent-write]
first-seen: karpathy-llm-wiki-gist
sources: [karpathy-llm-wiki-gist, xda-obsidian-cli-terminal-workflow, tech-bridge-karpathy-transformers-stanford, tech-bridge-company-brain-security, tech-bridge-agent-to-agent-as-search]
created: 2026-05-25
updated: 2026-09-10
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

## 전사 — 같은 저자의 2023년 scratch pad

[[andrej-karpathy|Karpathy]]가 이 패턴의 gist를 쓴 것은 2026년이지만, [[tech-bridge-karpathy-transformers-stanford]](~2023년 강연)에서 그는 이미 같은 발상을 **아키텍처 문제의 해법**으로 말하고 있었다.

> 머릿속에 담아두는 게 [[transformer|트랜스포머]]의 컨텍스트 길이라면, **어쩌면 우리는 그냥 노트를 주고 거기서 읽고 쓰게 하면 됩니다.**

당시의 프레이밍은 "컨텍스트 길이를 늘리는 200편의 논문 대신 모델에게 노트를 주자"였다. 3년 뒤 [[karpathy-llm-wiki-gist]]는 같은 구조를 **지식 축적**의 문제로 다시 제기한다 — 이번에는 노트가 단발성 메모가 아니라 *누적되는 인공물*이고, 유지보수자가 LLM이다.

두 진술을 나란히 두면 이 패턴이 무엇의 해법인지 선명해진다. scratch pad는 **한 세션 안의** 컨텍스트 한계를 우회하고, LLM wiki는 **세션들 사이의** 망각을 우회한다. 같은 처방(외부 마크다운 + 모델이 읽고 쓴다)이 시간 축만 늘어난 것이다. → [[context-resets-and-compaction]], [[memex]]

## 조직 규모 인스턴스와 자동 파이프라인 (2026-09-10)

2026-09-09 업로드 두 소스가 이 패턴을 **개인 밖으로** 가져간다.

**① [[company-brain|회사 두뇌]]** ([[tech-bridge-company-brain-security]]) — [[promptql|PromptQL]]의 자사 위키가 **5,000페이지, 서로 링크하는 마크다운**이다. Karpathy 패턴에 없던 두 층이 붙는다: **파일별 읽기/쓰기 스코프**(에이전트는 사용자 클레임으로 읽는다), 그리고 **모든 변경에 사람 이름**([[named-human-accountability]]). 그리고 이 vault의 규칙(*LLM이 위키를 전담, 사람은 읽기만*)이 **뒤집힌다** — 에이전트는 제안만 하고 사람이 승인한다([[no-silent-write]]). 이유는 조직에서는 *누가 볼 수 있는가* 와 *누가 책임지는가* 가 생기기 때문이다.

건강 지표도 하나 들어왔다 — **일일 업데이트 수의 추세**. 이 vault의 lint(모순·고아)가 *상태* 를 재는 것이라면 그것은 *성장* 을 잰다. ⚠️ 자사 2개월 데이터, 수치 없음.

**② [[sweeper-agent|청소부 에이전트]]** ([[tech-bridge-agent-to-agent-as-search]]) — 각 비공개 사일로 안의 에이전트가 정책에 따라 **하루의 끝에** 공유해도 되는 정보를 공유 위키로 옮긴다. 발표자 [[jean-denis-greze]]는 *"AI가 자동으로 만드는 위키"* 가 오픈소스 개인 에이전트 세계와 작은 회사 양쪽에서 **즉각적 ROI**를 낼 것이라 본다. 즉 이 패턴의 ingest 단계를 **사일로 경계를 넘는 자동 파이프라인**으로 만든 것이다.

같은 소스가 이 패턴의 **실패 형태**도 준다 — *"LLM이 실수해서 정보 하나가 틀리면 영원히 오염된다."* 에이전트 이름을 Apex→Ivy로 바꿨는데 개인 위키가 한 달째 Apex를 기억한다. 이 vault의 lint 항목 중 *모순* 이 잡을 수 있는 종류이나, **정정이 왜 안 되는가**(메모리 뱅크 어딘가에 남는다)는 lint 밖의 문제다. → [[agent-memory]]

## References

- [[karpathy-llm-wiki-gist]]
- [[understand-anything]] · [[code-knowledge-graph]] (LLM Wiki의 그래프 대응물)
- [[tech-bridge-company-brain-security]] — 조직 규모 인스턴스(5,000페이지·스코프·사람 승인) · [[company-brain]]
- [[tech-bridge-agent-to-agent-as-search]] — 청소부 에이전트·영구 오염 · [[sweeper-agent]]
