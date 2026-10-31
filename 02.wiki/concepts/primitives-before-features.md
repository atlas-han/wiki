---
title: "기능보다 기본 단위 먼저 (Primitives Before Features) — 출시가 쉬워진 시대의 제품 일관성"
type: concept
category: pattern
tags: [product-design, product-cohesion, primitives, feature-bloat, enshittification, say-no, verifier, taste, codex, threads]
aliases: [primitives before features, primitive-first, 기본 단위 먼저, 기능 덜어내기, product cohesion, 제품 일관성, enshittification]
related: [verifiable-goals, taste-vs-judgment, product-polish-patterns, slop-cannon, ai-slop, codex, codex-app-server, subagent-vs-thread-handoff, smarter-software-vs-cheaper-software]
first-seen: tech-bridge-ben-davis-codex-product-cohesion
sources: [tech-bridge-ben-davis-codex-product-cohesion]
created: 2026-10-31
updated: 2026-10-31
---

# 기능보다 기본 단위 먼저 (Primitives Before Features)

**모델이 기능을 싸게 찍어 내는 시대에 제품이 망가지는 방식은 기능 부족이 아니라 기능 사이의 이음매이고, 처방은 새 기능보다 먼저 기본 단위(primitive)를 하나로 정하고 나머지를 그 위에 다시 얹는 것**이라는 제품 설계 입장. 이 위키에서는 [[ben-davis|Ben Davis]](추정)의 Codex 비판 [[tech-bridge-ben-davis-codex-product-cohesion]]에서 처음 정리된다. ⚠️ 1인 사용자의 의견이고 성과 사례는 없다.

## 진단 — 왜 이음매가 생기나

세 단계로 이어진다.

1. **출시 비용이 0에 가깝다**: *"It's never been easier to ship a feature, to make something new and put it in production."*(04:31~04:35) *"You give a model a task, it will perform that task."*(04:39~04:41)
2. **모델은 verifier가 없는 판단에 약하다**: *"Anything that can't be expressed with a clean verifier function the models still just aren't amazing at."*(00:52~00:56) 제품 경험 · UI는 *"very hard to encode (…) into a verifier function"*(01:23~01:29). 그래서 *"they're not going to do it in the best possible way, and a lot of weird edges are going to naturally start to form."*(04:42~04:47) → [[verifiable-goals]]의 경계
3. **거절할 비전이 없으면 쌓인다**: *"If you don't have a very strong vision, and especially way to say no to things."*(04:48~04:52) — 결과가 *"enshitification where things just keep getting more and more features and random nonsense"*(04:26~04:31).

증상으로 든 예(전부 Codex · ChatGPT, 화자 체감): 할 일 목록이어야 할 priority view가 최근 기록 타임라인처럼 동작함 · chat / work / Codex로 나뉜 입구 · Spaces 페이지와 thread가 *"trying to stick them together"*(03:58~04:03).

## 처방 — 순서가 있다

| 단계 | 내용 (en-orig) |
|---|---|
| 1. 덜어내기 | *"I would start cutting features before I made new ones."*(05:11~05:16) |
| 2. 기본 단위 하나 | *"A Coda[=Codex] thread should become the base building block for everything (…) for the CLI, for the desktop app, for the web app"*(05:20~05:30) |
| 3. 그 위의 두 번째 primitive | Spaces를 *"a separate primitive sitting over here"*, page는 *"an entity that can then be manipulated by a thread directly"*(05:42~05:55) |
| 4. 결합은 컨텍스트로만 | *"I wouldn't have threads tied directly to the spaces"* — Space에서 발사하면 normal thread가 열리고 Space는 prompt 컨텍스트로 들어간다(06:06~06:20) |
| 5. 위치 무관 | thread는 cloud ↔ local, Spaces는 headless 제어(05:55~06:06) |

요지는 **두 기능을 서로 붙이지 말고, 둘 다 같은 기본 단위를 통해 만나게 하라**는 것이다.

## 이 위키에서의 좌표

- [[codex-app-server]] — OpenAI는 App Server를 *Codex app · CLI · VS Code 확장의 공통 프로토콜* 이라 말한다. **프로토콜 층의 공통 기반**이다. 이 개념은 **제품 층**(사용자가 보는 단위)의 공통 기반을 요구한다. 층이 달라 모순은 아니지만, *하네스가 같아도 제품은 따로 놀 수 있다* 는 관찰이다.
- [[subagent-vs-thread-handoff]] — thread를 작업 단위로 보는 다른 소스들. 여기서는 thread가 **제품 전체의 단위**로 승격된다.
- [[product-polish-patterns]] — 에이전트가 *요청하지 않으면 안 하는* 완성도 목록(개별 화면 수준). 이 개념은 그보다 한 층 위, **기능 사이의 일관성**이다.
- [[slop-cannon]] · [[ai-slop]] — 코드 층에서 *만들기 쉬워서 쌓이는 것* 의 제품 층 판본.
- [[taste-vs-judgment]] — "verifier가 없는 판단은 사람 몫"이라는 입장의 제품 판본. 화자는 *"Maybe eventually someone will figure it out"*(01:29~01:30)이라며 닫지 않는다 → [[taste-encoded-evals]]가 그 시도의 하나.

## ⚠️ 유보

- 한 사람이 한 제품군(Codex · ChatGPT)을 두고 말한 의견이고, 화자 스스로 *"dunking on them"*(04:57)이라 한다. 처방을 적용한 사례 · 결과는 없다.
- *"Coda"* → Codex 판독 추정.
- 화자는 *enshittification*을 **기능 비대**의 뜻으로 느슨하게 쓴다(*"you can call it"*). 이 말의 원래 정의는 이 소스에 없고 위키에도 페이지가 없다.

## References

- [[tech-bridge-ben-davis-codex-product-cohesion]] — first-seen
- [[ben-davis]] · [[codex]] · [[openai]]
- 관련: [[verifiable-goals]] · [[taste-vs-judgment]] · [[product-polish-patterns]] · [[codex-app-server]]
