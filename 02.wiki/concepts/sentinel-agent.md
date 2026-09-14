---
title: 센티널 에이전트 (Sentinel Agent)
type: concept
category: pattern
tags: [security, prompt-injection, human-in-the-loop, monitoring, agents]
aliases: [감시 에이전트, sentinel]
related: [prompt-injection, generator-evaluator-pattern, deny-and-continue, no-silent-write, named-human-accountability, lethal-trifecta, confidential-vm]
first-seen: tech-bridge-zuckerberg-muse-personal-agent
sources: [tech-bridge-zuckerberg-muse-personal-agent]
created: 2026-09-14
updated: 2026-09-14
---

# 센티널 에이전트

**핵심 에이전트와 별도로, 들어오고 나가는 트래픽과 데이터만 감시하며 사람 검토를 트리거하는 에이전트.** [[muse|Muse]]의 보안 층 중 하나.

> **핵심 에이전트가 있고, 그 외에 들어오고 나가는 트래픽과 데이터를 감시하는 **센티널(sentinel) 에이전트들**을 만들었습니다.** 목적은 **당신이 검토하고 싶을 만한 것을 알려 주는 것**입니다.
>
> **센티널이 하는 일은 — 누군가 **프롬프트 인젝션** 같은 걸 하려는지 보고, 당신의 Muse 에이전트가 **당신이 편치 않을 만한 것을 내보냈는지** 봅니다. 그렇다면 센티널이 **"사람이 개입하는 검토"를 트리거할 권한**을 갖습니다.** — [[tech-bridge-zuckerberg-muse-personal-agent]] (34:33~35:14)

## 두 방향을 본다

| 방향 | 무엇을 찾는가 | 이 위키의 기존 개념 |
|---|---|---|
| **들어오는 것** | **[[prompt-injection\|프롬프트 인젝션]] 시도** | [[lethal-trifecta]]의 *신뢰할 수 없는 입력* |
| **나가는 것** | **과잉 공유** — *"당신이 편치 않을 만한 것"* | [[discretion-capability]] · [[black-box-agent-approach]] |

**나가는 방향까지 보는 것이 이 패턴의 고유점이다.** 이 위키의 보안 기록 대부분은 **들어오는 것**(인젝션·오염)과 **할 수 있는 것**(권한)을 다뤘고, **무엇을 말했는가**를 감시하는 층은 없었다.

## 권한의 배치 — 핵심은 여기다

> **로그인·결제·민감 정보 전송은 매번 승인해야 합니다.** *"이런 종류는 일반적으로 괜찮다, 항상 허용"* 이라 말할 수는 있습니다. **하지만 일반적으로 Muse 에이전트는 그런 판단을 스스로 내릴 수 없습니다. 그건 시스템과 아키텍처에 꽤 깊이 박혀 있습니다.** (35:14~35:38)

**판단 권한을 에이전트에게서 빼앗아 별도 층에 둔다.** [[generator-evaluator-pattern]]을 보안 축으로 옮긴 형태이고, [[deny-and-continue]]·[[no-silent-write]]와 같은 계열이되 **판정자가 별도 에이전트**라는 점이 다르다.

이 위키의 [[named-human-accountability]]와도 맞물린다 — **센티널의 산출물은 결정이 아니라 사람에게 가는 호출**이다.

## 열려 있는 것 — 이 소스가 전혀 다루지 않는다

- ⚠️ **탐지율·오탐이 없다.** 얼마나 잡는지, 얼마나 자주 잘못 깨우는지 전혀 없다. **오탐이 잦으면 사용자가 "항상 허용"을 눌러 층 전체가 무력화된다** — 소스는 이 위험을 언급하지 않는다.
- ⚠️ **센티널 자신이 인젝션의 대상이 될 가능성**이 다뤄지지 않는다. 센티널도 모델이고 **적대적 입력을 읽는다**. [[lethal-trifecta]]가 가리키는 자리가 비어 있다.
- ⚠️ **센티널의 모델·독립성**이 없다. 핵심 에이전트와 같은 모델이라면 **같은 편향과 같은 취약점**을 공유한다 — 2026-09-09 이래 이 위키가 반복 표시해 온 *평가자의 독립성* 문제다.
- ⚠️ **"편치 않을 만한 것"의 기준**이 없다. 개인마다 다른 민감도를 어떻게 학습하는지.

> ⚠️ **전부 당사자 진술이다.** *"다른 에이전트들을 봐도 우리가 여기에 넣은 정교함과 깊이에 근접한 곳은 없다"* 는 주장에 비교 대상이 없다.

## 자막 주의

**ko 자막에서 *prompt injection* 이 사라졌다** — *"누군가가 무단으로 접근하려는 시도가 있는지"*. 위키의 핵심 보안 용어가 **일반적인 무단 접근으로 뭉개졌다.** 2026-09-12의 *harness → "코딩 실력"* 과 같은 **추상화 방향의 소실**이다.

## References

- [[tech-bridge-zuckerberg-muse-personal-agent]] · [[muse]] · [[meta]]
- 관련: [[prompt-injection]] · [[confidential-vm]] · [[least-privilege-connectors]] · [[generator-evaluator-pattern]] · [[deny-and-continue]] · [[no-silent-write]] · [[named-human-accountability]] · [[lethal-trifecta]] · [[discretion-capability]]
