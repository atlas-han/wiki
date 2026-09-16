---
title: 권력 균형으로서의 안전 (Balance of Power as Safety)
type: concept
category: theory
tags: [ai-safety, open-source, policy, diffusion, governance]
aliases: [견제와 균형이 안전이다, 접근 제한은 안전이 아니다]
related: [personal-superintelligence, training-time-risk, regulatory-capture, default-legal-regulation, intelligence-abundance, agent-governance-layers]
first-seen: tech-bridge-zuckerberg-muse-personal-agent
sources: [tech-bridge-zuckerberg-muse-personal-agent, tech-bridge-dario-amodei-cbs-interview]
created: 2026-09-14
updated: 2026-09-16
---

# 권력 균형으로서의 안전

**미래 안전의 토대는 접근을 제한하는 것이 아니라, 올바른 견제와 균형 그리고 권력의 균형을 세우는 것이다.** [[mark-zuckerberg]]가 [[tech-bridge-zuckerberg-muse-personal-agent]]에서 세 원칙 중 셋째로 제시한다.

> **① 사람에게 권한을 주는 것이 세계 번영의 원천이고 역사 내내 그랬다. ② AI의 주된 용도는 자동화가 아니라 새로운 것의 발명이다. ③ 미래 안전의 토대는 접근을 제한하는 것이 아니라 올바른 견제와 균형, 그리고 권력의 균형을 세우는 것이다.** (01:29~01:56)

## 이 위키의 안전 축을 반으로 가른다

지금까지 모인 안전 담론은 **게이트를 어디에 둘 것인가**를 다퉜다.

| 소스 | 게이트의 위치 |
|---|---|
| [[training-time-risk]] · [[tech-bridge-altman-frontier-rl-pause]] | **배포 → 훈련**으로 앞당김 |
| [[project-glasswing]] · [[coordinated-vulnerability-disclosure]] | 발견과 공개의 절차 |
| [[tech-bridge-build-time-vs-runtime-tools]] | 도구가 노출되는 **시점** |
| **이 개념** | **게이트 자체가 위험이다** |

> **많은 사람이 "이 기술은 아주 강력하니 많은 사람이 접근하지 못하게 제한해야 한다"고 생각합니다. 저는 개인적으로 **소수의 랩이나 사람이 이만큼 유능한 것을 통제하게 되는 쪽이 훨씬 더 걱정**됩니다.** (02:08~02:22)

## 세 갈래 논증

### ① 역사 논증

> **권력을 사람들 손에 쥐여 줄 때, 대부분의 진보는 기득권이나 기성 체제에서 나오지 않습니다. 주변부에 있는, 아이디어가 진지하게 받아들여지지 않는 사람들에게서 나옵니다. 그런데 그들이 자기가 하는 일을 증명할 만큼의 도구를 갖게 되면 그게 아주 강력해집니다.** (02:23~02:41)

### ② 사이버보안 논증

> **시스템을 해킹할 수 있는 AI를 누군가 가진 것에 대한 최선의 해독제는, 모두가 AI에 접근해 자기 시스템부터 단단하게 만드는 것**입니다. **지난 수십 년 사이버보안의 역사가 그랬습니다 — 오픈소스 소프트웨어는 사람들이 보고 뜯어볼 수 있기 때문에 역설적으로 사람들 손에 쥐여 줌으로써 더 안전하고 안정적인 환경이 됩니다.** (03:05~03:34)

사례가 하나 붙는다 — *"[[hugging-face|Hugging Face]]는 세계 100대 기관은 아닐지 몰라도 중요합니다. **침입을 감지했을 때 그들이 한 일은 오픈소스 모델로 돌아선 것이었습니다.**"* → **"상위 100개 기관에만 준다"는 배분 방식의 반례로 쓰인다.**

### ③ 법정 비유

> **한 사람만 초지능 변호사를 가지면 이기지 못할 사건도 이길 수 있습니다. 하지만 모두가 가지면 아주 효율적인 스파링이 되고, 아무도 어리석은 주장이 그대로 서 있게 두지 못합니다. 그러면 정의가 훨씬 더 효율적이고 공정하게 실현되겠죠.** (53:45~54:14)

> **피해야 할 것은 한 사람 또는 소수만 초지능 변호사를 갖고 나머지는 못 갖는 경우입니다. 그러면 모든 시스템과 제도가 그걸 가진 사람들에게 유리하게 뒤틀립니다.** (54:15~54:32)

## 검토되지 않은 전제

> ⚠️ **공격과 방어의 대칭성.** 세 논증 모두 **같은 도구가 양쪽에 같은 이득을 준다**는 전제 위에 선다. 소스는 이 전제를 논증하지 않는다. 이 위키가 기록한 반대 방향의 관측이 있다 — [[ai-vulnerability-discovery]], [[claude-mythos-preview]]의 사이버 capability frontier, [[project-glasswing]]. **양쪽 다 당사자 진술이다.**
>
> ⚠️ **②(자동화가 아니라 발명)는 주장만 있고 근거가 없다.** 같은 위키의 [[ai-jobs-impact]] 기록과 연결되지 않는다.
>
> ⚠️ **화자의 인센티브.** 오픈 웨이트 전략을 쓰는 회사의 CEO다. 다만 **본인이 열성분자가 아님을 명시한다** — *"우리가 하는 모든 게 오픈소스인 것도 아닙니다. 오픈 모델 몇 개를 내고, 비공개로 하는 일도 있습니다."*

## 흥미로운 순서 바꾸기

오픈소스가 **수단으로 격하된다.**

> **[진행자] 오픈소스가 당신이 걱정하는 흐름에 대한 대응인가요?** — **아니요, 가장 중요한 건 사실 그냥 기술을 개인의 손에 쥐여 주는 것**입니다. 그래서 **[[muse|Muse]] 개인 에이전트 같은 것이 어쩌면 훨씬 더 중요**합니다. (04:54~05:17)

**"무엇을 공개하느냐"보다 "누가 쓸 수 있느냐"를 위에 놓는다.** → [[personal-superintelligence]] · [[intelligence-abundance]]

## 자연적 한계 주장

소스는 이것을 **선택이 아니라 제약**으로도 제시한다.

> **소수의 랩이 이만큼 중요하고 유능한 기술을 통제하며 막대한 부를 자기들에게 쌓는 일은 **허용되지 않을 것**이라고 봅니다. 기술적으로도 작동해야 하지만 **사회적으로도 작동해야** 하고, 그 둘은 함께 가야 합니다.** (13:57~14:24)

> **우리가 만드는 기술이 일자리를 만들지 못하거나, 광범위한 번영을 만들지 못하거나, 우리가 짓는 인프라가 지역 사회에 도움이 안 된다면, 그건 계속되도록 허용되지 않을 겁니다.** (11:12~11:24)

## References

- [[tech-bridge-zuckerberg-muse-personal-agent]] · [[mark-zuckerberg]] · [[meta]]
- 관련: [[personal-superintelligence]] · [[training-time-risk]] · [[intelligence-abundance]] · [[regulatory-capture]] · [[default-legal-regulation]] · [[hugging-face]] · [[ai-vulnerability-discovery]] · [[ai-jobs-impact]]

## 같은 공포, 반대 처방 — Amodei (2026-09-16 · [[tech-bridge-dario-amodei-cbs-interview]])

[[dario-amodei|Dario Amodei]]가 이 페이지의 **공포를 공유하면서 반대로 간다.**

> **단 하나의 정부가 단 하나의 기업만큼이나 쉽게 이 기술을 남용할 수 있다는 것이 우려됩니다. 하지만 민주적으로 선출된 정부들의 조합이라면 — 어떤 형태의 감독, 어떤 형태의 공동 거버넌스.** (18:46~19:06)

| | [[mark-zuckerberg]] (이 페이지) | Amodei |
|---|---|---|
| 두려워하는 것 | 소수의 랩·사람이 통제 | 단일 기업 **또는 단일 정부**가 통제 |
| 처방 | **확산** — 접근 제한이 위험 | **공동 감독** — 다수 민주 정부 |
| 공개 | 오픈 모델 | *"생물 테러리스트가 쓸 수 있는 모델을 공개하지 않기로"* 를 미·중 협약에 |

Zuckerberg는 통제 주체를 **없애고**, Amodei는 통제 주체를 **복수화·민주화**한다. 그리고 Amodei의 *"모델을 공개하지 않기로"* 는 이 페이지의 첫 문장(*"접근을 제한하는 것이 아니라"*)과 **정면으로 맞선다.** ⚠️ 해소하지 않는다 — 둘 다 자기 회사의 형태와 맞는 처방이다. → [[joint-democratic-oversight]]
