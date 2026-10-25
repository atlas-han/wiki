---
title: Matt Pocock
type: entity
category: person
tags: [ai-hero, typescript, educator, agent-skills, code-review]
aliases: [맷 포콕, mattpocockuk]
links:
  - https://x.com/mattpocockuk
  - https://www.linkedin.com/in/mapocock/
  - https://aihero.dev
sources: [tech-bridge-pocock-pr-bottleneck, tech-bridge-lauren-tan-agent-dev-workflow, tech-bridge-lauren-tan-pocock-podcast-full, tech-bridge-pocock-skills-implement-spec-pr-retro]
created: 2026-10-09
updated: 2026-10-25
---

# Matt Pocock

설명란상 **AI Hero(aihero.dev) 창립자, TypeScript 커뮤니티 교육자.** [[tech-bridge-pocock-pr-bottleneck]]에서 **에이전트 시대의 PR 병목**을 자기 스킬 저장소(AIhero.dev/skills)를 축으로 풀었다 — 측정이 아니라 실무 처방. 이 위키에서는 [[adjective-verb-steering]]·[[impeccable]]이 *Leitwort* 를 그의 트윗에서 가져왔다고 적은 것(⚠️ 원문 미확보)이 이름의 첫 등장이고, **본인이 화자인 소스는 이것이 처음이다.**

> ⚠️ **신원 근거.** 발표 자막엔 **자기소개가 없다.** 이름·AI Hero·TypeScript는 **설명란에만** 있다. 자막 정황은 정합한다 — *"And so these are my skills. AIhero.dev/skills."*(22:14~22:16), *"the rubric of my skills, which is you've kind of heard about, maybe you've used them"*(00:28~00:32), *"previous AI engineer talks I've given"*(08:33~08:36). TypeScript는 발표 주제가 아니다.

## 발표에서 (자막 근거)

- 소프트웨어 팩토리엔 가속기와 **브레이크 세 겹**(자동 검사 → 자동 리뷰 → 사람 리뷰)이 필요, 없으면 *"slop cannon"*(02:18~02:26) → [[slop-cannon]] · [[software-factory]]
- *"checks can lie"* — 동어반복·구조 민감·실패할 수 없는 테스트(04:47~08:12) → [[structure-sensitive-tests]]
- Ousterhout의 deep modules로 테스트를 인터페이스에 묶는다(08:38~09:27) → [[deep-modules]]
- *"don't put coding standards in your implement agent"*(11:34~11:39) — 구현은 과부하, 리뷰 서브에이전트는 과소부하 → [[generator-evaluator-pattern]] · [[automated-code-review]]
- *"don't outsource automated review. Build your own"*(15:01~15:07), *"The reviewer should commit"*(15:43~15:46)
- PR마다 one-way/two-way door · blast radius → *merge danger* 요약(17:21~18:36) → [[action-reversibility]] · [[risk-proportional-human-review]]
- *"you're reviewing the system that creates it (…) never (…) write the same comment twice"*(20:14~20:24) — retro 스킬 → [[skill-self-improvement]]

## 스킬 저장소 (화자 진술)

AIhero.dev/skills — 발표에서 언급된 것: **코드베이스 설계 스킬**(deep module 기회를 HTML 문서로, locality·leverage·seam 어휘), **코드 리뷰 스킬**(diff + coding standards 파일, 서브에이전트), **PR 스킬**(*"currently in progress"* 16:37~16:42), **retro 스킬**(*"a new skill"* 20:32~20:34). *"I'll be shipping version 1.3 this week"*(22:19~22:21). ⚠️ 저장소를 열어 보지 않았다 — 어떤 스킬이 어느 버전에 있는지 미확인.

## 태도

**자기 실패 사례를 재료로 쓴다** — 동어반복 테스트·소스를 읽는 테스트는 *"stuff that I found my agents doing"*(05:42~05:46). 그리고 **벤더 리뷰어보다 팀 고유 표준**을 민다(*"don't outsource"*). 단 효과 주장은 전부 자기 경험이고 소개하는 스킬은 자기 제품이다.

## References

- [[tech-bridge-pocock-pr-bottleneck]] · [[ai-engineer]]
- 이름 선행 언급: [[adjective-verb-steering]] · [[impeccable]] (Leitwort 트윗, ⚠️ 원문 미확보)
- 설명란: <https://x.com/mattpocockuk> · <https://aihero.dev> (⚠️ 열어 보지 않았다)

## 진행자로 — Lauren Tan 대담 (2026-10-10 · [[tech-bridge-lauren-tan-pocock-podcast-full]])

[[lauren-tan|Lauren Tan]] 대담의 진행자. 10-03 해설 영상 [[tech-bridge-lauren-tan-agent-dev-workflow]]에서는 태그·ASR(*"몇 포코"*)로만 판독했는데, 풀버전에서 **발화로 확인**된다 — Lauren의 *"how much do you trust, you know, me and Matt, right?"*(1:01:10~1:01:15), *"you obviously have done a lot of work with TypeScript and total TypeScript"*(27:52~27:56). 제목·설명란엔 이름이 없다.

- **자기 진술**: *"I did a drama degree"*(09:21~09:23), 언어·단어 선택에 *"obsessed"*(07:21~07:27) — 에이전트가 붙잡아 재사용하는 단어(*TDD*, *grilling*) → [[adjective-verb-steering]]와 같은 관심. *"I think I might have to change some of the course that I'm filming next week"*(48:04~48:07).
- **그의 스킬 이름이 발화로 나온다**: *"grill me with docs"*·*"wayfinder"*(1:00:55~1:01:00, Lauren 발화). Lauren은 그의 **동어반복 테스트 제거** 팁을 베꼈다고 말한다(08:21~08:38) → [[structure-sensitive-tests]].
- **질문 틀이 자기 발표의 틀이다** — one-way / two-way door(54:58~55:21, [[tech-bridge-pocock-pr-bottleneck]]의 *merge danger*), 다크 팩토리(50:41~50:49), *"sampling instead of blocking"*(54:35~54:37). 정의 하나: *"a good codebase is a codebase that's easy to make changes in"*(24:21~24:28).
- ⚠️ *"TypeScript famously has a 25,000line type uh file"*(31:18~31:24)는 진행자 진술, 이 위키는 확인하지 않았다. 두 사람 모두 자기 스킬을 권한다(*"if you trust us both, of course, use our skills"* 1:01:13~1:01:16).

## 제3자 소개 — /implement-spec · /pr · /retro (2026-10-25 · [[tech-bridge-pocock-skills-implement-spec-pr-retro]])

Tech Bridge 해설 영상이다. 설명란은 *"Eric Tech가 소개한 Matt Pocock의 세 가지 스킬"* 이라 적었다. **본인 목소리로 확정되는 구간은 없다** — 발췌 화자는 [[eric-tech|Eric Tech]]로 추정된다. 저장소 표기는 <https://github.com/mattpocock/skills>(설명란, ⚠️ 열어 보지 않았다)이고, 10-05 발표의 *AIhero.dev/skills* 와 같은 것인지는 확인하지 않았다.

- **/implement-spec** — 10-05 발표에 없던 스킬이다. 의존 관계를 보고 바로 시작할 수 있는 티켓부터 여러 에이전트에 나누고 결과를 한 갈래에 모은다.
- **/pr** — 요약(다이어그램) · 근거(스크린샷, 테스트) · merge danger(롤백, blast radius). 발표에서는 *"currently in progress"* 였다. → [[agent-change-evidence]]
- **/retro** — 핵심 파일 위치를 남겨 다음 탐색을 줄이고, 기계가 볼 것은 자동 검사로, 판단은 사람이 읽을 규칙으로 보낸다. → [[skill-self-improvement]]
