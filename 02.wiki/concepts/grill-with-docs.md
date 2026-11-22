---
title: "Grill with Docs — 만들기 전에 질문으로 들볶고, 용어와 결정을 문서로 남긴다"
type: concept
category: pattern
tags: [agent-skills, requirements, glossary, naming, adr, alignment, spec-driven-development, matt-pocock]
aliases: [grill-with-docs, grill me with docs, grill me, 그릴 위드 독스, 질문 먼저, grilling]
related: [spec-driven-development, plan-to-ticket-pipeline, intent-md, fuzzy-intent-discovery, agent-skills, context-resets-and-compaction, codebase-gardening]
first-seen: tech-bridge-pocock-21k-lines-questions-before-code
sources: [tech-bridge-pocock-21k-lines-questions-before-code]
created: 2026-11-22
updated: 2026-11-22
---

# Grill with Docs

**구현을 맡기기 전에 에이전트가 사람에게 번호 붙은 질문을 던져 둘이 같은 그림을 볼 때까지 맞추고, 그 과정에서 정해진 용어는 용어집에, 굵직한 결정은 결정 기록(ADR)에 바로 적는 방식.** [[matt-pocock|Matt Pocock]]의 스킬 저장소 [[mattpocock-skills|mattpocock/skills]]에 있는 스킬 이름이기도 하다. 위키에는 [[tech-bridge-pocock-21k-lines-questions-before-code]](2026-11-21 한국어 해설)로 들어왔다 — 이름 자체는 [[tech-bridge-lauren-tan-pocock-podcast-full]]에서 *"grill me with docs"* 로 먼저 발화됐다. ⚠️ 해설 전달이다: Pocock의 원음은 캡션에 없고 스킬 파일도 열지 않았다.

## 정의 (해설)

- *"그릴 위드 독스는 이름 그대로 사람을 들볶는 스킬입니다."*(02:25~02:27) *"사람과 에이전트가 같은 그림을 볼 때까지 질문을 던집니다."*(02:29~02:30)
- *"정해진 용어는 그 자리에서 바로 용어집에 적고 굵직한 결정은 문서로 남깁니다."*(02:32~02:36)
- 언제 쓰나 — 디프의 크기로 고른다: *"디프가 작으면 질문 없이 한 번에 시키면 됩니다. 크면 그릴 위드 독스라는 스킬로 질문부터 받습니다."*(01:23~01:27) *"한 세션에 안 담길 만큼 크면 웨이파인더로 넘깁니다."*(01:29~01:30)[=wayfinder]

## 작동 방식 (한 기능의 사례)

1. **첫 요청에는 할 일 목록이 없다.** *"지금 뭐가 불편한지, 어떤 모습으로 원하는지만 있습니다."*(02:20~02:23)
2. **질문이 코드를 보고 고쳐진다.** *"에이전트는 백그라운드 에이전트를 띄워 코드 베이스를 뒤지고 찾은 내용에 맞춰 질문 두 개를 고쳐 다시 냅니다."*(02:51~02:56)
3. **질문의 중심은 이름이다.** *"이름이 정해지면 기능도 다 정해진 셈이라고 말합니다."*(03:14~03:16) 후보 이름은 **시나리오 테스트** 로 고른다 — *"후보 이름을 실제로 쓸 법한 문장에 넣어 보고 어디서 어색해지는지 표를 따지는 겁니다."*(03:52~03:56)[=표로] 떨어뜨리는 칸 가운데 하나는 *"매트가 일하면서 소리내어 말하는 단어인가?"*(04:07~04:08) 이고, 용어집에 같은 말이 이미 다른 뜻으로 있는지도 검색한다.
4. **어색함이 남으면 결정 기록으로.** *"이름에 다이어그램이 들어가지만 실제 다이어그램은 아니라는 점은 결정 기록 ADR로 따로 남겼습니다."*(04:20~04:24) 이유는 체스터턴의 울타리이고, *"이렇게 기록해 둬야 다음 실행에서도 맥락을 아는 질문을 받을 수 있다고도 말합니다."*(05:01~05:05)
5. **질문과 나란히 프로토타입.** 화면 구성처럼 써 봐야 아는 문제는 서브 에이전트에게 시안 세 개를 한꺼번에 시킨다 — *"그는 마음에 안 드는 시안이 오히려 더 많은 걸 알려준다고 말합니다."*(05:15~05:16)
6. **끝은 스펙.** *"질문 번호가 40에 이르자 그는 정리를 시킵니다."*(07:08~07:09) 문답이 문서로 정리돼 있으니 대화는 압축해도 된다 → [[context-resets-and-compaction]]

## 왜 이름인가 (해설의 테제)

> *"이름이 정해지면 데이터 모델이 정해지고 에이전트가 혼자 골라야 할 선택지는 그만큼 줄어듭니다."*(13:14~13:18)

사례의 저장소에는 560줄짜리 용어집이 있었고, 새 개념(*썸네일 다이어그램*)은 기존 용어(다이어그램 · 스냅샷 · 보존 스냅샷 · 신)와 부딪히지 않는 자리를 찾아야 했다. 에이전트가 처음 내놓은 이름(*썸네일 드로잉*)은 사람이 거절했다.

## 이웃 개념과의 차이

- [[plan-to-ticket-pipeline]]의 plan mode — 해설은 Pocock이 이 방식을 플랜 모드와 비교한다고 전한다: *"만들기 전에 무엇을 만들지부터 맞추니 결과를 예측하기 쉬워진다는 겁니다."*(03:01~03:03) 계획(어떻게)보다 앞선 합의(무엇을)라는 뜻으로 읽힌다. ⚠️ 비교의 원음은 캡션에 없다.
- [[spec-driven-development]] — 스펙을 먼저 쓰는 것이 아니라 문답의 **부산물** 로 스펙이 나온다.
- [[fuzzy-intent-discovery]] — 질문 하나를 정보 이득으로 고르는 검색 쪽 논의와 달리, 여기서는 질문이 번호를 달고 묶음으로 오고 답은 사람이 받아쓰기로 말한다.
- [[intent-md]] — 의도를 문서로 고정한다는 점이 같고(그 페이지가 도구 예시로 *grill me* 를 든다), 남기는 문서가 용어집과 ADR이라는 점이 다르다.

## 미해결

- 단일 사례(혼자 쓰는 앱의 기능 하나), 스킬 저자 본인의 시연. 질문 40개 · 영상 속 40분이 일반적인 비용인지는 모른다.
- 이름에 매달리는 이유를 Pocock이 직접 푼 답(04:31~04:49)은 무캡션이다. 위의 테제는 해설의 문장이다.
- 스킬 파일(프롬프트)의 실제 내용은 미열람.

## References

- [[tech-bridge-pocock-21k-lines-questions-before-code]] · [[mattpocock-skills]] · [[matt-pocock]] · [[spec-driven-development]] · [[plan-to-ticket-pipeline]]
