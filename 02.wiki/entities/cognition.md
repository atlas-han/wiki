---
title: Cognition
type: entity
category: org
tags: [coding-agents, acquisition, rust, dioxus]
sources: [tech-bridge-ambitious-software-agent-era, tech-bridge-jensen-huang-cbs-interview, tech-bridge-introspection-loop-is-the-product, tech-bridge-death-of-code-review]
created: 2026-09-14
updated: 2026-10-03
---

# Cognition

**[[dioxus|Dioxus]]를 인수한 회사.** 본 위키 첫 등장은 [[tech-bridge-ambitious-software-agent-era]]이고, **소스가 이 회사에 대해 말하는 것은 세 문장이 전부**다.

> **차세대 소프트웨어의 도구를 만들고 싶으시다면, Dioxus를 인수한 Cognition이 채용 중입니다. Dioxus 팀은 미래에 동참하려고 Cognition에 합류했고, 여러분도 그러시기를 바랍니다.** (18:29~18:40)

## 소스에서 확인되는 것

| 확인되는 것 | 근거 |
|---|---|
| **Dioxus를 인수했다** | [[jonathan-kelley]] 발언 |
| **Dioxus 팀이 합류했다** | 같음 |
| **채용 중이다** | 같음 |
| 자기 규정은 *"차세대 소프트웨어의 도구"* | 같음 |

**그 외에는 아무것도 없다** — 설립 시기, 제품, 규모, 인수 시점과 조건, Dioxus의 향후 거버넌스(오픈소스로 남는지)까지 전부 소스에 없다.

> ⚠️ **ko 자막이 첫 언급에서 회사명을 보통명사로 바꿨다** — *"차세대 소프트웨어 도구인 **인지 컴퓨팅** 분야에서 일하고 싶으시다면"*. 바로 다음 문장에서는 ko도 *"Cognition에 합류했으며"* 로 되돌아와 **한 문장 건너 표기가 갈린다.** 하필 **인수 사실을 전하는 문장**이다.

## 위키에서의 위치

이 위키의 조직 축에서 **"오픈소스 프로젝트를 인수한 회사"** 라는 자리를 처음 채운다. 지금까지 오픈소스와 회사의 관계는 [[block|Block]]→[[goose|Goose]]의 **Linux Foundation 기증**([[tech-bridge-acp-universal-remote]])과 [[minimax]]의 **모델 공개**가 있었는데, **인수는 처음**이다.

> **다음 소스가 나오기 전까지 이 페이지는 채용 공고 한 문단이 전부라는 사실을 그대로 둔다.**

## References

- [[tech-bridge-ambitious-software-agent-era]] · [[dioxus]] · [[jonathan-kelley]]

## 두 번째 소스 — 제품 사용자로서의 언급 한 마디 (2026-09-25 · [[tech-bridge-jensen-huang-cbs-interview]])

[[jensen-huang|Jensen Huang]](NVIDIA CEO)이 CBS 인터뷰에서 사내 사용 도구를 나열하며 *"우리는 [Cognition]을 사용합니다"*(01:19~01:23)라고 한다 — [[openai-astra|Astra]]·[[claude-code|Claude Code]]·[[cursor|Cursor]] 다음. **이 위키에서 Cognition이 "쓰이는 것"으로 나온 첫 언급**이다. ⚠️ **어떤 제품인지는 말하지 않는다** — 회사 이름뿐이다. 이 페이지의 *"채용 공고 한 문단이 전부"* 는 **한 줄 늘었을 뿐**이다.

> ⚠️ **ko 자막이 또 회사명을 보통명사로 바꿨다** — **"우리는 인지 기능을 사용합니다"**(01:19). 09-14의 **"인지 컴퓨팅"** 에 이어 **두 번째**. 이 회사 이름은 ko에서 **한 번도 안정적으로 옮겨진 적이 없다**(09-14 한 문장 건너 복구된 것 제외).

## 세 번째 소스 — "제품 → eval → 모델" 경로의 예로 (2026-09-30 · [[tech-bridge-introspection-loop-is-the-product]])

[[roland-gavrilescu|Roland Gavrilescu]]: *"Think of how um Cursor and Cognition went from building the best product to then uh building the best evals for the product, and finally building the best models based on the previous two artifacts."*(09:09~09:23). **이 위키에서 Cognition의 제품·eval·모델에 대한 첫 서술**이지만 외부 화자의 한 문장이고 근거가 없다 — 위 원칙대로 **자체 모델의 이름·존재를 이 문장으로 확정하지 않는다.** ⚠️ ko는 회사명을 또 **"인지 기능"** 으로 옮겼다(09:12) — 위 첫 소스의 *"인지 컴퓨팅"* 과 같은 유형이다. → [[valued-work-per-watt]]

## FrontierCode — "would you merge this?" 벤치마크 (2026-10-03 · [[tech-bridge-death-of-code-review]])

[[laurie-voss|Laurie Voss]] 진술(2차 인용): Cognition(*"the makers of Devon[=Devin]"*)이 관리자의 실제 질문 *"would you merge this?"* 를 중심으로 **FrontierCode**를 만들어 6월에 냈다(07:50~08:00). 관리자 20명+, 자기 저장소에서 과제 150개, 과제당 전문가 40시간+. 채점 항목은 동작 정확성·회귀·안전·범위 규율·테스트 품질·유지보수성 — *"a human review rubric uh made machine checkable"*(08:08~08:16). [[fable-5-1|Fable 5]] SWE-bench Pro 88% vs 최난도 구간 29%, GPT 5.5 6% 미만(08:20~08:48). → [[mergeability-gap]]

⚠️ en-orig는 같은 벤치마크를 *"Frontier Code"*(07:58)와 *"Frontierbench"*(08:08)로 부른다. 챕터는 *"FrontierCode"*. 벤치마크 문서는 확인하지 않았다.
