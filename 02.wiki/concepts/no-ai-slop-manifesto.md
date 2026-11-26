---
title: "안티 슬롭 선언 (No AI Slop: A Manifesto) — 다섯 가치 · 슬롭의 정의 · 서명자의 다짐"
type: concept
category: theory
tags: [ai-slop, manifesto, code-review, accountability, disclosure, software-factory, ai-engineer-code-summit, dex-horthy]
aliases: [No AI Slop Manifesto, No AI Slop, anti-slop manifesto, 안티 슬롭 선언, 슬롭 선언, slop manifesto]
related: [ai-slop, software-factory, verification-bottleneck, cognitive-offloading, human-provenance-value, slopcodebench, review-wip-limit, disposable-vs-durable-software]
first-seen: tech-bridge-dex-horthy-twelve-rules-no-slop-factory
sources: [tech-bridge-dex-horthy-twelve-rules-no-slop-factory]
links:
  - https://slopmanifesto.com
created: 2026-11-26
updated: 2026-11-26
---

# 안티 슬롭 선언 (No AI Slop: A Manifesto)

**AI 슬롭에 맞서 일하는 방식을 다섯 가치와 서명자의 다짐으로 적은 글.** [[dex-horthy|Dex Horthy]]가 [[ai-engineer|AI Engineer]] Code Summit 무대에서 공개했다고 전해진다 — 이 위키에는 그 발표의 한국어 해설 [[tech-bridge-dex-horthy-twelve-rules-no-slop-factory]](2026-11-25 업로드)로 처음 들어왔다: *"이 무대에서 덱스는 안티 슬롭 선언을 공개했습니다. 코드 서밋의 연사와 참가자들이 함께 쓴 글입니다."*(09:03~09:07)

> ⚠️ **전부 2차 전달이다.** 아래 문구는 한국어 내레이션이 옮긴 것이고, 위키는 선언문 원문(설명란 링크 slopmanifesto.com — 표기 *No AI Slop: A Manifesto*)을 열지 않았다. 영어 원문의 낱말 · 항목 수 · 순서 · 서명자는 확인하지 않았다. *안티 슬롭 선언* 은 내레이션의 이름이다.

## 본보기

*"2001년 엔지니어 17명이 스키 산장에 모여 애자일 선언을 썼던 것처럼 이번엔 AI 슬롭에 맞서는 선언을 쓰자는 겁니다."*(09:09~09:15) 가치를 *A보다 B* 의 짝으로 적는 형식도 그쪽을 따른 것으로 보인다(위키의 읽기).

## 다섯 가치

*"산출물보다 결과, 속도보다 이해, 모델의 첫 초안보다 내 생각, 쉬운 일보다 더 나은 일, 출력을 땜질하기 보다 시스템을 고치는 것."*(09:18~09:25)

| 덜 | 더 | 위키에서 닿는 곳 |
|---|---|---|
| 산출물 | 결과 | [[outcome-engineering]] |
| 속도 | 이해 | [[cognitive-debt]] |
| 모델의 첫 초안 | 내 생각 | [[cognitive-offloading]] |
| 쉬운 일 | 더 나은 일 | — |
| 출력을 땜질하기 | 시스템을 고치는 것 | [[hard-vs-soft-enforcement]] |

(오른쪽 칸은 위키가 붙인 연결이다 — 선언이 그렇게 말한 것이 아니다.)

## 슬롭의 정의

- ⭐ *"만드는 데 들인 노력보다 받는 사람에게 이해하라고 요구하는 노력이 더 큰 것."*(09:29~09:32)
- *"AI를 썼다고 다 슬롭은 아닙니다. 품질과 읽는 사람의 경험을 책임지지 않고 AI 출력을 넘길 때 슬롭이 됩니다."*(09:33~09:39)
- 발표자의 덧붙임(Horthy 원음 — en-orig 단일 트랙, 교차 확인 없음, 앞이 잘린 조각): *"the slop is asymmetric."*(09:51) AI는 사람의 판단을 대신하지 못하고 *"It can only amplify our judgment, or uh maybe perhaps our lack of judgment in certain cases."*(09:45~09:49)

→ [[ai-slop]] — 물건의 성질이 아니라 만든 쪽과 받는 쪽 사이의 **노력의 비** 로 정의한다.

## 믿음과 원인

- 첫 믿음: 에이전트는 *"한 사람이 평생 리뷰할 수 있는 양보다 많은 일을 하루만에 만들어냅니다."*(10:06~10:09) → [[verification-bottleneck]]
- 슬롭이 생기는 이유 셋: *"빼기보다 더하기에 쏠린 도구, 사람의 한계를 넘으라고 몰아붙이는 압박, 그리고 복리."*(10:13~10:17)
- 복리: 지식 베이스 · 채팅 · 코드의 *"슬롭이 쌓일수록 다음 에이전트가 그걸 읽고 베낍니다."*(10:19~10:21) 끝은 사람의 문제다 — *"그러다 팀은 슬롭과 싸울 의지마저 잃습니다."*(10:23~10:24)

## 서명자의 다짐

1. 생각과 책임: *"모델과 일해도 생각은 내가 하고 AI가 얼마나 도왔든 내 보낸 것은 내가 책임진다."*(10:27~10:31)
2. 밝히기와 확인: *"에이전트가 쓴 걸 보낼 땐 그렇다고 밝히고 중요한 부분은 확인한다."*(10:32~10:34)
3. 받는 쪽의 예의: *"슬롭을 받으면 친절하게 말해주고 먼저 검토해 달라고 한다."*(10:36~10:39) 발표자도 받는 쪽이 아니라 **들은 쪽** 이었던 적이 있다고 한다 — *"덱스는 자기도 그런 말을 들어본 적이 있다고 털어놨습니다."*(10:40~10:42)

## 선을 긋는 자리 — 전부 검토하라는 말은 아니다

- *"검토하지 않은 출력이 다 나쁜 것도 아닙니다. 한 번에 던지는 프롬프트나 바이브 코딩은 지렛대가 큰 도구입니다."*(11:28~11:33) → [[disposable-vs-durable-software]] · [[vibe-vs-agentic-coding]]
- *"슬롭이 나쁜 건 결과를 망칠 때입니다. 쓸모 있는 제품, 유지보수할 수 있는 시스템, 서로의 시간을 아끼는 일을 망칠 때요."*(11:35~11:40)
- 재는 것: *"중요한 건 코드 줄수나 머지한 PR 수, 동시에 돌리는 에이전트 수가 아니라 무엇을 내보냈고 누가 쓰고 그게 어떻게 돕는가입니다."*(11:20~11:26)
- 마지막 문장: *"우리 중 누구도 이걸 다 알아내지 못했다. 각자 무엇을 받아들이고 무엇을 거절할지 다시 배우는 중이다."*(11:44~11:48)

⚠️ 위 네 줄 가운데 어디까지가 선언의 문구이고 어디부터가 발표자나 해설의 말인지는 캡션으로 가를 수 없다 — 내레이션이 선언이라고 밝힌 것은 마지막 문장뿐이다.

## 위키에서의 자리

- **같은 행사, 다른 답.** [[lauren-tan|Lauren Tan]]의 [[tech-bridge-lauren-tan-all-code-is-slop]]은 슬롭 판정을 사람 눈에서 검사로 옮기자고 했다. 선언은 반대로 **사람의 책임과 밝히기** 를 적는다. 발표자의 규칙 12가지는 둘을 다 넣는다(기계가 잡을 건 기계에게 · 사람이 끝까지 쥐는 판단) → [[software-factory]]
- **밝히기.** *에이전트가 썼다고 밝힌다* 는 다짐은 [[human-provenance-value]]가 말하는 출처의 값과 닿는다 — 읽는 사람이 어디에 주의를 쓸지 고르게 해 준다(위키의 읽기).
- **측정 쪽의 짝.** 선언이 태도라면 [[slopcodebench]]는 같은 발표에서 든 수치다(최고 모델 16.33%).

## 미해결

- 원문의 문구 · 서명자 · 서명 수 · 공개 날짜. *연사와 참가자들이 함께 쓴 글* 이라는 한 줄 말고는 작성 과정이 소스에 없다.
- 다짐이 조직의 규칙(PR 템플릿 · 리뷰 정책)으로 옮겨진 사례는 소스에 없다.

## References

- [[tech-bridge-dex-horthy-twelve-rules-no-slop-factory]] · [[ai-slop]] · [[dex-horthy]] · [[software-factory]]
- 설명란 링크(위키 미열람): *No AI Slop: A Manifesto* https://slopmanifesto.com
