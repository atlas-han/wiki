---
title: "Tech Bridge — 구글 엔지니어가 말아주는 AI 하네스 | AI를 일하게 만드는 네 가지 설계 (한국어 해설 + Annie Wang 발췌): 기억 · 도구와 작업 순서 · 실행 환경과 권한 · 완료 기준"
type: source
tags: [annie-wang, google, adk, agent-harness, session, state, long-term-memory, mcp, workflow, retry-limit, sandbox, prompt-injection, data-flow, deterministic-evaluation, llm-as-judge, human-evaluation, commentary-format, video]
source-url: https://www.youtube.com/watch?v=8tjhiruPpBg
source-type: video
author: Tech Bridge (한국어 해설, 내레이터 미상) · 발췌 화자 [[annie-wang|Annie Wang]](Google — 설명란 근거, 발화에 이름 없음) · 원본 영상 링크 없음
date-published: 2026-10-25
ingested: 2026-10-26
created: 2026-10-26
updated: 2026-10-26
---

# Tech Bridge — 구글 엔지니어가 말아주는 AI 하네스

[[tech-bridge|Tech Bridge]]가 올린 **7:20, 공식 챕터 10** 영상. **멤버 전용을 거쳐** 2026-10-26 회차에 공개로 확인됐다(10-24 · 10-25에는 id만 보였다). 형식은 **"한국어 해설 + 원본 발췌"** 이고, 설명란은 *"구글 엔지니어 Annie Wang의 설명을 따라"* 라고만 한다 — 원본 영상의 제목 · 날짜 · 링크는 없다. 원본과 해설이 **같은 예제(고객 명단 CSV 내려받기 버튼)** 하나로 하네스의 네 층을 차례로 통과한다.

> **(해설의 줄거리)** *"코드를 아는 것과 파일을 바꾸고 결과를 확인하는 건 서로 다른 일이에요."*(00:05~00:13) 그 사이를 잇는 소프트웨어가 하네스다. 좋은 하네스를 고르는 네 질문: *"무엇을 기억하나요? 어떤 도구를 어떤 순서로 쓰나요? 어디까지 접근할 수 있나요? 무엇을 확인해야 완료인가요?"*(06:56~07:05)

> 원음: *"Those controls need to be enforced by software. Simply telling the model to be careful isn't enough."*(04:33~04:37)

이 위키에 생기는 것: [[annie-wang]](신규 — 인물). 기존 페이지에는 [[agent-harness-design]]의 **네 질문**, [[agent-memory]]의 **session · state · long-term memory 3분할**, [[model-context-protocol]]의 정의, [[agent-sandboxing]]의 **샌드박스와 데이터 흐름의 구분**, [[prompt-injection]] · [[hard-vs-soft-enforcement]]의 **"모델에게 조심하라고 말하는 것으로는 부족하다"**, [[generator-evaluator-pattern]]의 **결정적 평가 → judge → 사람 평가** 사다리가 붙는다.

**트랙과 인용.** 오디오 `Korean original` + `English (US)`, 메타 `language`=`en`. 받은 **ko = `lang=ko` 원 ASR**(`ko`·`ko-orig` 바이트 동일). 해설은 ko로, 발췌는 ko 트랙의 영어 조각과 en-orig를 대조해 인용한다. 판독 상세는 raw.

> ⚠️ 발췌 몇 구간은 앞부분이 무캡션이다(00:17~00:25 · 00:52~00:57 · 04:13~04:16). 발췌 화자는 이름을 말하지 않는다 — **Annie Wang 귀속은 설명란 근거**다.

## 1. 하네스란 (00:00~00:35)

- (해설) 고객 명단을 내려받는 버튼 하나를 만든다고 하자. *"구글의 애니왕은 그 사이를 이어주는 소프트웨어를 하네스라고 설명해요."*(00:13~00:15, ASR *"한스"*)
- **원음**(00:25~00:33): *"[—] harness. It provides cons[connections?], connect tools and enforce permissions and also manage all the back-and-forth communication."*

## 2. 기억과 맥락 — session · state · long-term memory (00:34~01:46)

- (해설) 처음엔 고객 명단 전체를 달라고 했다가 **이름과 이메일만** 으로 바꿨다. *"작업이 길어져도 이 조건을 놓치면 안 되겠죠?"*(00:37~00:46)
- **원음**(00:57~01:25): 세션은 에이전트 · 도구 · 결과와 *"all the transcript of your conversation"* — *"your original request and that follow-up instruction both belong to the session."* 상태는 *"more like a scratch pad for your application"* — 이름 · 이메일 · *status as ready for testing* 을 key-value로 두고 코드가 읽고 갱신한다.
- (해설) *"대화 기록은 작업일지, 상태는 지금 필요한 값을 적는 메모라고 보면 돼요. 여기에 다음 대화에서도 쓸 취향을 보관하면 장기 기억이 돼요. 무엇을 저장하고 다시 꺼낼지는 설계자가 정해요."*(01:27~01:43) → [[agent-memory]]

## 3. 도구와 MCP (01:26~02:15)

- **원음**(01:48~02:13): *"[The model] might decide, okay, I need to edit this file. But that decision doesn't change the file itself. A tool has to apply the edit and that tool could be a Python function. Another function might run tests or call an external API. You can also connect tools through an MCP server and MCP stands for model context protocol. It gives your application a standard way to discover and call tools exposed by a server."*(마지막 문장은 en-orig 기준) → [[model-context-protocol]]

## 4. 작업 순서와 두 가지 검사 (02:15~03:13)

- (해설) *"도구는 일을 하는 방법이고 작업 흐름은 그 방법을 어떤 순서로 쓸지 정하는 거예요."*(02:14~02:19, ASR *"작업 푸름"*) 파일을 잘 만들어도 버튼이 안 될 수 있으니 **코드 검사와 실제 버튼 검사**를 함께 돌리고, *"계속 실패할 때 멈추는 규칙도 있어야"* 한다(02:22~02:34).
- **원음**(02:34~03:12): 코딩 에이전트가 먼저 바꾸고, **두 검사를 병렬로** — export 로직 unit test, 버튼을 눌러 다운로드를 확인하는 browser test. 실패하면 피드백이 에이전트로 돌아가고, 둘 다 통과하면 review 단계로 간다. *"[ADK?] graph workflow let you define that structure. So a node can be an agent or a regular function and a connection determine what happens next. You can also set a retry limit so if agent keeps trying [—] fixing the problem the workflow stops and ask for help."* ⚠️ *"ads graph workfow"* 를 ADK graph workflow로 판독(태그 `ADK`, 추정). → [[deterministic-agent-pipeline]] · [[workflow-vs-agent]]

## 5. 실행 환경과 샌드박스 (03:13~03:55)

- (해설) *"버튼 하나 시험하려고 실제 고객 명단 전체를 맡길 필요는 없겠죠. 연습용 프로젝트와 가짜 고객 자료를 따로 주면 돼요."*(03:13~03:23)
- **원음**(03:30~03:55): *"[A c]oding agent often runs in a sandbox and that is an isolated environment with restrictions on which file and network services it can access. (…) You can work there without access to the production customer database. That's part of your [run]time design, deciding where the code executes."* → [[agent-sandboxing]]

## 6. 프롬프트 인젝션과 권한 통제 (03:55~04:43)

- (해설) 연습 공간 안에도 *"읽던 파일에 비밀번호를 다른 곳으로 보내라는 지시가 숨어 있을 수 있어요"*. *"파일에서 읽은 글을 새 명령으로 받아들이지 않고 실제 도구가 할 수 있는 일도 따로 제한해야 해요."*(03:57~04:13)
- **원음**(04:16~04:42): 제한된 권한, *"credentials kept out of reach"*, 네트워크 접근 제한, 민감한 동작 전에 하네스가 멈추고 승인을 묻게. 그리고 위 인용 — *"Simply telling the model to be careful isn't enough."* 샌드박스는 프롬프트 인젝션의 **영향을 줄일 뿐**이다. → [[prompt-injection]] · [[hard-vs-soft-enforcement]] · [[credential-injection-outside-sandbox]]

## 7. 내 컴퓨터 밖으로 나가는 자료 (04:43~05:29)

- (해설) *"프로그램이 내 컴퓨터에서 돈다고 해서 자료도 전부 그 안에만 남는 건 아니에요. (…) 실행 장소와 정보가 가는 곳을 따로 살펴야 해요."*(04:44~05:00)
- **원음**(05:02~05:29): *"Even if a tool runs on your laptop, it's output may be sent to a [hosted?] model. It might also be saved in session history, logs or longterm memory. So think about what data the agent actually needs, where it's allowed to go and how long it should be kept."* 예제에서는 가짜 고객 자료면 충분하다. → [[agent-sandboxing]] · [[lethal-trifecta]]

## 8. 완료 기준 — 결정적 평가 · judge · 사람 (05:29~06:55)

- (해설) *"AI가 다 됐다고 말해도 실제 파일을 확인하기 전에는 알 수 없죠."*(05:30~05:36)
- **결정적 평가**(원음 05:48~06:07): 샘플 고객 10명이 이름 · 이메일까지 그대로 들어갔는지 코드로 자동 확인 — *"that is deterministic evaluation"*.
- **judge**(해설 06:09~06:18): 숫자가 맞는다고 좋은 기능은 아니다. 완료 안내가 이해하기 쉬운지는 *"다른 AI에게 기준을 주고 검토하게"* 한다. 해설은 또 *"클로드 개발사의 실무 기록에서도 코드 검사만으로 놓친 문제를 실제 브라우저 조작으로 찾아냈어요"*(06:18~06:24)라고 덧붙인다 — 어느 문서인지 밝히지 않는다(⚠️ 외부 인용, 미확인 — [[anthropic-harness-design-long-running-apps]]의 Playwright 평가자와 같은 이야기일 수 있으나 대조하지 않았다).
- **사람 평가**(원음 06:29~06:55): *"The judge can make mistakes. So it is very helpful to compare its judgment with human review"* — 직접 써 보면 다운로드는 되는데 버튼 이름이 헷갈리거나 찾기 어려울 수 있다. → [[generator-evaluator-pattern]]

## 9. 네 가지 질문 (06:55~07:20, 해설)

- 위 인용. *"이 기준을 정하면 똑똑한 모델이 실제 일을 끝내도록 도울 수 있어요."*(07:07~07:10)

## 이 위키와의 연결

### 이어지는 것

- **[[tech-bridge-jediah-katz-harness-whats-left]](10-23 업로드)** — *"모델이 똑똑해져도 하네스에 남는 것"* 을 물은 편. 이 편은 같은 질문에 **기억 · 도구/순서 · 환경/권한 · 완료 기준** 네 층으로, 초보자용 예제 하나를 끝까지 따라가며 답한다.
- **[[hard-vs-soft-enforcement]]** — *"enforced by software. Simply telling the model to be careful isn't enough"* 는 이 페이지의 hard enforcement 쪽 주장을 구글 엔지니어의 입으로 한 문장에 담은 것이다.
- **[[agent-sandboxing]]** — 샌드박스(**어디서 실행되나**)와 데이터 흐름(**결과가 어디로 가나**)을 **별개의 질문**으로 분리한다. 노트북에서 돌아도 출력은 호스팅 모델 · 세션 기록 · 로그 · 장기 기억으로 나간다.
- **[[agent-memory]]** — session(대화 transcript) · state(key-value scratch pad) · long-term memory(다음 대화의 취향) 3분할은 ADK 류 프레임워크의 용어로 보인다(⚠️ 원본에서 프레임워크 이름을 확정하지 못했다).

## 해소하지 않고 표시만 한 것

- 원본 영상의 제목 · 날짜 · 링크 없음. 화자 귀속은 설명란 근거.
- *"ads graph workfow"* → ADK graph workflow, *"foring agent"* → coding agent, *"time design"* → runtime design, *"hosing model"* → hosted model은 판독 추정. *"cons"* · *"alles"* · *"res fixing"* 판독 불가.
- 해설의 Anthropic *"실무 기록"* 인용은 출처 미상.
- 멤버 전용 기간의 원래 업로드 날짜는 모른다(현재 `upload_date` 20261025는 공개 전환 시점 쪽일 수 있다 — 앞선 사례들과 같은 패턴).

## 등장 개체

- 인물: [[annie-wang]](신규)
- 조직: Google(조직 페이지 없음 — 소속 부서 미상) · [[anthropic]](해설의 외부 인용)
- 도구: ADK(태그 · 판독 추정, 페이지화하지 않음) · [[model-context-protocol|MCP]]
- 개념: [[agent-harness-design]] · [[agent-memory]] · [[model-context-protocol]] · [[deterministic-agent-pipeline]] · [[agent-sandboxing]] · [[prompt-injection]] · [[hard-vs-soft-enforcement]] · [[generator-evaluator-pattern]] · [[lethal-trifecta]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=8tjhiruPpBg> (7:20, `upload_date` 2026-10-25, 2026-10-25 18:00 KST)
- raw: `01.raw/articles/2026-10-25_구글 엔지니어가 말아주는 AI 하네스 - AI를 일하게 만드는 네 가지 설계.md`
- [[tech-bridge]] · [[annie-wang]] · [[tech-bridge-jediah-katz-harness-whats-left]]
