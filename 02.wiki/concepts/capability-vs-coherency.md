---
title: "능력과 일관성 (Capability vs Coherency) — 가장 잘할 때 무엇을 하느냐와 자기가 뭘 하는지 아느냐"
type: concept
category: pattern
tags: [model-evaluation, model-selection, coherency, long-running-agents, theo, gemini-4-neon, gpt-6-2-astra]
aliases: [capability coherency framing, coherency, 일관성, 능력과 일관성, coherency frontier]
related: [model-temperament-routing, jagged-capability-frontier, cost-vs-score-frontier, agent-change-evidence]
first-seen: tech-bridge-theo-gemini-4-neon-capability-vs-coherency
sources: [tech-bridge-theo-gemini-4-neon-capability-vs-coherency]
created: 2026-11-24
updated: 2026-11-24
---

# 능력과 일관성 (Capability vs Coherency)

**모델을 두 축으로 나눠 보는 틀 — *능력(capability)* 은 가장 잘할 때 무엇을 할 수 있느냐, *일관성(coherency)* 은 자기가 지금 뭘 하고 있는지 아느냐.** [[theo|Theo]]가 [[gemini-4|Gemini 4 Neon]]이 왜 좋은지 설명하려고 그린 그래프에서 나왔고, 위키에는 [[tech-bridge-theo-gemini-4-neon-capability-vs-coherency]](2026-11-23 한국어 해설)로 들어왔다. ⚠️ 한 리뷰어의 틀이다 — 축을 재는 방법도 눈금도 소스에 없고, 그래프 설명의 원음(06:06~06:32)은 무캡션이다.

## 정의

*"능력은 가장 잘 할 때 무엇을 할 수 있느냐? 일관성은 자기가 뭘 하고 있는지 아느냐입니다."*(05:44~05:50)

Theo 본인의 말(영어 원음이 캡션에 잡힌 두 곳 가운데 하나): *"the new frontier is not the capability frontier. The new frontier is coherency"*(10:48~10:51) 그는 이 틀을 앞으로 계속 쓰겠다고 한다 — *"we'll be going back to the capability coherency framing a lot going forward"*(10:40~10:44)

## Theo의 배치 (2026-11)

| 자리 | 모델 | 캡션 |
|---|---|---|
| 능력 높음 · 일관성 낮음 | [[openai-astra|GPT-6.2 Astra]] | *"그 그림에서 GPT 6.2 아스트라는 능력은 높지만 일관성이 낮습니다."*(05:53~05:56) |
| 그 반대 | [[muse-wonder|Muse Wonder]] Full | *"뮤즈 원더풀은 그 반대고요."*(05:58) |
| 오른쪽 위 | Neon · [[fable-5-2|Fable]] · [[claude-opus-5-5|Opus]] | *"네온은 페이블, 오퍼스와 나란히 오른쪽 위에 있습니다."*(06:00~06:01) |
| 왼쪽 아래 | Gemini 4 Carbon | *"카본은 왼쪽 아래였습니다."*(06:01~06:03) |

## 일관성이 드러난다고 한 자리

해설이 Neon에서 본 것으로 묶은 셋: *"읽기 쉽게 말하고 오래 일해도 길을 잃지 않고 결국 일을 끝낸다."*(10:34~10:36) 소스의 사례를 이 셋에 맞춰 보면(묶음은 위키의 읽기):

- **읽기 쉽게 말한다** — 3주째 쓰던 *일관성 테스트*(가상 서버의 폴더 생성이 느린 이유)에서 답이 *"6.3초 차이를 만든 원인은 세 가지."*(02:46~02:47) 로 시작했다. 같은 질문에 Astra는 디스크와 상관없는 이야기를 만들어 냈다고 한다.
- **길을 잃지 않는다** — 멈춘 줄 알았던 대화에서 재촉하자 *"대시보드는 이미 두 개 만들었는데 안티 그래비티 연결부에서 채팅이 안 보이고 있었다고요."*(04:36~04:41) — 자기가 어디까지 했고 왜 안 보이는지를 알고 있었다.
- **결국 끝낸다** — TypeScript 컴파일러의 Rust 재작성 최적화: *"네온에게는 같은 출발점에서 같은 목표를 줬습니다. 걸린 시간은 10시간."*(07:01~07:04) Astra는 크기를 줄였지만 속도가 56% 느려졌고, 다시 시키자 변경을 하나도 넣지 못했다.
- **지시의 끝 조건을 놓치지 않는다** — 계획을 블로그 글처럼 쓰되 스킬의 스타일 가이드는 무시하라는 요청에서 *"대부분 모델은 이 마지막 조건을 놓치고 스킬의 흑백 스타일로 돌아갔다고 합니다."*(07:49~07:51)

## 일관성이 가리지 못하는 것

같은 소스가 적은 약점은 이 축 밖에 있다. 코드 구조를 *설명* 하게 하면 72개 주장 가운데 열 개가 틀렸고(13위), 3D는 *"최신 모델들보다 한참 뒤쳐졌다고 합니다."*(09:01~09:03) 그런데도 그 저장소를 가장 많이 개선한 것은 Neon이었다 — *"설명할 때는 틀려도 구현할 때는 확인한다는 게 태오의 해석입니다."*(08:40~08:42) ⚠️ 해석이고 검증되지 않았다.

## 위키의 읽기

- **[[model-temperament-routing]]의 다음 판.** 11-16 편에서 Theo는 Opus와 Fable을 *기질* 로 갈랐다. 이번 틀은 기질이 아니라 **한 축의 높낮이** 로 모델 전체를 줄 세운다 — 그 편에서 남긴 두 모델이 여기서는 같은 구석(오른쪽 위)에 놓인다.
- **11-19 편의 불만에 붙인 이름.** [[tech-bridge-gpt-6-2-astra-launch-day-reactions]]에서 그가 Astra에 적은 불만 셋(엉뚱한 질문을 하고 멈춘다 · 설명을 알아듣기 어렵다 · 제자리를 돈다)과 결론(*분명히 아주 똑똑하다. 그런데 같이 일하기가 괴롭다*)이 *능력은 높고 일관성은 낮다* 는 한 칸으로 정리된다(위키의 읽기).
- **[[jagged-capability-frontier]]와 다른 질문.** 그쪽은 능력이 과제마다 들쭉날쭉하다는 관찰이고, 이쪽은 능력과 별개로 *자기 상태를 아는가* 를 묻는다. 벤치마크 점수가 한 축만 잰다는 점에서 [[cost-vs-score-frontier]]가 비용 축을 더한 것과 같은 종류의 보정이다.

## 미해결

- 일관성을 재는 절차가 없다. Theo의 *일관성 테스트* 는 질문 하나이고 그래프의 배치는 그의 판단이다.
- 사례는 전부 한 사람의 프로젝트 · 기기에서 나왔다. 독립 재현은 소스에 없다.

## References

- [[tech-bridge-theo-gemini-4-neon-capability-vs-coherency]] · [[theo]] · [[gemini-4]] · [[openai-astra]] · [[model-temperament-routing]]
