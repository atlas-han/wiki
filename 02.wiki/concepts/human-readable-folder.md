---
title: "사람이 읽는 폴더 (Human Folder) — 코드베이스를 엔진과 사람이 읽는 층으로 나눈다"
type: concept
category: pattern
tags: [codebase-structure, vibe-coding, comprehension, lint, comments, dsl, game-development, thariq-shihipar]
aliases: [human folder, spec folder, 휴먼 폴더, 사람이 읽는 폴더, engine / human split]
related: [cognitive-debt, read-fluency-for-agent-output, domain-specific-scripts, hard-vs-soft-enforcement, jagged-capability-frontier, harness-pruning]
first-seen: tech-bridge-thariq-shihipar-human-folder-unacceptable
sources: [tech-bridge-thariq-shihipar-human-folder-unacceptable]
created: 2026-11-23
updated: 2026-11-23
---

# 사람이 읽는 폴더 (Human Folder)

에이전트가 쓴 코드베이스를 **둘로 나눠**, 한쪽(엔진)은 모델에게 맡기고 다른 쪽(*spec* 또는 *human* 폴더)은 사람이 직접 읽고 고치는 층으로 지키는 구조. [[thariq-shihipar|Thariq Shihipar]]가 AI Engineer Code Summit 발표(2026-11)에서 자기 게임으로 보여 준 것으로, 위키에는 [[tech-bridge-thariq-shihipar-human-folder-unacceptable]](한국어 해설)로 들어왔다. ⚠️ 발표 원음은 무캡션이라 아래 인용은 전부 한국어 내레이션의 전달이고, 본인 말로 *초기 단계* 의 실험이다.

## 풀려는 문제

바이브 코딩으로 만든 자기 게임인데 캐릭터가 무엇을 하는지 모르겠다는 것. 그는 좋은 작품을 선택의 결과로 본다 — *"무엇을 넣고 무엇을 뺐는지가 작품을 만든다는 겁니다."*(08:06~08:08) *"그러려면 속속들이 아는 전문가여야 합니다."*(08:10~08:11) 그런데 *"바이브 코딩한 코드는 들여다봐도 무슨 일이 일어나는지 모르겠다는 겁니다."*(08:12~08:15) → [[cognitive-debt]]

## 구조

- **둘로 나눈다.** *"그의 해법은 코드 베이스를 둘로 나누는 것이었습니다."*(08:17~08:19) 하나는 엔진, 다른 하나는 *spec* 혹은 *human* 이라 부르는 폴더(08:19~08:23).
- **사람이 읽는 쪽에 규칙을 건다.** *"휴먼 폴더는 그가 직접 읽는 코드입니다. 린트를 걸고 클로드에게는 이 코드가 어떤 모양이어야 하는지 규칙을 줍니다."*(08:25~08:30) ⚠️ 규칙의 내용은 무캡션 구간(08:33~08:47)에 있다. → [[hard-vs-soft-enforcement]]
- **읽히는 모양.** 데모 파일 `rock.ts` — *"속도와 질량, 크기, 사거리가 적혀 있습니다."*(08:49~08:51) 매직 넘버 대신 *"미터와 초 단위를 쓰고 줄마다 무슨 뜻인지 주석이 붙어 있습니다."*(08:55~08:57)
- **논리가 한곳에 보인다.** *"엔진 속은 몰라도 이 캐릭터의 진짜 논리는 여기서 다 보입니다. 사실상 게임 전용 스크립트 언어를 만든 셈입니다."*(09:06~09:11) → [[domain-specific-scripts]]와 닮은 점: 도메인의 어휘를 담은 얇은 층을 따로 둔다(그쪽은 에이전트에게 줄 어휘, 이쪽은 사람이 읽을 어휘).
- **고치기 쉽다.** *"돌을 더 크게 하고 싶으면 숫자 하나를 바꾸면 됩니다."*(09:13~09:14)
- **분업.** *"복잡한 기본 블록은 여전히 클로드가 만듭니다. 다만 그걸 어떻게 엮을지는 그가 읽고 고칩니다."*(10:01~10:05) 사람이 읽는 층에서는 Cursor의 Tab 자동 완성을 많이 쓴다고 한다(09:18~09:20) — 에이전트에게 통째로 맡기는 대신 한 줄씩 받아 쓰는 방식이다.

## 위키의 읽기

- [[cognitive-debt|인지 부채]]의 기존 처방(작은 단계 · 속도 조절 · 리뷰 WIP 제한)은 **속도** 를 다룬다. 이것은 **구역** 을 다룬다 — 전부 이해할 수는 없으니 이해할 곳을 정하고 그곳의 가독성을 강제한다.
- [[read-fluency-for-agent-output]](쓰기는 넘기고 읽기는 남긴다)의 코드베이스판이다. 읽기를 남기려면 읽을 만한 코드가 있어야 하고, 그 조건을 폴더와 린트로 만든다.
- 전제는 [[jagged-capability-frontier|매끈한 안쪽]]이다 — 모델이 어떤 형식이든 고르게 잘 쓴다면, 사람이 읽기 좋은 형식을 요구해도 잃는 것이 없다.

## ⚠️ 유보

- 사례는 혼자 만드는 게임 하나다. 팀 단위 코드베이스나 엔진과 사람 층의 경계가 흐린 제품에서 통하는지는 소스에 없다.
- 엔진 쪽을 아무도 읽지 않을 때의 위험(보안 · 성능 · 회귀)은 다루지 않는다. 발표자는 하네스와 검사가 머지않아 필요 없어진다고 전망하나([[harness-pruning]]) 해설도 *그의 전망* 이라고 단서를 단다.
- 해설의 정리: *"휴먼 폴더도 본인 말로 아직 초기 실험입니다."*(11:11~11:13)

## References

- [[tech-bridge-thariq-shihipar-human-folder-unacceptable]] · [[thariq-shihipar]] · [[cognitive-debt]] · [[read-fluency-for-agent-output]] · [[domain-specific-scripts]]
