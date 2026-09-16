---
title: 스위스 치즈 모델 — AI 안전의 심층 방어 (Swiss Cheese Defense in Depth)
type: concept
category: pattern
tags: [ai-safety, defense-in-depth, security, kill-switch, layers, time]
aliases: [스위스 치즈 모델, 심층 방어, defense in depth]
related: [embedded-external-evaluators, training-time-risk, transcript-classifier, deny-and-continue, prompt-injection, project-glasswing, agent-governance-layers, slowdown-within-lead-margin]
first-seen: tech-bridge-dario-amodei-cbs-interview
sources: [tech-bridge-dario-amodei-cbs-interview]
created: 2026-09-16
updated: 2026-09-16
---

# 스위스 치즈 모델 — AI 안전의 심층 방어

**AI의 위험에서 우리를 지켜 줄 단 하나의 것은 없다. 구멍 난 방어층을 여러 장 겹치면 구멍이 어긋나 전체를 뚫기 어려워진다 — 그리고 층을 더 쌓는 데 필요한 것이 시간이다.** [[dario-amodei|Dario Amodei]]가 [[tech-bridge-dario-amodei-cbs-interview]]에서 **킬 스위치 무용론**에 답하며 제시한다.

## 맥락 — 킬 스위치는 한 장이다

진행자: *"AI 모델이 충분히 강력하면 중단 시도를 우회할 수 있고, 시뮬레이션에서도 봤다. 전혀 효과가 없을 수도 있다."*(11:18~11:25)

> 우리는 이것을 **심층 방어(defense in depth)** 로 생각합니다. 보안 커뮤니티에 **스위스 치즈 모델**이라는 개념이 있습니다. 한 장은 어떤 것을 막지만 구멍이 있습니다. **다섯 장을 겹치면 각 층의 구멍이 서로 다른 자리에 있어서 치즈 더미 전체를 뚫고 지나가기가 매우 어렵습니다.** (11:26~11:50)

> **AI의 위험에서 우리를 지켜 줄 단 하나의 것은 없습니다. 스택의 위아래 전 구간에서 조심해야 합니다.** 어떤 방어도 완벽하지 않지만, **모든 곳에서 조심한다면 — 그것이 추가 시간을 확보하면 할 수 있는 일인데 — 잘 풀릴 수 있습니다.** (11:54~12:14)

킬 스위치에 대한 위치가 이것으로 정해진다 — *"좋은 생각일 수 있다"*, *"만병통치약은 아니다"*, *"유일한 것도 아니다"*(10:57~11:16). **우회 가능성은 그 층을 버릴 이유가 아니라 다른 층이 필요한 이유**다.

## 이 위키의 층들 — 처음으로 한 스택으로 불린다

이 위키의 안전 장치는 각각 따로 들어왔다. 이 페이지가 그것들을 **한 더미의 치즈**로 본다.

| 층 | 페이지 | 어디를 막는가 |
|---|---|---|
| 훈련 게이트 | [[training-time-risk]] | 훈련 실행 여부 |
| 외부 관찰 | [[embedded-external-evaluators]] | 약속 이행 |
| 공개 보류 | [[project-glasswing]] · [[claude-mythos-preview]] | 배포 여부 |
| 행동 분류기 | [[transcript-classifier]] · [[deny-and-continue]] | 실행 중 행동 |
| 입력 방어 | [[prompt-injection]] 2층 방어 | 외부 콘텐츠 |
| 에이전트 바깥의 벽 | [[agent-governance-layers]] | 권한·자원 |
| 중단 | 킬 스위치 (이 소스) | 사후 |

⚠️ 이 표는 **위키의 정리**다. 소스는 층을 열거하지 않고 *"스택의 위아래 전 구간"* 이라고만 말한다.

## 시간이 층의 수다

마지막 절(*"추가 시간을 확보하면 할 수 있는 일"*)이 이 패턴을 **감속 논증**([[slowdown-within-lead-margin]])에 연결한다. 층을 하나 더 쌓는 데는 시간이 들고, 기술이 층보다 빨리 움직이면 더미가 얇아진다. 즉 **"멈추지 말고 늦추자"의 근거가 이 그림 안에 있다** — 늦춤은 층을 쌓을 시간이다. 같은 소스의 진단(*"안전장치를 빠르게 만드는 것으로 따라잡으려 했지만 이제 기술 속도를 조절해야"*)이 여기서 기하학이 된다.

## ⚠️ 유보

- **다섯 장이 무엇인지 소스에 없다.** 숫자는 비유다.
- **층이 상관될 때** — 스위스 치즈 모델의 알려진 약점(구멍이 같은 원인으로 정렬되는 경우)을 소스가 다루지 않는다. 이 위키의 **작성자=검증자** 문제가 그 사례다 — 같은 회사가 만든 층들은 구멍이 같은 자리에 있을 수 있다.
- *"시뮬레이션에서 우회를 봤다"* 는 **진행자 진술**이고 Amodei는 확인도 부정도 하지 않는다.

## References

- [[tech-bridge-dario-amodei-cbs-interview]] — first-seen
- [[dario-amodei]] · [[anthropic]]
- 관련: [[embedded-external-evaluators]] · [[slowdown-within-lead-margin]] · [[training-time-risk]] · [[agent-governance-layers]]
