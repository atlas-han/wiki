---
title: Grok 4.6
type: entity
category: model
tags: [cursor, spacex, benchmark, cost-efficiency]
sources: [tech-bridge-grokbot-agent-teams, tech-bridge-cursor-legacy-refactoring]
created: 2026-09-01
updated: 2026-09-09
---

# Grok 4.6

[[tech-bridge-grokbot-agent-teams]] 인터뷰 당일 발표된 모델. 소스 서술상 **[[cursor|Cursor]]와 SpaceX의 공동 발표**이며, SpaceX AI 팀과 진행한 **코드 학습을 넘는 범용 훈련** 방향의 연속선.

> ⚠️ Contradiction: Grok 이름·귀속은 소스가 말한 그대로 기록한 것이며 채널 밖에서 독립 확인하지 않았다. [[cursor]]·[[tech-bridge-grokbot-agent-teams]]의 같은 단서를 함께 볼 것.

## Cursor Bench 3.2

| 모델 | 점수 | 평균 작업당 비용 |
|---|---|---|
| **Grok 4.6 xhigh** | **70.8%** | **$2.81** |
| Fable 5 Max | 70.5% | $17.32 |

동등 점수대에서 **약 6배 저렴**. (ko 자막의 "GRT 4.6 ICS"는 "Grok 4.6 extra high"의 ASR.)

## 위키에서 알려진 사실

- 4.5보다 똑똑하면서 **토큰 비용은 동일**하다는 설명.
- [[lauren-tan]] 평가: 엔지니어링 작업에 "훨씬 더 성능이 좋고 정말 정말 빠르다". Fable 등 다른 모델도 병용.
- 함의는 조직 예산 — **가격이 곧 병렬성**이다. 1인이 봇 팀을 유지하는 [[persistent-agent-teams]] 그림은 작업당 비용이 한 자릿수 달러여야 성립한다.
- 결론은 단일 모델이 아니라 **요구에 맞는 모델 조합(mix)**.
- 가격 하락의 수혜자로 **자원이 부족한 스타트업·인디 개발자**가 지목됐다.

## 두 번째 소스 — 그리고 촬영 시점의 앵커가 되다 (2026-09-08 편)

[[tech-bridge-cursor-legacy-refactoring]]에서 Grok 4.6이 다시 나온다. 발표자는 **실행·편집 단계의 기본 선택**으로 쓰고(*"더 빠르고 효율적인 걸 원하니까"*), [[cursor-cloud|cloud agent]]에도 권한다.

> 성능은 강하지만 **Grok를 정말 강력하게 만드는 건 얼마나 싸고 그만한 성능에 얼마나 효율적인가**입니다. 실행 중심 모델인 Composer나 GPT보다는 조금 더 비싸지만, **장시간 작업 수행 능력에 비하면 다른 프런티어 랩들보다 매우 저렴합니다.**

반대편의 선택도 명시된다 — *"보통 [[anthropic|Anthropic]] 모델은 피합니다. 비싸질 수 있어서요."* → [[model-mixing-economics]]

**그리고 이 언급이 그 소스의 촬영 시점을 좁혔다.** 발표자가 *"어제 출시됐다고 말하고 싶네요"* 라 하고, 이 페이지의 원 소스 [[tech-bridge-grokbot-agent-teams]](2026-08-31)는 Grok 4.6을 **그 인터뷰 당일 발표**로 기록한다. → 워크샵은 **2026-09-01 무렵 촬영, 2026-09-08 업로드**로 추정된다. **이 위키에서 소스 간 교차 참조로 촬영 시점을 좁힌 첫 사례다.**

> ⚠️ *"어제"* 에는 발표자 본인의 유보(*"I want to say"*)가 붙어 있어 날짜를 확정하지 않는다.

## References

- [[tech-bridge-grokbot-agent-teams]] · [[cursor]] · [[persistent-agent-teams]]
