---
title: Token Economizer
type: entity
category: tool
tags: [microsoft, coding-agents, plugin, token-cost, hooks, claude-code, micro-skills, tool-pruning]
aliases: [TokenEconomizer, 토큰 이코노마이저, micro skills, 마이크로스킬]
links:
  - https://github.com/microsoft/TokenEconomizer
sources: [tech-bridge-ai-labs-token-economizer]
created: 2026-11-04
updated: 2026-11-04
---

# Token Economizer

**코딩 에이전트의 세션을 지켜보고 토큰 낭비를 뒤 세션에서 줄이는 [[microsoft|Microsoft]]의 플러그인.** [[claude-code|Claude Code]] · [[codex|Codex]] 등에 설치한다. 이 위키의 유일한 출처는 [[ai-labs|AI Labs]](설명란 근거)의 해설 · 시연 [[tech-bridge-ai-labs-token-economizer]]이다.

> ⚠️ **아래 동작 · 수치는 모두 발표자의 설명 · 전달 · 측정이다.** 저장소 링크는 Tech Bridge 설명란에서 가져왔고 **위키는 저장소와 공식 문서를 열어 보지 않았다.** 임계값 · 명령 철자 · 기본값 · 라이선스는 미확인이다.

> *"Instead of making a map, it learns from how you work."*(00:43~00:45)

## 줄이는 세 군데

| 낭비 | 동작(발표자 설명) | 기본값 |
|---|---|---|
| **반복 실수** → **micro skills** | 같은 실수가 반복되면 프로젝트 사실로 적고, 몇 세션의 확인 뒤 저장해 세션 시작 때 건넨다 | **꺼짐** |
| **쓰지 않는 도구** → [[usage-based-tool-pruning]] | *"If one of them doesn't get used across 10 of your messages over at least two sessions, the tool turns it off for that project."*(03:22~03:28) | 켜짐(추정, *"most of its features are turned on"*) |
| **막힌 작업** | 모델로 정말 막혔는지 확인 → 한 번만 다른 시도를 권함 → 그래도 막히면 사람에게 escape를 권함. *"It never stops Claude by itself."*(04:14~04:16) | 켜짐(추정, 위와 같음) |

## 훅으로 돈다

세션 시작 훅이 사실을 건네고, 도구 사용 후 훅이 막힘을 보고, 세션이 끝나면 돌아보며 사실 · 미사용 도구를 센다(04:53~05:18). *"The hooks run on their own at set times"*(04:42~04:44) → [[hook-enforced-workflow]]

## 명령 (발화 표기, 철자 미확인)

config · status · micro skills · tool prune · tool prune measure · tool prune restore. 되돌린 도구는 다시 끄지 않는다(10:07~10:11).

## micro skills와 prompt injection

기본으로 꺼 둔 이유 둘(05:28~06:07): 3세션마다 모델이 최근 세션을 읽어 한도를 쓰고, 사실의 재료가 **명령 출력**이기 때문이다.

> *"So, if you download a project from someone else, whoever made it could hide instructions in what its commands print. Those instructions would end up in the facts, and Claude would treat them as true in every session unless you change them yourself."*(05:50~06:01)

발표자는 자기 프로젝트에서는 켜라고 권한다(06:07~06:13). ⚠️ 그 선의 근거는 발화되지 않았다 → [[prompt-injection]].

## 콜드 스타트 — 처음에는 더 비싸다

*"it can even cost you more while it's still learning."*(06:48~06:52) Microsoft 시험에서 거의 모든 프로젝트가 처음에는 더 비쌌고 *"only got cheaper by the sixth task."*(06:56~06:58) 프로젝트마다 다시 배운다(06:58~07:06).

**AI Labs 수정판**: 저장소를 Claude에게 고치게 해 첫 세션에서 백그라운드로 같은 폴더의 지난 세션 기록을 먼저 읽게 했다(07:17~07:56). 새 프로젝트에는 소용없다(08:09~08:13). ⚠️ Microsoft 공식 동작이 아니고, 프롬프트는 화면에만 있어 자막에 없다.

## 수치 — 단위가 다르다, 합치지 않는다

| 출처 | 값 | 단위 | ⚠️ |
|---|---|---|---|
| Microsoft(전달) | Claude Code Sonnet 5 −23.6%, Opus 4.8 −30.9% | 작업 비용 | 277개 버그 · 6개 프로젝트 · 5개 구성 중 숫자는 2개만 발화, 원자료 미확인 |
| AI Labs(수정판, 데모) | 34,300 → 24,400, 약 29% | 메시지당 토큰(도구 끄기만) | 1개 프로젝트, 비용 아님 |
| AI Labs(다른 앱) | 99 → 79 스텝, 비용 약 21% | 3과제 합계 | 과제당 1회 비교, 모델 · 앱 · 검사 내용 미발화 |

## ⚠️ Contradiction — 끄는 것을 알려 주는가

발화: *"So, you won't even know it took a tool out of your context window."*(03:38~03:42) · *"the plugin turns them off without telling you"*(09:26~09:29). 설명란: *"공식 문서는 도구의 동작을 한 줄로 알린다고 설명합니다(2026년 11월 2일 확인)."* 설명란의 "도구의 동작"이 도구 끄기를 가리키는지 명시돼 있지 않고 공식 문서를 열어 보지 않아 미확정이다.

## 미해결

- 사실의 삭제 · 수정 경로, 사람 승인 유무. *"unless you change them yourself"* 만 있다.
- 막힘 판정의 시간 기준과 그 호출의 사용량. 세 기능 호출의 합계 비용 → [[hidden-harness-calls]]
- Codex · Copilot 쪽 동작 차이, 끄는 메커니즘, 프롬프트 캐시에 주는 영향 → [[prompt-caching]]

## References

- [[tech-bridge-ai-labs-token-economizer]] — first-seen
- <https://github.com/microsoft/TokenEconomizer> (⚠️ 설명란 링크, 열어 보지 않았다)
- [[microsoft]] · [[ai-labs]] · [[graft]] · [[usage-based-tool-pruning]] · [[prompt-injection]]
