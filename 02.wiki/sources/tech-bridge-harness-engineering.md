---
title: "Tech Bridge — 하네스 엔지니어링: 지금 최고의 에이전틱 엔지니어를 가르는 것"
type: source
tags: [harness-engineering, agent, ai-layer, ralph-loop, coding-agent]
source-url: https://youtu.be/-pqyzBxddyg
source-type: video
author: Tech Bridge (한국어 자막) · 발표자 추정 Cole Medin
date-published: 2026-06-03
ingested: 2026-06-03
created: 2026-06-03
updated: 2026-06-03
---

# Tech Bridge — 하네스 엔지니어링: 지금 최고의 에이전틱 엔지니어를 가르는 것

[[tech-bridge|Tech Bridge]] 채널이 한국어 자막을 입혀 재배포한 ~17분 영상. 2025년의 화두가 [[context-engineering|context engineering]]이었다면 2026년의 화두는 **[[harness-engineering|harness engineering]]** 이라는 주장으로 시작해, 모델을 감싸는 wrapper 설계의 전 계층(도구 하네스 → AI Layer → 다중 세션 오케스트레이션)을 정리한다.

> 발표자는 영상 안에서 "Cole"로 불리며 [[archon|Archon]]을 *"my open-source harness builder"* 로 소개 → **Cole Medin**으로 추정. 채널 Tech Bridge는 원본(영어 강연)에 한국어 자막을 붙인 것으로 보임. 본 위키에 저장된 트랜스크립트는 **자동 생성 영어 원본 자막(en-orig)** 기반.

## 핵심 takeaways

1. **harness engineering = [[context-engineering|context engineering]]의 진화**. 둘 다 "모델에 올바른 컨텍스트 생태계를 주는 것"이지만, harness engineering은 거기에 **control**(루프·오케스트레이션·sub-agent)과 **mindset 전환**을 더한다. 빠르게 buzzword가 되고 있다는 자기 경계도 포함.

2. **3계층 아키텍처**.
   - **Base LLM** ([[claude-opus-4-7|Claude]], GPT 등) — 순수 추론. 단독으로는 파일시스템 접근·명령 실행 불가.
   - **Tool Harness** — [[claude-code|Claude Code]], Codex 등. 회사가 모델 둘레에 엔지니어링한 하네스. *"도구를 고르는 순간 하네스를 고르는 것"* — 직접 정의하지 않아도 harness engineering의 일부.
   - **AI Layer** — 개발자가 직접 만드는 **최상위 래퍼**. harness engineering의 핵심 영역.

3. **AI Layer 6요소**: Global Rules · Skills & [[model-context-protocol|MCP]] · Codebase Search(LSP / [[code-knowledge-graph|지식 그래프]]) · Hooks · Sub-agents · 온디맨드 Context Docs. *"프로세스나 규칙을 주입하려면 이 6가지 중 하나를 통한다."*

4. **System Evolution 마인드셋** — *"every mistake becomes a rule."* 에이전트가 실수하면 모델 탓("다음 버전 기다리자")을 하는 대신, 실패를 **명시적 규칙**으로 변환해 하네스를 개선한다. 컨벤션 위반 → `agents.md`에 규칙 추가, 파괴적 명령 → pre-tool-use hook으로 차단. 인간이 피드백 루프(센서·리뷰 에이전트·스킬)의 주체가 되어 AI Layer를 지속 진화.

5. **다중 세션 오케스트레이션이 최종 진화**. 거대한 task/PRD를 단일 세션에 몰아넣으면 토큰 비효율 + 모델 과부하 → AI Layer가 아무리 좋아도 무너진다. 대신 역할이 분리된 세션에 **focused task**를 주고 아티팩트로 핸드오프.
   - **PIV 워크플로**: Plan → Implement → Validate를 *각각 별도 세션*으로 (토큰 효율 + 집중). 각 스킬이 markdown 아티팩트를 출력해 다음 세션으로 전달.
   - **[[ralph-wiggum-method|Ralph Loop]]** ([[geoff-huntley|Geoff Huntley]] / 영상 표기 "Jeffrey"): 이 핸드오프·PR 생성을 **자동화**한 하네스. 큰 작업을 세부 태스크로 분할하고 완료 표식(`done` 파일)까지 반복, 병렬 리뷰 에이전트(보안·정확성·단순성) 실행.

6. **Hooks의 실전 용도**(과소사용 지적): ① pre-tool-use 보안 훅(파괴적 명령·민감 파일 차단), ② stop validation 훅(완료 선언 시 테스트·린트·타입체크 강제, 실패 시 재반복), ③ 매 파일 수정 후 lint.

7. **생태계 도구**: [[archon|Archon]](오픈소스 하네스 빌더, Ralph Loop류를 자신의 SDLC에 맞춰 커스텀), Google Cloud Agent CLI(스폰서 — 에이전트 구축 스킬 + 로컬 Playground + 단일 명령 프로덕션 배포).

## 핵심 인용 (en-orig 트랜스크립트)

> A term that's popping up more and more in the AI space right now is harness engineering. It's the next big thing for this year, just like context engineering was for last year.

> Every mistake becomes a rule. ... every mistake becomes an opportunity to improve your harness.

> If you send too much into the LLM at once, it is going to fall flat on its face.

## 등장 개체·개념

- 채널/저자: [[tech-bridge|Tech Bridge]] (발표자 추정 Cole Medin)
- 인물: [[geoff-huntley|Geoff Huntley]] (Ralph 제작자 — 영상은 "Jeffrey Huntley"로 표기)
- 제품·도구: [[claude-code|Claude Code]], Codex, [[archon|Archon]], Google Cloud Agent CLI
- 모델: [[claude-opus-4-7|Claude]], GPT
- 개념: [[harness-engineering]] (메인), [[context-engineering]], [[ralph-wiggum-method|Ralph Loop]], [[model-context-protocol|MCP]], [[code-knowledge-graph]], [[agent-harness-design]]

> ⚠️ Contradiction: 영상은 Ralph 제작자를 "Jeffrey Huntley"로 표기하나, 본 위키는 [[geoff-huntley|Geoff Huntley]](Geoffrey "Geoff" Huntley, ghuntley.com)로 통일. 동일 인물로 판단.

## References

- [원문 영상](https://youtu.be/-pqyzBxddyg)
- 원문 캡처: `01.raw/articles/2026-06-03_하네스 엔지니어링 - 지금 최고의 에이전틱 엔지니어를 가르는 것은 무엇일까요?.md`
- 본 위키 비교 소스: [[anthropic-harness-design-long-running-apps]] (Anthropic 관점의 harness 설계)
