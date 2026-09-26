---
title: Post-training의 북극성 (RLHF · RLVR · 보정된 의사결정)
type: concept
category: technique
tags: [post-training, rlhf, rlvr, calibration, objective-function]
related: [rlhf, preference-reward-asymmetry, assistance-vs-automation, sutton-bitter-lesson, decision-quality, jev, system-1-model]
first-seen: tech-bridge-rlhf-assistance-vs-automation
sources: [tech-bridge-rlhf-assistance-vs-automation, tech-bridge-jev-agent-harness]
created: 2026-09-20
updated: 2026-09-26
---

# Post-training의 북극성

**post-training의 갈래를 알고리즘이 아니라 "무엇을 최적화하는가"로 구분하는 틀.** [[diogo-almeida|Diogo Almeida]]가 [[tech-bridge-rlhf-assistance-vs-automation]] Q&A에서 제시했다.

> **LLM [post-training]의 모든 갈래는 각자 최적화하려는 고유한 북극성(northstar)을 가지고 있습니다. 따라서 RLHF는 인간의 선호도를 최적화합니다. RLVR은 순수 정확성의 로그 오류율을 최적화합니다.** (15:56~16:11)

> **하지만 저희는 보정된 의사결정(calibrated decision-making)에 최적화된 세 번째 것을 하고 있는데, 기본적으로 사전 학습된 모델의 지능을 소프트웨어에 실제로 유용하도록 주입하는 것입니다.** (16:11~16:40)

| 갈래 | 북극성 | 이 소스의 판정 |
|---|---|---|
| **RLHF** | 인간 선호 | [[assistance-vs-automation\|보조]]에 탁월, 자동화에 부적합 → [[rlhf]] |
| **RLVR** | 순수 정확성의 **로그 오류율** | *"[[claude-code\|Claude Code]]가 순수하게 RLVR이었다면 완전히 달랐을 것"* (09:10) |
| **제3 ([[typesafe-ai\|TypeSafe]])** | **보정된 의사결정** | ⚠️ **미출시 · 검증 불가** |

## API의 모양이 다르다

> **사실 API의 모양조차 다릅니다. RLHF의 API 모양은 RLVR과 다르고, 그것은 또 우리가 하는 것과도 다릅니다. 그래서 우리는 처음부터 다시 생각하는 것과 같습니다.** (16:40~16:58)

> **우리가 instruction following을 만들어내기 전에는 아무도 instruction following이라는 개념을 생각해 본 적이 없었죠.** 보통 **post-train하는 새로운 방식에 큰 갈래가 생기면, 처음에는 완전히 낯설게 느껴지지만 나중에 돌이켜보면 아주 당연하게 여겨지게 되죠.** (16:58~17:16)

**"목표가 다르면 인터페이스가 다르다"** 는 주장이고, 그래서 이 구분은 학습 내부에 머물지 않고 **모델을 쓰는 쪽의 API까지 바꾼다**는 것이다.

## 위계 — 올바른 작업 > 데이터 > 컴퓨트

같은 자리에서 그 틀의 상위 명제가 나온다:

> **제 생각에 풀스택은 데이터가 연산 능력보다 더 중요하고, 올바른 작업(the right task)을 하는 것이 데이터보다 훨씬 더 중요하다는 것입니다.** (15:49~15:56)

**이 위계가 이 페이지의 존재 이유다** — *무엇을 최적화할지 고르는 것* 이 데이터·컴퓨트보다 앞선다는 주장. → [[sutton-bitter-lesson]]

> ⚠️ 바로 앞 문장에서 화자는 [[sutton-bitter-lesson|Bitter Lesson]]을 **통상과 반대 방향으로 요약한다**(*"알고리즘이 연산 능력보다 더 중요하다"*, 15:38~15:49). ko·en-orig 양 트랙이 일치해 **자막 오류로 보기 어렵지만 판정할 근거가 없다.** 이 위키는 판독하지 않는다.

## 이 위키에서의 좌표

이 위키가 **보정(calibration)** 을 다룬 자리들([[decision-quality]]·[[aleatoric-epistemic-uncertainty]]·[[all-or-nothing-accuracy]])은 전부 **출력을 어떻게 읽을 것인가** 였다. 여기서는 **학습 목표의 이름**으로 쓰인다.

그리고 [[preference-reward-asymmetry]]와 짝을 이룬다 — 선호 최적화가 **불확실성 표현을 벌한다**면, 그 반대 목표는 **보정**일 수밖에 없다.

## ⚠️ 유보

- **제3의 목표에 대해 확인 가능한 것은 이름뿐이다.** 손실 함수·데이터·평가·규모 전부 없다. **이 표의 세 번째 행은 주장이지 관측이 아니다.**
- **RLVR 서술도 한 문장뿐**이다 — *"순수 정확성의 로그 오류율"*.
- 화자는 **그 제3의 것을 파는 회사 소속**이다.
- **2026-09-26:** 같은 회사의 모델 [[jev|Jev]]가 [[tech-bridge-jev-agent-harness]]([[langchain|LangChain]] 소개)로 들어왔다 — *상태 + 질문 → 타입이 지정된 답과 확률*, 텍스트 생성 없음(→ [[system-1-model]]). 이것이 위 *"API의 모양조차 다르다"* 의 구체형일 **수는 있지만**, 그 영상은 학습 목표·보정·Almeida를 **말하지 않는다.** **세 번째 행은 여전히 주장이지 관측이 아니다** — 반환 확률이 보정되어 있는지조차 주장되지 않았다.

## References

- [[tech-bridge-rlhf-assistance-vs-automation]] — first-seen
- [[diogo-almeida]] · [[typesafe-ai]]
- 관련: [[rlhf]] · [[preference-reward-asymmetry]] · [[assistance-vs-automation]] · [[sutton-bitter-lesson]] · [[decision-quality]]
