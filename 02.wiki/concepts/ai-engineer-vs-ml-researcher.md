---
title: AI 엔지니어 vs 머신러닝 연구원 — 엔진과 자동차 (AI Engineer vs ML Researcher)
type: concept
category: theory
tags: [ai-engineer, career, roles, judgment, systems]
aliases: [엔진과 자동차, AI 엔지니어의 정의, 배선하는 사람]
related: [three-tier-ai-skill-stack, taste-vs-judgment, workflow-vs-agent, agent-knowledge-sourcing, agent-distributed-systems, cognitive-offloading]
first-seen: tech-bridge-ai-engineer-three-tier-skill-stack
sources: [tech-bridge-ai-engineer-three-tier-skill-stack]
created: 2026-09-16
updated: 2026-09-16
---

# AI 엔지니어 vs 머신러닝 연구원

**머신러닝 연구원이 모델(엔진)을 처음부터 학습시킨다면, AI 엔지니어는 이미 있는 모델을 데이터·도구·메모리·가드레일에 배선해 쓸모 있는 시스템(자동차)으로 만드는 사람이다.** [[cedric-clyburn|Cedric Clyburn]]([[ibm|IBM Technology]])이 [[tech-bridge-ai-engineer-three-tier-skill-stack]]에서 직무를 정의한다 — **이 위키가 AI 엔지니어라는 직무 자체의 정의를 받는 첫 소스**다.

## 정의

> **AI 엔지니어는 머신러닝 연구원이 아닙니다.** 연구원은 기초 모델을 처음부터 학습시키고, 논문을 내고, 깊은 수학과 석사 이상을 요구합니다. **AI 엔지니어는 이미 존재하는 모델을 사용해 구축합니다** — 연구자들이 개발한 프론티어 모델이나 오픈소스 모델 같은 것들로. **그 모델을 가져다 유용한 작업을 수행하는 시스템에 배선하는 겁니다.** 데이터에 연결하고, 도구와 외부 정보에 접근을 주고, **메모리 루프와 가드레일**을 붙이고. (01:15~02:17)

> **머신러닝 연구자들이 엔진을 만든다면, AI 엔지니어들은 자동차를 만드는 사람들입니다.** 지금처럼 모델들이 쏟아져 들어오는 시기에는 이 자동차를 만들 수 있는 사람이 절실히 필요합니다. (02:17~02:32)

동사가 **배선(wire)** 이다. 정의의 내용물은 이 위키가 따로 쌓아 온 것들의 목록이다 — 데이터 연결([[retrieval-augmented-generation]]), 도구·외부 정보([[model-context-protocol]]·[[agent-knowledge-sourcing]]), 메모리([[agent-memory]]), 가드레일([[agent-governance-layers]]). **직무 기술서가 위키의 목차와 겹친다.**

## 어려운 것은 코드가 아니라 판단

> **AI 코딩 도구 덕분에 코드 생성이 쉬워졌으므로, 이제 어려운 부분은 코드 자체가 아니라 판단력입니다.** 애플리케이션을 어떻게 구조화할지, 무엇을 만들지, 왜 어떤 접근이 다른 접근보다 나은지. **수업에서 항상 배울 수 있는 건 아니지만, 직접 만들어 보면서 확실히 배울 수 있습니다.** (00:36~01:07)

[[taste-vs-judgment]]의 여섯 입장이 전부 **이미 일하는 사람**의 말이었다면, 이 소스는 **진입 전의 사람**에게 같은 말을 하고 처방이 다르다 — *만들어 보라*. 학위(*"꼭 필요한 것은 아닐 수도"*)와 수업을 밀어내고 **건설을 판단의 학습 경로**로 놓는다. [[cognitive-offloading]]의 우려(도구에 맡기면 학습이 손상된다)에 대한 이 소스의 답은 **무엇을 맡기고 무엇을 남기는가의 경계** — [[read-fluency-for-agent-output]].

## 위키에서의 자리

- 이 위키의 *AI engineer* 는 지금까지 **조직**([[ai-engineer|AI Engineer]] — 컨퍼런스 운영)이거나 **직함**이었다. 이 페이지는 **직무**다. 둘은 무관하다.
- [[agent-distributed-systems]] — 소스의 결론 문장(*"모든 AI 제품은 근본적으로 잘 구조화된 API 호출들"*)이 그 페이지의 전제와 같다.
- [[workflow-vs-agent]] — 직무의 핵심 산출물이 *루프* 라는 것.

## ⚠️ 유보

- **"절실히 필요"** — 수요 주장에 근거가 없다.
- 이 정의는 **모델을 만들지 않는 벤더**([[ibm]])의 채널에서 나온다. *연구원이 아니어도 된다* 는 메시지가 누구에게 유리한지 소스가 다루지 않는다.
- 연구원과 엔지니어 사이의 **중간 직무**(파인튜닝·평가 등)는 언급이 없다.

## References

- [[tech-bridge-ai-engineer-three-tier-skill-stack]] — first-seen
- [[cedric-clyburn]] · [[ibm]]
- 관련: [[three-tier-ai-skill-stack]] · [[taste-vs-judgment]] · [[read-fluency-for-agent-output]] · [[workflow-vs-agent]]
