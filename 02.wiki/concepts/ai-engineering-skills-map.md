---
title: "AI engineering 네 역량 — Ng 팀의 skills map (AI Engineering Skills Map)"
type: concept
category: theory
tags: [ai-engineering, skills-map, career, coding-agents, software-engineering-fundamentals, trade-offs, error-analysis, evals, context-advantage, andrew-ng]
aliases: [AI engineering skills map, 네 가지 역량, four key skills, 근본적 맥락 우위, fundamental context advantage]
related: [shaping-the-build, ai-engineer-vs-ml-researcher, three-tier-ai-skill-stack, read-fluency-for-agent-output, ai-jobs-impact, production-trace-eval-flywheel, taste-vs-judgment, cognitive-offloading]
first-seen: tech-bridge-andrew-ng-ai-engineering-skills-map
sources: [tech-bridge-andrew-ng-ai-engineering-skills-map]
created: 2026-11-01
updated: 2026-11-01
---

# AI engineering 네 역량 — Ng 팀의 skills map

**AI engineering은 직함이 아니라 모든 개발 직군이 갖출 역량 묶음이고, 그 핵심은 (1) AI 앱 빌드 · 배포, (2) 소프트웨어 공학 기본기, (3) 코딩 에이전트 활용, (4) shaping the build의 넷이다.** [[andrew-ng|Andrew Ng]](제목 · 설명란 · 태그 근거)이 자기 팀의 조사 결과로 [[tech-bridge-andrew-ng-ai-engineering-skills-map]]에서 제시한다. 이 넷을 가르는 기준은 **사람이 근본적인 맥락 우위(fundamental context advantage)를 갖는가**다.

> *"by that I don't mean people that will take on an AI engineering job title, but rather people in all sorts of job roles, including software engineering, front-end, back-end, DevOps, mobile, that will benefit from here having AI engineering skills."*(00:27~00:42)

## 네 역량

| # | 역량 | 왜 (en-orig) |
|---|---|---|
| 1 | **AI 앱 빌드 · 배포** | AI 앱은 *"uncertain"* 하다 — *"Whether you prompt an LLM or train a supervised learning algorithm, you don't know in advance what outcome you get."*(03:30~03:36) 그래서 성능 모니터링과 *"error analysis and eval's loop"*(03:47~03:52)가 실력 차이를 만든다. |
| 2 | **소프트웨어 공학 기본기** | *"what's the read-write ratio, what's a transaction"*(01:32~01:36). 기본기를 모르면 *"the coding agent will make a bunch of trade-offs that you didn't even know it made a trade-off and just bites you later."*(04:37~04:45) |
| 3 | **코딩 에이전트 활용** | *"Third is the ability to use coding agents."*(01:40~01:42) — 발췌에서 따로 풀지는 않는다. |
| 4 | **shaping the build** | *"participating in deciding what to build and also influencing the process by which something gets built."*(01:54~01:58) → [[shaping-the-build]] |

방법(화자 진술): *"we looked at over 10,000 job descriptions"*(00:56~00:59), 구조화 인터뷰 수십 건, 자체 설문, 파트너 대화. ⚠️ 문서 · 링크는 영상에 없다.

## 기준 — 근본적 맥락 우위

> *"one of the key things that distinguishes whether AI will take this over or not is whether or not humans have a fundamental context advantage."*(02:02~02:11)

사람은 고객과의 대화에서 본 표정, 몇 년 전 읽은 시장 보고서처럼 에이전트가 모르는 것을 안다(02:13~02:31). 그래서 *"there's a large set of tasks where humans have a fundamental context advantage that we'll want humans to do for a long time."*(02:54~03:00) 역량 4(무엇을 만들지)가 이 기준의 직접 적용이고, 역량 2(기본기)는 **에이전트가 내린 결정을 알아보는 능력**이다.

## 기본기는 천천히 바뀐다

배포 · 모니터링 · 갱신의 기본 지식은 *"actually changing much slower than the PR hype says."*(04:07~04:09) 비용 · 지연 · 속도 · 신뢰성 사이의 trade-off(04:23~04:25)는 **존재를 알아야 고를 수 있다** — *"until you understand the fundamentals, you often don't even know what trade-offs exist to be made"*(04:28~04:35). 다만 Ng은 이해 없이 짜는 코딩으로 가능해진 것들에도 *"encouraged"*(04:55~04:57)라고 한다.

## 이 위키의 다른 역량 지도와

- [[three-tier-ai-skill-stack]](Clyburn, IBM) — *기초 · AI 특화 · 배포* 의 **학습 순서**. 기초를 건너뛰면 나중에 청구된다는 점이 Ng의 역량 2와 같다. 차이: Clyburn의 표에는 **무엇을 만들지 결정**하는 칸이 없고, Ng의 지도에는 RAG · 쿠버네티스 같은 **기술 목록**이 없다.
- [[ai-engineer-vs-ml-researcher]] — Clyburn은 AI 엔지니어를 **직무**(모델을 배선하는 사람)로 정의했다. Ng은 반대로 **직함이 아니라** 프런트엔드 · 백엔드 · DevOps · 모바일 모두의 역량이라 한다.
- [[read-fluency-for-agent-output]] — 에이전트 출력을 읽을 만큼의 유창성. Ng의 역량 2는 그보다 넓게 **에이전트가 몰래 고른 trade-off를 알아볼 만큼**을 요구한다.
- [[ai-jobs-impact]] — Ng의 08-30 *30~40% task는 AI, 나머지는 보완* 프레임이 개발자 직군에서는 **맥락 우위가 있는 task가 남는다**로 구체화된다.
- [[production-trace-eval-flywheel]] — 역량 1의 *error analysis · eval 루프* 가 실무 소스들에서 갖는 모양.

## ⚠️ 유보

- 조사 방법 · 결과 문서가 영상에 없다. 팀 이름은 ASR *"Y Combinator I"* 로 깨져 있고 DeepLearning.AI로 **판독 추정**한다(태그 · 설명란 근거).
- 역량 3(코딩 에이전트 활용)의 내용은 발췌에 없다.
- 맥락 우위가 *"for a long time"* 남는다는 것은 전망이다. Ng 스스로 카메라가 모든 표정을 기록하는 날을 반농담으로 단서 단다(02:45~02:53).

## References

- [[tech-bridge-andrew-ng-ai-engineering-skills-map]] — first-seen
- [[andrew-ng]] · [[tech-bridge-andrew-ng-ai-opportunity]](skills map *작업 중* 언급)
- 관련: [[shaping-the-build]] · [[three-tier-ai-skill-stack]] · [[ai-engineer-vs-ml-researcher]] · [[read-fluency-for-agent-output]]
