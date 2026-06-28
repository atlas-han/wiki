---
title: How engineers at Nextdoor use Codex to build without limits
type: source
tags: [source, openai, codex, agent, case-study, outcome-engineering]
created: 2026-06-27
updated: 2026-06-27
source-url: https://openai.com/index/nextdoor/
source-type: article
author: OpenAI
date-published: 2026-06-09
ingested: 2026-06-27
---

# How engineers at Nextdoor use Codex to build without limits

[[openai|OpenAI]]의 **고객 케이스 스터디**. [[nextdoor|Nextdoor]](110M+ 사용자, 11개국) 엔지니어링이 [[codex|Codex]](GPT‑5.4/5.5 기반)를 어떻게 쓰는지를 [[cory-dolphin|Cory Dolphin]](Head of Engineering)의 발언 중심으로 소개한다. 본 위키의 **첫 OpenAI/Codex/GPT 소스**.

> ⚠️ **성격**: 벤더 마케팅 콘텐츠. 조직·워크플로 변화에 대한 *주장* 위주이며 정량 벤치마크나 기술 디테일은 거의 없다. capability 평가가 아니라 *프레이밍* 자료로 취급한다.

## 핵심 요약

1. **Outcome engineering** — 핵심 메시지. "에이전트를 반복 프롬프팅 → 원하는 결과를 정의하고 함께 engineer". → [[outcome-engineering]] 개념 페이지로 추출.
2. **엔지니어가 스택 위로** — 시스템 전문가에 묶이지 않고 제품 end-to-end 소유. 3개 팀(mobile/frontend/backend) 협업이 필요했던 기능(Opportunity Alerts의 지도 표시)을 1명이 구축. 병목이 엔지니어링 → 전략으로 이동.
3. **재현 어려운 디버깅** — embedded Rust DB·tight race condition·K8s pod 기동 실패 등에 Codex 활용. *"clean environment and harness for investigation"* 제공. GPT‑5.4/5.5의 persistence·deep root-cause 강조.
4. **Fast Mode (Codex + GPT‑5.5)** — 빠른 피드백 루프, 팀이 "addicted".

## 핵심 인용

> "Codex has fundamentally changed how we think about engineering, to the point that we can't even imagine engineering without it." — Cory Dolphin

> "away from iteratively prompting an agent, and towards outcome engineering, where engineers start to think about the result they want to see and work with an agent to engineer that result."

> "We're moving so much faster that the bottlenecks are no longer in engineering. It's really now a question of, how can we identify the right things to build and the right strategy."

> "With GPT‑5.4 and 5.5 … Codex excel[s] at being extremely persistent … diving deep into some seemingly esoteric technical details to arrive at the root cause."

## 등장 개체

- [[cory-dolphin]] — Nextdoor Head of Engineering, 본 글의 유일한 인용 화자
- [[nextdoor]] — 사례 주체, 동네 기반 소셜 플랫폼
- [[openai]] — 발행처, Codex·GPT 제공사
- [[codex]] — OpenAI coding agent (GPT‑5.4/5.5, Fast Mode)

## 관련 개념

- [[outcome-engineering]] — 본 소스에서 추출한 핵심 개념
- [[verifiable-goals]] · [[sprint-contract]] — outcome=verifier 매핑
- [[harness-engineering]] — "harness for investigation" 언급

## References

- 원문: <https://openai.com/index/nextdoor/>
- raw: `01.raw/articles/2026-06-10_How engineers at Nextdoor use Codex to build without limits.md`
