---
title: 형용사·동사 조향 (Adjective–Verb Steering)
type: concept
category: pattern
tags: [design, steering, vocabulary, agent-skills, language, control]
aliases: [Leitwort, designing at the speed of adjectives, 형용사 조향]
related: [steering-altitude, no-one-shot-design, agent-skills, generator-evaluator-pattern, context-engineering, structured-brand-context, intentional-out-of-distribution, multimodal-elicitation, impeccable]
first-seen: tech-bridge-impeccable-design-steering
sources: [tech-bridge-impeccable-design-steering]
created: 2026-09-12
updated: 2026-09-12
---

# 형용사·동사 조향

**에이전트를 "이걸 디자인해 줘"가 아니라 "더 bolder하게", "distill해", "harden해" 같은 디자인 어휘로 조향하되, 각 단어가 이 프로젝트에서 무엇을 뜻하는지를 스킬이 정의한다.** [[paul-bakaus]]가 [[impeccable]]을 만든 접근([[tech-bridge-impeccable-design-steering]]). 발표 제목은 *"형용사의 속도로 디자인하기"* — *"그리고 방 안의 코끼리를 꺼내자면, 형용사만이 아니라 동사이기도 합니다."*

## 어휘

| 단어 | 뜻 (화자 정의) |
|---|---|
| **bolder** | 그라데이션·글래스·네온이 **아니라** — **위계(hierarchy)·스케일·결정적 타이포.** 디자인 시스템을 깨지 않으면서 주의를 올린다 |
| **quieter** | (시각적으로 절제 — ⚠️ ko는 "소리를 줄이면") |
| **distill** | *"기본적으로 단순화"* |
| **polish** | — |
| **denser** | — |
| **harden** | *"이 디자인이 전반에서 동작하는지 확인"* — 특정 기기 성능, 반응형 |
| **overdrive** | 완전히 과한 것 — 반농담으로 만들었으나 커뮤니티가 열광 |

> 이건 **디자인 세계에서 우리가 쓰는 단어들**이에요. (08:36~08:39)

## 왜 어휘인가 — 같은 모델, 다른 언어

> 두 사람이 정확히 같은 과제를 시도하는 걸 봤는데 — 한 명은 디자인을 전혀 만져 본 적 없는 엔지니어, 다른 한 명은 디자이너 — **같은 모델, 같은 하네스**를 써도 **쓰는 언어에 따라** 결과에 **확연한 차이**가 있습니다. 그래서 저는 그 언어를 **스킬로, 시스템으로 압축**했습니다. (08:42~09:07)

⚠️ 관찰 진술, 표본·조건 없음. 다만 이 위키의 [[agent-skills]]에 새 종류를 준다 — 절차([[ibm]])도 프레임워크 지식([[flutter]])도 도메인 판단([[tech-bridge-six-agent-skills|페이월]])도 아닌 **어휘의 정의**를 담는 스킬.

## Leitwort — 뒤에 정의가 없으면 그냥 프롬프트

> **형용사는 Leitwort입니다.** (…) 이 단어들은 여러분이 **의미를 불어넣는** 말입니다. **모델에게 이미 어떤 의미가 있지만, 여러분이 그것을 관심 영역으로 번역**하는 거죠. (10:45~11:16)

> **뒤에 아무것도 없는 형용사는 그냥 좀 더 나은 프롬프트일 뿐입니다.** 그래서 쓰는 단어로 무엇을 뜻하는지 에이전트에게 정말로 말해야 합니다. 훈련 자료 안에서 너무 많은 다른 뜻을 갖고 있으니까요. (13:36~13:52)

*Leitwort*(독일어, 이끄는 말)는 Matt Pocock의 트윗에서 가져왔다고 밝힌다(⚠️ 원문 미확보, en-orig *"light wart"* → ko "가벼운 사마귀"). 요점은 — **단어는 모델 안에서 다의적**이므로, 조향이 되려면 *이 프로젝트에서의 뜻* 을 고정해야 한다. 정의 없이 *"더 bolder하게"* 라고 하면:

> 모델은 자기 나름의 bolder 기준은 있지만 **하고 싶은 대로 하죠** — 새 색을 발명하고, 새 그라데이션을 발명하고. (09:46~09:56)

## 자기 점검 문장

> 이건 Impeccable에서 *bolder* 라고 하면 로드되는 **파일의 실제 문장**입니다 — **"누군가에게 당신의 작업을 보여주고 'AI가 이걸 더 bolder하게 만들었다'고 말하라. 그들이 믿으면, 당신은 실패한 것이다."** 에이전트가 종종 돌아보며 *"내가 좀 나쁜 작업을 한 것 같다"* 고 합니다. (10:18~10:41)

이 문장은 **성공 기준을 산출물이 아니라 관찰자의 반응**으로 정의한다 — *AI가 한 것처럼 보이면 실패*. [[ai-slop|슬롭]]의 정의(*"모두가 알아본다"*)를 거꾸로 쓴 verifier다. ⚠️ 그런데 [[generator-evaluator-pattern]]이 *생성과 평가를 분리* 하라고 한 것과 달리 이것은 **평가 기준을 생성자의 지시 안에** 둔다. 자기 평가 편향(*"모델은 자기 작품을 후하게 평가한다"*)이 여기서 어떻게 되는지 소스는 다루지 않는다 — 일화(*"종종 돌아본다"*)뿐.

## 이 위키에서의 자리

- **[[steering-altitude]]** — 이 어휘가 *직접 조작(픽셀)* 과 *완전 위임(목표)* 사이의 **고도**를 구현한다. 형용사는 픽셀보다 높고 *"디자인해 줘"* 보다 낮다.
- **[[multimodal-elicitation]]** — 그쪽이 *사용자가 어휘를 갖고 있지 않아도 이미지에 마우스를 올릴 수 있다* 며 **어휘 없는 사용자**를 전제했다면, 이쪽은 **어휘를 주는 것**이 해법이다. 화자의 최고 코멘트가 *"모두가 소통할 수 있는 디자인의 공유 언어"* 라는 점에서 둘 다 **공통 언어**를 목표로 한다.
- **[[structured-brand-context]]** — *bolder* 의 정의에 *"디자인 시스템을 깨지 않으면서"* 가 들어 있다. 브랜드 제약을 *데이터* 로 주는 대신 *단어의 뜻* 에 넣은 것.
- **[[intentional-out-of-distribution]]** — *"몇 가지는 어기되 나머지는 지킨다"* 가 bolder의 정의 구조와 같다.
- **[[context-engineering]]** — 어휘 정의는 컨텍스트의 한 종류이고, 스킬이라 [[tech-bridge-flutter-ai-workflow|progressive disclosure]]로 *bolder* 라고 할 때만 로드된다(*"bolder라고 하면 로드되는 파일"*).

## ⚠️ 미해결

- 어휘의 전체 목록·개수 — 발화된 7개뿐.
- 각 단어의 정의가 **프로젝트마다 어떻게 달라지는가** — *"여러분의 맥락에서 bolder"* 라고 하지만 스킬이 프로젝트를 어떻게 읽는지 없음.
- 효과 측정 없음. 당사자.

## References

- [[tech-bridge-impeccable-design-steering]] (first-seen) · [[paul-bakaus]] · [[impeccable]]
- 관련: [[steering-altitude]] · [[no-one-shot-design]] · [[agent-skills]] · [[generator-evaluator-pattern]]
