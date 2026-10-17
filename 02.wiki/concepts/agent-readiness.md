---
title: "에이전트 준비도 (Agent Readiness)"
type: concept
category: pattern
tags: [agent-readiness, codebase-hygiene, ai-adoption, power-law, tests, linters, documentation, reproducible-env]
related: [codebase-gardening, software-factory, greenfield-vs-brownfield-agent-risk, executable-standards, agent-org-adoption, hard-vs-soft-enforcement, ai-slop]
first-seen: tech-bridge-factory-software-factory
sources: [tech-bridge-factory-software-factory, tech-bridge-dx-ai-impact-trends, tech-bridge-tessl-harness-engineering-factory, tech-bridge-factory-bug-report-to-production]
created: 2026-10-02
updated: 2026-10-17
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

## 다른 회사, 같은 점검표 — "예전엔 그냥 좋은 DevEx라 불렀다" (2026-10-03 · [[tech-bridge-dx-ai-impact-trends]])

[[getdx|DX]]의 [[justin-reock|Justin Reock]]이 같은 것을 **플랫폼의 AI 준비도(platform's AI readiness)** 라고 부른다: *"In 2024 we gave everybody a coding assistant. In 2025 we started building agents. Now we're realizing that our infrastructure wasn't ready for any of this."*(13:17~13:27) 준비도를 재면 *"how efficient you're going to be spending tokens and providing context to these agents"*(13:33~13:41)를 더 잘 다룬다고.

| DX 항목 (13:41~13:50) | Factory 항목 (위) |
|---|---|
| *"clear and accurate, well structured documentation"* | 문서화 |
| *"data structures with straightforward relations"* | — (새 항목) |
| *"manageable modular code"* | 코드 스타일 · 깨끗한 코드베이스 |
| *"reliable local CI and non-flaky test suites"* | 테스트 · 린터 · 재현 가능한 환경 |

⭐ *"If, by the way, any of this sounds familiar to you, it's because we used to just call this good developer experience, right? But it turns out that what's good for humans is also good for agents. So we may finally paradoxically be making those investments that we should have been making over the last couple of decades."*(13:50~14:05)

- **에이전트 준비도 = 미뤄 둔 DevEx 투자.** 두 벤더가 독립적으로 거의 같은 목록에 닿았다. Reock의 표현은 이 개념에서 *에이전트 전용* 이라는 인상을 걷어낸다.
- **power law와 같은 그림을 다른 데이터로** — DX는 변경 실패율의 회사별 변동성이 AI 이후 커졌고, 그 갈림은 *"your release pipeline, your automated testing"*(05:29~05:33)에서 온다고 본다: *"The pattern remains the same. the amplitude has changed as a result of AI."*(05:33~05:38) → [[dora-metrics]]
- **느린 CI가 PR을 키운다** — 빌드 45분~1시간이면 AI가 만든 함수 넷을 PR 하나에 몰아넣는다(07:28~07:46). *reliable local CI* 가 점검표에 있는 이유의 구체적 메커니즘.
- ⚠️ 두 회사 모두 이 점검을 **파는** 쪽이다(Factory는 Agent Readiness, DX는 준비도 측정). 독립 연구는 아직 이 위키에 없다.

## 다른 면 — 코드베이스 위생이 아니라 접근·권한·실행 환경 (2026-10-11 · [[tech-bridge-tessl-harness-engineering-factory]])

[[dru-knox|Dru Knox]]([[tessl|Tessl]])의 레이어 2(*"a massive grabag that I call agent it"* 12:39~12:45, 챕터명은 "에이전트 레디 인프라" — ⚠️ 명칭 판독 불가)는 같은 "준비" 문제를 **환경 쪽**에서 본다: 로컬 설정이 많은 프로젝트를 남에게 넘길 때 *"you realize with horror all of the dependencies that you thought were cleanly isolated and are not"*(12:49~12:55) — 에이전트에게도 같다. 항목: CLI·API 접근 · 제품을 클릭해 볼 방법(13:01~13:09) · company brain에 작업 방식 적기(13:32~13:40) · 내부 서비스 접근(거버넌스) · 프로덕션 로그(컴플라이언스) · 코드 실행 환경(13:40~13:59). ⭐ *"I promise it's worse than you think."*(13:10~13:12) 권고는 *"spend a week, spend two weeks and just get it done"*(13:27~13:30).

| | Factory의 agent readiness | Knox의 레이어 2 |
|---|---|---|
| 대상 | 코드베이스 (테스트·린터·문서·스타일·재현 환경) | 조직 환경 (접근·권한·로그·실행 샌드박스·지식) |
| 실패의 모습 | AI가 코드를 더 나쁘게 만든다 | 에이전트가 사람 없이 PR을 못 올린다 |

두 벤더 모두 이 단계를 팩토리의 **선행 조건**으로 둔다. ⚠️ 당사자 진술.

## 8기둥 — 같은 회사의 확장판 (2026-10-17 · [[tech-bridge-factory-bug-report-to-production]])

[[davis-palmie|Davis Palmie]]([[factory-ai|Factory]]): *"At Factory, we have the concept of agent readiness, and we evaluate this based on eight pillars."*(13:23~13:28) 동기는 *"the undertaking of building the Factory will expose tribal knowledge, manual processes, and outdated info. Unblocking these is not only going to help your agents, but it's also going to help your engineering teams."*(13:05~13:21)

| # | 기둥 | en-orig (13:30~14:18) |
|---|---|---|
| 1 | validation | *"Do you have guardrails like linters and formatters in place?"* |
| 2 | build system | *"Are your build commands in CI well documented?"* |
| 3 | feedback loops | *"Do you have unit and integration tests tight?"* |
| 4 | docs | *"do you have docs like read me's, agents.md files?"* |
| 5 | dev environment | *"Are your dev environments cleanly reproducible such that an agent can use them?"* |
| 6 | code modularity | *"Is your code modular with clear boundaries and rules against sprawl?"* |
| 7 | observability | *"How long does it take you to find out why something went wrong?"* |
| 8 | security | *"are you proactively security scanning so that you don't have to worry about leaked secrets or vulnerabilities?"* |

- Tereza(10-01)의 점검표(재현 환경·테스트·문서·스타일·린터)와 DX의 4항목에 **build system(CI 명령 문서화) · observability · security scanning · 모듈 경계(*"rules against sprawl"*)** 가 더해진다.
- 결론은 위 DX 편의 Reock과 같은 쪽이다: *"if your agents and your human engineers are going to walk the same roads, paving them well is doubly useful."*(14:23~14:29) 맺음에서도 *"agent readiness is really a precursor to effective engineering, whether it's an agent or a human that ends up in that system."*(17:19~17:25)이라고 한다.

⚠️ 기둥 이름은 1·2·3·7(*validation*, *build system*, *Feedback loops*, *observability*)만 발화된다. 4·5·6·8의 이름은 질문 내용에서 위키가 붙였다. 점수화 방식, Tereza 판본과 같은 제품인지 개정판인지는 발화되지 않는다. ko는 agent readiness를 **"약제 준비"**(13:24)로 옮긴다.
