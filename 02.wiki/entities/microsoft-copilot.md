---
title: Microsoft Copilot (Chat · Co-work · Code · Autopilot)
type: entity
category: product
tags: [microsoft, copilot, autopilot, long-running-agent, human-in-the-loop, enterprise-ai, pricing]
aliases: [Copilot, Autopilot, Co-work, Copilot tasks, 코파일럿, 오토파일럿]
links: []
sources: [tech-bridge-nadella-copilot-autopilot]
created: 2026-09-29
updated: 2026-09-29
---

# Microsoft Copilot

[[microsoft|Microsoft]]의 AI 애플리케이션 제품군. [[tech-bridge-nadella-copilot-autopilot]]의 **출시 행사 현장 대담**에서 [[satya-nadella|Satya Nadella]]가 새 Copilot을 **chat · co-work · code · Autopilot** 네 폼팩터의 묶음으로 설명했다. PC 시대 Office처럼 *"Copilot in the AI era is the coming together … of all of these functions"*(01:54~02:01).

> ⚠️ **이 페이지는 CEO 한 사람의 출시일 진술이다.** 가격·성능·채택 수치가 없고, 진행자가 *"experiment a little bit with the new Copilot"*(00:12~00:16)했다는 것 외에 제3자 사용기가 없다. **GitHub Copilot**(코딩 도구)과는 다른 제품이다 — 화자는 둘을 나란히 든다(08:28~08:31).

## 폼팩터

| 폼팩터 | 소스의 서술 | 과금 (진행자 정리 05:50~05:59) |
|---|---|---|
| **Chat** | *"using chat as a new way to even search for information"*(00:48~00:50) | 좌석(seat) |
| **Co-work** | *"started doing things like task delegation"*(00:55~00:57). Excel에서는 Co-work가 **outer loop**, Excel 안의 에이전트 루프가 **inner loop**(03:17~03:22) | 사용량 |
| **Code** | *"what's the real difference between creating a website, an app, or a document. Guess what? There is not."*(01:11~01:16) — 앱을 만들어 OneDrive 문서처럼 호스팅 | — |
| **Autopilot** | *"a long-running business process agent"*, 사람이 *"in the loop both at the input and at the output"*(01:34~01:44). *"something that has an identity, it does complete jobs"*(03:24~03:28) | 사용량 |

이전 단계로 **Copilot tasks**가 OpenClaw와 *"just around the same time"* 출시됐다(02:44~02:48) — 설명은 없다.

## 왜 Autopilot만 따로 내지 않나

진행자는 *"the real star of the show is Autopilot"* 이라며 소비자 개인 에이전트([[muse|Muse]] 등)를 쓰는 입장에서 *"Just give me Autopilot"* 이라 한다(02:02~02:09). 답:

> Autopilot's a fantastic until you have to do something with the output of an Autopilot. (02:54~02:59)
> when it hands off or when I'm trying to instruct it, I need my Copilot and my Co-work. (03:28~03:33)

즉 **자율 실행(Autopilot)과 보조(Copilot/Co-work)를 번갈아 쓰는 조합**이 제품이다 → [[assistance-vs-automation]]. 그리고 Autopilot의 전제는 **신뢰** — *"can I really trust it with all of my credentials?"*(04:20~04:22) — 이고, 그 답으로 [[agent-365|Agent 365]]의 호스팅 환경을 든다(12:44~13:00).

## 모델 — "auto가 제품"

사용자는 모델을 고르지 않는다. **learned router**가 작업 강도에 따라 고르고, 자체 **MAI 모델**과 하네스가 OpenAI(특히 [[openai-astra|Astra]])·Anthropic·Grok 모델을 호출한다. 고객은 **자기 모델(BYO)** 을 넣을 수 있다(08:15~11:10). → [[model-mixing-economics]]

## 가격

좌석은 *"entitlements to usage"*, 그 위에 *"usage-based functionality that any user at any time can use with no limits"*(06:16~06:53). Autopilot은 *"a certain cost footprint"* 에서 시작해 *"it'll only reduce after that"*(07:35~07:38). → [[software-marginal-cost]]

## ⚠️ 유보

- **Autopilot의 identity** — *"has an identity"* 가 계정·권한 단위의 신원인지 은유인지 설명하지 않는다. [[agent-identity-separation]]과 연결될 수 있으나 소스가 잇지 않는다.
- **"human in the loop at the input and at the output"** — 중간 단계에서의 개입·중단 수단은 말하지 않는다.
- 출시 범위·일정 — 진행자의 *"I know that you're rolling it out sort of over time"*(02:28~02:30)뿐. 가격 수치 없음.

## References

- [[tech-bridge-nadella-copilot-autopilot]] — 첫 소스
- [[microsoft]] · [[satya-nadella]] · [[agent-365]]
