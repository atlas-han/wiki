---
title: "Tech Bridge — 샘 알트만이 OpenAI와 일상을 운영하기 위해 AI를 실제로 활용하는 방법 (DevDay 2026 대담): Dots·Space·Decisions API·Ultra-fast, 르네상스 대 산업혁명"
type: source
tags: [openai, sam-altman, devday, persistent-agent, dots, space, live-documents, decisions-api, jev, system-1-model, inference-speed, bring-your-own-subscription, platform, startups, ai-jobs, agent-swarm, members-only, video]
source-url: https://www.youtube.com/watch?v=wrii8VocfZU
source-type: video
author: Tech Bridge (한영자막 재배포) · 대담 [[sam-altman]] × 진행자 "Dan"([[dan-shipper|Dan Shipper]] — 성·소속 Every는 설명란에만) · OpenAI DevDay 2026 키노트 당일, 라이브 관객
date-published: 2026-10-04
ingested: 2026-10-09
created: 2026-10-09
updated: 2026-10-09
---

# Tech Bridge — 샘 알트만이 OpenAI와 일상을 운영하기 위해 AI를 실제로 활용하는 방법 (DevDay 2026)

[[tech-bridge|Tech Bridge]]가 재배포한 **31:27 대담, Q&A 없음, 공식 챕터 14개.** [[openai|OpenAI]] **DevDay 2026 키노트 당일**, 라이브 관객 앞에서 진행자 "Dan"(설명란 링크로 [[dan-shipper|Dan Shipper]]·Every로 판독)이 [[sam-altman|Sam Altman]]을 인터뷰한다. 이 위키에서 Altman이 직접 말하는 소스로는 여섯 번째이고(3부작·G20·Dreamforce 다음), **처음으로 Altman이 자기 업무에 AI를 어떻게 쓰는지를 일화 단위로 말한다.** 중심은 그날 출시한 상시 가동 에이전트 [[openai-dots|Dots]](신규)와 협업 도구 [[chatgpt-space|Space]](신규), 그리고 속도 — *"ultra fast"* 로만 프롬프트한다는 고백과 *"IQ 가격 인하 다음은 속도의 민주화"* → [[inference-speed-as-capability]] (신규).

> **사람들은 훨씬 더 많은 것을 원하고, 기준은 그 어느 때보다 높다. AI는 산업혁명(기계 중심)이 아니라 르네상스(사람 중심)여야 한다 — 그래서 플랫폼을 열고, 구독을 들고 다니게 하고, 1~2인 회사가 할 수 있는 일을 다시 따진다. Altman 자신에게 그 르네상스의 첫 체감은 Dot이 돌려준 아침 시간이고, 다음 축은 지능의 가격에 이은 속도의 가격이다.**

> *"developers, they've never been able to do more, but there's never been a higher bar either"* (00:34~00:40) · *"the dots the new thing we launched today is the first thing that has given me back control of my mornings"* (08:15~08:24) · *"software was really not designed on the whole for collaborating with AI"* (15:42~15:45) · *"there are way more good ideas outside of our building than inside"* (21:41~21:46) · *"bringing down the like price of IQ (…) Now there's this new vector that is clearly going to be very important of speed"* (29:42~29:58)

ASR·ko 보정: ko가 제품 이름을 일반 명사로 옮긴다 — **Space → "우주"**(15:27, 16:12), **Dot → "담당자"·"상사"·"팀원"**(09:46, 14:20, 16:36, 17:04), **Jev → "새롭게 떠오르는 인물"**(18:52), Codex → "코덱". ⭐ **ko가 Jev 대목을 뒤집었다** — *"it's pretty different and I don't think we can go (…) we have other things to go do"*(20:19~20:31)를 **"상당히 다르고 … 크게 다르지 않다"** 로. *"a big seven production"*(09:33, ⚠️ "big SEV in production"으로 판독)을 ko는 **"빅 세븐 프로덕션과 함께 작업"** 으로 지어냈고, Y Combinator는 **"YMCA"**(25:15). en-orig는 ChatGPT를 *"ChachiBT"*, Codex를 *"codecs/codeex"*, Pareto를 *"paro"* 로 들었다. **이번 `en` 파일은 en-orig와 바이트 단위로 같아** 독립 판독 근거가 없다. 전체 목록은 raw. **인용은 en-orig에서만** 했다.

> ⚠️ **멤버십 전용 → 공개.** 2026-10-02에 멤버십 전용으로 확인돼 건너뛰었고([[tech-bridge]] *"멤버 전용 대기"* 목록), **2026-10-09 공개 확인.** `upload_date`는 공개 후 **2026-10-04**로 바뀌어 있다(멤버십 확인일보다 늦다).
>
> ⚠️ **행사·시점.** *"it's dev day"*(02:23), *"I've been at all four dev days"*(02:29~02:32), 설명란 slug *"openai-devday-2026"* → **DevDay 2026, 키노트 당일 녹화.** 날짜는 발화되지 않는다 — **2026-10-02 이전**만 확정.
>
> ⚠️ **화자 표지 `>>` 가 부정확하다** — 질문과 답이 한 캡션에 붙고(00:42), 같은 화자 안에 표지가 끼며(08:29), 표지 없이 화자가 바뀐다(03:16→03:18, 20:19). 아래에서 화자를 가른 곳은 문맥 판독이고, **애매한 곳은 표시했다**(raw 헤더).
>
> ⚠️ **판매자의 무대 진술이다.** 출시 당일 자사 제품을 CEO가 말하고, 진행자는 베타 참여자이자 Jev를 *"사내 빌드 방식을 바꾼"* 것으로 소개하는 이해당사자다. 반대 심문이 없다. 수치는 거의 없고, 있는 것(22개 출시·10,000 에이전트·8배/100배)은 조건이 없다.

## 1. 수요는 사람에게서 온다 (00:00~02:44)

- 진행자: 4년 전이었다면 DevDay에 개발자가 별로 없을 줄 알았는데 *"there's more developers than ever"*(00:08~00:12).
- Altman: *"people just want so much more stuff. People's expectations are so high"*(00:25~00:28). 일자리에 대해 *"never like as doomery about the job stuff as other people"* 이었지만 그래도 **잠재 수요의 크기**와 *"how much like people have remained at the center"* 에 *"on the upside"* 로 놀랐다(00:44~01:01).
- 한계는 있다 — *"some areas of work where there's actually not much creativity required and we don't care about the person doing it and many of those tasks or jobs will be done by AI"*(01:07~01:20). 그러나 *"no shortage of new things"*.
- 왜 사람 중심인가: *"we just we don't care that much about what the machines do (…) we're obsessed with other people"*(01:34~01:42).
- ⭐ **나비에-스토크스, 4일.** 진행자의 농담 *"if an agent solves a Navier Stokes in a data center but no one finds out, did it really solve it?"*(01:56~01:59)에 이어 — *"10,000 agents worked super hard for 4 days in perfect coordination with each other and did this amazing thing and almost none of the public reaction was about that actually the problem being solved"*(02:03~02:14). 반응은 *해석*과 *관련된 사람들* 이야기였다. ⚠️ 표지 없음 — Altman으로 읽는다(raw). → [[agent-swarm]] · [[ai-formal-verification]]

→ [[ai-jobs-impact]]

## 2. 22개 출시, 플랫폼, 르네상스 (02:23~07:37)

- 진행자 집계 *"by my account 22 new things today"*, 작년 약 9, 재작년 4~5(02:26~02:36). Altman: *"just wait for next year"*, 키노트 *"50 minutes"* 에 맞추려 여럿 뺐다(02:43~02:46). 이유 — *"we try to practice what we preach (…) we better build more ourselves"*(02:49~02:59).
- 새 병목 질문에 답은 두 방향(03:18~04:08): ① **상시 지능** — *"persistent intelligence, active intelligence, whatever people want to call it"*, *"agents that are running in the background 24/7 connected to your systems doing stuff proactively for you"* ② **생태계 개방** — 부족한 것은 아이디어가 아니라 *"the creative spirit to figure them out and build them"*, 그래서 ChatGPT 안에 앱, *"bring their subscription wherever they'd like"*, 마켓플레이스.
- 진행자: Bill Gates의 Windows — *"create more value than you capture"*(04:16~04:20). Altman: *"we clearly have not yet figured out the app store equivalent"*, 그러나 플랫폼은 됐다(04:35~04:45).
- **두 학파**(04:45~05:18): *"only going to be one company in the world"* 를 믿거나 바라는 쪽 vs *"a renaissance in the number of companies (…) one person companies, small team companies"* 를 믿는 OpenAI.
- **르네상스 대 산업혁명** — *"the Renaissance was fundamentally centered around people and the industrial revolution was fundamentally centered around machines"*(05:48~05:56). 산업혁명은 사람을 *"this like cognitive machine doing some extremely specialized thing"* 으로 바꿨다(06:23~06:28). *"house cats"* 미래론이 슬프다(06:32~06:41). 바라는 것: 과학·예술·창업의 물결, 그리고 *"people get to back in control of their lives"*(07:07~07:09).

## 3. Dots — 아침을 돌려준 상시 가동 에이전트 (07:39~15:27) → [[openai-dots]] (신규)

Altman이 르네상스의 *"very trivial example"* 로 꺼낸다(08:09~08:15).

| 일화 | en-orig |
|---|---|
| ⭐ **아침 시간.** 이른 아침이 *"maximum creativity"* 시간이었는데 큰 회사를 운영하며 밤새 일이 터지고, 폰을 보면 *"I polluted my brain"*, 안 보면 한 시간 사이 재난이 커졌다. 이제 *"I trust my dot to go have good judgment about what I need to think about, not think about if there's something very urgent, otherwise handle things for me"* — 그 시간에 창작하거나 아이들과 논다 | 08:26~09:15 |
| ⭐ **키노트 5분 전.** 키노트 중 *"a big seven[=SEV?] production"* — 라이브 데모·동시 배포의 위험. Tibo(성 미발화)의 Dot이 5분 전에 *"I see that you're in the dev day keynote (…) I know what the demo is because I was able to like look at the presentation um in space (…) this sub is probably going to make the demo not work. Would you like me to try to fix it?"* — 고치지는 못했다, *"maybe the next version we'll be able to go fix that in prod"* (⚠️ Altman이 전하는 제3자 일화) | 09:33~10:11 |
| **이 대담 직전.** Dot이 *"You have one little break between now and this thing you're going to go to with Dan. you have to pay attention to this one thing"* | 10:27~10:37 |
| **이름.** Altman의 Dot은 *"Doie"*(전엔 *"Alfred"*, 많은 사람이 *"Doy"* 라 부른다), 진행자 것은 *"Boo"* → [[agent-persona-naming]] | 10:43~10:54 |
| **기본값.** *"It has become the default way that I use chat"* — 진행자 *"Me too"*. 진행자: 베타에서 *"a little bit buggy"*, 모바일 등 여러 표면, *"its own cloud computer"*(⚠️ 화자 미확정). Altman: *"better rapidly each week (…) going to definitely take some time to smooth it all out"* | 10:58~11:31 |
| **진행자 일화.** 항공편 변경 중 *"you have a meeting during this flight"* — 캘린더에 없고 Slack에서 읽은 것. → *"bring context together from across your entire life"*(⚠️ 화자 미확정) | 11:32~11:57 |
| ⭐ **연구 측 조건.** *"maybe most important was Astra. (…) you needed a smart enough model (…) getting the model over the intelligence bar was a key part"* → [[openai-astra]] | 12:01~12:15 |
| ⭐ **고용으로도 못 했을 결정.** 설명하기 어려운 새 기능 — 산책 중 메모를 Dot에 던지면 *"the dot went off and built like five or six versions"*, 피드백·반복. 잠들며 긴 음성 메모를 남기면 *"wake up in the morning and not only is the thing built, but it like went off and did like the next seven steps"* | 12:15~13:44 |
| ⭐ **포기했던 검색.** *"Slack search is obviously terrible. So I mostly use codecs[=Codex] to search it"* — 10~20분 실패, *"codeex doesn't usually fail"*. 다음 날 Dot이 *"I noticed you were trying to do this thing and you didn't find it but I like kept thinking about it overnight and I found it for you"* — 텍스트가 아니라 **스크린샷**이었고, *"looked at like image every screenshot"* | 13:46~14:44 |
| **주의 해킹.** *"the kind of like crazy attention hacking of social media and phones and notifications had gotten way worse than I realized for me personally"* — 몇 주 써 보고 안 것 | 14:59~15:23 |

**이 위키에서 Dots가 놓이는 자리.** 09-06 Altman의 *"능동적 컴퓨터"*, 09-23 Dreamforce의 *"세 번째 단계의 문턱"* 이 **이름 붙은 제품**이 됐다 → [[persistent-agent-teams]]. 같은 범주의 앞선 사례는 Meta [[muse|Muse]]([[tech-bridge-zuckerberg-muse-in-daily-use]]) — 이름 짓기·먼저 제안·밤새 정리가 겹친다 → [[agent-persona-naming]] · [[proactive-idea-feed]] · [[nightly-memory-consolidation]]. ⚠️ **권한·감사·프라이버시는 한 마디도 없다** — Dot은 Slack 전체·캘린더·발표 자료를 읽고, *"fix that in prod"* 를 다음 버전 목표로 말하는데도. [[ai-privilege]](09-06 Altman 자신의 제안)도 나오지 않는다.

## 4. Space — 살아 있는 문서 (15:27~18:44) → [[chatgpt-space]] (신규)

- 진행자: *"a big bet to do three like office suite type tools in one launch"*(15:30~15:33). Altman: 하려던 게 아니었다 — *"software was really not designed on the whole for collaborating with AI"*, 혼자 쓰거나 AI가 대신 쓸 수는 있지만 *"multiple people and multiple people's AIs all working together like a lot of the current abstractions we have break down"*(15:42~16:03).
- 쓰는 법: 새 아이디어는 *"writing the oldfashioned way because it helps me like think about it"*, 후속은 Dot이나 다른 사람의 Dot이(16:29~16:40).
- ⭐ **live documents** — *"I don't think we have a word for this yet"*, *"a doc that is going to automatically update as people interact or as other things change in the world"*, *"seven people's dots can working together create something new that kind of existed in all of our heads to some degree but was like an emergent thing"*(16:42~17:12).
- 예: 공유 대시보드 대신 *"a changing summary of the business just for me"* — Slack 메시지를 다 보고 계속 갱신(17:18~17:48).
- ⭐ **요즘 관심사** — *"how we're thinking about the safety alignment and security challenge in front of us"*, 6개월 전엔 *"revenue and growth and metrics"*(17:50~18:03). Dot이 매일 무엇을 가장 중요하게 본다고 생각하는지를 *"over the course of years"* 시각화하고 싶다(18:07~18:21). 진행자는 *"a live dashboard of my mood"* 를 원한다(18:22~18:41).

→ [[multiplayer-agent-context]]

## 5. Decisions API와 Jev — 경쟁 연구소의 System 1 모델을 OpenAI CEO가 말하다 (18:44~20:48)

- 진행자: *"the decisions API is one of the sneaky most important things today because Jev is this new hot thing that has honestly changed how we think about building things internally"* — Jev에서 시작했나, 원래 있었나(18:47~19:03).
- Altman: *"Do uh used to work at open and um do is awesome and he was talking about this class of ideas for a long time"*(19:04~19:12) · *"Diego has inspired me for a long time on thinking about this"*(19:45~19:47). ⚠️ **ASR 이름** — 이 위키는 [[diogo-almeida|Diogo Almeida]](OpenAI 출신, 현 [[typesafe-ai|TypeSafe]], 09-19 편 en-orig *"Diego Mida"*)로 판독한다.
- **Luna**(⚠️ 미판독 모델명)의 1순위 요청은 *"I want it to be even cheaper and even faster"*(19:27~19:30). *"seeing the response to Jev made us more excited to prioritize things in that direction"*(19:37~19:43). 방향: *"make the technology super fast and super low cost for common use cases"*(19:53~20:00).
- ⭐ **네오랩 질문**(20:02~20:19)에: *"As I understand the approach of Jev, it's pretty different and I don't think we can go (…) maybe we could go do something from scratch like that but I think we have other things to go do"* — OpenAI는 *"the best cheapest fastest most capable model at every point on the paro[=Pareto] curve of cost and speed and modality"*, *"new architectures new technologies that are things we just can't cover all of but for the (…) mainline workhorse like we will try to deliver that"*(20:19~20:48).

**읽기.** [[jev|Jev]]와 [[system-1-model]]은 지금까지 **TypeSafe 본인(09-19)과 파트너 LangChain(09-25)** 의 말로만 이 위키에 있었다. **처음으로 경쟁 프론티어 랩의 CEO가 이름을 부르고, 사용자(Every)가 사내 채택을 말한다.** 그러나 Altman의 답은 **"우리는 Jev를 만들지 않는다 — 주력 모델을 더 싸고 빠르게 한다"** 이다. ⚠️ **Decisions API가 무엇인지(타입 출력·확률·별도 모델 여부)는 대담 어디에도 없다** — 챕터 제목이 그 공백을 *"최고 가성비/속도 모델"* 로 덮었다. 그리고 ⚠️ ko는 바로 이 대목을 *"크게 다르지 않다"* 로 뒤집었다.

## 6. 앱·구독·스타트업 (20:48~27:54)

- 진행자: *"Codex native apps"* 를 졸랐는데 *"You finally did it"*, *"plug-in extensions"*, 그리고 ⭐ *"being able to bring your tokens from your CHT[=ChatGPT] subscription to an app developer"* — 앱 개발자는 *"how much AI can I let my users use so that it doesn't bankrupt me?"*, 싼 모델 → 나쁜 경험의 딜레마였는데 *"great, you can use whatever model you want under your subscription"*(20:51~21:21). → [[bring-your-own-subscription]] (신규)
- Altman: 가장 기대되는 건 *"the ones that we haven't thought of"*, *"way more good ideas outside of our building than inside"*(21:29~21:46). 구독 이동은 *"we just want that ourselves"* — *"I hate having to sign up for 100 subscriptions"*, *"it's your subscription (…) you should get to use wherever you want"*(22:16~22:44).
- *"I've never seen startups get as successful this quickly"*(23:04~23:08), *"I would love to be a startup investor again"*, *"a golden age"*(23:19~23:32). 투자 원칙은 늘 *"find the absolute best founders I can that are working on the ambitious projects"*(23:46~23:54).
- *"OpenAI just killed X startup"* 트윗은 *"works because people like doomerism but it never actually happens"*(24:03~24:10). 이유: *"we're going to give you all of the same tools we use"*(24:22~24:28), *"like fire or something (…) maybe we like brought it down from the mountain but we want to give it to everybody"*(24:57~25:08).
- **스타트업 통념 재검토** — 진행자: 공동 창업자 필수, YC 투자 구조는 *"based on a previous (…) cost structure"*(25:08~25:21). Altman: 불변은 *"make something people want"*, 그러나 *"how much work you can get done with one person or two people (…) feels totally different and I don't think there has been enough re-examination of that in the sort of startup conveyor belt of Silicon Valley yet"*(25:26~26:03).
- **CEO가 만든다** — *"we are not a gigantic company (…) maybe the big tech companies have like a hundred times more people than we do"*(26:16~26:25), *"if you lower friction a little bit people build way more"*(26:29~26:35). Dots로 *"I hope I launch something to the world"* — 플러그인 확장, 혹은 *"maybe I'll ship a real OpenAI product"*(26:47~27:12). 22개 출시도 *"we could not have done all of this stuff without having AI to help us"*(27:37~27:43).

## 7. Ultra-fast — 속도가 다음 축이다 (28:02~31:27) → [[inference-speed-as-capability]] (신규)

- 진행자: *"Do you do all your prompting on ultraast[=ultra fast]?"* — *"I do."*(28:02~28:05). Altman의 걱정: *"we kind of get out of touch with people building on our tools"*, 모두가 늘 쓸 수는 없다는 걸 알지만 *"I have such a hard time dragging it back over"*(28:09~28:29).
- ⭐ 왜: Bret Victor(⚠️ 강연명 미발화)의 *"creators should have an immediate connection to what they're creating and how speed and the feedback loop was so important"* — *"I did not realize what a difference that makes to my kind of iterative thinking loop"*, *"it's like a wild difference"*(28:42~29:18).
- 진행자: ultra fast 세계, *"the Astra is a more expensive model world"* — 더 좋은 지능에 더 내는 것(29:26~29:36).
- ⭐ Altman: 지금까지 *"bringing down the like price of IQ"*, 이제 *"this new vector that is clearly going to be very important of speed"*. *"our own chip is going to be an incredible contributor to letting us get very fast inference in the hands of everybody"*, *"invest in the democratization of this like we have for model intelligence"*(29:38~30:17).
- *"You can pay us for it and do it now"*(30:25). *"8x at a great price in the notistant future, but then we'll have 100x faster and (…) GPT7 Galaxy or whatever"*(30:29~30:41, ⚠️ 마지막은 농담조). 구조: *"there will always be a real frontier in terms of intelligence or speed or whatever else at a higher price"*, 동시에 *"put Moore's law to shame, relentless focus on driving value per dollar up"*(30:47~31:12).

→ [[intelligence-abundance]] · [[compute-constrained-growth]]

## 이 위키와의 연결

### 이어지는 것

- **[[persistent-agent-teams]]** — 09-06 *"능동적 컴퓨터"*·09-23 *"세 번째 단계의 문턱"* 이 **출시된 제품(Dots)과 CEO의 사용 일화**가 됐다. *"팀이 아니라 하나의 상시 에이전트"* 라는 09-06의 독해도 맞다 — 다만 Space에서는 **여러 사람의 Dot이 함께** 일한다.
- **[[muse]] · [[agent-persona-naming]] · [[proactive-idea-feed]] · [[nightly-memory-consolidation]]** — Meta Muse 두 편(09-17)과 같은 범주. 이름 짓기가 양쪽 다 화제가 됐다(Agrippa·Pip ↔ Doie·Alfred·Boo). *"kept thinking about it overnight"* 은 Muse의 *밤사이 정리* 와 닮았지만 **기억 압축이 아니라 미해결 작업의 계속**이다.
- **[[jev]] · [[system-1-model]] · [[diogo-almeida]]** — 경쟁 랩 CEO의 첫 언급, 사용자(Every)의 사내 채택 진술. 그리고 **OpenAI는 같은 것을 만들지 않고 주력 모델의 비용·속도로 답한다**는 입장.
- **[[agent-swarm]] · [[ai-formal-verification]]** — 09-20 [[greg-brockman|Brockman]]의 *1만 개 에이전트·나비에-스토크스* 와 09-23 Altman의 *"7대 난제 중 하나"* 가 **한 대화 안에서 이어졌다**(문제 이름은 진행자, 규모·기간은 Altman). **기간 4일은 처음.** Lean 형식화는 여기서도 나오지 않는다.
- **[[openai-astra]]** — Dots의 연구 측 핵심 조건이 Astra(*"over the intelligence bar"*). 진행자는 Astra를 *"more expensive model"* 로 부른다 — 09-06 *"더 비싸고 큰 모델 등급"* 과 같다.
- **[[codex]]** — CEO가 **Slack 검색 도구로** Codex를 쓴다(*"doesn't usually fail"*), 예전 사이드 프로젝트도 Codex로. DevDay에 Codex 네이티브 앱·플러그인 확장.
- **[[ai-jobs-impact]]** — *"never as doomery"*, 잠재 수요가 예상보다 컸다 — 09-06 *"두 마음 — 예상보다 적었다"* 와 같은 방향의 반복.
- **[[intelligence-abundance]]** — 09-07 *"전기처럼 싸진다"* 의 형평 논거에 **두 번째 축(속도)** 이 붙었다.

### 갈리는 것

> ⚠️ **Contradiction: '집중' 대 '22개 출시'.** 09-06 Altman은 지난 12개월 *"사이드 퀘스트가 너무 많았다 — 대부분 제 잘못"*, 09-20 [[greg-brockman|Brockman]]은 *"올해의 주제는 '집중'"*·Sora 취소·*"단일 통합 스택"* 이라 했다([[openai]]). 이 대담은 **하루 22개 출시**(진행자 집계), **오피스 스위트형 도구 3종**(Space), 앱 마켓플레이스, CEO 본인의 *"plug-in extension"* 계획을 말한다. Altman은 이를 *"practice what we preach"* 와 *"AI 덕에 가능했다"* 로 설명할 뿐 **'집중'과 어떻게 양립하는지 말하지 않는다.** (위키의 독해: 출시물 대부분이 Dots·Space·구독·앱으로 **ChatGPT 한 표면**에 묶여 있다는 점이 *단일 스택* 과 맞을 수는 있다 — 화자의 말은 아니다.)

> ⚠️ **상시 에이전트의 권한·프라이버시가 빠졌다.** Dot은 Slack 전체·캘린더·키노트 자료를 읽고, 다음 버전은 *"fix that in prod"* 를 하리라 한다. 같은 CEO가 09-06에 상시 에이전트의 데이터 문제로 [[ai-privilege|AI 특권법]]을 제안했고 09-23엔 HF 사건을 *"정렬 문제"* 로 말했는데, **이 대담에선 권한·감사·승인 경계가 한 번도 나오지 않는다.** 그러면서 요즘 관심은 *"safety alignment and security challenge"* 라고 한다(17:50~17:56). 위키의 표시다.

> ⚠️ **Decisions API의 정체.** 진행자는 Jev와 같은 계열로 소개하고, Altman은 *"Jev 접근은 꽤 다르다, 우리는 그걸 처음부터 하지 않는다"* 고 답한다. **두 말이 어떻게 맞는지(같은 문제를 주력 모델의 싼 등급으로 푸는 API인지)는 소스에 없다.**

## 해소하지 않고 표시만 한 것

- **DevDay 2026 날짜** — 발화 없음. 2026-10-02 이전.
- **진행자 신원** — 자막엔 *"Dan"* 한 번. Dan Shipper·Every는 설명란 링크.
- **"Do"/"Diego" = Diogo Almeida** — 판독. 성 미발화.
- **"Tibo"** — 성·직함 미발화, 판독하지 않음.
- **"a big seven production"·"this sub"** — *SEV in production* 으로 추정.
- **"Luna"** — OpenAI 모델명으로 들리나 이 위키에 기록 없음.
- **"GPT7 Galaxy"** — 농담조, 제품명으로 읽지 않음.
- **8배·100배** — 기준·시점 없음. 자체 칩의 이름·시점 없음(09-06 진행자가 말한 *Jalapeno* 와 같은 것인지 미확인).
- **Bret Victor 강연** — 이름·연도 미발화(*"15 20 years ago"*, 화자 스스로 부정확하다고 함).
- **10,000 에이전트·4일** — 같은 사건 여부는 정황. 문제 이름은 진행자가 꺼냈다.

## 등장 개체

- 인물: [[sam-altman]] · [[dan-shipper]] (신규, ⚠️ 설명란 판독) · [[diogo-almeida]](ASR *"Do"*·*"Diego"*) · Tibo(페이지 없음) · Bill Gates(지나가는 언급) · Bret Victor(페이지 없음)
- 조직: [[openai]] · [[typesafe-ai]](간접 — Jev) · Every(설명란, 페이지 없음) · Y Combinator(페이지 없음) · Slack
- 제품·모델: [[openai-dots]] (신규) · [[chatgpt-space]] (신규) · Decisions API(정체 미상, 페이지 없음) · [[jev]] · [[openai-astra]] · [[codex]](네이티브 앱·플러그인 확장) · ChatGPT 앱·마켓플레이스 · Luna(⚠️ 미판독) · ultra fast(추론 등급, 정식 표기 미확정) · OpenAI 자체 칩
- 개념: [[inference-speed-as-capability]] (신규) · [[bring-your-own-subscription]] (신규) · [[persistent-agent-teams]] · [[agent-persona-naming]] · [[proactive-idea-feed]] · [[nightly-memory-consolidation]] · [[multiplayer-agent-context]] · [[system-1-model]] · [[agent-swarm]] · [[ai-formal-verification]] · [[ai-jobs-impact]] · [[intelligence-abundance]] · [[compute-constrained-growth]] · [[ai-privilege]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=wrii8VocfZU> (31:27, `upload_date` 2026-10-04 · 멤버십 전용 → 공개)
- raw: `01.raw/articles/2026-10-04_샘 알트만이 OpenAI와 일상을 운영하기 위해 AI를 실제로 활용하는 방법입니다.md`
- 설명란 링크: <https://every.to/vibe-check/vibe-check-dots-always-on-agents-in-chatgpt> · <https://every.to/vibe-check/vibe-check-openai-devday-2026> · <https://help.openai.com/en/articles/20001549-getting-started-with-space-in-chatgpt> (⚠️ 열어 보지 않았다)
- 같은 화자: [[tech-bridge-altman-frontier-rl-pause]] · [[tech-bridge-altman-agi-superintelligence]] · [[tech-bridge-altman-astra-hardware]] · [[tech-bridge-altman-g20-economic-boom]] · [[tech-bridge-altman-benioff-dreamforce]]
- 관련 소스: [[tech-bridge-brockman-agi-era-defender-window]] · [[tech-bridge-jev-agent-harness]] · [[tech-bridge-rlhf-assistance-vs-automation]] · [[tech-bridge-zuckerberg-muse-in-daily-use]]
- [[tech-bridge]] · [[sam-altman]] · [[openai]]
