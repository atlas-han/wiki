---
title: "에이전트에게 곱해지는 마찰 (Agent Friction Multiplier)"
type: concept
category: pattern
tags: [developer-experience, dev-loop, ci, prompt-caching, rewrite-economics, platform-engineering, agents]
aliases: [마찰은 에이전트를 더 세게 막는다, 계산이 바뀌었다, friction compounds for agents]
related: [codebase-gardening, rust, prompt-caching, hard-vs-soft-enforcement, inference-speed-as-capability, learning-curve-as-feature, structure-sensitive-tests]
first-seen: tech-bridge-theo-coding-is-gardening
sources: [tech-bridge-theo-coding-is-gardening]
created: 2026-11-11
updated: 2026-11-11
---

# 에이전트에게 곱해지는 마찰

**느린 개발 서버 · 무거운 CI · 불안정한 테스트 같은 개발 환경의 마찰은 사람보다 에이전트를 훨씬 세게 막는다. 그래서 예전엔 *본전이 안 맞던* 플랫폼 정비와 재작성이 이제는 맞는다**는 주장. [[theo|Theo]]가 말하고 [[tech-bridge-theo-coding-is-gardening]]이 전한다. 이름은 위키가 붙였다.

> ⚠️ **한 사람의 진술을 해설자가 옮긴 2차 전달이다.** 측정값은 없고 5분 · 5분은 예시다.

## 주장

> *"마찰은 사람보다 에이전트를 훨씬 세게 막습니다. 개발 서버가 뜨는데 5분이 걸리면 에이전트는 확인할 때마다 5분씩 멈춥니다. 캐시 유지 시간이 5분이면 그 사이 캐시도 놓치고요."*(03:34~03:45)

> *"느린 개발 서버, 느리고 무거운 C로는이를 병렬로 돌리기 어렵고 릴리스가 두려우면 머지 버튼을 덜 누르게 됩니다."*(03:45~03:52)[=CI로는 일을]

곱해지는 이유를 위키가 정리하면 셋이다.

| 마찰 | 사람에게 | 에이전트에게 |
|---|---|---|
| 느린 개발 서버(5분) | 하루 몇 번의 기다림 | **확인할 때마다** 멈춤 — 루프 횟수만큼 곱해진다 |
| 캐시 유지 시간(5분) | 무관 | 기다리는 동안 [[prompt-caching\|프롬프트 캐시]]를 놓쳐 다음 호출이 비싸진다 |
| 무거운 CI · 불안정한 테스트 | 짜증 | 병렬 실행이 막히고, 실패 신호가 시끄러워 머지가 줄어든다 |

## 계산이 바뀌었다 — 재작성의 본전

- 예전: Twitch에서는 600~800명이 쓰는 도구라도 다시 쓰는 건 본전이 안 맞았다. Apollo GraphQL 2 → 3 업그레이드는 *"여덟 명 남짓이 한 달 넘게 매달린 일입니다."*(03:08~03:09)
- 지금: *"세 명짜리 팀을 조금 더 빠르게 하려고 타입스크립트를 러스트로 다쓰고 있습니다."*(03:26~03:30)[=다시 쓰고]

재작성 비용은 에이전트가 낮췄다. 마찰 제거의 이득은 에이전트가 키웠다. 두 변화가 같은 방향이라 손익분기점이 크게 움직인다(위키의 읽기).

## 같은 소스의 처방

- **마찰을 지운다**: 시끄러운 테스트 약 43% 삭제(실행 시간 59% ↓) → [[structure-sensitive-tests]] · [[codebase-gardening]]
- **마찰을 대화 한 번으로 지운다**: Twitch 교훈 — *"개발자가 겪는 마찰의 상당수는 대화 한 번과 플랫폼에 작은 변경 하나면 사라진다."*(01:46~01:51)
- **신호는 남긴다**: PR마다 전송량 검사 → [[hard-vs-soft-enforcement]]

## 위키의 다른 페이지와 맞닿는 자리

- [[rust]] — *어려움의 부호가 바뀌었다*(Rust의 학습 곡선이 에이전트 시대에 자산)와 같은 결론(재작성할 만하다)이지만 이유가 다르다. 그쪽은 **컴파일러가 에이전트를 묶어 준다**, 이쪽은 **빠른 루프가 에이전트를 덜 멈추게 한다**.
- [[inference-speed-as-capability]] — 모델 쪽 속도를 능력으로 보는 프레이밍이다. 이 페이지는 **환경 쪽 속도**를 같은 자리에 놓는다.

## References

- [[tech-bridge-theo-coding-is-gardening]] — 2026-11-10, §6 *계산이 바뀌었다*
