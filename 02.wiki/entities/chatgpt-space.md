---
title: Space (ChatGPT)
type: entity
category: product
tags: [openai, chatgpt, collaboration, office-suite, live-documents, multiplayer, devday-2026]
aliases: [Space, ChatGPT Space, 스페이스, live documents, 살아 있는 문서]
links:
  - https://help.openai.com/en/articles/20001549-getting-started-with-space-in-chatgpt
sources: [tech-bridge-altman-devday-dots, tech-bridge-ben-davis-codex-product-cohesion]
created: 2026-10-09
updated: 2026-10-31
---

# Space (ChatGPT)

[[openai|OpenAI]]가 DevDay 2026에 낸 **사람과 AI(여러 사람의 AI 포함)가 함께 쓰는 협업 도구.** 진행자는 *"three like office suite type tools in one launch"* 라 불렀다. 본 위키에는 [[tech-bridge-altman-devday-dots]]로 첫 등장한다. 이름은 설명란 링크 *"getting-started-with-space-in-chatgpt"* 를 따른다(⚠️ 열어 보지 않았다). 슬러그의 `chatgpt-` 는 일반 명사와의 혼동을 피하려는 위키의 선택이다.

> ⚠️ **세 도구가 무엇인지(문서·표·슬라이드 등) 대담은 말하지 않는다.** 아래는 [[sam-altman|Altman]]의 진술과 진행자의 한 마디가 전부다. ⚠️ ko 자막은 **Space를 줄곧 "우주"로** 옮긴다(09:58, 15:27, 16:12).

## 왜 만들었나

> *"software was really not designed on the whole for collaborating with AI"* (15:42~15:45) · *"especially when it's multiple people and multiple people's AIs all working together like a lot of the current abstractions we have break down"* (15:54~16:03)

처음부터 목표는 아니었다(*"We didn't set out wanting to do this"* 15:34). *"the space of human AI collaboration is really important to explore"* (16:05~16:09).

## live documents

> *"I don't think we have a word for this yet, but for lack of a better word, these like live documents um creating a doc that is going to automatically update as people interact or as other things change in the world"* (16:45~16:55)

- **여러 Dot의 공동 작업** — *"seven people's dots can working together create something new that kind of existed in all of our heads to some degree but was like an emergent thing"* (17:04~17:12). 설명란의 *"7명의 에이전트"* 는 이 한 마디다 — 정해진 기능 수치가 아니다.
- **개인 대시보드** — 공유 대시보드 대신 *"a changing summary of the business just for me"*, Slack 메시지를 보고 계속 갱신 (17:18~17:48).
- **사람의 몫** — 새 아이디어는 *"writing the oldfashioned way because it helps me like think about it"*, 후속은 Dot이 (16:29~16:40).
- 키노트 데모 자료도 Space에 있었다 — Tibo의 Dot이 그걸 보고 데모 실패를 예고했다(09:56~09:58) → [[openai-dots]]

## 이 위키에서의 좌표

- [[multiplayer-agent-context]] — 여러 사람이 **하나의** 에이전트를 공유하는 패턴이었다면, Space는 **여러 사람 각자의** 에이전트가 한 문서를 공유한다.
- [[spec-driven-development]] — *living document*(살아 있는 명세)라는 말이 이미 쓰인다. ⚠️ 같은 뜻은 아니다 — SDD 쪽은 사람이 갱신하는 명세, 여기는 세계 변화에 따라 **자동 갱신**되는 문서.

## ⚠️ 유보

- 세 도구의 구성, 권한(누구의 Dot이 무엇을 고칠 수 있나), 충돌 해결, 버전 관리 — 전부 없다.
- *"emergent thing"* 의 사례 없음.

## References

- [[tech-bridge-altman-devday-dots]] — first-seen
- [[openai]] · [[sam-altman]] · [[openai-dots]]
- 관련: [[multiplayer-agent-context]] · [[spec-driven-development]] · [[persistent-agent-teams]]
- 외부: <https://help.openai.com/en/articles/20001549-getting-started-with-space-in-chatgpt> (⚠️ 미확인)

## ⚠️ 같은 기능일 수 있는 사용자 관찰 — Codex 옆의 "spaces" (2026-10-31 · [[tech-bridge-ben-davis-codex-product-cohesion]])

> ⚠️ **동일성 미확정.** 이 소스의 화자([[ben-davis]] 추정)는 *spaces*(복수)를 *"one of the big new headline features that they shipped"*(02:21~02:24)라 부르지만 "ChatGPT Space"라는 이름 · 링크는 없고, [[codex|Codex]] thread와 묶어 말한다. 이 페이지의 DevDay 2026 Space와 같은 제품일 가능성은 있지만(둘 다 OpenAI의 최근 문서형 협업 기능, 공유 가능) **합치지 않고 교차 참조만 한다.**

- 사용 방식: 영상마다 템플릿에서 복사한 단계 · 저장된 프롬프트를 *"fire off into a codex thread"*(02:47~02:51), 편집자와 *"shared spaces"*(02:54~02:56)를 쓴다. 한 줄 평 *"basically notion with a bunch of AI stuff built into it with a lot of rough edges around it."*(03:14~03:18)
- 거친 점: 모델이 page를 바꿀 때 *"it will force your view, your entire computer back onto that page"*(03:25~03:29), thread가 Space 안과 일반 thread 양쪽에 보인다.
- 처방: Spaces를 thread 위의 **별도 primitive**로, page는 thread가 조작하는 entity로, headless 제어 가능하게(05:37~06:06) → [[primitives-before-features]]
- 위 Altman의 *live documents*(자동 갱신 문서) · 여러 Dot의 공동 작업과 비교하면, 이 관찰은 **사람이 저장해 둔 프롬프트로 에이전트를 발사하는 작업 템플릿**이다. 같은 제품이라면 쓰임의 다른 면이다.
