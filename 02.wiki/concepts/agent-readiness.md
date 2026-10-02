---
title: "에이전트 준비도 (Agent Readiness)"
type: concept
category: pattern
tags: [agent-readiness, codebase-hygiene, ai-adoption, power-law, tests, linters, documentation, reproducible-env]
related: [codebase-gardening, software-factory, greenfield-vs-brownfield-agent-risk, executable-standards, agent-org-adoption, hard-vs-soft-enforcement, ai-slop]
first-seen: tech-bridge-factory-software-factory
sources: [tech-bridge-factory-software-factory]
created: 2026-10-02
updated: 2026-10-02
---

# 에이전트 준비도 (Agent Readiness)

**코딩 에이전트를 들이기 전에 코드베이스가 에이전트를 받을 준비가 됐는지 보는 위생 점검(hygiene check) — 재현 가능한 개발 환경, 좋은 테스트, 문서화, 일관된 스타일, 린터.** [[factory-ai|Factory]]의 같은 이름 점검 프레임워크를 [[tereza-tizkova|Tereza Tížková]]가 [[tech-bridge-factory-software-factory]]에서 소개했다.

> *"we have something called agent readiness and it's a framework. I don't like the word framework but take it as a hygiene check of your code base and things you should do"* (17:44~17:55)

## 왜 — AI 도입은 power law (16:45~17:39)

> *"when adopting AI, you either succeed big or you can fail big. the same way it's a bit of power law"* (16:49~16:57)

- 코드베이스가 구조화돼 있지 않으면 소프트웨어 팩토리로의 전환이 *"actually make you end up worse and make your code degrading"*(17:04~17:12)
- *"there is a big and growing gap in productivity between those who just adopted AI versus those who actually thought about it a bit more"*(17:12~17:19)
- ⚠️ *"another data from Stanford"*(17:21~17:30) — 문서화·구조 없이는 AI가 코드를 나쁘게 만든다는 데이터. **연구 이름·수치 미발화**
- *"sometimes AI really makes a mess and this can really compound more and more and it's difficult to go back"*(17:32~17:39)

## 점검 항목 (18:06~18:25)

| 항목 | en-orig |
|---|---|
| 개발 환경 재현성 | *"how reproducible is your developer environment"* |
| 테스트 | *"if you have written good tests"* |
| 문서화 | *"if you have all things well documented"* |
| 코드 스타일 | *"what's the style of your code"* |
| 테스트·린터 | *"all the tests and llinters[=linters]"* |
| 그 밖 | *"everything that you would do also to keep code base clean"* |

근거: 코드베이스 상태와 *"how good you're going to adopt the AI and end up productive"* 사이의 *"nice correlation"*(17:55~18:06). ⚠️ 상관의 크기·표본 미발화. 큰 고객들이 점검 후 *"recommended actions"* 를 따른다(18:28~18:37).

## 위키의 다른 페이지와

- **[[codebase-gardening]]** (Lauren Tan) — 같은 직관의 **메커니즘 쪽**: 코드베이스가 에이전트의 기억이고 안티패턴이 바이러스처럼 복제된다 → 린트로 출혈을 막고 정원사를 둔다. Agent Readiness는 그 **도입 전 점검표**이고, 정원 가꾸기는 **도입 후 유지**다.
- **[[greenfield-vs-brownfield-agent-risk]]** — 기존 코드베이스의 위험. power law의 "fail big" 쪽.
- **[[executable-standards]] · [[hard-vs-soft-enforcement]]** — 린터·테스트는 문서보다 강한 강제. 점검표의 절반이 실행 가능한 기준이다.
- **[[agent-org-adoption]]** — 조직 도입의 성패. Tereza의 *"rebuild it from scratch"* 와 같은 축.
- **[[software-factory]]** — 3원칙 중 *always improving* 의 전제 조건.

## 미해결

- 점수화 방식(통과/실패, 등급)과 각 항목의 가중치.
- "Stanford 데이터"가 무엇인지.
- 준비도가 낮은 코드베이스에서 **먼저 에이전트로 준비도를 올리는** 경로가 가능한지(닭과 달걀).

## References

- [[tech-bridge-factory-software-factory]] — first-seen
- [[codebase-gardening]] · [[software-factory]] · [[greenfield-vs-brownfield-agent-risk]] · [[executable-standards]] · [[agent-org-adoption]]
- [[factory-ai]] · [[tereza-tizkova]]
