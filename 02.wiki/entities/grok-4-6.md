---
title: Grok 4.6
type: entity
category: model
tags: [cursor, spacex, benchmark, cost-efficiency]
sources: [tech-bridge-grokbot-agent-teams, tech-bridge-cursor-legacy-refactoring, tech-bridge-lauren-tan-trusting-agents]
created: 2026-09-01
updated: 2026-09-13
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

## 세 번째 소스 — 그리고 촬영 시점 추정의 반증 (2026-09-12 편)

[[tech-bridge-lauren-tan-trusting-agents]]에서 [[lauren-tan]]이 **발표 당일에** 언급한다.

> 저희가 **오늘** Grock 4.6을 발표했습니다. (…) **아주 똑똑하고 벤치마크에서 정말 좋습니다.** 그리고 **토큰당 비용이 4.5와 같은 것으로 알고 있습니다.** 그러니 **같은 비용으로 더 많은 지능**을 얻는 셈이죠.

> ⚠️ *"토큰당 비용이 같다"* 에 **화자 본인의 유보**가 붙어 있다 — *"틀리게 말하는 게 아니길 바랍니다."*

귀속도 다시 확인된다 — **Cursor와 SpaceX AI**:

> 저는 **Cursor와 SpaceX AI**가 비용 대 지능의 파레토 프런티어를 정말 최적화하려는 영역이라고 봅니다. **가장 큰 모델을 만들고 싶은 게 아닙니다 — 돌리는 데 극도로 비싸니까요.**

> ⚠️ 그 소스의 **설명란은 "xAI"** 라고 부르지만 **자막에 "xAI"는 한 번도 나오지 않는다.** 위키는 자막을 따라 **SpaceX AI**로 적는다.

### ⚠️ 위 "2026-09-01 무렵" 추정이 흔들린다

위 절은 [[tech-bridge-cursor-legacy-refactoring]]의 *"어제 출시"* 와 [[tech-bridge-grokbot-agent-teams]]의 **업로드 날짜(2026-08-31)** 를 이어 워크숍 촬영을 09-01 무렵으로 잡았다. 그런데 이 소스는 **Grok 4.6 발표 당일**이면서 동시에 **"이번 달은 아직 12일밖에 안 됐다"** 고 말한다(양 트랙 일치).

**그 추정의 약한 고리는 업로드 날짜를 촬영 날짜로 쓴 것**이다(이 위키가 2026-09-03에 금지한 바로 그것). 이 소스는 **Grok 4.6 발표일이 어떤 달의 12일**임을 시사하지만 **달을 확정할 근거가 없다** — 업로드일(09-12)일 수는 없다(Grok 4.6은 08-31·09-08 업로드분에서 이미 출시된 모델로 논의된다).

→ **어느 날짜도 채택하지 않는다.** 기존 추정은 지우지 않고 **반증 증거와 나란히 둔다.**

## References

- [[tech-bridge-grokbot-agent-teams]] · [[cursor]] · [[persistent-agent-teams]]
