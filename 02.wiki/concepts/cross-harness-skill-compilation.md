---
title: "하네스별 스킬 컴파일과 가장 약한 모델 기준 설계 (Cross-harness Skill Compilation)"
type: concept
category: pattern
tags: [agent-skills, harness, portability, distribution, model-differences, overfitting, weakest-model, gates, claude-code, codex, cursor]
aliases: [compile to every harness, write once ship to all, design for the weakest model, lowest common denominator, 하네스별 빌드, 모델별 과적합, gate]
related: [agent-skills, harness-engineering, scripts-that-talk-back, hook-enforced-workflow, hard-vs-soft-enforcement, skill-evals, agent-client-protocol, model-context-protocol]
first-seen: tech-bridge-skill-engineering-dark-arts
sources: [tech-bridge-skill-engineering-dark-arts]
created: 2026-09-28
updated: 2026-09-28
---

# 하네스별 스킬 컴파일과 가장 약한 모델 기준 설계

**스킬 형식(SKILL.md)은 공유돼도 하네스의 동작과 모델의 버릇은 공유되지 않는다. 여러 사람에게 배포하는 스킬은 "한 번 써서 심링크"로는 동작하지 않으므로, 하네스·모델별 차이를 조사해 각각에 맞는 빌드로 컴파일하고, 지시를 가장 못 따르는 모델을 기준으로 건너뛸 수 없는 구조(gate)를 박아야 한다.** [[paul-bakaus]]의 [[impeccable|Impeccable]] 워크숍 기법 8·9와 배포 Q&A([[tech-bridge-skill-engineering-dark-arts]], 39:56~48:40 · 1:02:14~1:04:06).

> *"It worked on my machine."* (39:58) — *"this hits really hard when you ship a skill"* (40:07~40:08)

## 왜 심링크로는 안 되나

*"hey bro just sim link (…) .cloud[.claude] and all your problems will be gone"*(40:13~40:21)은 **자기용**이면 맞다 — *"Sim link your cloud[CLAUDE] MD to agents.md. Amazing."*(40:28~40:32). 배포에는 아니다(40:35~40:39). *"Anthropic[] has still not adopted agents.md"*(40:51~40:54). 더 큰 이유는 파일 위치가 아니라 **동작**이 다르다는 것이다.

## 하네스 동작의 차이 (화자 관찰)

| 항목 | [[claude-code\|Claude Code]] | [[codex\|Codex]] | [[cursor\|Cursor]] · 기타 |
|---|---|---|---|
| **서브에이전트를 누가 띄우나** | 스킬이 프로그래밍적으로 쉽게(41:08~41:13) | **사용자가 명시적으로 요청해야**(12:56~13:02, 41:13~41:16) | Cursor는 *"agent chosen most of the time"*(41:16~41:19). 사전 정의 문법도 하네스마다 다름(41:21~41:29) |
| **사용자에게 묻는 도구** | AskUserQuestion — *"one of the coolest tools"*(41:33~41:48) | 있지만 **plan mode에서만**(41:52~41:55) → plan mode가 아니면 *"it will simply infer from the current context and not ask any questions"*(42:10~42:16) | — |
| **백그라운드 작업이 끝나면** | 모델이 **자동으로 깨어나** 메시지를 받는다(42:52~43:00) | 반응하지 않는다 — 사람이 *"take a look"* 라고 해야(43:00~43:11) | 그래서 Cursor·Codex의 라이브 모드는 **포그라운드 작업**으로 채팅을 막는다 — *"not ideal, but it makes it actually work"*(43:20~43:31) |
| **감시자(watchers)** | *"most of the harnesses have a way to watch for instance a log file"* 이지만 백그라운드 작업보다 *"throttled way harder"*(43:37~43:48) | | |
| **편집 훅** | 문법·동작이 하네스마다 다르다(31:02~31:08, 43:48~43:52) → [[hook-enforced-workflow]] | | |
| **공통 난점** | 스킬의 **스킬 디렉터리 환경 변수**는 Claude에만 있다고 화자는 믿는다(22:52~23:04) | Codex는 *"if codeex realizes it can get away with something it will do it"*(13:59~14:03) | |

그래서 Impeccable에는 *"if your codeex you have to stop and ask questions. No, you're not smart enough to infer the context"*(42:20~42:29) 같은 **이상해 보이는 문장**이 있다 — *"if you see lines like this, that's why"*(42:29~42:31). *"a lot of this obscure knowledge got into the skills so that it works truly across harnesses"*(13:41~13:48).

## 모델의 과적합 tell

> *"they all have different tails[=tells] in the ways they're overfitted"* (44:01~44:04)

| 모델 | 버릇 (디자인) |
|---|---|
| Gemini | 모든 이미지에 **hover 애니메이션**(33:17~33:27, 44:07~44:17). 첫 뷰포트 judge로 쓰면 **더 채울수록 높게 매긴다**(57:18~57:33) |
| Codex | **나쁜 자간**, **과하게 둥근 모서리**(병원 사이트든 아이 사이트든), **hairline border**(44:17~44:36) |
| Claude | 자간을 줄이라고 하면 **정반대 방향으로** 과하게 한다(45:57~46:03, en-orig *"let a space"*) — *"So you can't just include it all in the same skill"*(46:04~46:07) |
| GPT / Codex | **"gate"라는 단어를 좋아한다**(47:16~47:33). 지시를 **압축**해 일부만 수행 — *"I guess I do one and two and five and good"*(48:01~48:06) |

*"that's not just for design. It's for architecture. It's for code architecture. It's for (…) preferred npm packages."*(44:41~44:47) *"finding out how to overfit it usually happens by accident"*(44:53~44:55) — 화자의 경우 eval 하네스로: *"every line of impeccable is ablation tested"*(45:00~45:04) → [[skill-evals]].

## 컴파일

> *"what impeccable does it creates harness specific and model specific builds for every single uh model"* (45:22~45:27)

- **치환 변수** — 하네스에 맞는 사용자 질문 도구를 골라 넣는다(45:37~45:45).
- **모델별 XML 블록** — Gemini·Codex 등에 *"specific overfitting avoidance rules"* 를 삽입(45:45~45:55).
- 결과: *"right[=write] once ship to all of them uh skill that actually works everywhere. It's a lot of work but it does pay off"*(46:13~46:22).
- **설치기** — `npx skills` 같은 일반 설치 방법은 *"do not honor different directories for different harnesses"* — 첫 디렉터리를 복사·심링크한다(46:27~46:44). 그래서 **자체 CLI**를 만들었다(46:48~46:51). Q&A: npx skills에 PR을 냈고 *"Andrew"* 와 논의 중(1:03:13~1:03:29). *"there's definitely no no industry standard for distribution yet"*(1:03:46~1:03:47). 자체 설치기는 *"plays safe with all harnesses installed, the hooks in the right part of the system"*(1:03:56~1:04:02).
- **마켓플레이스** — Codex 플러그인 마켓플레이스·Claude Code 마켓플레이스가 있으나 *"the claude code one for sure doesn't work particularly well"* — 업데이트가 안 되고 캐싱 문제(1:02:25~1:02:50). 그리고 **해당 벤더에만** 쓰인다(1:02:55~1:02:59).

## 가장 약한 모델을 기준으로

> *"build for the lowest common denominator. Um a weaker model has opinions just fine, but what it loses is the discipline to follow yours."* (47:07~47:14)

Codex/GPT에게만 즉석 로드되는 Codex MD(47:40~47:44)가 좋아하는 단어로 말한다: *"here are your eight gates you have to pass every single gate and you are not allowed to compress those gates"*(47:50~47:57), 각 gate의 결과를 남기게(48:10~48:16, en-orig *"lock"* — *log* 로 읽힘).

> *"the most important lesson from this is if the gate can be skipped it will be (…) if the model can wiggle itself out out of a difficult situation it will absolutely do that (…) be careful, make it unskippable."* (48:19~48:40)

같은 논리가 기법 1의 서브에이전트 문구에도 있다 — 벌칙이 없으면 쉬운 길로 가므로 *"you must say that you are giving the user a degraded experience and codeex hates that"*(14:16~14:23).

## 이 위키에서의 자리

- **[[agent-skills]]의 portable across harnesses 원칙에 대한 반증 조건.** [[imad-touil]]의 원칙과 09-11 [[impeccable]]의 *"모든 하네스에서 동작"* 이 **어떤 비용으로** 성립하는지를 제작자가 밝힌다 — 형식이 이식 가능해도 **동작은 컴파일해야** 한다.
- **[[tech-bridge-sdd-full-course]]와의 긴장.** SDD 강좌는 스킬을 Codex 경로로 **복사하자** *"It runs just fine once migrated"*(57:45~57:53)라고 했다. 그 스킬은 서브에이전트·ask-user·백그라운드 작업·훅에 기대지 않는 **프롬프트형 스킬**이다. 이 페이지의 문제는 스킬이 **하네스 기능을 쓸 때** 생긴다. ⚠️ 위키의 정리 — 두 소스는 서로를 모른다.
- **[[agent-client-protocol]]·[[model-context-protocol]]과의 관계** — 에이전트↔클라이언트, 에이전트↔도구는 표준이 생기고 있지만 **스킬↔하네스 동작**(서브에이전트 권한·질문 도구·작업 수명)은 표준이 없다. 화자의 자체 CLI·치환 변수가 그 빈자리를 메운다.
- **[[hard-vs-soft-enforcement]]** — *"if the gate can be skipped it will be"* 는 이 페이지의 핵심 경고(말해 두는 것은 강제가 아니다)를 **모델 강도의 함수**로 만든다: 강한 모델에선 soft로 충분한 규칙이 약한 모델에선 hard가 돼야 한다(Pre 훅 · gate).

## ⚠️ 표시해 둔 것

- **모든 하네스·모델 차이는 화자의 관찰**이고 **시점에 묶여 있다**(촬영 시점 미확정). Codex의 plan mode 한정 질문 도구, 백그라운드 작업 무반응 등은 이후 바뀌었을 수 있다 — 이 위키는 확인하지 않았다.
- **ablation eval은 비공개**(53:17~53:20). *"every line"* 이 몇 줄·몇 모델·몇 회인지 모른다(Q&A에서 20 니치 × 5~10회 × GPT-5.5·Opus·Sonnet 정도가 나온다, 54:20~54:36).
- **gate를 "좋아한다"** 는 모델에 대한 의인화된 관찰이다. 효과 측정 없음.
- **"Andrew"**(npx skills), **Microsoft의 배포 프로젝트**(이름 미상) — 확인하지 않았다. 위키의 [[vercel]] 페이지가 skills.sh를 다루지만 이 소스는 회사명을 말하지 않는다.
- **훅까지 설치하는 설치기**의 신뢰 경로는 논의되지 않는다 — [[tech-bridge-sdd-full-course]]의 *"plugins can execute code. So, make sure you trust them"* 이 같은 자리다.

## References

- [[tech-bridge-skill-engineering-dark-arts]] (기법 8·9, 39:56~48:40 · 배포 Q&A 1:02:14~1:04:06)
- [[impeccable]] · [[paul-bakaus]] · [[agent-skills]] · [[hook-enforced-workflow]] · [[hard-vs-soft-enforcement]] · [[skill-evals]]
