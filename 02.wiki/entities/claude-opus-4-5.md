---
title: Claude Opus 4.5
type: entity
category: model
tags: [anthropic, claude, opus]
aliases: [Opus 4.5]
sources: [anthropic-harness-design-long-running-apps, anthropic-managed-agents, tech-bridge-company-brain-security, tech-bridge-vercel-eve-filesystem-agent]
links: []
created: 2026-05-25
updated: 2026-09-19
---

# Claude Opus 4.5

[[anthropic|Anthropic]] Claude 시리즈의 한 세대 전 플래그십. [[anthropic-harness-design-long-running-apps]] 초기 실험의 메인 coding 모델.

## 알려진 사실

- [[anthropic-harness-design-long-running-apps]] 첫 버전(레트로 게임 메이커)의 generator. Solo 20분 $9 vs full harness 6시간 $200 비교의 그 모델.
- [[claude-sonnet-4-5|Sonnet 4.5]]에서 두드러졌던 [[context-anxiety|context anxiety]]는 Opus 4.5 시점에서 *자체적으로* 사라짐 → [[context-resets-and-compaction|context resets]]을 harness에서 dropped 가능 ([[anthropic-managed-agents]] 인용).
- [[anthropic-harness-design-long-running-apps]] 시점에서는 sprint construct로 work decomposition을 받아야 일관성을 유지 → [[claude-opus-4-6]] 등장 후 제거.
- (2026-09-10) [[tech-bridge-company-brain-security]]의 SRE 사례에서 [[promptql|PromptQL]] 에이전트의 **현재 모델**로 지칭된다 — 엔지니어가 LIKE 쿼리를 쓴 에이전트에게 *"이 멍청아. 이게 Opus 4.5야. 이러지 마"*. ko 자막은 *"작품번호 4.5"* 로 오역. 그 발표의 촬영 시점 앵커 중 하나.

## 위치

- 같은 세대 하위: [[claude-sonnet-4-5]]
- 후속: [[claude-opus-4-6]]

## 외부 증언 (2026-09-19 · [[tech-bridge-vercel-eve-filesystem-agent]])

[[vercel|Vercel]]의 [[andrew-qu|Andrew Qu]]가 이 모델과 [[claude-code|Claude Code]]의 조합을 **자사 에이전트를 세 번 실패한 뒤의 비교 기준**으로 삼는다.

> 그리고 나서 **[[claude-code|클로드 코드]]와 [Opus] 4.5**가 출시되었습니다. 음, 정확히 말하자면 **[Opus] 4.5가 출시되었고, 클로드 코드와 밀접한 관련**이 있는데 … **그들은 파일 시스템 에이전트라는 개념을 새롭게 제시했습니다.** (07:22~07:30)

> **"와, 클로드 코드와 [Opus] 4.5는 우리가 이전에 가지고 있던 것과 비교하면 거의 인공 일반 지능(AGI)이나 다름없네."** … **거의 모든 질문에 막힘없이 답해줬습니다.** (07:38~07:53)

**이 위키가 받은 이 모델에 대한 제3자 평가 중 가장 강한 표현**이고, 동시에 가장 느슨한 것이기도 하다 — *"거의 AGI"* 는 **자사 에이전트와의 상대 비교**이지 절대 평가가 아니다. 화자 자신이 비교 대상을 *"우리가 손으로 키운 에이전트"* 라고 못 박는다.

⚠️ 수치는 *"eval 점수 두 배"* 하나뿐이고 실체가 없다. ⚠️ 화자는 모델의 능력과 [[claude-code|Claude Code]]라는 하네스의 기여를 **가르지 않는다** — 그가 실제로 가져간 것은 모델이 아니라 [[file-system-agent|파일 시스템이라는 설계]]였다. ⚠️ ko 자막이 한 문단에서 *오퍼스*·*오푸스* 두 표기로 갈린다.

## References

- [[anthropic-harness-design-long-running-apps]]
- [[anthropic-managed-agents]]
- [[tech-bridge-company-brain-security]] — 제3자 사용 언급 (2026-09-10)
