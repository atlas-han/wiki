---
title: 기밀 VM (Confidential VM)
type: concept
category: architecture
tags: [security, privacy, confidential-computing, agents, trust-boundary]
aliases: [confidential VM, 운영자도 볼 수 없는 실행 환경]
related: [sentinel-agent, least-privilege-connectors, credential-injection-outside-sandbox, lethal-trifecta, named-human-accountability, privacy-auto-mode]
first-seen: tech-bridge-zuckerberg-muse-personal-agent
sources: [tech-bridge-zuckerberg-muse-personal-agent, tech-bridge-zuckerberg-muse-in-daily-use]
created: 2026-09-14
updated: 2026-09-17
---

# 기밀 VM

**에이전트가 도는 가상 머신의 내용을 서비스 운영자 자신도 볼 수 없게 만들고, 그 약속을 기술적으로 검증 가능하게 한다는 설계.** [[muse|Muse]]의 보안 축이고, [[moxie-marlinspike|Moxie Marlinspike]]가 전담한다.

> **Muse 안에 이 모든 정보를 둘 수 있고, **Meta조차 그 안의 내용을 볼 수 없다는 약속**을 할 수 있습니다. 그리고 **그 약속은 기술적으로 검증 가능합니다**.** — [[tech-bridge-zuckerberg-muse-personal-agent]] (31:47~32:04)

## 논증의 구조 — 선례에서 온다

> **10년 넘게 WhatsApp을 세계 최대 종단간 암호화 시스템으로 만들었고, Meta조차 사람들이 보내는 메시지를 볼 수 없도록 설계했습니다.** 그러면 **정부가 접근하는 것, 해커가 접근하는 것, Meta 내부 누군가가 나쁜 짓을 하는 것 — 그 모든 걱정을 **테이블에서 치울 수 있습니다.**** (30:33~31:25)

**"볼 수 없게 설계하면 위협 모델 전체가 사라진다"** 는 것이 이 설계의 핵심 주장이다. 에이전트로 확장하면 **에이전트의 메모리·작업 산출물·연결된 데이터 전부**가 그 경계 안으로 들어간다.

## 왜 지금 필요한가 — 요구의 출처

> **이게 유용하려면 최첨단 지능만으로는 부족하고 **당신을 진짜로 이해해야** 합니다.** 목표를 이해하려면 **메시징, 이메일, 건강 정보까지 온갖 것에 연결**하게 됩니다. **그러려면 사람들이 시스템에 아주 높은 수준의 확신을 가져야 합니다.** (29:58~30:31)

**개인 에이전트의 효용과 프라이버시 위험이 같은 원천에서 나온다** — 연결. 이 위키의 [[lethal-trifecta]](민감 데이터 + 외부 통신 + 신뢰할 수 없는 입력)가 가리키는 바로 그 조합이다.

## 이 위키의 신뢰 경계 기록에서

| 소스 | 경계가 어디에 그어지는가 |
|---|---|
| [[tech-bridge-company-brain-security]] (09-10) | **샌드박스에 자격증명을 두지 않는다** — 프록시가 주입 → [[credential-injection-outside-sandbox]] |
| [[tech-bridge-agent-to-agent-as-search]] (09-09) | **조직과 조직 사이** — 공유 사일로·블랙박스 |
| [[tech-bridge-build-time-vs-runtime-tools]] (09-10) | **도구의 노출 시점** — 빌드타임 vs 런타임 |
| **기밀 VM** | **운영자 자신까지 배제** |

**가장 바깥으로 밀어낸 경계**이고, 이 위키에서 **에이전트의 실행 환경 자체를 신뢰 경계로 삼은 첫 기록**이다.

## 대안과의 비교 — 로컬 실행

소스가 직접 대조한다.

> **올해 초 [[openclaw|OpenClaw]] 같은 게 나왔을 때 많은 사람이 **Mac Studio**를 사기 시작했습니다. 한 방법은 말 그대로 **집에 물리적으로 장비를 두고 돌리는 것**입니다.** (33:05~33:16)

> **하지만 Mac Studio를 사서 설정하고 집에서 돌릴 사람이 **수십억 명**이 되지는 않을 것 같습니다 — 특히 **지금처럼 RAM 가격이 비싼 시기에는**요.** 그리고 **기술적으로도 어렵습니다.** (33:19~33:31)

목표는 **로컬의 보장을 클라우드의 편의로 옮기는 것**이다:

> **자기 컴퓨터나 VM을 직접 설정하지 않아도 되고 클라우드에서 프로비저닝할 수 있어야 하지만, **집 책상 밑에 상자가 있을 때와 같은 보안과 기밀성**을 원했습니다.** (33:47~34:01)

나중에 시장 규모로 판정한다 — *"클라우드에 아주 안전한 기밀 VM을 둘 수 있어도 집에 Mac Studio를 원하는 사람은 여전히 있을 겁니다. **수백만은 될지 몰라도 수십억은 아닐 겁니다.**"*

## 열려 있는 것

- ⚠️ **검증 방법이 없다.** *"기술적으로 검증 가능"* 이라고만 하고 **원격 증명인지, 공개 감사인지, 하드웨어 신뢰 근거인지** 제시되지 않는다. *"몇 주 안에 더 공개하겠다"* 로 넘어간다.
- ⚠️ **위협 모델이 명시되지 않는다.** 무엇을 막고 무엇을 못 막는지 — 특히 **에이전트 자신이 데이터를 밖으로 내보내는 경우**(이건 [[sentinel-agent|센티널]]의 몫으로 넘겨진다).
- ⚠️ **"아무도 안 하고 있다"** 는 주장에 비교 대상이 없다.
- ⚠️ **근거가 인물에 걸려 있다** — *"밴드를 다시 모아 Moxie가 이걸 설계하게 한 것이 토대"*. 이 위키는 이것을 [[named-human-accountability|이름 붙은 책임]]으로 기록하되 **기술적 근거의 대체물로 받아들이지 않는다.**

## References

- [[tech-bridge-zuckerberg-muse-personal-agent]] · [[muse]] · [[meta]] · [[moxie-marlinspike]] · [[openclaw]]
- 관련: [[sentinel-agent]] · [[least-privilege-connectors]] · [[credential-injection-outside-sandbox]] · [[lethal-trifecta]] · [[named-human-accountability]] · [[privacy-auto-mode]] · [[black-box-agent-approach]]

## 두 번째 서술 — 검증 주장이 비교 주장으로 바뀌었다 (2026-09-17)

[[tech-bridge-zuckerberg-muse-in-daily-use]]가 같은 논증(WhatsApp 선례 → 기밀 VM)을 반복하는데 **결론 문장이 다르다.**

> **WhatsApp을 종단간 암호화되게 설계해서, 당신이 메시지를 보낼 때 Meta가 그 메시지를 볼 수 없게 했습니다 — 우리가 원한다 해도요.** **그 원칙을 가져와서 여기서는 기밀 VM이라고 부르는 아키텍처를 설계하려 했습니다.** (14:48~15:14)

> **아주 참신합니다. 제가 아는 한 다른 누구도 이런 걸 갖고 있지 않습니다.** (…) **업계에서 견줄 데 없는 수준의 보안·프라이버시·신뢰를 만든다**고 생각합니다. (15:16~15:39)

| | 앞 편 (31:47~32:04) | 이번 편 |
|---|---|---|
| 핵심 주장 | *"그 약속은 **기술적으로 검증 가능합니다**"* | *"**견줄 데 없는** 수준"* · *"**다른 누구도 갖고 있지 않다**"* |
| 성격 | **검증 가능성** 주장 | **비교 우위** 주장 |
| [[moxie-marlinspike\|Moxie Marlinspike]] | 전담으로 명시 | **언급 없음** |

> ⚠️ **검증 가능성이 이번 편에서 사라지고 비교 주장만 남았다.** 그리고 **비교 근거가 없다** — 어떤 제품과 비교했는지, *"다른 누구도 없다"* 를 무엇으로 확인했는지 말하지 않는다. 이 소스만 읽으면 **기밀 VM의 약속을 무엇으로 확인하는지 알 수 없다.**

진행자가 사용자 쪽에서 본 것을 덧붙인다 — *"제 Muse의 VM, 즉 개인 컴퓨터를 처음 봤을 때 (…) **메모리나 데이터 같은 것들이 거기 다 저장돼 있고, 오직 우리 에이전트만을 위한 것**이더군요"*(17:12~17:32). **사용자가 VM 내부를 들여다볼 수 있다**는 서술은 이번 편이 처음이다.

⚠️ [[nightly-memory-consolidation|메모리 압축]]이 이 VM 안에서 도는지 소스가 연결하지 않는다.
