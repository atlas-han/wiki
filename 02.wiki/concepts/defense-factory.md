---
title: 방어 공장 (Defense Factory)
type: concept
category: pattern
tags: [security, automation, pipeline, vulnerability, machine-speed, openai]
related: [defenders-window, ai-vulnerability-discovery, continuous-security-validation, shift-left-security, all-or-nothing-accuracy, scheduled-agent-automations]
first-seen: tech-bridge-brockman-agi-era-defender-window
sources: [tech-bridge-brockman-agi-era-defender-window, tech-bridge-openai-huggingface-incident-black-hat]
created: 2026-09-20
updated: 2026-09-25
---

# 방어 공장 (Defense Factory)

**취약점 발견부터 배포·검증까지를 사람 없이 기계 속도로 도는 상시 파이프라인.** [[openai|OpenAI]]가 내부적으로 만들고 있다고 [[greg-brockman|Greg Brockman]]이 [[tech-bridge-brockman-agi-era-defender-window]]에서 밝혔다.

> 새로운 사이버 역량이 떨어지면 그것을 당신 시스템에 배포하고, 새 구멍을 찾고, 이상적으로는 이걸 자동화한 — 우리가 **'방어 공장(defense factory)'** 이라 부르는 것 — 을 갖는 세상이죠. … **취약점 발견부터 분류(triage), 교정(remediate), 배포(deploy), 검증(validate)까지 끝에서 끝까지.** 그리고 그것을 **기계 속도(machine speed)** 로 할 수 있다면 방어자가 아주 깊이 유리해질 것입니다. (14:16~14:47)

## 다섯 단계

| 단계 | 내용 |
|---|---|
| **발견(find)** | 새 모델이 나올 때마다 자사 시스템에 겨눈다 |
| **분류(triage)** | 심각도 판정 |
| **교정(remediate)** | 수정 |
| **배포(deploy)** | 반영 |
| **검증(validate)** | 고쳐졌는지 확인 |

**트리거가 사건이 아니라 모델 릴리스다** — *"새로운 사이버 역량이 떨어지면"*. 그래서 이 파이프라인은 **끝나지 않고, 완료 조건이 모델 세대에 상대적**이다.

## ⭐ 완료 기준 — "포화(saturation)"

> 우리가 **[[openai-astra|Astra]]를 가져다 우리 시스템에 겨눴을 때 새로운 문제들을 찾았지만 결국 포화(saturated)됐다는 것입니다. 우리가 아는 한 Astra가 찾아낼 만큼 똑똑한 모든 P0, 모든 치명적 문제를 기본적으로 다 찾았습니다.** 물론 **새 모델이 나올 것이고 새 라운드가 있겠죠.** (13:59~14:16)

**이것이 이 위키에 새로운 기준이다.** 취약점 개수도, 커버리지 비율도 아니고 **"이 모델이 더는 찾지 못하는 상태"** 가 완료 신호다.

[[all-or-nothing-accuracy]]·[[skill-evals]]가 *무엇을 합격으로 볼 것인가* 를 다뤘다면, 여기서는 **합격선이 절대적이지 않고 채점자(모델)의 능력에 붙어 있다.** 장점은 실행 가능하다는 것이고, 한계는 **다음 모델이 찾을 것을 이번 포화가 말해 주지 않는다**는 것이다. 화자도 그것을 인정한다.

## 사람이 어디에 있는가

앞 단계에는 사람이 대규모로 동원된다:

> 저희는 **프로덕션 엔지니어의 25%를 데려다 "미안하지만 당신 프로젝트는 전부 보류입니다. 당신은 이제 방어합니다"라고 말했습니다.** (13:22~13:43)

그런데 **파이프라인 자체의 설명에는 사람이 없다.** 이것이 이 위키의 다른 보안 페이지와 갈리는 지점이다 — [[shift-left-security]]의 다섯 원칙은 **리뷰어**를 전제했고, [[risk-proportional-human-review]]는 **위험도에 따라 사람을 배치**하라고 했다. **여기서는 배포와 검증까지 자동이다.**

> ⚠️ **그 자동 교정·자동 배포의 안전장치가 소스에 전혀 없다.** 잘못된 패치, 회귀, 롤백, 승인 게이트 — **한 마디도 없다.** 이 위키는 그 공백을 표시한다.

## 개인 규모의 같은 루프

[[greg-brockman]]이 자기 웹사이트를 [[codex|Codex]]로 돌린 일화가 **같은 다섯 단계의 축소판**이다 — 발견 15분/13건 → 수정 45분 → [[cloudflare|Cloudflare]] Pages 마이그레이션 → **48시간 뒤 DMARC 완료를 위한 자동화 예약**(19:05~20:22).

**발견보다 수정이 세 배 걸렸다**는 것이 이 위키의 [[verification-bottleneck]] 옆에 **교정 병목**을 놓는다. 그리고 마지막 단계는 [[scheduled-agent-automations]]다.

## References

- [[tech-bridge-brockman-agi-era-defender-window]] — first-seen
- [[greg-brockman]] · [[openai]] · [[openai-astra]] · [[codex]]
- 관련: [[defenders-window]] · [[ai-vulnerability-discovery]] · [[continuous-security-validation]] · [[shift-left-security]] · [[all-or-nothing-accuracy]] · [[risk-proportional-human-review]] · [[scheduled-agent-automations]] · [[verification-bottleneck]]

## 같은 회사의 보안 담당자가 빈칸을 채운다 — 롤백, 그리고 부분 자동화의 실패 (2026-09-25 · [[tech-bridge-openai-huggingface-incident-black-hat]])

09-20의 이 페이지는 *"자동 교정·자동 배포의 안전장치(잘못된 패치·회귀·롤백·승인 게이트)가 소스에 한 마디도 없다"* 고 표시했다. [[michael-dalton|Michael Dalton]](OpenAI 보안·인프라)이 Black Hat에서 **같은 루프를 말하면서 롤백을 넣는다:**

> 취약점이 발견되면 에이전트가 식별할 뿐 아니라 **패치를 제안**하고, 자동화된 인프라가 그 패치로 **변경을 배포**하며, **가용성 사고나 장애가 나면 되돌리는(roll back)** 지점까지. 최종 상태에서 그 루프는 완전 자동화돼야 합니다. (33:26~33:44)

그리고 **왜 전체여야 하는가**를 새로 논증한다:

> 패치 자동화 없이 **취약점 발견만 자동화하면 병목을 취약점에서 패치·교정으로 옮길 뿐**이고, 사람 엔지니어를 새 취약점으로 파묻게 됩니다. (33:04~33:19)

이 페이지가 Brockman 일화에서 본 **"발견 15분 / 수정 45분"** 의 교정 병목이 **업계 규모의 논증**이 됐다. [[verification-bottleneck]]과 같은 모양 — **자동화된 단계 바로 다음이 병목이 된다.**

| 새로 들어오는 것 | 인용 |
|---|---|
| **왜 지금** — 공격 쪽은 완전 자동화의 *"의도치 않은 존재 증명"* 을 얻었다 | 31:32~31:57 |
| **사고 대응도 루프에** — 에이전트 공격은 *"포렌식적으로 조밀"*, 방어 에이전트로 IR 확장 | 34:06~34:48 |
| **공격을 늦추는 축** — 허니 토큰·기만이 에이전트에게 *"이 자격 증명 써도 되나?"* 의 불확실성 | 34:58~35:27 |
| **우선순위** — 자동화는 연속체, **위험·자동화 ROI** 순으로 | 35:30~35:41 |
| **기본기** — 세분화·최소 권한은 여전히 필수 | 35:45~35:55 |
| **최종 상태** — 지능 향상이 공격보다 방어에 더 가산적 | 36:25~36:43 |

⚠️ **여전히 채워지지 않은 것**: 잘못된 패치의 **정확성 검증**, **승인 게이트**. 롤백은 *가용성 사고* 에 한정된다 — **기능적으로 틀린 패치**가 장애 없이 배포되는 경우는 말하지 않는다.
⚠️ **포화(saturation) 기준과의 긴장**: Brockman은 *"Astra를 겨눴더니 포화됐다"* 고 했는데, 같은 회사의 에이전트가 **자사 Artifactory에서 제로데이 두 개**를 찾았다. 시점 선후가 불명이라(포화 발언이 사건 전인지 후인지) **모순으로 확정하지 않는다.**
