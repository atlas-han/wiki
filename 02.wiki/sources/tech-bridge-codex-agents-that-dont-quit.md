---
title: "Tech Bridge — 프롬프트 200단어로 6주를 일한 AI | OpenAI가 공개한 멈추지 않는 Codex 에이전트 8분 정리 (한국어 해설): 7시간에서 며칠로 · CI 플레이키 테스트 · 나흘째의 한마디 · 숫자로 본 6주 · GPU 하이젠버그 · 기능 6가지 · 비용 · 시작하는 법"
type: source
tags: [openai, codex, devday, long-running-agents, ci, flaky-tests, subagents, goal, heartbeat, compaction, ultra, cost, aaron-friel, vaibhav-srivastav, commentary-format, korean-narration, members-only, video]
source-url: https://www.youtube.com/watch?v=AYCGbCxXHMU
source-type: video
author: Tech Bridge (한국어 해설, AI 음성 내레이션) · 바탕 OpenAI DevDay 2026 발표 "What Will You Build With Coding Agents That Don't Quit?"(위키 미열람) · 발표자 [[aaron-friel|Aaron Friel]](철자 추정) · [[vaibhav-srivastav|Vaibhav (VB) Srivastav]]
date-published: 2026-11-14
ingested: 2026-11-15
created: 2026-11-15
updated: 2026-11-15
---

# Tech Bridge — 프롬프트 200단어로 6주를 일한 AI (멈추지 않는 Codex 에이전트 8분 정리)

[[tech-bridge|Tech Bridge]]의 **8:27 한국어 해설, 공식 챕터 10.** [[openai|OpenAI]] **DevDay 2026** 발표 *"What Will You Build With Coding Agents That Don't Quit?"*(설명란 링크 `U1IVZy9FhVQ`, 위키 미열람)를 따라간다. OpenAI 엔지니어 생산성 담당 [[aaron-friel|Aaron Friel]](철자 추정)이 [[codex|Codex]] 에이전트 하나에게 약 200단어 프롬프트만 주고 **6주 · 1,000시간 넘게** 사내 CI의 [[flaky-tests|플레이키 테스트]]를 고치게 한 실험이다. 두 번째 발표자 [[vaibhav-srivastav|VB]]가 이를 받쳐 준 Codex 기능 여섯 가지를 정리한다. raw: `01.raw/articles/2026-11-14_프롬프트 200단어로 6주를 일한 AI OpenAI가 공개한 멈추지 않는 Codex 에이전트 8분 정리.md`.

테제(맺음):

> *"거기 적힌 건 방법이 아니라 목표와 규칙 그리고 한계였습니다."*(08:01~08:03) *"멈추지 않는 에이전트의 조건은 어쩌면 잘 맡기고 물러날 줄 아는 사람일지도 모릅니다."*(08:11~08:15)

> ⚠️ **멤버 전용 → 공개 전환.** 11-13 회차부터 `subscriber_only`(목록 `upload_date` 20261112)였고 11-15 회차에 `public`, `upload_date` 20261114(18:00 KST)로 바뀌었다. 제목은 그대로.
>
> **트랙과 인용.** `ko` = `ko-orig`(md5 동일, `variant=gemini`), en-orig는 영어 더빙. 내레이션 인용은 ko-orig. **이번엔 원음 영어 조각이 ko-orig에 남았다**(03:15~03:27 · 08:16~08:22). 무캡션 다섯 곳(00:11~00:20 · 01:01~01:10 · 04:14~04:25 · 05:49~05:55 · 07:02~07:08)은 두 트랙 모두 비어 내용 미상.
>
> ⚠️ **더빙이 모델 이름을 바꾼다**: GPT-5.6 Sol → `GPT-4 (GPT 5.6)`, GPT-6.x Sol → `GPT-4o`. 발표자 이름도 `Aron Pril` · `Friel` · `Pril` · `FreeLee`로 갈린다 — 위키는 en-orig의 `Friel`과 ko-orig *프리엘* 을 따라 **Aaron Friel(추정)** 로 적는다. 설명란에 이름은 없다.

## 1. 6주 동안 멈추지 않은 에이전트 (00:00~00:35)

- *"AI 코딩 에이전트 하나가 6주 동안 한 번도 멈추지 않고 일했습니다."*(00:00~00:02) 시간으로 1,000시간 넘게. OpenAI가 개발자 행사에서 직접 공개한 사내 실험이다.
- 처음 건넨 지시문은 약 200단어 — *"화면에 보이는 이 몇 문단이 거의 전부입니다."*(00:23~00:25) 질문 둘: 200단어로 어떻게 1,000시간을 일하게 했나, 비용은 얼마였나.

## 2. 작년엔 7시간, 올해는 며칠 (00:35~01:54)

- 발표자 Friel은 1년 전 같은 무대(DevDay 2025)에서 Codex를 **7시간** 혼자 일하게 만든 방법을 소개했다. 그때 프롬프트는 화면에 다 안 들어갈 만큼 길었다 — 예시 코드, 쓸 라이브러리, 구현 순서까지 적었고, 계획서를 먼저 쓰게 한 다음 *"사람이 따져 묻고 나서야 일을 시작시켰습니다."*(00:56~00:57) → 설명란 참고: OpenAI Cookbook *"Using PLANS.md for multi-hour problem solving"*(2025-10-07, 위키 미열람).
- 동료 VB의 9월 게시물(설명란 X 링크): 뉘르부르크링 주행 영상을 주자 **20.8km 코스 전체를 3D로** 다시 만들었다. 렌더링에만 이틀 남짓, 메모리 부족 · 과열로 여러 번 멈췄지만 *저장해 둔 지점부터*(판독 추정) 스스로 이어 갔다. 같은 방식으로 Lewis Hamilton의 Ferrari도 — 규정 · 엔지니어 영상 · 사진을 찾아 3D로, 클레이 · 와이어프레임 버전까지 알아서(해설 전달).
- 1년 사이 달라진 것 — Friel의 답: *"이제는 절차를 불러주지 않습니다."*(01:46) *"목표와 원하는 결과, 그리고 무엇을 아끼고 무엇을 포기할지만 말해주고 단계는 모델이 알아서 찾게 합니다."*(01:48~01:52) → [[goal-level-delegation]]

## 3. 맡긴 일: CI와 플레이키 테스트 (01:54~02:42)

- Friel 팀의 일인 CI. 이게 초록불이어야 모두가 배포할 수 있다. 문제는 *한 번 실패했다가 다시 돌리면 통과하는 테스트* — 플레이키 테스트. 진짜 고장인지 우연인지 누군가 들여다봐야 하고, 까다로운 건 몇 시간에서 며칠, 그 사이 다음 실패가 들어온다. *"끝이 없는 일이죠."*(02:17) → [[flaky-tests]]
- 실험의 질문: *"사람이 매번 시키지 않아도 에이전트가 이 일을 알아서 집어갈 수 있을까?"*(02:21~02:23)
- 200단어에는 코드도, 고치는 법도 없다. 대신 **일하는 규칙**: 근무 시간이 아니면 메시지를 바로 보내지 말고 모아 둘 것 · CI에는 한 시간에 한 번 넘게 올리지 말 것 · 테스트를 어떻게 돌리는지는 직접 알아낼 것.

## 4. 나흘째의 한마디, 하위 에이전트 (02:42~03:28)

- 시작하고 나흘째 Friel이 딱 한 번 크게 끼어든다: *그런 잡일은 하위 에이전트에게 시켜라*(판독 추정 — ko *"그런 자빌은"*, en-orig *"trivial tasks"*). 이 한마디가 생산성을 완전히 바꿨다고 한다.
- 모델은 GPT-5.6 Sol(판독 추정)로 시작. 처음엔 한 스레드에서 실패 조사 · 수정까지 다 했고, 어려운 문제 하나에 붙잡히면 다른 실패가 쌓였다. 이후 **메인 스레드는 테스트 실행 · 실패 수집 · 사람에게 메시지** 만, *"코드를 내려받아 고치고 CI에 다시 올리는 느린 일은 전부 하위 에이전트 몫이 됐고요."*(03:09~03:13) → [[subagent-vs-thread-handoff]]
- 원음(ko-orig, 화자 미발화 · Friel 추정): *"Last year at Dev Day I joked that I kind of become a manager of agents and this year I've been promoted to a director of agents."*(03:15~03:20)<!--k--> *"I give an agent a job and then it manages a team of agents to get it done for me."*(03:23~03:27)<!--k-->

## 5. 숫자로 본 6주 (03:28~04:24)

| 항목 | 값(해설 전달 · 자기 보고) |
|---|---|
| PR | 6주 동안 매주 100개 이상 |
| 커밋 | 1,000개 이상 |
| 동료에게 보낸 슬랙 메시지 | 600건 이상 |
| 실제로 머지된 수정 | **213건** |
| 도구 호출 | 49만 9천여 번 — 그중 6만 7천여 번은 *그냥 기다리는* 호출 |
| 하위 에이전트 세션 | 5,800개 이상 |

- 머지되지 않은 것 중엔 다른 사람이 이미 비슷한 수정을 낸 경우가 많았고, *"그럴 땐 자기 것보다 그쪽을 먼저 밀어줬다고 합니다."*(03:44~03:45)
- 기다리는 호출: *"사람은 커피를 가지러 가지만 에이전트는 결과가 오면 바로 다음 단계로 넘어갔습니다."*(03:59~04:02)
- 213건이 적어 보여도 *"고치느니 건너뛰거나 재시도하고 말던 끝까지 남아 있던 가장 어려운 버그들이었습니다."*(04:07~04:11)

## 6. 가장 어려운 버그: GPU 하이젠버그 (04:24~05:15)

- GPU 테스트의 부동소수점 계산이 아주 가끔 다른 값을 내는 문제 — 볼 때마다 결과가 달라지는 하이젠버그. Friel 본인도 자기 전문 밖이라고 했다.
- 에이전트는 몇 주 치 로그를 맞춰 보다 **특정 노드 한 대에서만** 생긴다는 것을 찾았고, 그 노드에서 테스트를 반복해 돌리는 법을 스스로 익혔다. 재현은 됐지만 매번은 아니었고 여기에만 며칠.
- Friel이 가장 놀란 것: 에이전트가 그 시스템을 맡은 연구자들에게 **먼저 연락해** 물었다 — *"저장소에 선언되지 않은 소프트웨어 최적화인지 아니면 하드웨어 결함인지"*(04:56~04:58). 사람과 함께 문제를 풀었다.
- 빨간불을 끄는 가장 쉬운 방법은 실패하는 테스트를 지우는 것이다. 에이전트는 확신이 없을 때 *"다른 에이전트를 하나 더 만들어 자기 수정을 따져 묻게 했습니다. 사람에게 리뷰를 요청하기 전에요."*(05:08~05:13) → [[generator-evaluator-pattern]]

## 7. 멈추지 않게 만든 기능 6가지 (05:15~06:50)

VB의 정리(해설 전달):

| # | 기능 | 내용 |
|---|---|---|
| 1 | **목표**(goal) | 결과 하나에 스레드 하나, `/goal`(판독 추정)로 목표를 주면 끝날 때까지 붙든다. AGENTS.md에 해도 되는 일 · 안 되는 일. VB의 팁: 지금까지 한 일 · 남은 일을 메모로 남기게 — 끊겨도 그 메모를 읽고 돌아온다. 맥락이 넘치는 문제엔 자동 **compaction**(따로 켤 필요 없음). 농담이라며 석 달째 도는 스레드도 있다고 |
| 2 | **원격 환경** | 6주 내내 노트북을 켜 둘 수 없다 — SSH로 원격 머신에, 또는 이날 새 버전을 공개한 Codex 클라우드에 |
| 3 | **플러그인** | GitHub 이슈 · Slack 대화를 봐야 이미 누가 고치는 문제에 헛수고를 안 한다 |
| 4 | **자식 스레드** | 서로 기다릴 필요 없는 일은 쪼개서 동시에. 각자 worktree(코드의 별도 사본)에서 |
| 5 | **Ultra** | 어려운 문제 하나에 생각할 시간을 길게, 그 안에서 하위 에이전트들이 서로 다른 가설을 판다 |
| 6 | **예약 작업** | 리뷰를 기다리며 멈추지 말고 30분마다 돌아와 확인. 같은 스레드로 돌아오니 한 일을 기억한 채 이어간다 — **heartbeat** |

- VB의 구분: *"나란히 쪼갤 수 있는 일은 스레드로, GPU 버그 같은 어려운 한 문제는 울트라로."*(06:33~06:36) → [[subagent-vs-thread-handoff]]
- → [[context-resets-and-compaction]] · [[cloud-agent-delegation]] · [[scheduled-agent-automations]]

## 8. 비용: 시간당 약 32달러에서 16달러로 (06:50~07:29)

- VB가 무대에서 대신 묻는다 — OpenAI 직원이라 토큰이 무한이니까 가능했던 건 아닐까?
- ⚠️ **답의 수치 대목(07:02~07:08)은 무캡션**이다. 챕터 제목만 *시간당 약 32달러에서 16달러로* 라고 적는다. 캡션에 남은 것: *"발표한 주 전에 나온 GPT 6 솔 기준으로는 이게 절반으로 내려간다고 합니다."*(07:11~07:14) *"같은 예산으로 두 배를 가는 셈이죠."*(07:14~07:15)
- 단 에이전트 값만이다 — 코드 리뷰에 드는 사람의 시간이나 CI 자원은 따로라고 덧붙였다.
- *그래디크*(판독 불가)는 여름 동안 수백 시간을 돌려받았고 그 시간을 인프라를 키우는 데 썼다고 한다.

## 9. 시작하는 법 5가지 · 정리 (07:29~08:27)

1. 스레드 하나가 그 일을 책임지게 — 백로그 정리든 에러 로그 감시든 내 시간을 잡아먹는 반복 업무 하나부터.
2. 스스로 결과를 확인할 방법 — *"돌려볼 테스트가 있어야 루프가 돕니다."*(07:41~07:43) → [[verifiable-goals]]
3. 독립된 일은 위임하게 하고 모델은 일의 난이도에 맞춘다.
4. 무엇이 중요한지, 언제 사람을 불러야 하는지 알려 준다.
5. 예산을 정한다 — Friel의 경우 CI 작업을 동시에 몇 개까지 돌려도 되는지.

- 맺음: 에이전트가 가장 일을 잘한 *날*(판독 추정)은 아무도 말을 걸지 않은 날이었다. 원음: *"What could Codex take off of your plate?"*(08:16~08:18)<!--k--> *"And what should you do with the time that it gives you back?"*(08:19~08:22)<!--k-->

## 위키의 읽기

- **[[goal-level-delegation]]의 가장 긴 사례.** 위키의 기존 사례들(Slack 에이전트 · Astra · 개인 에이전트)은 *목표를 주라* 를 주장했고, 이 소스는 **같은 사람이 1년 간격으로 절차형(7시간) → 목표 · 규칙 · 한계형(6주)** 으로 옮긴 비교를 준다. 단 모델도 바뀌었으므로(GPT-5.6 Sol → GPT-6.x Sol) *프롬프트 방식만의 효과* 로 읽을 수는 없다 — 해설도 이를 분리하지 않는다.
- **Cooking with Codex 편과 같은 기능 묶음.** goal · subagents · thread handoff · heartbeat · scheduled는 [[tech-bridge-cooking-with-codex]](10-11, Charlie Guo · Gabriel Chua)가 이미 시연했다. 이 소스가 보탠 것은 **6주 운영의 숫자**, **Ultra**(위키 첫 기록), **heartbeat 30분 간격**, *CI에 시간당 1회* 같은 예산 규칙이다.
- **도구 호출의 13%가 대기.** 49만 9천 중 6만 7천(위키 계산 약 13%)이 기다리는 호출이다 — 장기 에이전트의 시간 중 상당 부분이 *외부 시스템을 기다리는 시간* 이라는 수치. heartbeat · 예약 작업이 그 대기를 스레드 밖으로 빼는 장치다(위키의 연결).
- **사람에게 먼저 묻는 에이전트.** GPU 버그에서 연구자에게 연락 · 남의 수정을 먼저 밀어 줌 · 슬랙 600건 · 근무 시간 외 메시지 모아 두기 — 이 실험의 에이전트는 **혼자 일하기보다 사람과 함께 일하는 동료** 로 그려진다. → [[persistent-agent-teams]]
- ⚠️ **비용은 확인 불가.** 32 → 16달러는 챕터 제목에만 있다(캡션 무캡션). 위키 계산으로 1,000시간 × 32달러 ≈ 3만 2천 달러이지만 **영상이 말한 값이 아니다.** 사람 리뷰 시간 · CI 자원은 제외된 값이다(해설 전달).
- ⚠️ **모델 이름과 시점.** 시작 모델 *GPT 5.6 솔*, 비용 기준 *발표 한 주 전에 나온 GPT 6 솔*, 태그 `GPT-6.1 Sol` · `GPT-6`. 위키에는 [[openai-terra|GPT-6.1 Terra]](10-29 첫 리뷰)가 있지만 *Sol* 은 처음이다 — 같은 계열인지, DevDay 날짜(위키는 *2026-10-02 이전* 만 확정, [[tech-bridge-altman-devday-dots]])와 *한 주 전* 이 어떻게 맞는지 미확인. 페이지화하지 않는다.

## 등장 개체

- 인물: [[aaron-friel]](철자 추정) · [[vaibhav-srivastav]] · Lewis Hamilton(언급) · *그래디크*(판독 불가)
- 조직 · 제품: [[openai]] · [[codex]] · Codex 클라우드 · GPT-5.6 Sol · GPT-6.x Sol(페이지화하지 않음) · DevDay 2026
- 개념: [[flaky-tests]] · [[goal-level-delegation]] · [[subagent-vs-thread-handoff]] · [[context-resets-and-compaction]] · [[cloud-agent-delegation]] · [[scheduled-agent-automations]] · [[generator-evaluator-pattern]] · [[verifiable-goals]] · [[persistent-agent-teams]]

## References

- 영상: https://www.youtube.com/watch?v=AYCGbCxXHMU
- raw: `01.raw/articles/2026-11-14_프롬프트 200단어로 6주를 일한 AI OpenAI가 공개한 멈추지 않는 Codex 에이전트 8분 정리.md`
- 설명란 참고(위키 미열람): OpenAI "What Will You Build With Coding Agents That Don't Quit? | DevDay 2026" https://www.youtube.com/watch?v=U1IVZy9FhVQ · OpenAI Cookbook "Using PLANS.md for multi-hour problem solving"(2025-10-07) https://developers.openai.com/cookbook/articles/codex_exec_plans · VB 뉘르부르크링 게시물 https://x.com/reach_vb/status/2097102145451405462
