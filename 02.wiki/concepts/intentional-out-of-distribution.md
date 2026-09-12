---
title: 의도적 분포 이탈 (Intentional Out-of-Distribution)
type: concept
category: technique
tags: [creativity, ai-slop, design, generation, temperature, rules]
aliases: [creativity API, 창의성 API, purposely out of distribution]
related: [ai-slop, generator-evaluator-pattern, signal-layer, structured-brand-context, adjective-verb-steering, impeccable]
first-seen: tech-bridge-taste-labs-measuring-slop
sources: [tech-bridge-taste-labs-measuring-slop, tech-bridge-impeccable-design-steering]
created: 2026-09-12
updated: 2026-09-12
---

# 의도적 분포 이탈

**창의성은 무작위가 아니다 — 도메인의 규칙과 기대를 먼저 알고, 몇 가지를 의도적으로 어기되 나머지는 지킨다.** [[thais-castello-branco]]([[taste-labs]])가 [[tech-bridge-taste-labs-measuring-slop]]에서 [[ai-slop|슬롭]]의 *반복* 에 대한 처방으로 제시했고, 별명은 *창의성 API*.

## 온도가 아니다

> 이건 그냥 **무작위성일 수 없습니다.** 모델의 **온도(temperature)를 올리고** 손가락 꼬며 잘 되길 바라는 게 아니에요. (10:23~10:32)

> 창의성은 보통 무작위가 아니고, 그 상황에 완전히 어긋나게 느껴지는 것을 하는 것도 아닙니다. **몇 가지에서 의도적으로 갈라지되, 그 카테고리의 기대에 대한 준수는 나머지에서 유지하는** 것이죠. (10:50~11:04)

예시: 스타트업 피치 덱을 요청받으면 먼저 *좋은 피치 덱은 어떤 모습인가* 를 알고, 그다음 **어디를 어길지** 고른다. 즉 두 단계다 — **규칙의 인식** → **선택적 위반**. 첫 단계가 없으면 이탈은 창의성이 아니라 오류다.

## 왜 필요한가 — 평균으로의 붕괴

> 기성(off-the-shelf) 모델은 **스타일 면에서 무너지고, 평균으로 무너지는(collapse with the mean)** 경향이 있죠. 그러면 어떻게 창의성을 시스템에 되돌려 놓을까? (01:41~01:48)

화자가 말하는 훌륭함의 조건 — *"반드시 평균적이지 않은 것, **의도적으로 분포 밖(out of distribution)** 에 있는 것"*(03:00~03:03). 이것이 개념의 이름이다. ⚠️ ko 자막은 *distribution* 을 **"유통"** 으로 옮겨 이 개념이 자막에서 사라졌다.

## 형태 — 영감 기계

> 에이전트에게 일종의 **영감 기계(inspiration machine)** 가 되어, 슬롭 사이트에서 보는 그 평균·중심이 아니라 **실제로 분포 밖에 있는** 것을 만들게 하는 시스템. (10:01~10:14)

⚠️ *"공식 이름이 될지 모르겠다"* — 별명뿐이고 출시·동작·인터페이스 없음.

## 이 위키에서의 자리

- **[[generator-evaluator-pattern]]의 반대편에서 같은 목표.** [[anthropic-harness-design-long-running-apps]]는 *originality 가중치를 높여 모델을 aesthetic risk-taking 쪽으로 밀었고* 그 결과 10번째 반복에서 3D 갤러리 룸이 나왔다 — **평가자의 압력**으로 분포를 벗어나게 한 것이다. 이 개념은 **생성자 쪽에 영감을 주입**한다. 둘은 보완적이며 소스는 서로를 모른다.
- **[[impeccable]]의 `overdrive`** 는 *"완전히 오버 더 톱인 것"* 을 만드는 명령 — 의도적 이탈을 **사용자가 명시적으로 호출**하는 형태다. 그리고 [[adjective-verb-steering]]의 *bolder* 정의(*"디자인 시스템을 깨지 않으면서"*)가 정확히 *"나머지는 지킨다"* 에 해당한다. 같은 날 두 소스가 같은 구조를 다른 쪽에서 말했다.
- **[[signal-layer]]** — [[lena-hall]]의 *"AI는 수렴 기계 — 그대로 두면 모든 게 똑같아진다"* 에 대한 **기술적 대응**이다. Hall의 처방이 *사람이 신호를 정의하라* 였다면 이쪽은 *시스템이 이탈을 만들라* 다.
- **[[structured-brand-context]]** — 규칙의 인식을 브랜드에서 가져오면, 이 개념은 *그 브랜드 안에서의 이탈* 이 된다.

## ⚠️ 미해결

- "몇 가지"를 **누가 어떻게 고르는가** — 사람인지 시스템인지, 무엇을 근거로. 없음.
- 도메인 규칙의 출처 — 마이닝인지 사람이 쓴 것인지 없음.
- 이탈의 정도를 재는 방법 — [[slop-probes|프로브]]가 반복을 재듯 *이탈의 성공* 을 재는 장치는 없다.

## References

- [[tech-bridge-taste-labs-measuring-slop]] (first-seen) · [[taste-labs]]
- [[tech-bridge-impeccable-design-steering]] — `overdrive` · bolder의 제약
- 관련: [[ai-slop]] · [[generator-evaluator-pattern]] · [[signal-layer]]
