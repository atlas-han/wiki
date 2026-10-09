---
title: "도메인 전용 스크립트 (Domain-Specific Scripts)"
type: concept
category: technique
tags: [agent-tools, scripts, root-cause-analysis, tacit-knowledge, developer-experience, rails]
aliases: [domain specific scripts, 도메인 전용 스크립트, 도메인 스크립트, leaky funnel script]
related: [scripts-that-talk-back, feedforward-feedback-steering, human-plumbing, harness-engineering, executable-standards, tools-and-context-over-harness, context-engineering]
first-seen: tech-bridge-rails-harness-engineering
sources: [tech-bridge-rails-harness-engineering]
created: 2026-10-09
updated: 2026-10-09
---

# 도메인 전용 스크립트

**에이전트에게 원시 데이터(DB·문서·코드 조각) 전체를 보여 주는 대신, 사람의 도메인 멘탈 모델을 담은 작은 스크립트 — 안정된 정의로 대상을 분류하는 — 를 주면 분석이 일관되고 정확해진다.** 같은 스크립트가 사람의 암묵지도 드러낸다. [[joel-quenneville|Joël Quenneville]], [[tech-bridge-rails-harness-engineering]] (23:44~27:48).

## 사례 — 새는 깔때기

문서를 들여와 처리·다른 데이터와 연결·내부 게시하는 파이프라인, 자동화율 *"only about 5%"*(24:13~24:17). LLM에게 시스템 전체(⚠️ en 의역: 실제 프로덕션 데이터 포함 — en-orig 결손 구간 24:17~24:29)를 보게 했더니:

> *"It misses the big picture. It sees snippets of a database here, a bit of a document there, uh some source code even here. But every time I ask it questions or ask it to find root causes (…) it doesn't give me a clear picture and it actually gives me contradictory answers."* (24:32~24:50)

화자의 멘탈 모델 — *"we are working with a funnel, a leaky funnel"*(24:59~25:02). 그래서 문서 모집단을 *파이프라인 어디까지 갔고 어디서 떨어졌는지* 로 분류하는 스크립트를 쓰고 LLM에게 그것을 가리켰다 — *"wow, it got so much better"*(25:24~25:27).

## 왜 좋아지나 — 세 가지

| | 발화 |
|---|---|
| ① **안정된 정의** | *"having stable definitions means that its populations are now comparable. It used to not even have a consistent definition of what counted as successfully exited the pipeline. And so anytime two agents were trying to come up with a story, they conflicted."* (25:30~25:47) |
| ② **더 높은 수준의 어휘** | 컬럼·코드 줄 사이의 패턴이 아니라 *"buckets and bales[=bails?] and pipelines and exit points. I gave it a richer set of primitives for thinking and communicating about the work"* (26:04~26:13) |
| ③ **분류 자체** | 같은 이유로 실패한 버킷에서 조사를 시작하는 것이 *"a great way to start digging deeper"* (26:16~26:27) |

## 사람에게도 좋다

> *"this is not just for agents. Having a domain specific script is really good for humans, too. (…) they help address a sort of blind spot that's often in the heads of all of the developers on our team. It's all tacet[=tacit] knowledge."* (26:31~27:13)

같은 출력을 시각화 도구에 넣어 파이프라인 상태를 한눈에 봤다(27:16~27:32). Rails에선 rake 태스크·shebang 스크립트로 프레임워크를 그대로 쓰며 곁가지 스크립트를 쉽게 만든다(27:36~27:48).

## 위키에서의 자리

- **[[scripts-that-talk-back]]** ([[paul-bakaus|Bakaus]]) — 같은 *"스크립트 출력으로 에이전트를 조향"* 계열. Bakaus는 **다음 행동 지시**(절차), Quenneville은 **분류·어휘**(개념)를 준다.
- **[[tools-and-context-over-harness]]** ([[ryan-lopopolo|Lopopolo]]) — 하네스가 아니라 도구·컨텍스트에 투자하라는 주장의 구체적 사례.
- **[[executable-standards]]** — 부족 지식(tribal/tacit)을 문서가 아니라 실행 가능한 것으로 옮긴다는 같은 방향. 이쪽은 표준이 아니라 **진단 어휘**다.
- **[[feedforward-feedback-steering]]** — 결정론적 분류(computational)가 LLM 분석(inferential)을 받치는 혼합형(⚠️ 위키의 배치, 화자는 칸을 지정하지 않았다).

## ⚠️ 유보

- **결과 수치 없음** — *"so much better"* 뿐, 자동화율이 5%에서 얼마가 됐는지 말하지 않는다.
- 프로젝트·회사·도메인 미발화.
- *"bales"* 는 `en` *"dropouts"*, ko "탈영" — bails(이탈)로 판독, 추정.
- ⚠️ en·ko 공유 오류: *"try to find the root cause"*(25:22~25:27)가 `en`·ko에서 **"RuboCop을 찾아라"** 로 — 이 사례를 ko로만 읽으면 린터 이야기가 된다. ko는 *populations comparable* 도 **"두 나라의 인구"** 로 옮겼다.

## References

- [[tech-bridge-rails-harness-engineering]] · [[joel-quenneville]] · [[scripts-that-talk-back]] · [[tools-and-context-over-harness]] · [[executable-standards]]
