---
title: AI Privilege (AI 비밀유지특권)
type: concept
category: theory
tags: [privacy, policy, law, privilege, ambient-computing, data-retention, openai]
related: [intent-alignment, regulatory-capture, persistent-agent-teams, prompt-injection]
first-seen: tech-bridge-altman-astra-hardware
sources: [tech-bridge-altman-astra-hardware]
created: 2026-09-06
updated: 2026-09-06
---

# AI Privilege (AI 비밀유지특권)

**의사·변호사와의 대화에 적용되는 비밀유지특권(privilege)을 AI와의 대화에도 법으로 부여하자는 제안.** [[sam-altman|Sam Altman]]이 [[tech-bridge-altman-astra-hardware]]에서 주변을 듣는 기기(ambient device)의 프라이버시 우려에 답하며 제시했다.

> 저는 **AI 특권법(AI privilege law)** 이 있어야 한다고 생각합니다. **정부가 기업에 채팅 기록 같은 걸 강제로 요구해서는 안 된다**고 생각해요. 의사나 변호사와 상담할 때는 **특권**이라는 개념이 있잖아요. 하지만 ChatGPT와 대화할 때는 그런 특권이 없죠. 있어야 한다고 생각합니다.

## 왜 지금인가 — 안전 대 프라이버시

제안의 동기가 **다른 lab에 대한 경계**로 서술된다.

> 제가 걱정하는 건, 다른 생각을 가진 사람들이 *"안전 위험이 너무 커서 AI 프라이버시는 존재할 수 없다"* 고 주장하며 비슷한 논리를 펼칠 거라는 점입니다.

즉 안전 논리가 감시 논리로 전용될 수 있다는 우려다. 이 위키의 [[intent-alignment]] 두 번째 원칙(권력의 분산)과 같은 뿌리이고, [[regulatory-capture]]에서 [[andrew-ng]]가 경고한 *"공포로 규제를 끌어오기"* 와도 맞닿는다 — 다만 여기서는 규제 대상이 모델이 아니라 **사용자 데이터**다.

## 두 방향의 제약

진행자의 지적 — 의사·변호사도 데이터 **사용**에 제약이 있다 — 을 받아들인다.

| 방향 | 내용 |
|---|---|
| **정부 → 기업** | *"정부가 할 수 있는 일에는 법적인 제한이 있어야"* — 채팅 기록 강제 제출 금지 |
| **기업 자체** | *"기업도 AI와 공유하는 데이터에 대해 많은 제약을 둬야"* — *"특히 AI가 내 컴퓨터를 감시하고, 메시지를 듣고, 나랑 대화까지 한다면"* |

현재의 자기 규율로 든 것 — 기업 데이터 미학습, **zero data retention**, *"매우 강력한 내부 통제"*. 그리고 자기 위치의 인정 — *"저희는 **역사상 가장 개인적인 데이터베이스 중 하나**를 보유하고 있다고 생각합니다."*

## 왜 이 위키에 있는가

이 위키의 에이전트 축이 향하는 곳이 정확히 이 문제를 만든다.

- [[persistent-agent-teams]] — 봇이 사용자의 모든 도구에 로그인한 채 상주. 그 페이지는 *"권한·감사 경계를 소스가 다루지 않는다"* 고 유보했다.
- [[tech-bridge-altman-astra-hardware]]의 **능동적 컴퓨터** — *"끊임없이 실행되면서"*, 탁상·주머니·착용형 기기가 주변을 듣는다.
- [[goal-level-delegation]] — 위임이 커질수록 에이전트가 보는 맥락도 커진다.

세 흐름 모두 **에이전트가 보는 데이터의 양**을 늘리고, 이 페이지는 그 데이터의 **법적 지위**를 묻는다. 소스 안에서 Altman 본인이 *"사람들이 지금보다 훨씬 더 열띤 반응을 보여야 할 부분"* 이라 말한다.

## ⚠️ 유보

- **제안**이지 제도가 아니다. 어느 관할에서 어떤 형태로 입법하자는 것인지 소스에 없다.
- 제안자가 그 데이터의 보유자다 — 특권은 사용자를 정부로부터 보호하지만 **기업으로부터** 보호하는 장치는 "자체 제약"에 맡겨진다.
- 안전과의 충돌 지점(예: [[training-time-risk]]에서 말한 모니터링이 사용자 대화를 읽는가)은 소스가 다루지 않는다.

## References

- [[tech-bridge-altman-astra-hardware]] — first-seen
- 관련: [[intent-alignment]] · [[regulatory-capture]] · [[persistent-agent-teams]]
