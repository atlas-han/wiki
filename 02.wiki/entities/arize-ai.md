---
title: Arize AI
type: entity
category: org
tags: [observability, evals, llm-ops, developer-relations]
aliases: [Arize, Arise AI, "a rise tracing"]
links:
  - https://arize.com
  - https://x.com/arizeai
sources: [tech-bridge-death-of-code-review, tech-bridge-uber-debug-assist]
created: 2026-10-03
updated: 2026-10-09
---

# Arize AI

[[laurie-voss|Laurie Voss]]가 developer relations를 이끄는 회사. 본 위키에는 [[tech-bridge-death-of-code-review]]의 화자 소속으로 처음 등장한다.

> ⚠️ **이 위키의 소스는 회사를 설명하지 않는다.** 자막에서 확인되는 것은 셋뿐이다 — 화자의 소속(*"head of developer relations at Arise AI"* 00:15~00:18, en-orig는 세 트랙 모두 *"Arise"*, 설명란 링크 arize.com으로 판독), 화자의 관심사(*"These days I think about AI and how to test it"* 00:21~00:25), 그리고 행사 후원 정황(*"There are enough pitches for ARISE at this conference"* 22:15~22:18). **제품·기능은 발화되지 않았다.**

## 이 위키에서의 위치

화자는 결론에서 출시 후 **프로덕션 궤적 관측**이 마지막 리뷰어라고 하면서(21:48~22:25) 자사 홍보는 하지 않겠다고 한다. ⚠️ 위키의 표시: 그 결론은 관측·평가 도구 시장과 겹치므로 **이해관계가 있는 화자의 진술**로 읽는다. → [[automated-code-review]] · [[production-trace-eval-flywheel]]

### 2026-10-09 — 고객 쪽에서 처음 이름이 나왔다 ([[tech-bridge-uber-debug-assist]])

[[uber|Uber]]의 [[kriti-dangi|Kriti Dangi]]가 Q&A에서 사내 디버깅 에이전트 [[debug-assist|Debug Assist]]의 트레이싱 도구로 언급했다: *"we do have built-in tracing um if you are aware, it's called a rise tracing, and that comes in really really handy. So, we have plugged it in with LangChain, as well as each of the LLM calls that we make"*(25:23~25:33) — 서브에이전트뿐 아니라 *"every tool call (…) all the MCPs that we call, every bash command that the agent runs"*(25:35~25:43)를 본다. en-orig는 *"a rise tracing"*, `en` *"Arize tracing"*, ko *"Arize 트레이싱"* — Arize로 판독. **이 위키 소스에서 Arize의 제품 기능(에이전트 트레이싱)이 처음 발화된 자리**다. ⚠️ 화자는 직전에 *"I work in observability space"*(25:18~25:20)라고 했다 — 관측 쪽 사람의 도구 선택이며, Arize 소속 여부는 발화되지 않는다.

## 미해결 사항

- 제품(관측·eval 플랫폼으로 알려져 있으나 이 위키 소스에 근거 없음) — 별도 소스 ingest 필요. **부분 해소(2026-10-09)**: 고객 쪽 발화로 *에이전트 트레이싱* 기능이 처음 언급됐다([[tech-bridge-uber-debug-assist]]). 제품 문서·범위는 여전히 미확인.

## References

- [[tech-bridge-death-of-code-review]] · [[laurie-voss]] · [[tech-bridge-uber-debug-assist]]
- <https://arize.com> (⚠️ 열어 보지 않았다)
