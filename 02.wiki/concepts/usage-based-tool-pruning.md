---
title: "사용 이력 기반 도구 끄기 (Usage-Based Tool Pruning) — 안 쓴 도구를 지난 세션 기록으로 골라 뺀다"
type: concept
category: pattern
tags: [tool-pruning, context-engineering, token-cost, claude-code, harness-design, tool-bloat, silent-change]
aliases: [usage-based tool pruning, tool prune, 도구 끄기, 미사용 도구 제거, 사용 이력 기반 도구 제거]
related: [deferred-tool-context, toolbox-pattern, harness-pruning, token-minimization-trap, agent-tool-design-practices, hidden-harness-calls, prompt-caching, no-silent-write, token-economizer]
first-seen: tech-bridge-ai-labs-token-economizer
sources: [tech-bridge-ai-labs-token-economizer]
created: 2026-11-04
updated: 2026-11-04
---

# 사용 이력 기반 도구 끄기 (Usage-Based Tool Pruning)

**지난 세션에서 쓰이지 않은 도구를 자동으로 골라 그 프로젝트의 컨텍스트에서 뺀다. 도구 정의가 매 메시지에 실려 가는 비용을 줄이는 대신, 에이전트가 할 수 있는 일이 조용히 줄어들 수 있다.** 이 위키의 첫 사례는 [[token-economizer|Token Economizer]]이고 출처는 [[ai-labs|AI Labs]](설명란 근거)의 해설 [[tech-bridge-ai-labs-token-economizer]]이다.

> *"If one of them doesn't get used across 10 of your messages over at least two sessions, the tool turns it off for that project."*(03:22~03:28)

## 사례의 모양 (⚠️ 발표자 설명, 저장소 미열람)

| 칸 | 내용 |
|---|---|
| **신호** | 사용 횟수만 — 10메시지 · 최소 2세션 동안 미사용 |
| **범위** | 프로젝트 단위. *"A tool the plugin turned off stays off in that project"*(09:59~10:01) |
| **승인** | 없음. *"it does this without asking you."*(03:36~03:38) ⚠️ 설명란의 *"한 줄로 알린다"* 와 어긋남 → [[token-economizer]] |
| **가시성** | 명령으로 목록 · 미사용 세션 수 · 메시지 수를 볼 수 있다(09:11~09:20) |
| **효과 측정** | 전체 도구일 때와 쓰는 도구만일 때의 메시지당 토큰(09:41~09:45) |
| **복구** | restore 명령. *"And once you've given a tool back, the plug-in won't turn it off again."*(10:07~10:11) |

## 실패 모양 — 드물게 쓰는 도구

발표자가 복구 절차를 말하며 스스로 실패를 예고한다: *"this command is the place to check whenever Claude suddenly can't do something it used to do."*(09:29~09:33) 미사용은 불필요와 다르다. 배포 · 릴리스처럼 드물게 쓰는 도구는 이 신호로 구분되지 않는다(위키의 판단, 발표자는 예를 들지 않는다). 그리고 에이전트가 도구 없이 다른 길로 돌아가면 사용자는 끈 도구가 원인이라는 것을 알기 어렵다.

## 다른 답들과 비교

| | **사용 이력 끄기** | [[deferred-tool-context\|지연 로딩]] | [[toolbox-pattern\|툴박스]] | [[harness-pruning]] |
|---|---|---|---|---|
| 언제 고르나 | 세션이 끝난 뒤, 다음 세션을 위해 | 실행 중, 필요할 때 | 반복마다 | 모델이 좋아졌을 때 |
| 누가 고르나 | 사용 기록(규칙) | 모델 | 검색 하네스 | 하네스 제작자 |
| 뺀 뒤 에이전트가 되찾나 | **아니다** — 사람이 restore | 그렇다 — 호출해 로드 | 다음 검색에서 | 해당 없음 |
| 근거 | 과거 사용 | 현재 필요 | 현재 과제 | 모델 능력 |

핵심 차이는 **되돌리는 주체**다. 지연 로딩은 숨기기만 해서 모델이 다시 찾을 수 있고, 여기서는 사람이 복구해야 한다. 표의 "되찾나" 칸은 발화된 복구 절차에서 읽은 것이고, 에이전트가 스스로 되살리는 경로가 있는지는 저장소를 보지 않아 미확정이다.

## 측정 (⚠️ 전달 · 특정 프로젝트, 합치지 않는다)

- 발표자 전달(Microsoft 시험): *"Microsoft's own numbers show this one saves the most tokens"*(03:30~03:34). 기능별 숫자는 발화되지 않는다.
- 발표자 데모(수정판, 4세션 프로젝트): 276개 미사용, *"every message went from about 34,300 tokens down to about 24,400"*(09:47~09:51), 약 29%.
- 위키 산술: 9,900 ÷ 276 ≈ 도구당 약 36토큰. 전체 스키마라기엔 작아 보이며 이미 이름 목록만 실린 값일 수 있다(추정, 설명 없음). **그렇다면 이 기법의 이득은 이미 지연 로딩을 쓰는 환경에서 줄어든다.**
- 메시지당 토큰은 비용이 아니다. 캐시 할인 반영 여부가 발화되지 않았다 → [[prompt-caching]]

## 이 위키에서의 자리

- [[token-minimization-trap]]은 비대한 도구 카탈로그를 *빼도 되는 쪽*에 두었다. 이 패턴은 그 왼쪽 칸의 자동화다. 다만 같은 페이지의 경고대로 비용이 재작업으로 옮겨 가는지는 이 측정이 보지 않는다(99 → 79 스텝 비교는 몇 개 과제에서 통과 여부만 본다).
- [[no-silent-write]]의 반대쪽 사례다 — 에이전트의 능력을 바꾸는 변경이 *묻지 않고* 일어난다. 같은 도구가 막힌 작업은 *"It never stops Claude by itself."*(04:14~04:16)라고 사람에게 넘기는 것과 대비된다(위키의 읽기).
- [[harness-pruning]]은 사람이 모델 능력을 근거로 하네스를 지우는 일이었고, 이 패턴은 규칙이 사용 기록을 근거로 도구를 뺀다. 이름은 비슷하지만 신호와 주체가 다르다.

## ⚠️ 유보

- 사례 하나, 출처 하나, 저장소 미열람. 임계값 10 · 2의 근거는 발화되지 않았다.
- 끄는 메커니즘(설정 · 권한 · 시스템 프롬프트 어느 층인지), 세션 중 적용 시점, 캐시 접두 영향은 미발화.
- MCP 도구와 내장 도구를 구별하는지 미발화. 276개 · 303개의 내역도 없다.

## References

- [[tech-bridge-ai-labs-token-economizer]] — first-seen
- [[token-economizer]] · [[deferred-tool-context]] · [[toolbox-pattern]] · [[harness-pruning]] · [[token-minimization-trap]] · [[no-silent-write]] · [[prompt-caching]]
