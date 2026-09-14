---
title: 기밀 VM (Confidential VM)
type: concept
category: architecture
tags: [security, privacy, confidential-computing, agents, trust-boundary]
aliases: [confidential VM, 운영자도 볼 수 없는 실행 환경]
related: [sentinel-agent, least-privilege-connectors, credential-injection-outside-sandbox, lethal-trifecta, named-human-accountability, privacy-auto-mode]
first-seen: tech-bridge-zuckerberg-muse-personal-agent
sources: [tech-bridge-zuckerberg-muse-personal-agent]
created: 2026-09-14
updated: 2026-09-14
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
