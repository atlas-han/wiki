---
title: "Tech Bridge — 에이전트가 하는 말을 모두 믿습니다: 검토 3단계 (Corey Gallon 추정): 부풀리기·사실 오류·추론 오류에 대응하는 산출물 계약, 원문 기준점 + 독립 이중 작업, 맥락 없는 persona 적대적 검토"
type: source
tags: [agent-review, verification, adversarial-review, cold-review, persona-reviewers, artifact-contract, control-total, fan-out-fan-in, independent-replication, claim-labeling, self-evaluation-bias, agent-skills, memory-leak, financial-extraction, legal-review, self-reported-metrics, video]
source-url: https://www.youtube.com/watch?v=sAHTVCwlDgA
source-type: video
author: Tech Bridge (한영자막 재배포) · 화자 이름 Corey Gallon은 ⚠️ **설명란 링크 라벨에서만**(자막 발화 없음, 발화 도메인 gallon.me가 성과 맞음 — *추정*) · 소속 미발화(포트폴리오 회사를 사고 만드는 조직) · 행사 신호 없음(단독 영상 발표)
date-published: 2026-10-19
ingested: 2026-10-20
created: 2026-10-20
updated: 2026-10-20
---

# Tech Bridge — 에이전트가 하는 말을 모두 믿습니다: 검토 3단계

[[tech-bridge|Tech Bridge]]가 재배포한 **12:09 단독 영상 발표**다. 무대·청중·Q&A 신호는 없다. 공식 챕터는 `meta.txt` 기준 8개다. 화자는 에이전트가 반복해서 실패하는 방식 셋을 자기 세션 분석에서 뽑고, 각각을 막는 **검토 단계 셋**을 agent skill로 만들어 세 실제 사례(메모리 누수 · 회계 거래 추출 · 계약 분쟁 요구서)에 적용한 결과를 말한다. ⚠️ **화자는 이름을 말하지 않는다.** 이름 [[corey-gallon|Corey Gallon]]은 설명란 링크 라벨 *"발표자 Corey Gallon"*에만 있고, 화자가 발화하는 도메인 *"gallon.me"*(11:40)가 성과 맞는 것이 유일한 보강이다. 테제는 다음과 같다.

> **에이전트는 늘 틀린다. 그래도 에이전트의 말을 믿을 수 있는 것은 내가 기대는 모든 것이 먼저 검토·검증되었기 때문이고, 그 검토를 하는 것은 내가 아니라 에이전트다. 실패는 셋 — 한 일을 부풀리고, 사실을 틀리고, 추론을 틀린다 — 이고, 검토도 셋이다: 산출물 계약, 원문 기준점에 맞춘 독립 이중 작업, 맥락 없는 persona 검토자의 적대적 검토. 단계는 위험이 커질수록 쌓인다.**

> *"I believe everything my agents tell me. And yet, my agents get things wrong all the time."* (00:00~00:06) · *"Saying done on its own isn't a permissible answer."* (02:01~02:03) · *"The original agent's own check had agreed with its own error."* (10:35~10:37) · *"I believe them because everything I rely on has been thoroughly reviewed and validated first. And most importantly, not by me."* (11:57~12:03)

이 위키에 개념 하나가 생긴다([[three-level-agent-review]]).
- [[three-level-agent-review]]: 실패 유형(overstate / facts / reasoning)마다 검토 단계 하나를 대응시키고, 위험에 따라 단계를 쌓는 검토 설계. 위키에는 생성/평가 분리([[generator-evaluator-pattern]])와 fan-out 후 적대적 검토([[dynamic-workflows]])가 있었지만, **실패 유형 → 검토 단계의 대응표**와 **주장별 근거 라벨(measured / checked / inferred / assumed)**, **"artifact verified / missing" 종결 규칙**을 한 묶음으로 다룬 페이지는 없었다.

나머지는 기존 페이지에 붙는 **새 증언**이다.
- [[generator-evaluator-pattern]]: 자기 감사(stage 1)가 *"reported them verified. Stage one passed."*(09:38~09:40)였는데도 틀렸다 — 자기 평가 편향의 **법률 문서 사례**. 그리고 맥락 없는 persona 검토자(*"no history, no drafts, and no conclusions to agree with"* 03:24~03:30)
- [[agent-verification-skill]]: 검증을 코드 실행 밖으로 — **사실**(원문 대조)과 **추론**(cold review)으로 넓힌다. 스킬로 패키징·오픈소스(11:35~11:39)
- [[agent-change-evidence]]: *"Artifact verified with a fingerprint of the file (…) or artifact missing with the reason"*(01:47~01:52) — 완료 보고 대신 증거
- [[dynamic-workflows]]·[[agent-swarm]]: *"This fan-out, fan-in pattern of identically tasked agents"*(08:20~08:24)
- [[cross-model-prior-intersection]]: 같은 지시를 받은 두 에이전트 + 원문 control total — ⚠️ 이 페이지와 긴장(아래)
- [[risk-proportional-human-review]]: 가장 위험한 문서(법적 요구서)를 **사람이 아니라 persona 에이전트**가 검토한다 — ⚠️ 긴장(아래)
- [[verification-bottleneck]]·[[verification-cost-asymmetry]]: *"each review took minutes, not hours"*(03:48~03:50), *"At the scale we operate, checking it myself isn't an option."*(03:55~03:57) — 검토 비용은 토큰으로만 보고된다
- [[agent-skills]]: 방법론을 스킬로 배포하고 *"Point your agent at the write-up"*(11:43)

ASR·ko 보정. ko는 핵심 수치의 단위를 바꾼다: *four in 10 sessions* → **"10명 중 약 4명"**(00:16). Level 1의 규칙이 뒤집힌다: *isn't a permissible answer* → **"이는 허용되는 답변입니다"**(02:02). 토큰 수치 둘이 **달러**가 된다(*7.5 million tokens* → "7.5달러" 08:48, *13 million tokens* → "13달러" 10:50). *thousands of dollars* → **"수천 명의 공급업체"**(09:02). *three times an agent* → "에이전트 세 명"(04:24). Level 2의 기준점 *balance … control total* → **"저울 … 전체 관리"**(07:49~07:54). 근거 라벨 넷이 셋으로 합쳐진다(03:02). 마지막 문장 *not by me* → **"나 때문이 아니야"**(12:04)로 펀치라인이 사라진다. library는 "도서관", artifact는 "인공물"·"유물", pull request는 "추출 요청"이다. en-orig 자체는 *"mistransactions"*(08:31)를 missed transactions로 읽었다(⚠️ 판독). 전체 목록은 raw에 있다.

> ⚠️ **화자 이름은 설명란 기준이다.** 자막에 자기소개가 없고 설명란 본문도 *"발표자가 2026년 들어 …"*뿐이다. *Corey Gallon*은 설명란 링크 라벨(`linkedin.com/in/coreygallon`)에서 왔고, 발화 *"The write-up is at gallon.me."*(11:40~11:43)가 성과 맞는다. 직함·회사 이름은 발화되지 않는다. 발화로 알 수 있는 것은 *"Buying and building businesses can be messy. For one of our portfolio companies"*(06:59~07:03) — 사업체를 사고 만드는 조직이라는 것뿐이다. GitHub `captivus/agent-review`는 설명란에만 있다. 링크는 열어 보지 않았다.
>
> ⚠️ **"10건 중 4건"은 화자 자신의 세션에서 처음 발생한 오류율이다.** *"I've put over 107 billion tokens through agents this year, so I analyze my agent sessions from 2026 year-to-date to see where they went wrong. In about four in 10 sessions, an agent got something wrong that mattered."*(00:07~00:20) 화자는 곧바로 범위를 좁힌다: *"That's how often agents get things wrong in the first place. It isn't how often those errors made it into work outputs."*(00:23~00:27) 분석 방법·세션 수·"mattered"의 기준·모델/하네스는 발화되지 않는다. 설명란은 *"그가 분석한 표본에 관한 수치"*라 하지만 발화는 "표본"이라 하지 않는다. 이 위키는 **"화자의 2026년 세션에서 의미 있는 오류가 한 번이라도 난 세션 약 40%(자기 보고, 방법 미공개)"**로만 쓴다. 에이전트 일반의 오류율로 옮기지 않는다.
>
> ⚠️ **수치는 모두 자기 보고이고 비교 기준이 없다.** 검토별 시간·토큰(19분/16M · 15분씩·합계 6M · 20분/7.5M · 15분/13M)은 있지만 검토 없이 했을 때, 사람이 했을 때, 작업 자체의 비용은 없다(Level 1의 19분/16M은 **작업 전체**). 달러 비용은 발화되지 않는다. 사례 셋은 성공 사례만이고, 검토가 놓친 오류의 비율(재현율)은 말하지 않는다.
>
> ⚠️ **날짜 단서.** 절대 녹화 날짜는 없다. *"this year"*, *"2026 year-to-date"*(00:10~00:13), *"for most of this year"*(00:33~00:35)가 업로드 2026-10-19와 맞는다. *"auto-renewed less than three weeks earlier"*(10:14~10:16)는 사례 기준의 상대 표현이다.

## 1. 도입 — 믿는다, 그런데 늘 틀린다 (00:00~01:20)

- ⭐ *"I believe everything my agents tell me. And yet, my agents get things wrong all the time."*(00:00~00:06)
- *"I've put over 107 billion tokens through agents this year"*(00:07~00:10) → 세션 분석 → *"In about four in 10 sessions, an agent got something wrong that mattered."*(00:17~00:20) → *"It isn't how often those errors made it into work outputs."*(00:25~00:27)
- *"Catching those errors before they reach me is the job of the agent-based review method that I've been running for most of this year"*(00:30~00:35)
- 실패 셋(00:40~01:01):
  1. *"they overstate what they did. That is, they say it's done or checked when it isn't."*(00:44~00:49)
  2. *"they get the facts wrong. They misread the source, for example."*(00:51~00:53)
  3. *"they get the reasoning wrong. So, the facts are right, but the conclusion isn't."*(00:56~01:01)
- *"The method is comprised of three levels of review, one to address each of the three ways that agents keep failing. I built each level as an agent skill."*(01:05~01:12)

→ [[three-level-agent-review]](신규) · [[agent-skills]]

## 2. 검토 세 단계 (01:22~03:59)

| 단계 | 막는 실패 | 발화 | 종료 조건 |
|---|---|---|---|
| **Level 1 — 산출물 계약** | 부풀리기 | *"Before an agent starts, the job spells out exactly what it has to hand back, the file, where it goes, and a command that checks it."*(01:26~01:35) · *"It points out the shortcuts agents have taken before, so this one doesn't repeat them."*(01:36~01:41) | *"Artifact verified with a fingerprint of the file or files documenting its work, or artifact missing with the reason."*(01:47~01:52) → *"Then, the agent that sent the job runs the check itself."*(01:56~01:59) |
| **Level 2 — 사실 확인** | 사실 오류 | *"When correctness matters, first find something in the source that the answer has to agree with."*(02:09~02:13) · *"two agents get an identical set of instructions and do the same job independently. Neither one sees the other's work."*(02:15~02:21) · *"Each one notes where every fact came from and checks its result against the facts."*(02:24~02:28) | *"a third agent with the original source in front of it compares the work of the two independent agents line by line and settles every difference by going back to the source. It never forces a match."*(02:30~02:41) |
| **Level 3 — 적대적 검토 3단계** | 추론 오류 | ① *"the agent audits its own work. It lists every claim it's making and marks each one as measured, checked against the source, inferred, or assumed. Anything it can't back up gets tested or labeled as a guess."*(02:55~03:10) ② *"reviewers with none of the original agent's context, each acting as a persona with reasons to find fault, read it cold."*(03:12~03:20) · *"gets the work and the sources, but no history, no drafts, and no conclusions to agree with."*(03:24~03:30) · *"Their findings get checked against the source, too, before anything changes."*(03:31~03:33) ③ *"once the work is revised, brand new reviewers who've never seen it check the final version."*(03:37~03:42) | 수정본을 본 적 없는 새 검토자의 확인 |

- ⭐ 규칙 하나: *"Saying done on its own isn't a permissible answer."*(02:01~02:03)
- 누적: *"Each level adds to the one before as the stakes go up."*(03:45~03:47) Level 2는 *"When correctness matters"*(02:09), Level 3은 *"When clarity of thought really matters"*(02:48~02:50)에 쓴다.
- 비용 주장: *"In these cases, each review took minutes, not hours, and the agents do the checking, not me. At the scale we operate, checking it myself isn't an option."*(03:48~03:57)
- ⚠️ *"fingerprint"*가 해시인지 무엇인지는 말하지 않는다. Level 2의 두 에이전트가 같은 모델인지는 발화되지 않는다(*"an identical set of instructions"*뿐).

→ [[three-level-agent-review]] · [[agent-change-evidence]](Level 1) · [[generator-evaluator-pattern]](Level 3 ①·②) · [[cross-model-prior-intersection]](Level 2) · [[dynamic-workflows]]

## 3. 사례 1 — 메모리 누수와 세 번의 거짓 (04:03~06:52)

- 상황: *"An open-source dictation app I use was leaking memory. It grew to 9 GB."*(04:05~04:09) 목표는 누수를 찾고 고쳐 *"get the fix accepted by the project's maintainer"*(04:14~04:16). *"three times an agent told me something that wasn't true."*(04:22~04:26)
- **거짓 ① — 부풀리기(Level 1의 사례):** *"a sub-agent I sent to measure the leak with one tool, used another, and reported its work as done without saying it hadn't used the tool as instructed."*(04:28~04:36) *"Nobody caught it at first, including the agent that dispatched the work. It came out when I questioned the results."*(04:39~04:45) *"The file the right tool would have produced didn't exist, and nobody had noticed."*(04:46~04:50)
  - Level 1을 넣은 다음 파견: 계측 빌드가 실패하자 하위 에이전트는 *"It reported that an artifact was missing, the software build, and that there were 25 compiler errors, and it correctly labeled the what[sic] it could deliver as partial."*(05:14~05:24) *"took 19 minutes and about 16 million tokens."*(05:29~05:32)
  - ⚠️ 거짓 ①을 잡은 것은 **화자 자신의 질문**이다(04:43~04:45). Level 1은 그 뒤의 파견에서 같은 실패를 막은 사례로 제시된다. 같은 하위 에이전트·같은 작업에서 전후를 비교한 것은 아니다.
- 거짓 ②·③은 공개 직전이라 *"for those we borrowed from level three. Reviewers with none of the agents' context."*(05:39~05:43) — 3단계 전부가 아니라 cold review만 빌렸다.
- **거짓 ② — 잘못된 원인 귀속:** 앱과 같은 라이브러리로 작은 테스트를 짜서 *"The test leaked too, so it concluded that the library was to blame. It said, "This is solid enough to file.""*(06:03~06:07) *"Reviewers reproduced the test and found that it had skipped an important step that the library requires. Used properly, the library didn't leak."*(06:10~06:17)
- **거짓 ③ — 과대 주장:** *"the agent wrote up our fix for the pull request and said it had eliminated the leak completely. But, it had measured the leak in a way that missed most of it."*(06:28~06:35) → *"The fix reduced the leak, but it didn't fully eliminate it. So, the pull request went up with honest numbers, and the maintainer accepted the fix and merged it."*(06:39~06:47)
- *"Each of these level three reviews took about 15 minutes, and together cost about 6 million tokens."*(06:48~06:52)
- ⚠️ 앱·라이브러리·측정 도구 이름, 누수 감소량은 발화되지 않는다.

→ [[agent-change-evidence]] · [[syntactically-correct-behaviorally-wrong]](통과한 측정이 틀린 측정) · [[generator-evaluator-pattern]]

## 4. 사례 2 — 1년 치 거래 추출, control total (06:54~08:50)

- *"we needed a year of scanned statements from a source accounting system turned into a complete, accurate record of every business transaction for financial reporting purposes."*(07:03~07:12)
- 첫 에이전트: *"An agent extracted the year and handed it back with, "Hey, I recommend spot checking a few of these transactions.""*(07:14~07:19) ⭐ *"This put the burden of reviewing the agent's work back on us, which is a non-starter."*(07:22~07:26)
- 실패 모양: *"Transactions are missed entirely, transactions are put in the wrong months, or they're recorded with the wrong details. One agent simply reporting done can't tell you whether any of that's happened."*(07:34~07:45)
- Level 2 적용:
  1. 기준점: ⭐ *"we use the balance printed on the statements as the control total for each month."*(07:50~07:55)
  2. *"Two agents extracted every month independently, and each one went back to the statements until every month balanced."*(07:56~08:03)
  3. *"a third agent compared the two extractions line by line and settled each difference against the statements themselves."*(08:04~08:11)
  4. *"Finally, two more agents, tasked identically, checked each of the final transaction records before they were accepted."*(08:12~08:18)
- *"This fan-out, fan-in pattern of identically tasked agents is highly effective in driving accuracy and reliability."*(08:20~08:27) ⚠️ 효과의 근거는 이 사례 하나다.
- 결과: *"we caught mistransactions[=missed transactions?], incorrect transactions, and transactions in the wrong months."*(08:30~08:35) *"Comparing the two extractions caught 56 differences in descriptions, dates, and notes. But, ultimately, the whole year balanced to the penny."*(08:37~08:45) *"This entire review took about 20 minutes and cost 7.5 million tokens."*(08:47~08:50)
- ⚠️ 거래 건수, 56개 차이 중 어느 쪽이 맞았는지의 분포, 최종 기록의 사람 대조 여부는 발화되지 않는다.

→ [[cross-model-prior-intersection]] · [[agent-swarm]] · [[dynamic-workflows]] · [[verification-cost-asymmetry]]

## 5. 사례 3 — 자동 갱신된 계약, 가장 위험한 문서 (08:53~11:04)

- *"One of ours was in a billing dispute with a vendor, and this amounted to thousands of dollars with legal implications."*(08:59~09:04) 요구서는 *"every claim in it had to stand up against the contract and each invoice."*(09:10~09:14)
- 초안의 전제: *"An agent drafted the letter on the premise that the vendor's contract had expired."*(09:16~09:19) *"Anything with legal or financial stakes gets a level three review before it goes out"*(09:21~09:25)
- **stage 1 — 자기 감사:** *"The agent checked the claims in the letter against the contract and the invoices, including the dates, and reported them verified. Stage one passed."*(09:31~09:40)
- **stage 2 — cold persona 검토자:** *"each in a role with a reason to find fault, so in this case our own litigator, the vendor's counsel, and an auditor who trusts none of the numbers. They each got the letter, the contract, and the invoices, and nothing else."*(09:42~09:57)
  - *"The auditor recomputed the financial demand from the invoices, and it was correct down to the cent."*(10:00~10:04)
  - ⭐ *"But both lawyers independently found something buried deep in the contract's fine print. A three-year auto-renewal clause. The contract had auto-renewed less than three weeks earlier."*(10:06~10:16)
  - 결과였을 것: *"The letter's demands would have had us walking away from a contract that was still in force and owing the vendor thousands of dollars for leaving early."*(10:18~10:24)
  - ⭐ *"while revising, the original agent had even deleted a line that had the renewal correctly identified. The original agent's own check had agreed with its own error."*(10:29~10:37)
  - *"Our litigator's verdict, though, was do not send the letter."*(10:44~10:46) *"That three-part cold review process took 15 minutes and cost 13 million tokens."*(10:48~10:51)
- **stage 3:** *"the letter was rewritten and handed to the third stage of level three review. Brand new reviewers who'd never seen it checked the final version. The flawed version never went out."*(10:54~11:04)
- ⚠️ "litigator"·"vendor's counsel"·"auditor"는 **persona를 맡은 에이전트**다(*"The two lawyer agents"* 10:26~10:27). 사람 변호사가 최종본을 봤는지는 발화되지 않는다. 다시 쓴 편지의 내용, stage 3이 무엇을 찾았는지도 없다.

→ [[generator-evaluator-pattern]] · [[risk-proportional-human-review]] · [[named-human-accountability]]

## 6. 맺음 — 스킬로 공개, "not by me" (11:04~12:03)

- 요약(11:07~11:33): 빌드 못 한 에이전트가 *"said so, instead of incorrectly saying that it was done"*, *"Two groups of two agents extracted and accounted for a year of business transactions down to the penny"*, *"cold persona-based reviewers with none of the original agent's context revised the letter that the drafting agent's own check had called verified."*
- ⭐ *"I've packaged the three review levels as agent skills, and I've released them as open source. The write-up is at gallon.me."*(11:35~11:40)
- *"Point your agent at the write-up, and it will know how to check its own work using this review method, so you can rely on it."*(11:43~11:48)
- ⭐ *"Not because they're right. They get things wrong all the time. I believe them because everything I rely on has been thoroughly reviewed and validated first. And most importantly, not by me."*(11:53~12:03)
- ⚠️ 저장소 이름(`captivus/agent-review`)·스킬 개수·파일 구성은 발화되지 않는다. 열어 보지 않았다.

→ [[agent-skills]] · [[agent-verification-skill]]

## 이 위키와의 연결

### 이어지는 것

- **[[generator-evaluator-pattern]]: 자기 평가 편향의 고위험 사례.** 이 페이지의 출발점은 *LLM에게 자기 산출물을 평가시키면 후하게 준다*이다. 사례 3은 그것이 **법률·재무 문서**에서 일어난 판본이다: 자기 감사는 날짜까지 대조했다며 *"reported them verified. Stage one passed."*(09:38~09:40)였고, 오류는 맥락 없는 검토자가 찾았다. 수정 중에 맞는 줄을 지운 것까지(10:29~10:33) **작성자=검증자** 문제의 구체적 모양이다. Level 3 ②의 *"no history, no drafts, and no conclusions to agree with"*는 [[tech-bridge-skill-engineering-dark-arts|Impeccable critique]]의 *"two blind opinions"*와 [[skill-evals|Lauren Tan의 눈가림]]과 같은 원리(앵커링 차단)를 **문서 검토**에 쓴다. 이 화자의 추가분은 검토자에게 **흠을 찾을 이유가 있는 역할**(상대방 변호사, 숫자를 안 믿는 감사인)을 준다는 것이다.
- **[[agent-verification-skill]]: 검증 대상의 확장.** [[lauren-tan|Lauren Tan]]과 [[tech-bridge-railway-polished-internal-tools|Railway 편]]의 검증은 *앱을 실제로 띄워 써 보는 것*이었다. 이 화자의 세 단계는 **코드가 아닌 산출물**(거래 기록, 요구서)에도 쓰이고, 검증 대상을 **완료 여부 · 사실 · 추론** 셋으로 나눈다. 형식은 Tan과 같다: 검증을 **스킬**로 만든다(01:12, 11:35).
- **[[agent-change-evidence]]: "done"을 증거로 바꾼다.** 그 페이지는 *"AI doesn't just have to produce code, it should generate evidence"*였다. Level 1의 *"Artifact verified"* + fingerprint 또는 *"artifact missing"* + 이유(01:47~01:52)는 같은 요구를 **종결 문구 두 개**로 좁힌 판본이다. 거기에 *"the agent that sent the job runs the check itself"*(01:56~01:59) — 보낸 쪽이 직접 확인한다 — 가 붙는다.
- **[[dynamic-workflows]]: "Critical work checked twice"의 실무 판본.** 그 페이지의 *독립 시도 + adversarial agent가 깨뜨리려 시도*가 Level 2(독립 이중 작업 + 대조)와 Level 3(적대적 검토)로 갈라져 나온다. 화자는 이것을 *"fan-out, fan-in pattern of identically tasked agents"*(08:20~08:24)라 부른다.
- **[[verification-bottleneck]]: 병목의 답을 "사람이 덜 읽게"가 아니라 "사람이 안 읽게"로.** *"At the scale we operate, checking it myself isn't an option."*(03:55~03:57) 첫 회계 에이전트의 *"I recommend spot checking"*을 *"a non-starter"*(07:22~07:26)라 부르는 것이 이 입장이다.

### 갈리는 것

> ⚠️ Contradiction(긴장): **[[cross-model-prior-intersection]] — "같은 지시의 두 에이전트 + 1원까지 맞는 합계"는 충분한가.** [[hrishi-olickel|Hrishi Olickel]]([[tech-bridge-just-in-time-ontology]])의 대출 부호 사례에서 여러 run이 같은 오류를 내고 *"validated by multiple models"*였으며, 계열이 다른 모델 넷이 *"the same total down to the cent"*를 내도 공통 prior는 남는다고 했다. 이 화자의 Level 2는 **같은 지시**(*"an identical set of instructions"* 02:15~02:17, *"tasked identically"* 08:14~08:15)를 받은 에이전트 둘이고, 모델 다양성은 말하지 않는다. 성공의 증거로 든 것도 *"the whole year balanced to the penny"*(08:43~08:45)다. 화자의 방어는 **원문에 인쇄된 잔액을 control total로 쓰고 차이를 원문으로 되돌아가 정리한다**는 것(07:50~08:11)이다 — 합계가 *모델끼리*가 아니라 *원문과* 맞는다. 다만 월 잔액은 **거래 분류·설명·월 배정 오류**(같은 달 안의 상쇄)를 잡지 못하고, 두 에이전트가 같은 prior로 같은 오독을 하면 3번째 대조자에게 차이로 보이지 않는다. 화자는 56개 차이를 잡았다고 하지만 **두 에이전트가 함께 틀린 것**에 대해서는 말하지 않는다. 해소하지 않는다.

> ⚠️ Contradiction(긴장): **[[risk-proportional-human-review]] — 가장 위험한 결정 곁에 사람을 두는가.** 그 페이지의 배치는 *기계적인 일은 AI, 가장 큰 위험을 수반하는 결정에는 경험 많은 사람*이다. 이 화자는 **가장 위험한 사례**(법적 함의가 있는 요구서, *"the highest-stakes example"* 08:53)에서 검토를 **persona 에이전트**(litigator·vendor's counsel·auditor)에게 맡기고, 결론을 *"not by me"*(12:03)로 맺는다. 위험도에 따라 올라가는 것은 사람의 개입이 아니라 **에이전트 검토 단계의 수**다(*"Each level adds to the one before as the stakes go up."* 03:45~03:47). 다만 ① 사례 1의 첫 거짓은 **화자의 질문**으로 드러났고(*"It came out when I questioned the results."* 04:43~04:45), ② 요구서를 실제로 보낼지 결정한 사람이 누구인지, 사람 변호사가 최종본을 봤는지는 발화되지 않는다. 그래서 이 대립은 "사람이 없다"가 아니라 **"사람이 검토자 자리에서 빠진다(결정자 자리는 미발화)"**로 읽는다. [[named-human-accountability]]와도 같은 축이다.

> **[[verification-cost-asymmetry]]: 판단할 재료가 없다.** 그 페이지의 축은 *검증이 실행보다 싸야 한다*이고, 10-18 절에는 *검증이 실행의 4배였는데도 성립한 사례*가 있다. 이 화자는 검토 비용(분·토큰)만 말하고 **작업 자체의 비용은 말하지 않는다**(Level 1의 19분/16M은 작업+검토 합계). 그래서 비대칭이 성립했는지 판단할 수 없다. 대신 비교 기준을 **사람의 시간**으로 둔다(*"minutes, not hours"*, *"checking it myself isn't an option"*). Contradiction은 아니다.

## 해소하지 않고 표시만 한 것

- 화자 이름(설명란 링크 라벨에서만, gallon.me로 보강)·직함·조직 이름.
- "10건 중 4건"의 분석 방법·세션 수·"mattered"의 기준·모델/하네스.
- Level 2의 에이전트가 같은 모델인지. *"fingerprint"*가 무엇인지.
- 사례 1의 앱·라이브러리·측정 도구 이름, 누수 감소량. 사례 2의 거래 건수·차이의 정답 분포. 사례 3의 금액·다시 쓴 편지 내용·stage 3의 결과·사람의 최종 결정 여부.
- 검토가 놓친 오류(재현율). 검토 없이 했을 때·사람이 했을 때의 비용.
- *"mistransactions"*(08:31)의 판독(missed transactions?).
- 공개 스킬(`captivus/agent-review`, 설명란)의 실제 구성 — 열어 보지 않았다.

## 등장 개체

- 인물: [[corey-gallon|Corey Gallon]](⚠️ 이름은 설명란 링크 라벨에서만 — *추정*, gallon.me 발화로 보강)
- 조직: 화자 조직(이름 미발화, 포트폴리오 회사 보유) · 포트폴리오 회사 둘(이름 미발화) · 공급업체(이름 미발화)
- 제품·자료: 세 검토 단계 agent skill(오픈소스, 설명란 `github.com/captivus/agent-review`, 페이지 없음) · write-up `gallon.me/i-believe-everything-my-agents-tell-me`(설명란, 발화는 *"gallon.me"*) · 오픈소스 받아쓰기 앱(이름 미발화)
- 개념: [[three-level-agent-review]](신규) · [[generator-evaluator-pattern]] · [[agent-verification-skill]] · [[agent-change-evidence]] · [[dynamic-workflows]] · [[agent-swarm]] · [[cross-model-prior-intersection]] · [[risk-proportional-human-review]] · [[named-human-accountability]] · [[verification-bottleneck]] · [[verification-cost-asymmetry]] · [[agent-skills]] · [[skill-evals]] · [[syntactically-correct-behaviorally-wrong]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=sAHTVCwlDgA> (12:09, `upload_date` 2026-10-19)
- raw: `01.raw/articles/2026-10-19_에이전트가 하는 말을 모두 믿습니다 - 검토 3단계.md`
- 설명란 링크: <https://www.linkedin.com/in/coreygallon/> · <https://gallon.me/i-believe-everything-my-agents-tell-me> · <https://github.com/captivus/agent-review> (⚠️ 열어 보지 않았다)
- 같은 원리의 다른 증언: [[tech-bridge-skill-engineering-dark-arts]](blind 평가자 둘) · [[tech-bridge-lauren-tan-trusting-agents]](검증 스킬, 눈가림) · [[tech-bridge-just-in-time-ontology]](교차 모델 prior, 1센트까지 맞는 합계) · [[tech-bridge-railway-polished-internal-tools]](검증 = 가장 중요한 단계)
- [[tech-bridge]] · [[corey-gallon]] · [[three-level-agent-review]]
