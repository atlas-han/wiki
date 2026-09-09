---
title: 모델 혼합의 경제학 (Model Mixing Economics)
type: concept
category: framing
tags: [model-selection, cost, planning-vs-execution, agent-swarm, budget]
aliases: [모델 혼합, 계획 모델과 실행 모델, 모델 라우팅]
related: [cloud-agent-delegation, grok-4-6, plan-to-ticket-pipeline, compute-constrained-growth, harness-engineering]
first-seen: tech-bridge-cursor-legacy-refactoring
sources: [tech-bridge-cursor-legacy-refactoring, tech-bridge-grokbot-agent-teams]
created: 2026-09-09
updated: 2026-09-09
---

# 모델 혼합의 경제학

**한 작업 안에서 단계마다 다른 모델을 쓰는 것이 성능이 아니라 예산의 문제로 다뤄진다**는 프레이밍.

> **하나의 더 무거운 모델을 계획(planning)에, 더 실행 중심인 모델을 실제 코드 작성에** 쓰는 것이 전체 예산에 정말 유용합니다. — [[tech-bridge-cursor-legacy-refactoring]]

## 실제 선택이 두 번 시연된다

| 단계 | 고른 모델 | 이유 (소스의 표현) |
|---|---|---|
| **계획** | GPT-5.6 계열 | *"글쓰기에 정말 좋은 모델"* · *"Grok보다 더 나은 작가"* |
| **실행·편집** | [[grok-4-6\|Grok 4.6]] | *"더 빠르고 효율적인 걸 원하니까"* |

그리고 **피하는 선택**도 명시된다:

> 저는 여기서 보통 **[[anthropic|Anthropic]] 모델은 피합니다. 비싸질 수 있어서요.**

## 클라우드는 압력이 더 강하다

> cloud agent는 오래 걸릴 수 있고 **스크린샷과 비디오를 돌려주기 때문에 일반 로컬 에이전트보다 토큰을 더 씁니다.** 그래서 **더 싸고 빠른 모델**을 쓰는 게 좋습니다.

즉 [[cloud-agent-delegation]]의 자기 검증 기능이 **토큰 비용을 올리고, 그것이 모델 선택을 되밀어낸다.** 기능과 경제가 맞물리는 자리다.

⚠️ 주장된 수치 — **마이그레이션 전체에 3~4달러.** 조건(규모·레포)이 명시되지 않는다.

## SQLite 케이스 스터디

> 우리 **에이전트 스웜** 덕분에 이 모델들의 조합으로 SQLite를 재구축할 수 있었고 **Fable 단독이나 GPT-5.5 단독보다 훨씬 저렴했습니다.**

> **모델은 각기 다른 것을 잘하고 각기 다른 것에 활용되어야 합니다.**

⚠️ **수치가 없다.** *"훨씬 저렴"* 뿐이고 블로그 링크는 채팅으로 넘겼다고만 한다. 벤치마크 차트는 화면에만 있고 자막에 값이 없다.

## 이 위키에서의 자리

[[grok-4-6]] 페이지가 이미 기록한 **가격이 곧 병렬성**이라는 논리의 연장이다. 저기서는 *봇 팀을 유지하려면 작업당 비용이 한 자릿수 달러여야 한다* 는 조직 예산의 문제였고, 여기서는 **한 작업 내부에서 단계별로 모델을 갈아 끼우는** 형태로 나타난다.

그리고 이것을 가능하게 하는 것이 [[harness-engineering|하네스]]다 — Cursor는 플랫폼과 모델 사이의 층(도구 실행·캐시 관리·동적 컨텍스트 관리·컨텍스트 조립)을 **cursor harness**라 부르고, 모델 교체가 그 층 위에서 일어난다.

> ⚠️ **당사자 진술.** 모델 유연성을 파는 회사가 모델 유연성이 중요하다고 말하는 구조다. 경쟁 모델의 가격·성능 비교도 판매자 진술이며 독립 확인이 없다.

## References

- [[tech-bridge-cursor-legacy-refactoring]] · [[cursor]] · [[grok-4-6]] · [[tech-bridge-grokbot-agent-teams]]
