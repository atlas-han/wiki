---
title: "지연 도구 컨텍스트 (Deferred Tool Context)"
type: concept
category: technique
tags: [tools, tool-bloat, progressive-disclosure, context-engineering, lazy-loading, mcp, tokens]
related: [toolbox-pattern, context-engineering, agent-skills, context-rot, context-resets-and-compaction, model-context-protocol, agent-tool-design-practices, software-factory, push-vs-pull-context-retrieval]
first-seen: tech-bridge-factory-software-factory
sources: [tech-bridge-factory-software-factory]
created: 2026-10-02
updated: 2026-10-02
---

# 지연 도구 컨텍스트 (Deferred Tool Context)

**연결된 도구의 전체 스키마를 처음부터 컨텍스트에 싣지 않고, 짧은 목록과 짧은 설명만 두었다가 에이전트가 실제로 필요로 할 때 그 도구를 호출해 전체 정의를 로드하는 방식.** 도구에 적용한 progressive disclosure. [[factory-ai|Factory]]는 이를 **deferred context engine**이라 부른다 — [[tech-bridge-factory-software-factory]] ([[tereza-tizkova|Tereza Tížková]]).

> *"we just progressively disclose what's in the context and what tools to use"* (16:00~16:05) · *"important thing is nothing is actually removed. is just hidden and not reachable until needed"* (16:23~16:29)

> ⚠️ **벤더 수치.** *"you can save 50% of tokens or more"*(16:40~16:42) — 도구가 많을수록 절감이 커진다는 말뿐, 측정 조건(도구 수, 과제, 기준선)이 없다.

## 문제 — 도구 bloat (15:07~15:52)

- 기업은 Figma·Notion·Gmail·Drive·Slack 등 *"hundreds tools on average"*(15:25~15:30, ⚠️ 출처 없음)
- 도구마다 *"specification in the code (…) schema and parameters and log[=long] descriptions"*(15:33~15:37)
- 결과 둘: ① **비슷한 이름의 도구를 잘못 고른다**(*"pick wrong tools if there are two tools that sound similar"* 15:41~15:45) ② **컨텍스트를 잃는다** — 창을 채워 *"need to compress"*(15:45~15:50) → [[context-rot]] · [[context-resets-and-compaction]]

*"there is this elephant in the room, context with agents"*(15:07~15:10) — 장기 미션을 도는 [[software-factory]]에서 특히.

## 메커니즘 (15:55~16:42)

1. 처음엔 *"short list of the tools and uh only a short descriptions"*(16:14~16:19)
2. 코드 작업 중 필요해지면 *"they can call the tool and fully load it"*(16:19~16:23)
3. 지워지는 것은 없다 — 숨겨져 있을 뿐(16:23~16:29)
4. 도구가 많을수록 절감이 커진다(16:32~16:42)

판독 미확정: *"we basically have a surprise tools uh that help later only if they are actually needed"*(16:05~16:11) — 세 자막 트랙 모두 *surprise tools*. "필요할 때만 나중에 꺼내는 도구" 정도로 읽는다.

## 같은 결론, 다른 메커니즘

| | **지연 도구 컨텍스트** (Factory) | **[[toolbox-pattern\|툴박스 패턴]]** (Oracle) | **[[agent-skills\|스킬]]** progressive disclosure |
|---|---|---|---|
| 상시 컨텍스트 | 도구 이름 + 짧은 설명 목록 | 없음 — 매 반복 검색 결과만 | 스킬 프런트매터 몇 줄 |
| 로드 트리거 | **에이전트가 도구를 호출**할 때 | 하네스가 **벡터 검색**으로 매 반복 조립 | 에이전트가 스킬을 고를 때 |
| 빼기 | 언급 없음(숨김 → 로드) | 필요 없어지면 뺀다 | 언급 없음 |
| 규모 대응 | *"hundreds tools"* | *"도구가 수천 개면?"* → 인덱스 | 스킬 수가 늘면 판단 흐림 우려 |

공통: **목록은 싸게, 본문은 필요할 때.** 차이: 누가 고르는가(에이전트 vs 검색 하네스)와, 한 번 로드한 정의를 다시 빼는가.

> 위키의 정리: Factory의 방식은 **에이전트가 짧은 설명만 보고 도구를 고를 수 있어야** 성립한다 — 그런데 화자가 든 첫 번째 실패가 *비슷한 이름의 도구를 잘못 고른다*였다. 짧은 설명이 그 혼동을 줄이는지 키우는지는 말하지 않는다. [[agent-tool-design-practices]]의 *도구 이름·설명 설계*가 여기서 더 중요해진다.

## 미해결

- **프롬프트 캐시와의 관계** — 로드할 때마다 도구 정의가 추가되면 캐시 접두가 바뀌는가. [[toolbox-pattern]]도 같은 질문(매 반복 재조립의 비용)을 미해결로 둔다.
- 짧은 설명을 누가 쓰는가(사람 vs 자동 요약).
- 50% 절감의 측정 조건.

## References

- [[tech-bridge-factory-software-factory]] — first-seen
- [[toolbox-pattern]] · [[agent-skills]] · [[context-engineering]] · [[model-context-protocol]] · [[push-vs-pull-context-retrieval]] · [[software-factory]]
- [[factory-ai]] · [[tereza-tizkova]]
