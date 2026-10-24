---
title: "Tech Bridge — 하네스는 더 이상 필요 없을까? AI가 똑똑해져도 남는 3가지 (한국어 해설 + Jediah Katz 강연 발췌): data flywheel, GrokBot에서 되돌아온 가드레일, 인프라 · trust and security · efficiency"
type: source
tags: [harness, harness-pruning, jediah-katz, cursor, grokbot, ai-engineer, data-flywheel, guardrails, long-running-agents, always-on-agents, least-privilege, efficiency, commentary-format, video]
source-url: https://www.youtube.com/watch?v=NUyLH7tjQpg
source-type: video
author: Tech Bridge (한국어 해설, 내레이터 미상) · 발췌 화자 [[jediah-katz|Jediah Katz]](설명란 — 커서에서 AI 에이전트 도구를 만들었던 개발자) · 원본 강연 [[ai-engineer|AI Engineer]] *Smarter Models Killed the Harness. Here's What's Left*(`7Y4sbZgBdnc`, 이 위키에 없음)
date-published: 2026-10-23
ingested: 2026-10-24
created: 2026-10-24
updated: 2026-10-24
---

# Tech Bridge — 하네스는 더 이상 필요 없을까? AI가 똑똑해져도 남는 3가지

[[tech-bridge|Tech Bridge]]가 올린 **8:28, 공식 챕터 10** 영상. 형식은 [[tech-bridge-stripe-collison-cherny-ai-dev-workflow]](10-22)와 같은 **"한국어 해설 + 원본 발췌"** 이고, 원본은 [[ai-engineer|AI Engineer]]에서 [[jediah-katz|Jediah Katz]]가 한 강연 *Smarter Models Killed the Harness. Here's What's Left*(설명란). 화자는 발췌에서 [[cursor|Cursor]]와 [[grokbot|GrokBot]]을 1인칭 *"we"* 로 말한다.

> **(해설의 줄거리)** 하네스 = *"AI가 실제로 일하도록 둘러싼 장치들"*(01:12~01:17). 익숙한 코딩을 도와주던 장치는 data flywheel로 모델에 흡수돼 줄어든다. 그러나 **새 작업**을 맡기면 새 장치가 다시 필요하고, **오래 실행 · 권한 · 비용** 셋은 모델이 배우는 것만으로 없어지지 않는다(08:05~08:16).

> 원음: *"I mentioned how [at] Cursor we found ourselves removing things from the harness, removing prompting, removing guard rails as the models got smarter. But curiously in Grockbot[GrokBot] we've actually found ourselves putting back a lot of these things, adding new prompting, adding new guard rails. And that's because there's a lot of new tasks in this new way of working."*(03:50~04:09)

이 위키에 생기는 것: [[jediah-katz]](신규 — 인물). 기존 페이지에는 [[harness-pruning]]의 **"지웠던 것을 다시 넣는다"(같은 회사의 1인칭 반례)**, [[always-on-agent-architecture]]의 **"노트북은 잠든다"**, [[least-privilege-connectors]]의 **"API 키 파일을 통째로"**, [[grokbot]] · [[cursor]] · [[ai-engineer]]의 새 사례가 붙는다.

**트랙과 인용.** 오디오 `Korean original` + `English (US)`, 메타 `language`=`en`. 받은 **ko = `lang=ko` 원 오디오 ASR**(tlang 없음) — 해설은 ko로 인용. 영어 원음 발췌는 ko 트랙의 영어 조각과 en-orig(영어 트랙, 내레이션은 더빙 추정)를 **대조해** 인용한다. 판독·무캡션 구간 상세는 raw.

> ⚠️ **발췌 11구간 중 4구간이 두 트랙 모두 무캡션이다** — 오프닝 인용(00:13~00:20), 코딩 요령 축소의 근거(01:20~01:45, *"두 연구"* 의 정체 포함), 총괄 AI 그림(03:01~03:27), 사내 버그→배포 사례(04:32~05:02). 이 구간들은 **해설만** 남는다.

## 1. 하네스 = 생각하는 머리를 둘러싼 장치 (00:00~01:20, 해설)

- 도입 질문(해설): *"AI가 더 똑똑해지면 AI에게 일을 시키는 도구는 필요 없어질까요? 코드는 잘 짜는데 메일을 마음대로 보내면 어떨까요?"*(00:00~00:08)
- 정의(해설): *"모델을 생각하는 머리라고 해 볼게요. 생각만 해서는 파일을 고치거나 프로그램을 켤 수 없죠. 어떤 도구를 쓸지, 어디까지 허용할지, 하던 일은 어디에 남길지 정해 줘야 해요. 이렇게 AI가 실제로 일하도록 둘러싼 장치들을 하네스라고 불러요. 한 때는 여기에 코딩 요령도 많이 넣었어요."*(01:00~01:20) → [[harness-engineering]] · [[agent-harness-design]] · [[brain-hands-decoupling]]

## 2. 줄어드는 것 — data flywheel (01:20~03:01)

- (해설) 근거로 *"두 연구"* — *"같은 AI에 서로 다른 작업 도구를 붙여도 시험 점수가 크게 달라지지 않았다"*. 단 *"강연에 나온 코딩, 머신 러닝 시험의 맥락에서 봐야"* 한다(01:45~01:59). ⚠️ 연구명은 무캡션 구간에 있을 수 있다 — 미확인.
- **원음**(02:12~02:31): *"[we] call the data flywheel. So in this process the harness brings harder and harder coding tasks within reach. At that point, more users can productively attempt those tasks with agents. That means more coding data is shared with the labs. And eventually the models learn natively how to do these skills well."*
- (해설) 비유: *"자전거의 보조 바퀴"* — 도구가 어려운 일을 해 볼 수 있게 돕고 *"그 경험이 학습 자료가 돼요. AI가 익숙해지면 보조 코드를 덜 써도 되죠"*(02:43~02:55). → [[harness-pruning]]의 **메커니즘 설명**: 하네스 → 사용 → 랩으로 가는 데이터 → 네이티브 능력. [[ride-the-optimization-trajectory]] · [[sutton-bitter-lesson]]과 같은 축.

## 3. 되돌아오는 것 — 새 작업에는 새 안전장치 (03:01~05:18)

- (해설) *"이제 AI는 코딩창 밖으로 나가요."* 총괄 AI가 작은 일을 다른 AI에게 나눠 주는 그림 — *"역할을 쉽게 이해하기 위한 예"*(03:27~03:41). → [[persistent-agent-teams]]
- **원음** ⑥(03:50~04:09, 위 인용): Cursor에서는 *removing prompting, removing guard rails*, GrokBot에서는 *putting back … adding new prompting, adding new guard rails* — 이유는 *"a lot of new tasks in this new way of working"*.
- (해설) *"메일을 언제 보내도 되는지, 일이 길어지면 언제 알려야 하는지, 이런 문제는 코드를 잘 짜는 것만으로 풀리지 않아요. [새 일]에서 막히는 곳을 도구가 먼저 도와주는 거죠."*(04:14~04:24, ⚠️ *"세일"* ASR → 새 일 추정) → [[agent-attention-management]] · [[action-reversibility]]
- (해설) 사내 사례: *"버그를 찾고 고치고 확인하고 배포 뒤에 지켜보는 일까지 이어져요"*(05:02~05:05, 원음은 무캡션). *"이런 흐름을 맡기려면 AI가 멈추지 않고 일할 수 있어야겠죠."*

## 4. 남는 것 셋 (05:18~07:37)

### ① 오래 실행되는 인프라
- **원음**(05:21~05:40): *"First of all, there is the infrastructure and runed[?] to make an autonomous colleague reliable. Over the past year plus, we've gone from agents that work on a typical task for minutes to hours to days, and even longer. And there's just no way that this can work on one person's laptop which might go to sleep."*
- (해설) *"노트북을 덮어도 일은 이어지고 다시 접속하면 하던 작업을 찾을 수 있어야 해요."*(05:44~05:50) → [[always-on-agent-architecture]] · [[durable-execution]] · [[cloud-agent-delegation]]

### ② trust and security — 권한
- (해설) *"AI가 메일을 쓸 줄 알아도 누구에게 언제 보내도 되는지는 따로 정해야겠죠."*(05:53~05:59)
- **원음**(06:02~06:37): *"a simple harness with just bash and all your, you know, all your API keys in a file can solve coding tasks, but you probably don't want to give all your API keys in a file to the model. Um, or if you're okay with that, I'm sure that your head of security would have something to say. … [at] companies where we want to have permissions that are scoped down to specific agents and specific people but it's also important to have guard rails for anyone who doesn't want to wake up [?]"* — 끝은 판독 불가(해설로 보아 1만 달러 청구서).
- (해설) *"여기서 1만 달러는 위험을 설명하려고 든 예시예요. 실제로 이런 사고가 났다는 보도는 아니에요."*(06:37~06:42, 설명란도 같은 고지) *"AI가 일을 잘 끝냈는지와 필요한 권한만 썼는지는 함께 살펴봐야 해요."* → [[least-privilege-connectors]] · [[credential-injection-outside-sandbox]] · [[agent-sandboxing]]

### ③ efficiency — 비용
- **원음**(06:55~07:04): *"And then finally there's efficiency. If you think back to those two studies I showed where the choice of harness did not make [?]"* — 이후 판독 불가.
- (해설) *"시험 점수가 비슷해도 실제로 쓰는 경험은 달라질 수 있어요. 같은 설명을 되풀이해서 보내는지 작업에 맞는 모델을 고르는지에 따라 시간과 비용이 달라지니까요."*(07:11~07:21) → [[prompt-caching]] · [[model-mixing-economics]]
- (해설) 도구 선택 기준: *"어려운 문제를 푸는 능력과 함께 오래 일하는지 권한을 지키는지 비용을 아끼는지도 보면 좋아요."*(07:23~07:32)

## 5. 전망과 맺음 (07:32~08:28)

- 원음 조각 *"90% agent workun[?] laptop"*(07:42). 설명란: *"'6개월 안에 에이전트 작업의 90%가 노트북 밖에서 실행된다'는 수치는 발표자의 전망입니다."* 해설: *"수치는 현재 사용률이 아니라 발표자의 전망이에요."*(07:58~08:00) ⚠️ **"6개월"은 설명란에만 있다.**
- 맺음(해설): *"익숙한 코딩을 도와주던 일부 장치는 줄어들어요. 그래도 오래 실행하고 권한을 정하고 비용을 줄이는 일은 남아요. 새 일을 맡길 때는 새 도구도 필요하고요."*(08:05~08:16)

## 이 위키와의 연결

### 이어지는 것

- **[[harness-pruning]] — 메커니즘과 균형추를 한 강연이.** 이 위키의 pruning은 Anthropic Claude Code 팀 증언(todo · AskUserQuestion)에서 왔다. Katz는 **왜 지워지는지**(data flywheel)와 **왜 다시 생기는지**(새 작업)를 같은 회사의 두 제품(Cursor → GrokBot)으로 보여 준다 — 기존 *"하네스가 붙는 층이 위로 올라간다"* 의 1인칭 사례.
- **[[always-on-agent-architecture]] — 같은 GrokBot 계열의 두 번째 화자.** [[lee-robinson|Lee Robinson]]의 *"You can close your computer"* 와 Katz의 *"one person's laptop which might go to sleep"* 이 같은 요구다.
- **[[least-privilege-connectors]]** — *"all your API keys in a file"* 는 이 페이지가 모은 원칙의 반례 그림, *"scoped down to specific agents and specific people"* 는 그 처방.
- **[[tools-and-context-over-harness]]** — "하네스는 고정, 도구·컨텍스트에 투자"와 달리 Katz는 **하네스 쪽에 남는 일(인프라·보안·효율)** 을 명시한다. 정의 범위가 다르다(⚠️ 아래).

### 갈리는 것

> ⚠️ **"하네스 선택이 점수를 크게 바꾸지 않는다"(해설이 전한 두 연구) vs 이 위키의 하네스 효과 기록.** [[harness-engineering]] · [[agent-harness-design]]에는 하네스가 결과를 바꾼다는 사례가 여럿 있다. 해설 스스로 *"코딩, 머신 러닝 시험의 맥락"* 으로 범위를 좁혔고, 연구 원문은 무캡션이라 확인할 수 없다. 해소하지 않는다.

## 해소하지 않고 표시만 한 것

- 무캡션 4구간(오프닝 인용 · 두 연구 · 총괄 AI 그림 · 사내 사례)의 원음.
- *"runed"*(runtime?), *"one000"*(1만 달러?), *"differas"/"peras"*, *"workun"*.
- 04:21 *"세일"* — *새 일*로 읽었다(en-orig 더빙은 *sales*).
- *"6개월"* 은 설명란에만 있다.
- 원본 강연(`7Y4sbZgBdnc`)의 날짜·길이 — 열어 보지 않았다. Katz의 현재 소속(설명란은 과거형 *"만들었던"*, 내레이션은 *"만들던"*).

## 등장 개체

- 인물: [[jediah-katz]](신규) · (연결) [[lee-robinson]]
- 조직: [[cursor]] · [[ai-engineer]] · Tech Bridge
- 제품: [[grokbot]]
- 개념: [[harness-pruning]] · [[harness-engineering]] · [[always-on-agent-architecture]] · [[least-privilege-connectors]] · [[durable-execution]] · [[tools-and-context-over-harness]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=NUyLH7tjQpg> (8:28, `upload_date` 2026-10-23)
- raw: `01.raw/articles/2026-10-23_하네스는 더 이상 필요 없을까 - AI가 똑똑해져도 남는 3가지.md`
- 원본 강연(설명란, 미확인): <https://www.youtube.com/watch?v=7Y4sbZgBdnc>
- 같은 형식(해설 + 발췌)의 선례: [[tech-bridge-stripe-collison-cherny-ai-dev-workflow]] · [[tech-bridge-zuckerberg-wang-muse-wonder-cheeky-pint]]
- [[tech-bridge]] · [[jediah-katz]]
