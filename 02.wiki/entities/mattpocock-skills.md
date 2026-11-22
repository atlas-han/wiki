---
title: mattpocock/skills
type: entity
category: tool
tags: [agent-skills, claude-code, matt-pocock, grill-with-docs, implement-spec, retro, open-source]
aliases: [mattpocock/skills, Matt Pocock skills, AIhero.dev/skills, 매트 포콕 스킬 저장소]
links:
  - https://github.com/mattpocock/skills
sources: [tech-bridge-pocock-21k-lines-questions-before-code, tech-bridge-pocock-skills-implement-spec-pr-retro, tech-bridge-matt-pocock-home-repo-pattern]
created: 2026-11-22
updated: 2026-11-22
---

# mattpocock/skills

[[matt-pocock|Matt Pocock]]의 공개 [[agent-skills|에이전트 스킬]] 저장소. 위키에는 [[tech-bridge-pocock-skills-implement-spec-pr-retro]](10-25, 스킬 셋의 제3자 소개)와 [[tech-bridge-matt-pocock-home-repo-pattern]](11-16, 홈 레포에서 포인터로 연결)에 이름으로 먼저 나왔고, [[tech-bridge-pocock-21k-lines-questions-before-code]](11-21 한국어 해설)에서 **스킬 사슬 전체가 한 기능 위에서 도는 모습** 이 처음 전해져 페이지를 만든다. ⚠️ 위키는 저장소를 열지 않았다 — 아래는 전부 Tech Bridge 해설이 옮긴 것이고 스킬 이름의 표기는 ASR 판독이다.

## 소스에서 확인되는 것 (11-21 해설)

- 규모: *"깃허브 스타가 32만 개를 넘었습니다."*(00:34~00:36) *"본인 말로는 세계에서 스타가 가장 많은 스킬 저장소입니다."*(00:37~00:38) ⚠️ 해설이 읽은 값 · 본인 주장.
- 소개 문구: *"바이브 코딩이 아니라 진짜 엔지니어링에 매일 쓰는 스킬이라는 겁니다."*(00:42~00:45) *"스킬 하나하나는 작고 고치기 쉽고 서로 조합할 수 있게 만들었다고 적었습니다."*(00:46~00:49)
- 고쳐지는 방식: 자기 회고(retro)에서 나온 이슈를 저장소에 올리고 스킬은 그렇게 조금씩 고쳐진다고 한다(내레이션 전달) → [[skill-self-improvement]]

## 스킬 사슬 (한 기능 = 21,349줄의 사례)

| 단계 | 스킬(ASR → 판독) | 하는 일(해설) |
|---|---|---|
| 입구 | — | 디프 크기로 고른다: 작으면 질문 없이 한 번에 · 크면 grill-with-docs · 한 세션에 안 담기면 wayfinder |
| 맞추기 | *그릴 위드 독스* → [[grill-with-docs]] | 사람을 질문으로 들볶고 용어집 · 결정 기록을 남긴다 |
| 정리 | *투 스펙* → to-spec | *도착지 문서* — GitHub 이슈 하나(사용자 이야기 47개 · 구현 결정 · 범위 밖 항목) |
| 나누기 | *투 티켓* → to-tickets | 거기까지 가는 길을 세션 단위 작업으로(티켓 9개) |
| 구현 | *임플리먼트 스펙* → implement-spec | 서로 막지 않는 티켓 세 개부터 병렬로, 사람은 자리를 뜬다 |
| 회고 | *레트로* → retro | 세션 기록과 리뷰 코멘트를 읽혀 에이전트가 일하는 환경을 고친다 |

- 두 스킬의 구분: *"투 스펙은 도착지 문서를 쓰고 투 티켓은 거기까지 가는 길을 세션 단위 작업으로 자릅니다."*(07:11~07:14)
- retro의 정의: *"코드가 아니라 에이전트가 일하는 환경을 고치는 스킬입니다."*(10:33~10:35)
- ⚠️ PR을 일곱 개로 나눈 것이 스킬(10-25 소스의 /pr)을 쓴 것인지 그냥 시킨 것인지는 캡션으로 알 수 없다. *to-spec* · *to-tickets* 의 정확한 철자도 미확인.

## 앞선 소스와의 관계

- 10-25 해설의 /implement-spec · /pr · /retro가 이 저장소의 스킬이다. 11-21 해설에서 implement-spec과 retro가 같은 역할로 다시 나온다.
- 10-05 발표([[tech-bridge-pocock-pr-bottleneck]])의 *AIhero.dev/skills* 와 같은 것인지는 여전히 확인하지 않았다.
- [[home-repo-pattern]] — 그의 홈 레포에서 이 저장소는 포인터 한 줄로 연결된다(11-16 해설).
- 이웃: [[pstack]](Lauren Tan — 두 사람이 서로의 스킬을 보완적이라 말한다) · [[gstack]].

## 미해결

- 저장소 미열람: 스킬 목록 · 버전 · 스타 수 미확인.
- 효과 주장은 저자 본인의 사례 하나다.

## References

- [[tech-bridge-pocock-21k-lines-questions-before-code]] · [[tech-bridge-pocock-skills-implement-spec-pr-retro]] · [[tech-bridge-matt-pocock-home-repo-pattern]] · [[matt-pocock]] · [[grill-with-docs]] · [[agent-skills]]
