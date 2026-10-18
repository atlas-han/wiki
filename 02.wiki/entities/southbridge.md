---
title: Southbridge
type: entity
category: org
tags: [data-pipelines, ai-data-work, harness, open-source, entity-resolution, ontology]
aliases: [Southbridge, South Ridge, Hank Weave, Hank Wave, Hankweave]
links: []
sources: [tech-bridge-just-in-time-ontology]
created: 2026-10-18
updated: 2026-10-18
---

# Southbridge

[[hrishi-olickel|Hrishi Olickel]]이 약 2년 전 창업한 회사다. 데이터 작업에 모델을 넣는 파이프라인을 만든다. 이름은 자막에서 발화된다(*"when I founded Southbridge 2 years ago"* 01:56~02:01, 06:29는 ASR *"South Ridge"*). 설명란에는 회사명이 없다. 공식 사이트는 이 위키가 확인하지 않았다. 이 위키 첫 등장은 [[tech-bridge-just-in-time-ontology]]다.

## 자기 서술

- *"We are best described as obsessives. Obsessives who embed intelligence into pipelines. Pipelines that can scale, they can run over and over again to take work truly off our hands, and pipelines that can mature in cost, performance, and speed all on their own."*(05:16~05:31)
- 작업 체제 셋: write once/run once · write many/run once · write many/run many(*"bread and butter"*)(05:36~06:29). 반복 시스템으로 옮긴 일의 예: *"benchmark design, tracking, coding, to making subtitles for movies that we want to watch"*(06:34~06:40)
- 이력: *"early 3.5 turbo level models"*를 헬스케어 등에서 믿을 만하게 만드는 일 → Hank Weave → *"terabyte scale"*(06:53~07:10)
- 창업 명제의 철회: 단일 보편 스키마 → [[just-in-time-ontology]](04:33)

## Hank Weave (자사 오픈소스 하네스)

- *"building Hank Wave, our open-source harness for data work"*(07:03~07:06)
- *"a harness that takes the fast-moving surface of agent runtimes like Cloud Code[=Claude Code] and Pi, and then exposes a consistent, well-tested log and API interface with checkpointing, rollback, budget enforcement, everything built in."*(16:50~17:04) → [[harness-as-platform]]
- ⚠️ *"for headless data work, Hank Weave, I would say, is still the oldest, most stable, and the most open."*(17:09~17:15) 자사 평가이고 비교 대상의 이름은 없다.
- 실행 단위로 보이는 것: *"a version controlled Hank"*(13:38~13:40). 단계 사이 검사 코드 *"rigs"*와 *"bounded work segments that we call codons"*(19:07~19:11). → [[pareto-surfing]]
- ⚠️ 정식 표기(Hankweave?)와 저장소 주소는 자막만으로 확정하지 않는다.

## 오하이오 entity resolution (⚠️ 자기 보고)

[[jev]]를 넣은 파이프라인. 203,317 케이스, $795(예산 $800, 예상 약 $10,000), 10일, 실행 4,000회 이상, Jev 호출 90,000회, 약 60억 토큰. 상세는 [[tech-bridge-just-in-time-ontology]] 7절.

## References

- [[tech-bridge-just-in-time-ontology]] — first-seen
- [[hrishi-olickel]] · [[jev]] · [[just-in-time-ontology]] · [[pareto-surfing]] · [[harness-as-platform]]
