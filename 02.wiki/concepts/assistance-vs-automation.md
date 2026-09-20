---
title: 보조 vs 자동화 (Assistance vs Automation)
type: concept
category: theory
tags: [rlhf, automation, assistance, objective-function, human-in-the-loop]
related: [rlhf, preference-reward-asymmetry, post-training-northstars, smarter-software-vs-cheaper-software, workflow-vs-agent, risk-proportional-human-review, verification-cost-asymmetry]
first-seen: tech-bridge-rlhf-assistance-vs-automation
sources: [tech-bridge-rlhf-assistance-vs-automation]
created: 2026-09-20
updated: 2026-09-20
---

# 보조 vs 자동화 (Assistance vs Automation)

**오늘날의 AI가 어떤 과제에는 탁월하고 어떤 과제에는 못 미치는 이유를 난이도가 아니라 목적함수로 설명하는 구분.** [[diogo-almeida|Diogo Almeida]]가 [[tech-bridge-rlhf-assistance-vs-automation]]에서 제시했다.

## 출발점 — 설명이 필요한 관찰

> 어떻게 우리가 **미해결 수학 문제를 풀면서도 고객 서비스에는 실제로 결정을 내리기 위해 사람이 개입해야** 하는지 설명할 수 있을까요? (03:40~03:56)

**오른쪽(고객 서비스, 단순 업무)이 왼쪽(수학 난제)보다 훨씬 쉬워 보이는데 결과가 반대다.**

## 답 — 목표가 다르다

| | **보조 (assistance)** | **자동화 (automation)** |
|---|---|---|
| 과제의 목표 | **루프 안의 사람을 만족시키는 것** | **사람을 루프에서 없애는 것** |
| 사람의 자리 | 목표의 일부 (본질적으로 human-in-the-loop) | 제거 대상 |
| 이상적 최종 상태 | 계속 쓰이는 대화 상대 | *"사용자가 쳐다보지도 않는 서버에서 백그라운드로"*, 궁극적으로 **레거시 소프트웨어** |
| 예 | [[claude-code\|Claude Code]] · ChatGPT | 반복적 백오피스 처리 |
| 오늘날의 AI | **탁월** | **부적합** |

> **[Claude Code] 같은 것의 일은 단순히 코드를 작동시키는 것만이 아닙니다.** … **목표는 그 안에 있는 사람을 만족시키는 것입니다.** (04:25~04:43)

> 반면에 **이러한 모든 작업의 목표는 인간을 루프에서 없애는 것입니다.** … **이것이 바로 보조(assistance)와 자동화(automation)의 차이점입니다.** (04:43~05:00)

원인은 학습 절차에 있다 → [[rlhf]] · [[preference-reward-asymmetry]]

> **오늘날의 AI, 즉 RLHF에서 물려받은 모든 것이 human-in-the-loop 과제에는 매우 뛰어나지만 자동화 과제에는 적합하지 않다.** (05:00~05:18)

## 이 위키에서의 좌표

**[[workflow-vs-agent]]와 축이 다르다.** 그쪽은 *경로가 미리 정해져 있는가* 이고, 이쪽은 *루프 끝에 사람이 만족해야 하는가* 다. **루프가 완전히 동적이어도 사람을 만족시키는 것이 목표라면 여전히 보조다** — 즉 에이전트냐 워크플로냐를 건너뛴 구분이다.

그리고 이 위키가 에이전트의 성패를 설명해 온 층들 — [[agent-harness-design]]·[[context-engineering]]·[[agent-tool-design-practices]] — **위에 한 층을 더 놓는다.** 목적함수가 정해지면 아래층이 무엇을 해도 방향이 정해진다는 주장이다.

**기업들이 이미 경험적으로 도달한 결론이라고 말한다:**

> **모든 기업이 기본적으로 깨달은 교훈은 사업에 중대한 영향을 미치는 결정에는 인공지능을 쓰지 말라는 것**입니다. … **사용자에게 무한한 문서와 고객 서비스를 던져주는 것은 괜찮지만, 비싼 결정을 내리게 만드는 것은 안 된다는 거죠.** (05:18~05:41)

이것이 [[risk-proportional-human-review]]와 **같은 현상의 반대 어조**다 — 09-18 [[anna-gutowska|Gutowska]]는 *"가장 위험한 결정 곁에 사람을 두라"* 를 **처방**으로 말했는데, 여기서는 같은 배치가 **모델이 그 자리에 설 수 없다는 증상**으로 읽힌다.

그리고 [[verification-cost-asymmetry]]에 **원인 쪽 설명**을 준다 — 검증이 남는 이유는 모델이 틀려서가 아니라 **맞아 보이도록 최적화됐기 때문**이다.

## ⚠️ 유보

- **당사자 진술.** 화자는 *"제3의 길"* 을 파는 스텔스 회사 소속이다.
- **두 범주의 경계가 형식적으로 정의되지 않는다** — *"본질적으로 human-in-the-loop"* 인지 여부를 무엇으로 판정하는지 소스에 없다.
- **자동화가 좋은 일인지에 대한 논의가 소스에 전혀 없다** — 일자리·책임·오작동 귀속을 건드리지 않으면서 *사람이 결정해야 하는 상태* 를 결함으로 부른다.

## References

- [[tech-bridge-rlhf-assistance-vs-automation]] — first-seen
- 관련: [[rlhf]] · [[preference-reward-asymmetry]] · [[post-training-northstars]] · [[smarter-software-vs-cheaper-software]] · [[workflow-vs-agent]] · [[risk-proportional-human-review]] · [[verification-cost-asymmetry]] · [[claude-code]]
