---
title: "대규모 코드 변경 (Large-Scale Code Changes)"
type: concept
category: pattern
tags: [multi-repo, code-migration, batch-changes, codemod, vulnerability-remediation, deterministic-scripts, agents, enterprise]
aliases: [large-scale changes, LSC, batch changes, 일괄 변경, 저장소 9만 개, multi-repo changes]
related: [code-knowledge-graph, agentic-search, legacy-code-modernization, ai-vulnerability-discovery, workflow-vs-agent, scripts-that-talk-back, greenfield-vs-brownfield-agent-risk]
first-seen: tech-bridge-sourcegraph-codebase-visibility
sources: [tech-bridge-sourcegraph-codebase-visibility]
created: 2026-10-09
updated: 2026-10-09
---

# 대규모 코드 변경

**하나의 변경(보안 패치·API 이전·표준 정렬)을 수백~수만 개 저장소에 빠짐없이 적용하는 일.** 단일 저장소 안에서 잘 일하는 코딩 에이전트가 이 규모에선 *어디에 적용해야 하는지*부터 보지 못한다는 문제. [[dan-adler|Dan Adler]]([[sourcegraph|Sourcegraph]])가 [[tech-bridge-sourcegraph-codebase-visibility]]에서 제기했다.

> *"Sure, Claude Code can uh make this change, but I have 90,000 repositories to make it in."* (06:24~06:28) — 상위 10위 미국 은행 기술 리더(익명), npm 공급망 취약점에 관해

## 문제 — 변경은 쉽고, 범위가 어렵다

- **에이전트 쪽**: [[claude-code|Claude Code]]류 에이전트는 *"so unbelievably good at (…) solving the smallcale problems that most developers deal with every day"*(05:10~05:19) — 한 저장소 안의 변경은 해결된 문제로 취급된다.
- **조직 쪽**: *"Good luck doing that in 90,000 repositories, mapping out how these code bases all come to together, what's actually living in production across your company"*(06:49~06:59). 수만 저장소는 *"way too much to fit into a context window or even just to clone and GP[=grep] in real time"*(02:45~02:52).
- 그래서 병목은 **편집**이 아니라 **적용 범위의 발견과 완결성 확인**이다 — [[file-discovery-tax|탐색세]]를 저장소 경계 너머로 늘린 것.

## 처방 (화자 진술 — Agentic Batch Changes)

| 요소 | 진술 | en-orig |
|---|---|---|
| 기반 | 저장소 전체의 코드 그래프 + 검색 + *"compiler accurate output"* → [[code-knowledge-graph]] | 08:36~08:44 |
| 진입 | *"execute code changes across hundreds or thousands of repositories at once starting with a single prompt"* | 09:11~09:20 |
| 롤아웃 | 반복적으로, CI 상태·PR 코멘트에 반응해 자가 수정 | 09:22~09:29 |
| ⭐ 분업 | *"Use coding agents where it makes sense, where judgment is needed. Use deterministic scripts where it's not."* | 09:29~09:33 |
| 완결성 | *"tracking and auditability to be sure that you've covered 100% of the places where that patch is needed"* | 09:33~09:41 |

**에이전트와 결정론적 스크립트의 분업**이 핵심이다 — 판단이 필요한 자리만 에이전트, 반복되는 패턴은 스크립트. 이 위키의 [[workflow-vs-agent]](결정론적 워크플로 vs 자율 에이전트)를 **한 작업 안의 부품 단위**로 섞는 형태다.

## 사례 — Mercari (자사 얼리 액세스 사용자)

알려진 GitHub 코드 인젝션 이슈(*"where you have to set environment variables correctly"*)를 아는 저장소 **2곳**에 먼저 적용 → *"go explore the rest of our codebase"* → **잠재 취약점 80개** 추가 발견 → 결정론적 스크립트로 한 번에 일관 패치(10:13~10:44). *"This is like bas this is like config files"* — 설정 파일 수준의 패턴.

> ⚠️ 2 + 80 = 82인데 화자는 이어서 *"across 100 of the places where that risk exists"*(10:39~10:44)라 한다 — "100%"의 ASR 탈락일 수 있다(미확정). 80개는 *"potential"*. 사용자 이름 미발화.

## 이 위키의 다른 페이지와 맞닿는 자리

- **[[ai-vulnerability-discovery]]** — 에이전트가 취약점을 *"uncover and create"*(06:41~06:42)하는 속도가 올라갈수록, 발견 이후의 **전사 패치**가 새 병목이 된다. 발견 쪽 페이지에 **조치 쪽 짝**.
- **[[legacy-code-modernization]]** — 현대화가 *한 시스템을 바꾸는 일*이라면 이것은 *한 변경을 모든 시스템에 넣는 일*.
- **[[greenfield-vs-brownfield-agent-risk]]** — 대기업 브라운필드의 가드레일 논거는 **저장소 하나** 단위다. 저장소 9만 개 사이의 범위 문제는 그 논거 밖에 있다(⚠️ 두 소스 모두 이 경계를 말하지 않는다).

## ⚠️ 유보

- **근거가 자사 제품 발표뿐이다** — 공개 당일의 벤더 진술, 성능·정확도·오탐률 없음.
- *"OpenAI·Anthropic·Cursor는 이 인프라를 만들지 않는다"*(05:00~05:10)는 경쟁 구도 진술 — 이 위키에 확인 소스 없음.
- Google 등에서 오래 써 온 "large-scale changes" 관행과의 관계는 **소스에 없다** — 이 페이지의 이름은 일반 용어를 빌렸을 뿐이다.

## References

- [[tech-bridge-sourcegraph-codebase-visibility]] · [[sourcegraph]] · [[dan-adler]]
- [[code-knowledge-graph]] · [[file-discovery-tax]] · [[ai-vulnerability-discovery]] · [[workflow-vs-agent]]
