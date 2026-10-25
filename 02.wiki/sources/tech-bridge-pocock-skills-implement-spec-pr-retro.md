---
title: "Tech Bridge — AI는 끝냈다는데 왜 출시는 느릴까? Matt Pocock의 AI 코딩 스킬 3가지 (한국어 해설 + Eric Tech 영상 발췌): /implement-spec · /pr(요약 · 근거 · merge danger) · /retro"
type: source
tags: [matt-pocock, eric-tech, agent-skills, claude-code, implement-spec, pr, retro, code-review, change-evidence, merge-danger, blast-radius, parallel-agents, skill-self-improvement, commentary-format, video]
source-url: https://www.youtube.com/watch?v=vbdubFaBmfo
source-type: video
author: Tech Bridge (한국어 해설, 내레이터 미상) · 발췌 화자 [[eric-tech|Eric Tech]](추정 — 설명란 "Eric Tech가 소개한", 발화에 이름 없음) · 스킬 저자 [[matt-pocock|Matt Pocock]](목소리 확정 구간 없음) · 원본 영상 링크 없음
date-published: 2026-10-24
ingested: 2026-10-25
created: 2026-10-25
updated: 2026-10-25
---

# Tech Bridge — AI는 끝냈다는데 왜 출시는 느릴까? Matt Pocock의 AI 코딩 스킬 3가지

[[tech-bridge|Tech Bridge]]가 올린 **5:28, 공식 챕터 7** 영상. 형식은 **"한국어 해설 + 원본 발췌"** 인데 이번엔 **한 단계 더 떨어져 있다** — 설명란 *"Eric Tech가 소개한 Matt Pocock의 세 가지 스킬"* 이다. 즉 [[matt-pocock|Matt Pocock]]의 스킬을 [[eric-tech|Eric Tech]]가 소개한 영상을 Tech Bridge가 다시 해설한다. 발췌 화자는 이름을 말하지 않고, 원본 영상 링크도 없다(링크는 스킬 저장소 <https://github.com/mattpocock/skills> 하나).

> **(해설의 줄거리)** *"완성됐다는 말만으로는 안심할 수 없기 때문"*(00:03~00:07)에 출시가 느리다. 세 스킬이 그 간격을 메운다 — **/implement-spec** 은 의존 관계를 보고 바로 시작할 수 있는 일부터 나눠 병렬로 돌리고, **/pr** 은 검토 요청서에 **요약 · 근거 · 위험** 을 담고, **/retro** 는 끝난 작업을 돌아보며 **다음 작업의 환경**을 고친다. 맺음: *"만들기 → 확인하기 → 다음에 반영하기"*(챕터 05:03).

> 원음: *"Do we have a screenshot? Do we have testing passing? Right? Do we have any proof that this is actually working? rather than be like ok well should be fine. So the second part here is evidence and the third part here is the merge danger."*(02:49~03:01)

이 위키에 생기는 것: [[eric-tech]](신규 — 인물/채널). 기존 페이지에는 [[agent-change-evidence]]의 **"완료 옆에 확인한 결과를"**, [[risk-proportional-human-review]]의 **merge danger(롤백 · blast radius)**, [[skill-self-improvement]]의 **retro와 그 과잉 경고**, [[hard-vs-soft-enforcement]]의 **"기계가 볼 것과 사람이 읽을 것"**, [[matt-pocock]]의 스킬 셋이 붙는다.

**트랙과 인용.** 오디오 `Korean original` + `English (US)`, 메타 `language`=`en`. 받은 **ko = `lang=ko` 원 ASR**(`ko`·`ko-orig` 바이트 동일). 해설은 ko로, 발췌는 ko 트랙의 영어 조각과 en-orig를 대조해 인용한다. 판독·무캡션 상세는 raw.

> ⚠️ **발췌 6구간 전부 앞부분이 무캡션이거나 통째로 무캡션이다**(00:18~00:33 · 00:56~01:07 · 01:49~02:03 · 03:37~03:54 · 04:47~05:03). 남은 원음은 **각 스킬 설명의 뒷부분**뿐이다. /pr의 첫 요소(요약)와 /retro의 *"실수 분류"* 원음은 자막에 없다.

## 1. 왜 출시가 느린가 (00:00~00:33, 해설)

- *"AI가 코드를 빨리 짜 주는데 왜 출시는 여전히 느릴까요? 완성됐다는 말만으로는 안심할 수 없기 때문이에요."*(00:00~00:07) 세 스킬 = *"작업을 나누고 결과를 확인하고 같은 실수를 줄이는 방법"*(00:12~00:18). → [[verification-bottleneck]]

## 2. /implement-spec — 먼저 시작할 수 있는 일부터 (00:33~01:27)

- (해설) PR은 *"바꾼 코드를 합치기 전에 검토를 요청하는 절차"*, 코드가 쌓이면 *"확인하는 사람이 기다림의 원인"* 이 된다. 그런데 **그 앞에도 기다림이 있다** — *"일감을 하나씩 골라 AI에게 넘기는 일"*. 첫 스킬은 *"먼저 끝나야 할 일이 있는지 살피고 바로 시작할 수 있는 일을 나눠줘요"*(00:33~00:56).
- **원음**(01:07~01:26): *"[…] Pick dependencies to work them. This way we're going to have multiple different AI agents here working at the same times and it's going to process all the tickets much faster compared to what we had before. And eventually we going to have all those meringle[?] branch and it's going to [review?] it."*
- (해설) *"동시에 일한다고 모든 일을 한꺼번에 시작하는 건 아니에요. 앞 작업이 끝나야 시작할 수 있는 일은 기다려야 하죠. 서로 독립적인 일부터 진행하고 결과를 한 갈래에 모으는 거예요."*(01:27~01:40) → [[spec-driven-development]](명세 → 태스크) · [[agent-trust-curve]](병렬성)

## 3. /pr — 요약 · 근거 · 위험 (01:27~03:16)

- (해설) *"검토할 사람이 바뀐 내용을 빠르게 이해해야 해요. 두 번째 스킬은 검토 요청서에 요약, 근거, 위험을 담아요."*(01:38~01:49)
- **요약 — 글 대신 그림.** 원음(02:03~02:11): *"[…] other summaries that we seen what my will do is in that skill it will basically just try to create diagrams rather than just bunch of words that we have to read through"*. (해설) *"하지만 그림이 깔끔하다고 코드가 제대로 작동하는 건 아니죠."*(02:23~02:25)
- **근거.** (해설) *"로그인을 고쳤다면 수정 전에는 실패했고 수정 후에는 성공했다는 결과를 보여 줘야 해요."* — 단 *"이 예시는 저희가 이해를 돕기 위해 든 거예요"*(02:28~02:38). 원음(02:45~02:58): 스크린샷 · 통과한 테스트 · *"any proof that this is actually working (…) rather than be like ok well should be fine"*. → [[agent-change-evidence]]
- **위험 = merge danger.** 원음(03:01~03:11): *"Let's say if this po quest[pull request] breaks what is impact in production can we actually roll back if something happen and also what is the blast radius how much this change impacts if something goes wrong"*. (해설) *"위험을 적는다고 검토가 없어지는 건 아니에요. 어디를 더 꼼꼼히 봐야 할지 알려 주는 거죠."*(03:22~03:26) → [[risk-proportional-human-review]] · [[action-reversibility]]

## 4. /retro — 다음 작업의 환경을 고친다 (03:16~05:03)

- (해설) *"작업이 끝나도 남는 문제가 있어요. 다음 작업에서 똑같은 곳을 헤매고 같은 실수를 반복하는 거예요. 세 번째 스킬은 지난 작업을 돌아봐요."*(03:26~03:37, ⚠️ ASR *"진한 작업"*)
- **컨텍스트.** 원음(03:54~04:19): AI 에이전트가 버그 수정·기능을 맡았을 때 *"it might take long time for AI agent here to finding the right information. So maybe we to create a uh AGMD[?] file and this AGMD file contains a list of key files on exactly where they are and how to find them more quickly."* (해설) *"파일 위치를 알려주면 다음에는 찾는 시간을 줄일 수 있어요."*(04:25~04:28) ⚠️ *AGMD* 는 AGENTS.md 류로 보이지만 확정하지 않는다.
- **실수를 둘로 나눈다**(해설, 04:28~04:40): *"금지된 함수를 썼는지처럼 기계가 확인할 수 있는 일은 자동 검사로 막을 수 있죠. 판단이 필요한 기준은 사람이 읽을 규칙으로 남겨요."* → [[hard-vs-soft-enforcement]] · [[executable-standards]]
- **경고**(해설): *"다만 회고를 계속 자동으로 돌리면 기능보다 정리 작업만 늘어날 수 있어요."*(04:40~04:47) → [[skill-self-improvement]]

## 5. 맺음 (05:03~05:28, 해설)

- *"의존 관계를 보고 일을 나누고 검토할 근거와 위험을 모으고 다음 작업의 환경을 고쳐요. 저희가 주목한 건 더 많은 코드를 만드는 속도만이 아니에요. 사람이 확인하고 다음에는 덜 헤매게 만드는 흐름이에요. 지금 쓰는 AI는 완료했다는 말 뒤에 어떤 근거를 보여주나요?"*(05:03~05:26)

## 이 위키와의 연결

### 이어지는 것

- **[[tech-bridge-pocock-pr-bottleneck]] — 같은 스킬 저장소의 1차 진술.** 10-05 업로드 발표에서 Pocock 본인이 스킬 넷(코드베이스 설계 · 코드 리뷰 · PR · retro)과 *merge danger*(one-way/two-way door · blast radius), *"you're reviewing the system that creates it"* 를 말했다. 이 편은 그중 **PR · retro를 제3자(Eric Tech)가 시연한 것의 해설**이고, 발표에 없던 **/implement-spec** 이 새로 나온다. 발표에서 PR 스킬은 *"currently in progress"* 였다 — 이 편 시점엔 쓰이고 있다(⚠️ 버전·날짜 미확인).
- **[[agent-change-evidence]]** — 이 페이지의 *"코드 + 그 변경을 믿어도 되는 이유"* 가 스킬 하나로 구현된 사례. 다섯 질문 대신 **요약 · 근거 · 위험** 세 칸이다.
- **[[tech-bridge-kanat-alexander-disposable-vs-durable]](같은 날 업로드)** — 두 편 모두 검사를 **사람이 기억해서 누르는 것에서 시스템이 돌리는 것으로** 옮기고, 판단이 필요한 부분만 사람에게 남긴다.

### 갈리는 것

> ⚠️ **"retro를 계속 자동으로 돌리면 정리 작업만 늘어난다"(해설) vs [[skill-self-improvement]]의 자동 축적 사례.** 이 위키의 self-improvement 사례들은 관찰 → 개선안 축적을 대개 상시화하고, 반영만 사람이 거른다. 해설은 **실행 빈도 자체**를 비용으로 본다. 원음 근거는 없다(해설). 해소하지 않는다.

## 해소하지 않고 표시만 한 것

- 발췌 화자 = Eric Tech는 **추정**(설명란 + *"what my will do is in that skill"* 정황). Eric Tech 원본 영상의 제목·날짜·링크 없음. Matt Pocock 목소리 구간 없음.
- *"meringle"*, 끝의 *"review? / process"*, *"understandations"*, *"worse before"*, *"AGMD"*, 끝 *"M."* 판독 불가.
- 무캡션: 각 스킬 설명의 앞부분, /pr 요약 항목의 원음, 04:47~05:03.
- 스킬 저장소(github.com/mattpocock/skills)를 열어 보지 않았다 — /implement-spec · /pr · /retro의 실제 내용·이름·버전 미확인.

## 등장 개체

- 인물: [[eric-tech]](신규) · [[matt-pocock]]
- 제품: [[claude-code]](태그·해시태그만, 발화 없음)
- 개념: [[agent-change-evidence]] · [[risk-proportional-human-review]] · [[skill-self-improvement]] · [[hard-vs-soft-enforcement]] · [[agent-skills]] · [[spec-driven-development]] · [[verification-bottleneck]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=vbdubFaBmfo> (5:28, `upload_date` 2026-10-24)
- raw: `01.raw/articles/2026-10-24_AI는 끝냈다는데 왜 출시는 느릴까 - Matt Pocock의 AI 코딩 스킬 3가지.md`
- 스킬 저장소(설명란, 미확인): <https://github.com/mattpocock/skills>
- 1차 진술: [[tech-bridge-pocock-pr-bottleneck]] · [[tech-bridge-lauren-tan-pocock-podcast-full]]
- [[tech-bridge]] · [[matt-pocock]] · [[eric-tech]]
