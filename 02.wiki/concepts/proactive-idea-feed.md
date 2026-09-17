---
title: 아이디어 피드 (Proactive Idea Feed)
type: concept
category: pattern
tags: [ux, adoption, personal-agent, suggestion, meta, muse]
aliases: [ideas feed, 아이디어 피드, 먼저 제안하는 에이전트]
related: [agent-org-adoption, agent-persona-naming, fuzzy-intent-discovery, goal-level-delegation, scheduled-agent-automations, agent-memory, nightly-memory-consolidation]
first-seen: tech-bridge-zuckerberg-muse-personal-agent
sources: [tech-bridge-zuckerberg-muse-personal-agent, tech-bridge-zuckerberg-muse-in-daily-use]
created: 2026-09-17
updated: 2026-09-17
---

# 아이디어 피드

**사용자가 무엇을 시킬지 모른다는 문제를, 에이전트가 먼저 제안 목록을 만들어 푸는 제품 설계.** [[muse|Muse]]의 표면 중 하나이고, **두 소스에 걸쳐 나온다.**

앞 편([[tech-bridge-zuckerberg-muse-personal-agent]], 26:47~27:38)은 이것을 **[[agent-fleet-learning|함대 학습]] 질문에 대한 답**으로 내놓았다 — *"앱을 열면 메인 탭은 Muse와의 채팅이고, **당신이 말한 것들로부터 어떻게 확장할 수 있는지 아이디어를 보여 주는 탭**이 있습니다."* 뒤 편은 **같은 기능을 도입 문제의 해답으로** 내놓는다. **문제 진술이 붙은 것이 뒤 편의 기여다.**

문제 진술이 명확하다:

> **많은 사람이 AI에 대해 갖는 큰 문제 하나는 그걸로 뭘 해야 할지, 어떻게 최대한 끌어내야 할지 잘 모른다는 것입니다.** 그래서 제품에 특별히 넣은 것 중 하나가 **아이디어 피드(ideas feed)** 입니다 — **당신의 삶을 낫게 할 수 있는 것들에 대한 아이디어를 잔뜩 생성해 줍니다.** — [[tech-bridge-zuckerberg-muse-in-daily-use]] (12:17~12:34)

## 두 층 — 일반형과 개인화형

**일반형** — 누구에게나 해당되는 것부터 시작한다:

> **당신이 구독 중인 모든 서비스를 훑어보고 중복을 찾아내 돈을 아껴 줄 수 있습니다. 당신의 허락을 받고 가서 해지하고요.** **그건 아마 대부분의 사람에게 해당될 겁니다.**

**개인화형** — 맥락이 쌓이면 바뀐다:

> **당신과 당신이 아끼는 것들을 알아 가면서 당신에게 개인화된 아이디어를 내놓습니다.**

예: *"**따님을 위해 문명(Civilization) 게임 전략을 다루는 웹사이트를 만들어 드릴까요?**"*

## 제안이 자기 산출물 위에 쌓인다

이 소스에서 가장 구체적인 부분은 **두 번째 제안**이다.

> 그걸 쓰기 시작하고 나니까 **"제가 만든 그 웹사이트에 뭘 더 넣을까요?"** 라고 제안했습니다 — **게임을 하면서 역사와 게임에 나오는 문명들에 대해 따님에게 더 가르쳐 줄 수 있도록.** 그래서 *"그래, 그렇게 해"* 했고, **그게 만든 웹사이트에 탭이 하나 붙었습니다.**

**첫 산출물이 다음 제안의 근거가 된다.** 이것이 단발 제안과 다른 점이고, [[agent-memory]]·[[nightly-memory-consolidation]]이 있어야 성립하는 동작이다.

⚠️ **같은 예가 앞 편에도 있다** — 같은 문명 웹사이트, 같은 역사 탭 추가(23:32~24:15). 앞 편은 화자가 *"스스로 확장하고 능동적입니다"* 라고 요약했다. **두 편에 걸쳐 이 위키가 가진 아이디어 피드의 사례는 결국 둘뿐이다**(중복 구독 해지 · 문명 웹사이트).

> **이것의 더 흥미롭고 강력한 부분 중 하나가 바로 이겁니다 — 삶을 개선할 방법을 제안하고, 당신을 위해 또는 당신이 아끼는 사람들과 함께 할 수 있는 프로젝트를 제안해서 함께 더 많은 것을 할 수 있게 하는 것.**

## 사용자 쪽에서 본 값 — 영감의 축

진행자가 시간 절약과 별개의 축을 든다:

> **시간 측면이 있고, 저에게는 영감(inspiration) 측면도 있었습니다. (…) 한두 프로젝트에 너무 집중하면 어떤 그림이나 다른 면이 안 보이는데, 제 Muse Pip이 제가 공유한 맥락을 중심으로 아이디어를 주면 그게 제게 많은 창의성을 촉발했습니다.** (11:42~12:15)

**에이전트의 값이 처리량이 아니라 시야**라는 주장이다. 이 위키의 값 측정 페이지들([[agent-roi-measurement]]·[[mousepower]]·[[trusted-throughput]])은 모두 **일의 양**을 단위로 삼는데, 여기서는 **하지 않았을 일이 생긴 것**이 값이다.

## 도입 문제의 두 갈래

[[muse|Muse]]는 *"사람들이 뭘 해야 할지 모른다"* 에 두 가지로 답한다:

| 갈래 | 방식 | 페이지 |
|---|---|---|
| **먼저 제안한다** | 아이디어 피드 | 이 페이지 |
| **친근하게 만든다** | 이름·아바타·일하는 모습 | [[agent-persona-naming]] |

그리고 앞 편([[tech-bridge-zuckerberg-muse-personal-agent]])은 세 번째 갈래를 말했다 — **[[agent-fleet-learning|함대 학습]]**(다른 사용자의 익명화된 통찰). ⚠️ **이 편에서는 함대 학습이 언급되지 않는다.**

이 위키의 기존 문제의식과 맞물린다 — [[fuzzy-intent-discovery]]는 *사용자가 원하는 것을 스스로 모를 때 에이전트가 끌어내는 것*이고, 아이디어 피드는 그것을 **대화가 아니라 목록으로** 한다.

## 미해결 사항

- **제안의 수락률·품질**, 오제안 처리.
- **사례가 두 편 합쳐 둘뿐이다** — 중복 구독 해지와 문명 웹사이트.
- **중복 구독 탐지의 오탐** — *"허락을 받고 해지"* 말고는 안전장치 서술이 없다. 잘못 해지하면 어떻게 되는지 없다.
- **피드의 빈도·양**, 끄는 방법.
- **제안이 Meta 서비스 쪽으로 편향되는지** — [[business-in-a-box]] 절에서 *"모든 Meta 서비스에 연결"* 이 나오는데 소스가 이 둘을 연결하지 않는다.
- **제안 생성이 쓰는 데이터 범위** — [[least-privilege-connectors|최소 권한]]과의 관계.

## References

- [[tech-bridge-zuckerberg-muse-in-daily-use]] · [[muse]] · [[mark-zuckerberg]]
- 관련: [[agent-persona-naming]] · [[agent-org-adoption]] · [[fuzzy-intent-discovery]] · [[agent-memory]] · [[nightly-memory-consolidation]] · [[agent-fleet-learning]] · [[agent-roi-measurement]] · [[scheduled-agent-automations]]
