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
sources: [tech-bridge-pocock-pr-bottleneck, tech-bridge-lauren-tan-agent-dev-workflow, tech-bridge-lauren-tan-pocock-podcast-full, tech-bridge-pocock-skills-implement-spec-pr-retro, tech-bridge-matt-pocock-home-repo-pattern, tech-bridge-zechner-ronacher-verification-is-overrated, tech-bridge-pocock-21k-lines-questions-before-code, tech-bridge-pocock-networkchuck-what-to-learn-instead-of-languages]
created: 2026-10-09
updated: 2026-11-24
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

## 홈 레포 패턴 (2026-11-16 · [[tech-bridge-matt-pocock-home-repo-pattern]])

Tech Bridge 해설(그의 영상 `hWe-j78vNpc`와 같은 날 올라온 aihero.dev 글 기준, ⚠️ 원 자료 미열람 · 본인 음성 무캡션). 멀티 레포 조직에서 스킬 · AGENTS.md · 공유 문서 · 도구를 **집이 되는 저장소 하나** 에 모으고 다른 저장소는 경로 한 줄로 가리킨 뒤 에이전트는 늘 거기서 실행한다 — *"너무 뻔해서 올릴 생각도 안 했다"*(설명란)던 기법. X 게시물은 며칠 만에 조회수 28만 · 북마크 4,900(해설 전달). → [[home-repo-pattern]]

- 규모 사다리 ~20개 포인터 → ~400개 영역 파일(점진적 공개) → 수천 개 스킬 마켓플레이스. 모노레포가 되면 모노레포가 먼저.
- 자기 홈 레포를 **퍼스널 위키** 라 부른다 — *Karpathy 스타일 LLM 위키* 와 Gmail · Slack · Discord · YouTube · GitHub · Calendar 명령. 위키 유지 방법은 *다음 영상에서* → [[llm-wiki-pattern]]
- 공개 스킬 저장소 `mattpocock/skills`(10-25 소스의 그 저장소)도 홈 레포에서 포인터 한 줄로 연결된다.
- ⚠️ 해설이 짚는다: 한 사람의 경험, 효과 수치 없음, *에이전트 코딩 강의를 파는 사람* — 이 페이지 *태도* 절의 *효과 주장은 자기 경험 · 소개하는 스킬은 자기 제품* 과 같은 단서.

## 2026-11-21 — 진행자로: Pi 제작자 두 사람과의 라이브 ([[tech-bridge-zechner-ronacher-verification-is-overrated]])

2026-11-17 라이브 방송에 [[mario-zechner|Mario Zechner]]와 [[armin-ronacher|Armin Ronacher]]를 불렀다(Tech Bridge 한국어 해설로 전달, ⚠️ Pocock의 원음은 캡션에 없다). 해설은 그를 *타입스크립트 강사* 로 소개한다.

- 첫 질문: *"오퍼스 5.5 이후로 뭐가 달라졌나?"*(00:49~00:51)
- 본인의 구분 — 전술과 전략: *"눈 앞의 전투를 이기는 게 전술, 전쟁을 이기는 법을 고민하는 게 전략."*(02:59~03:02) *"에이전트는 전술에 강하고 전략에 약하다는 거죠."*(03:02~03:04)
- [[lauren-tan|Lauren Tan]]의 말을 끌어온다: *"코드 베이스와 API에서 뉘앙스를 최대한 없애야 한다고요."*(04:15~04:17)
- 방송 전에 Zechner가 한 *검증은 과대평가됐다* 는 말을 방송에서 되물은 사람이다 → [[verification-bottleneck]]

## 2026-11-22 — 본인의 70분 작업 영상: 질문 40개 → 21,349줄 → PR 7개 → 회고 ([[tech-bridge-pocock-21k-lines-questions-before-code]])

Tech Bridge 한국어 해설(11-21 게시)이 그의 작업 영상 `jVBlkOF8sHk` 를 따라간다. ⚠️ **원음은 두 트랙 모두 무캡션 — 본인 인용 0**, 아래는 내레이션이 간추린 말이고 수치는 해설이 화면에서 읽은 값이다. 위키는 원본 영상을 열지 않았다.

- 해설의 소개: 타입스크립트 강의로 이름을 알렸고 *"요즘은 이스킬 저장소로 더 유명합니다."*(00:32~00:33)[=이 스킬 저장소(추정)] → [[mattpocock-skills]](신규)
- **코드보다 질문이 먼저.** *"매트 포콕은 40분 가까이 코드를 한 줄도 쓰지 않았습니다."*(00:12~00:16) *"대신 AI가 던지는 질문 40개에 답하면서 단어 하나를 고르고 있었습니다."*(00:17~00:21) → [[grill-with-docs]](신규)
- **이름에 대한 집착이 작업 방식으로.** 10-10 대담의 *언어 · 단어 선택에 obsessed* 가 여기서는 560줄 용어집 · 이름 후보의 시나리오 테스트 · ADR로 나타난다. *"이름이 정해지면 기능도 다 정해진 셈이라고 말합니다."*(03:14~03:16)
- **도구.** *"도구는 클로드 코드, 모델은 오퍼스 5.5, 초론 수준은 중간이었습니다."*(01:34~01:35)[=추론 수준]
- **리뷰.** 21,349줄을 PR 일곱 개로 나누게 하고, 꼭 사람이 봐야 한다고 한 것은 DB 마이그레이션 하나. 코멘트 12개는 대부분 *주석이 너무 많다* 였고 전부 린트 규칙으로 만들자고 한다: *"여기서 본 건 다시는 보고 싶지 않다. 린트로 아예 없애 버리겠다."*(10:24~10:27) — 10-05 발표의 *같은 코멘트를 두 번 쓰지 마라* 의 실례. → [[hard-vs-soft-enforcement]] · [[comments]]
- **태도.** *"혼자 쓰는 앱이지만 사용자가 수십만 명인 서비스인 척하는 연습이라고 말합니다."*(08:53~08:56)
- **사람의 자리.** 설명란 요약: 사람이 쓸모 있는 곳은 처음(방향 맞추기)과 끝(리뷰 · 회고). ⚠️ 본인의 답(12:42~13:06)은 무캡션.
- ⚠️ 이 페이지 *태도* 절의 단서 그대로다 — 자기 스킬로 한 자기 사례 하나, 머지 뒤의 품질 평가는 없다.

## 2026-11-24 — NetworkChuck 대담: *언어 대신 배울 것은 단어다* ([[tech-bridge-pocock-networkchuck-what-to-learn-instead-of-languages]])

Tech Bridge 한국어 해설(11-24 07:00 KST 게시)이 NetworkChuck과의 2시간 대담(원본 `mU8WKII1gpk`, 미열람)을 따라간다. ⚠️ **대담 원음은 두 트랙 모두 무캡션 — 본인 인용 0**, 아래는 내레이션이 옮긴 말이다.

- **제목의 물음.** *"프로그래밍 언어, 지금 꼭 배워야 할까요?"*(00:00~00:02) — 답 *아니요* 는 설명란에만 있다. 해설의 소개: *"이렇게 답한 사람은 맷 턱 타입스크립트 강의로 이름을 알린 개발자입니다."*(00:08~00:12)[=Matt Pocock]
- ⭐ **틀: 전술과 전략.** Ousterhout의 책에서 가져온 구분으로 자기 작업 방식 전체를 설명한다 — 에이전트는 오늘 일을 끝내고, 집은 사람이 돌본다: *"그래서 집을 돌볼 사람이 필요하고 지금은 그게 바로 사용자라는 겁니다."*(01:52~01:54) → [[tactical-vs-strategic-programming]](신규)
- **하루 루프.** *"그릴링, 스펙과 티켓, 구현, 코드 리뷰, 그리고 회고."*(08:30~08:32) — 11-21 업로드 편의 사슬과 같다. → [[mattpocock-skills]] · [[grill-with-docs]]
- **15만 토큰.** *"그런데 메트는 15만 토큰쯤부터 불안해진다고 했습니다. 진행자가 너무 이르다며 놀랄 정도로요."*(04:58~05:03) → [[context-rot]]
- **모델 비교를 하지 않는다.** *"다음 모델이 다 고쳐주길 기다리지 말고 지금 내 문제를 고치라는 겁니다."*(06:12~06:16)
- **표준을 AI에게 맡기고 안 보는 것이 바이브 코딩이다.** 진행자의 습관에 대한 평으로 전해진다: *"잘하라고는 하는데 어떻게 잘하는지는 관심이 없는 거죠."*(07:01~07:03)
- **언어 대신 단어, 단어는 책에서.** *"배워야 할 건 프로그래밍 언어가 아니라 이런 단어입니다."*(12:13~12:15) *"그가 꼽은 책은 소프트웨어 설계의 철학, 실용주의 프로그래머, 페더스의 책 리팩토링, 익스트림 프로그래밍입니다."*(12:46~12:52)
- **이력(이 위키에 처음 들어옴).** *"매트 자신도 컴퓨터 공학 전공이 아닙니다. 연극을 전공하고 6년 동안 발성 코치로 일하다 2015년에 독학으로 넘어왔습니다."*(12:57~13:03)
- **태도.** *"매트가 가장 많이 한 말은 케어, 신경 쓴다는 말이었습니다."*(13:06~13:08)
- ⚠️ 핵심 답 셋이 무캡션이다 — AI가 전략을 못 하는 이유(00:51~01:37) · 높은 노력 수준이 왜 해로운지(05:30~06:01) · 무엇을 배워야 하느냐는 물음의 답(11:35~12:13). 적지 않았다.
