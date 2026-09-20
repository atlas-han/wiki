---
title: 방어 공장 (Defense Factory)
type: concept
category: pattern
tags: [security, automation, pipeline, vulnerability, machine-speed, openai]
related: [defenders-window, ai-vulnerability-discovery, continuous-security-validation, shift-left-security, all-or-nothing-accuracy, scheduled-agent-automations]
first-seen: tech-bridge-brockman-agi-era-defender-window
sources: [tech-bridge-brockman-agi-era-defender-window]
created: 2026-09-20
updated: 2026-09-20
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
