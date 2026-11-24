---
title: mattpocock/skills
type: entity
category: tool
tags: [agent-skills, claude-code, matt-pocock, grill-with-docs, implement-spec, retro, open-source]
aliases: [mattpocock/skills, Matt Pocock skills, AIhero.dev/skills, 매트 포콕 스킬 저장소]
links:
  - https://github.com/mattpocock/skills
sources: [tech-bridge-pocock-21k-lines-questions-before-code, tech-bridge-pocock-skills-implement-spec-pr-retro, tech-bridge-matt-pocock-home-repo-pattern, tech-bridge-pocock-networkchuck-what-to-learn-instead-of-languages]
created: 2026-11-22
updated: 2026-11-24
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

## 2026-11-24 — 대담에서 직접 돌린 스킬들과 *하루 루프* ([[tech-bridge-pocock-networkchuck-what-to-learn-instead-of-languages]])

NetworkChuck 대담을 따라간 한국어 해설이 저장소의 스킬을 루프 순서로 다시 보여 준다(내레이션 전달, 대담 원음 무캡션, 저장소 미열람 — 설명란에 링크만 있다).

- 스킬의 정의(해설): *"스킬은 AI의 일하는 수서를 적어 준 짧은 문서입니다."*(02:58~03:02)[=순서]
- 루프: *"그릴링, 스펙과 티켓, 구현, 코드 리뷰, 그리고 회고."*(08:30~08:32) 작은 일은 스펙을 건너뛴다 — *"작은 일이면 바로 구현 스킬로 넘어갑니다. 대화 하나를 넘길 만큼 크면 다른 길로 갑니다."*(06:17~06:21)
- 티켓의 크기: *"티켓 하나가 대화 하나. 대략 15만 토큰 안에 끝나게요."*(06:27~06:29) 서브 에이전트는 *"각자 워크 트리, 즉 따로 떨어진 작업 폴더에서 동시에 일하고 끝나면 합쳐서 PR 하나를 만듭니다."*(06:33~06:37)
- 코드 리뷰 스킬이 보는 둘: *"스펙대로 만들었는지, 그리고 코딩 표준을 지켰는지."*(06:40~06:43) 표준은 본인이 직접 쓴 문서다.
- PR 설명의 세 칸: *"바뀐 것의 요약, 작동한다는 증거, 그리고 뭐지 위험입니다."*(07:14~07:18)[=머지 위험]
- 회고: *"세션과 리뷰를 돌아보고 다음엔 무엇을 바꿀지 제안하게 합니다."*(08:24~08:27) *"다음엔 자동 검사로 막을 방법을 찾습니다."*(09:24~09:26)
- **이 위키에 처음 나오는 스킬 둘.** ① 아키텍처 개선: *"코드베이스를 이런 모양으로 바꿔주는 스킬이 임프루브 코드베이스 아키텍처입니다."*(10:39~10:42)[=improve-codebase-architecture(추정 철자)] — 대담 중에 돌린 보고서의 *"첫 지적은 두 기능에 거의 똑같은 코드가 150줄 겹친다는 것."*(10:45~10:49) 출처는 Michael Feathers의 책이라고 한다: *"아키텍처 개선 스킬도 거기서 나왔습니다."*(12:32~12:34) → [[deep-modules]] ② 가르치는 스킬(이름 줄은 ASR 불확실 — teach로 보인다): *"모르는 보고서를 넘기면 내가 아는 것을 기억하면서 퀴즈와 HTML 수업을 만들어 줍니다."*(12:36~12:41) → [[ai-assisted-learning]]
- 자동 PR의 확인 빈도: *"이런 자동 피알은 다섯 개에 하나쯤만 직접 확인합니다."*(11:21~11:23)

⚠️ 11-21 업로드 편의 스킬 이름(to-spec · to-tickets · implement-spec · retro)은 이 편 캡션에 나오지 않는다 — 내레이션은 *스펙* · *티켓* · *구현 스킬* · *회고 스킬* 이라고만 부른다. 같은 스킬인지는 대조하지 않았다.
