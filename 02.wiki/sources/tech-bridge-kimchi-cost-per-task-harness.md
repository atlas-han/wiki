---
title: "Tech Bridge — 토큰 제한을 멈추세요 (Cast AI · Kimchi): 토큰당 비용이 아니라 작업당 비용, 모델을 고르는 하네스, Ferment·Teleport·Studio"
type: source
tags: [token-economics, cost-per-task, model-routing, open-models, harness, long-running-agents, cloud-agents, team-collaboration, cast-ai, kimchi, vendor-claims, video]
source-url: https://www.youtube.com/watch?v=31XD1O74pks
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 "Laura"([[cast-ai|Cast AI]] 공동 창업자·사장, 성 미발화) · "Zilvinas"([[kimchi|Kimchi]] 엔지니어링 리드, 성 미발화·철자 미확정) · AI Engineer 행사 부스 세션 추정, 2026년 6월 말 이후 녹화(⚠️ 연도 추정)
date-published: 2026-10-07
ingested: 2026-10-09
created: 2026-10-09
updated: 2026-10-09
---

# Tech Bridge — 토큰 제한을 멈추세요: 하네스가 최적의 모델을 직접 고르게 (Cast AI · Kimchi)

[[tech-bridge|Tech Bridge]]가 재배포한 **17:39 2인 발표, Q&A 없음, 공식 챕터 16개.** [[cast-ai|Cast AI]]의 공동 창업자·사장 "Laura"와 [[kimchi|Kimchi]] 코딩 플랫폼 엔지니어링 리드 "Zilvinas"가 **자사 오픈소스 코딩 하네스 Kimchi**를 소개한다. 발화된 부제는 *"proprietary models for edge case but use open source for the rest"*(00:12~00:17). **벤더 제품 발표**다 — 앞 절반(Laura)은 토큰 경제 논증과 사내 성과, 뒤 절반(Zilvinas·Laura)은 제품 기능(Ferment·Teleport·Studio) 순회. 이 위키의 토큰 경제 축([[value-maxing]] · [[true-cost-to-perfect-answer]] · [[automatic-model-routing]])에 **"작업당 비용"을 모델 선택 기준으로 쓰는 하네스**와 **실제 모델 전환 기록(6월, Kimi 2.6 → MiniMax 3)** 을 더한다.

> **토큰을 배급하는 것은 틀렸다 — 관리자의 일은 토큰을 무제한·저렴하게 만드는 것이다. 모델은 토큰당 가격이 아니라 같은 품질의 작업당 비용으로 비교해야 하고, 그 선택은 사람이 아니라 결과에 집착하는 하네스가 해야 한다. 새 모델이 나오면 사람은 평가에 몇 주 걸리지만 하네스는 며칠 만에 옮겨 간다.**

> *"Our job is not to prevent the developer to use coding agent. Our job is to make sure they can use it as much as they want for as long as they want in a completely unlimited fashion."* (02:04~02:15) · *"On one side you see the cost per token. On the other side, you see the cost per task for the same task with the same quality. That is the important thing. Otherwise, you cannot compare Apple with Apple."* (03:07~03:23) · *"what we believe is that reading code is not enough anymore"* (10:48~10:52)

ASR·ko 보정: ko가 Gemini 3 Flash의 작업당 비용을 `en`을 따라 **"705달러"로**(en-orig는 *"$75"*, 03:46 — ⚠️ 판독 불가), *2.5 time less* 를 **"2.5배 더 성장"으로 반전**(05:31), Claude Code 과지출 *half a year ago* 를 **"반년 후"로**(07:42), 2,000줄 *PR* 을 **"지지율"로**(11:18), *open source or proprietary models* 를 **"장비를 소유하거나 소유자에게 개방"으로**(14:39) 옮겼다. en-orig는 회사를 *"Castai"*, 제품을 *"Kimshi"·"Kimmy"*, 둘째 화자를 일곱 가지 철자로 들었다. 전체 목록은 raw. **인용은 en-orig에서만** 했다.

> ⚠️ **벤더 발표, 모든 수치가 당사자 진술이고 출처가 없다.** 인도 회사 *"$500 million on anthropic alone in one months"*(00:46~00:52), Uber CTO가 *"in the last four months (…) used the entire budget of anthropic for the entire year"*(00:58~01:06) — 둘 다 보도·트윗 미특정. 작업당 비용 표는 *"the famous white paper in a university"*(03:02~03:05) — 논문 미특정. 사내 성과(2.5배·1.5배·62%)는 자사 차트. **이 위키는 원 자료를 하나도 열어 보지 않았다.**
>
> ⚠️ **화자 산수·수치 두 곳.** ① 토큰 **×1.5**(05:06~05:10), 비용 **÷1.5**(05:16~05:21)면 간격은 **2.25배**인데 화자는 *"2.5 times in the amount of savings"*(04:38~04:42), *"growing 3x less 2.5 time less"*(05:30~05:36)라 한다. ② Gemini 3 Flash 작업당 비용이 en-orig *"305, sorry, $75"* vs `en`·ko *"$705"*(03:44~03:47) — **$75면 MiniMax 2.7($148)의 절반, $705면 4.8배**로 비교 방향이 갈린다. 화자 결론은 *"they are all different"* 뿐이라 어느 쪽인지 문맥으로도 못 정한다.
>
> ⚠️ **화자·시점.** 설명란에 화자 이름이 없다. 첫 화자는 en-orig *"Laura"*, 동료는 en-orig *"he"* / `en` *"she"*(11:18~11:19)로 갈린다 — 실명 미확정(Cast AI 사장이 Laurent Gil이라는 판독은 위키 밖 지식, ⚠️ 추정). 둘째 화자는 `en`·ko *"Zilvinas"*, en-orig는 *"Zilinas·Julianas·Zilvenat·Zilmanas·Zinas…"*. 행사명 미발화 — 설명란 링크 ai.engineer, *"our booth (…) We are in U4"*(16:55~17:00). 모델 선택 차트가 **6월 3일 → 12일 → 21일**(06:05~06:25)이고 *"three months"* 사용(04:36~04:38) → **6월 21일 이후 녹화**, 연도는 [[minimax-m3]] 출시(2026년 6월 추정)로 2026년으로 읽는다. 업로드는 2026-10-07.

## 1. 토큰 비용 폭주와 "배급"이라는 잘못된 대응 (00:39~02:52)

- 최근 몇 주의 두 뉴스: 인도의 한 회사가 한 달에 Anthropic에만 5억 달러, Uber CTO가 넉 달 만에 연간 Anthropic 예산 소진(00:43~01:06). *"this is how much the token um the token maxing or the token cost is a thing for the enterprises"*(01:09~01:15). ⚠️ 5억 달러 일화는 [[tech-bridge-trusted-throughput]]([[mingsheng-hong|Mingsheng Hong]])에도 *"한 달에 Claude에 5억 달러"* 로 나온다 — 같은 보도인지 미확인.
- 기업의 대응은 사용 제한. 개발자에게 그것은 *"you can use your laptop (…) you have an hour battery and you can only charge once once once a day"*(01:31~01:42).
- ⭐ *"We at Kimchi think this is wrong. Our jobs as manager is to do the opposite is to ensure that we want to make the tokens unlimited and inexpensive."*(01:45~02:04)
- 사내 맥락: 직원 300명, 그중 3분의 2가 개발자, 3개월째 사용(02:19~02:33). ⚠️ 설명란의 *"사내 엔지니어 300명"* 은 화자가 정정한 첫 말이다.

→ [[value-maxing]] · [[token-minimization-trap]] · [[overspending-underusing-loop]]

## 2. 토큰당 비용 vs 작업당 비용 (02:52~04:17)

대학 연구(미특정) 슬라이드: 같은 과제를 **같은 품질로** 끝내는 데 드는 비용을 모델별로 비교한다(03:07~03:20). 값은 *"a blended average at the time this study was made"*(03:37~03:42).

| 모델 (발화) | 토큰당 | 작업당 | en-orig |
|---|---|---|---|
| Gemini 3 Flash | *"$3.5 per million token"* | **⚠️ *"$75"*(en-orig) / *"$705"*(`en`·ko)** | 03:27~03:47 |
| MiniMax 2.7 | *"1.5"*(단위 미발화) | *"$148"* | 03:50~03:59 |

⭐ *"It means the models are not the same. They don't cost the same, but they also not the same per task."*(04:03~04:08) — 토큰 단가가 싼 모델이 작업당으로도 싸다는 보장이 없다. 화자는 MiniMax 2.7을 *"one of my favorite"* 라 하지만 표의 방향은 위 ⚠️ 값에 달려 있다.

→ [[true-cost-to-perfect-answer]] — *"실행당 예산 × 기대 실행 횟수"* 를 같은 단위(작업당)로 본 두 번째 소스. 다른 점: Anthropic 편은 **합격률**을 분모에, 이 편은 **같은 품질**을 조건에 둔다.

## 3. 결과를 보고 모델을 고르는 하네스 · 사내 성과 (04:17~07:10)

- *"an automated harness that will select the right model for the task at the right time based on the outcome of the task"*(04:17~04:28).
- ⭐ **3개월 성과**(04:36~05:38): *"2.5 times in the amount of savings"*. 차트의 보라선은 *"what would have been cloud cost over time"*, 파란선은 *"what we paid"*, *"same outcome"*. 토큰 1.5배↑, 비용 1.5배↓. ⚠️ 산수(위) · *cloud* 는 Claude일 가능성(raw 헤더) · 기준선 산정법 미발화.
- ⭐ **모델 전환 기록**(05:40~06:25): 6월 초엔 주황, 하순엔 노랑 — *"It happened the 12th of June"*. *"The 3rd of June Kimmy[=Kimi] 2.6 is winning by far"*, *"21st of June, the one winning is Minimat[=MiniMax] 3"*. → [[minimax-m3]]가 6월 초 출시(이 위키 기록)된 지 **1~2주 만에 하네스의 1순위**가 됐다는, 이 위키 첫 **모델 교체 속도의 사용 기록**(⚠️ 자사 차트).
- ⭐ *"Us as human probably we can find and understand and test and be comfortable with a new model coming in. Do you think we look at this as human? Absolutely not. But an autonomous harness, an automated coding agent that is obsessed with stock[=?] and cost is going to do just that."*(06:27~06:47)

→ [[automatic-model-routing]] · [[model-mixing-economics]]

> ⚠️ **"결과 기반" 선택의 메커니즘은 말하지 않는다.** 무엇이 *outcome* 신호인지(Ferment 점수인지, 사용자 수락인지), 과제 시작 전에 고르는지 실패 후 바꾸는지, 전환 빈도·임계값 — 전부 미발화. Laura의 *"the harness select the model, ferment is constantly checking the quality"*(09:23~09:29)가 유일한 연결 고리다.

## 4. Kimchi 하네스와 Ferment (07:10~10:48)

- 기원(Zilvinas): *"we ended up spending too much on cloud[=Claude] code like half a year ago. We saw this uh cloud bill skyrocketing and we started working on our own harness"*(07:39~07:46). 내부는 *"py mono SSDK"*(07:48 — pi-mono로 추정, ⚠️), 하네스는 오픈소스로 돌려준다(07:51~07:57).
- ⭐ **Ferment**(김치 테마 — *발효*): 장시간 과제용. *"on average we estimate the human envelope[=involvement] for these tasks is uh typically happening only like every two hours every three hours"*(08:04~08:11). 질문을 몇 개 던진 뒤 *"autonomously runs a coding task for like more than two hours"*, *"it breaks it into milestones"*, 끝에 **산출물 점수**(08:16~08:31).
- 점수의 역할: *"the scoring is there to prove you that whatever model we will pick for you you will always have like good enough scoring for the output"*(08:37~08:46) — **모델 라우팅의 품질 보증 장치**로 제시된다.
- 루프: 변경 → 빌드 → 깨졌는지 확인 → 다시 수정·재빌드 → 이상 없으면 **스테이징 배포**(08:57~09:17). Laura의 해설: *"there is a a higher order model that is checking that quality and thinking that quality is not good enough please do it again"*(09:29~09:39).
- ⭐ 완료 기준: *"artifact is only considered complete once like the output of the scoring like at least B as a score"*, 마음에 안 들면 A를 노리게 다시 시킬 수 있다(09:51~10:07).
- ⭐ **스테이징에서 멈춤은 설계**: *"We still believe there's like some little human that needs to be in the loop before going to the production. At least at this point"*(10:11~10:18). 다음 단계는 프로덕션 메트릭·관측 데이터·SLO, Kubernetes 파드 크래시·헬스체크를 보고 자동 출시(10:18~10:45).

→ [[generator-evaluator-pattern]] · [[token-roles]](grading) · [[risk-proportional-human-review]] · [[production-trace-eval-flywheel]]

> ⚠️ **채점자가 누구인지 불명.** Zilvinas는 점수만 말하고, *"higher order model"* 은 Laura의 해설이다. 같은 하네스가 고른 모델의 산출물을 같은 하네스가 채점한다면 [[generator-evaluator-pattern]]의 작성자=검증자 문제가 그대로 남는다 — 채점 루브릭·채점 모델·B의 기준 모두 미발화.

## 5. "코드 읽기만으론 부족하다" (10:48~11:34)

*"the more vibe engineering or agentic engineering we do (…) the more code changes we get in our chain sets and it kind of becomes unbearable to read especially as you keep bringing like a little bit of a less technical personnel onto your pipelines"*(10:53~11:12). PM이나 Laura가 2,000줄 PR을 들고 오면 *"you need to actually review not just the differences but the actual intent which he wanted to achieve and the specifications which he provided to the coding agent"*(11:19~11:30).

→ [[verification-bottleneck]] · [[intent-alignment]] · [[spec-driven-development]] — 리뷰 대상이 **diff → 의도·스펙**으로 올라간다는 같은 방향([[tech-bridge-death-of-code-review]]의 *"stop reviewing PRs"*). ⚠️ 이 발표는 *그것을 어떻게* 하는지는 보여 주지 않는다 — Studio(§7)의 계획 공유가 간접적 답.

## 6. Teleport — 노트북을 닫아도 (11:35~14:10)

- 원격 보안 샌드박스, SaaS 또는 온프레미스(금융 등), 에이전트 세션을 관리하고 노트북·모바일에서 접근(11:38~12:04). *"it will keep on running until the task is done or until the human in the loop needs to be involved"*(12:25~12:31) — Ferment의 *"두세 시간마다 사람"* 과 짝.
- Laura의 기원 일화: 비행기에서 코딩하다 Wi-Fi가 끊겨서 — Zilvinas(추정)가 *"it was the battery"* 로 정정(12:47~13:09). 로컬과 **같은 느낌**으로, 실행은 **Google의 Kubernetes 클러스터 컨테이너**에서(13:12~13:43).
- ⭐ *"62% of our engineers are only using teleports when they are coding now"*(13:53~13:57). ⚠️ 측정 방법·모수 미발화.

→ [[cloud-agent-delegation]]

## 7. Studio — 팀 칸반 (14:10~16:51)

- *"If that teleport is something typically individual uses, studio is kind of like a teleport for teams and enterprises"*(14:17~14:23). Teleport 샌드박스 위에서 **과제·진행 중 작업·계획**을 팀과 공유 — 엔지니어가 받은 계획을 동료 엔지니어·PM이 리뷰(14:33~14:55). 목적: *"instead of like saying oh I'm going to type this prompt I'm going to try to execute it to the production only later on to learn that the specification and requirements were incorrect"*(15:02~15:10).
- Laura: *"If what you have is a is a is a terminal, a CLI, how do you share that with the others? Well, first he has to live somewhere else."*(15:27~15:36) — **Teleport가 Studio의 전제**. 검토 요청 세션을 동료가 *"I take it"* 하고 답하면 다시 진행 중으로(15:45~16:03), 5~10명 *"pizza team"*(16:08~16:10), 칸반(리뷰·진행·백로그, 16:26~16:38).
- 오픈소스 범위: *"Most of it at least the harness is entirely open source. Uh studio and teleport. You need a Google account"*, 5분 설치(17:06~17:17). ⚠️ Studio·Teleport의 오픈소스 여부는 문장이 끊겨 불분명.

→ [[plan-to-ticket-pipeline]] · [[cloud-agent-delegation]]

## 이 위키와의 연결

### 이어지는 것

- **[[automatic-model-routing]]** — [[tech-bridge-factory-software-factory|Factory]]는 **과제 전에 난이도를 분류**해 *"임계값 위 최저가"* 를 고른다. Kimchi는 **결과(점수)로 선택을 보증**한다고 말한다 — 사전 분류 vs 사후 품질 게이트. 그리고 이 편엔 **시간축 기록**(6월 Kimi 2.6 → MiniMax 3)이 있다: 라우터의 이점이 *한 과제 안의 비용* 만이 아니라 **새 모델을 사람보다 빨리 채택하는 것**이라는 주장.
- **[[true-cost-to-perfect-answer]]** — Anthropic 편의 *"완벽한 답 하나까지의 비용"* 과 같은 단위(작업당). 이 편은 그것을 **모델 비교**에, 그쪽은 **전략(조언·채점·회고) 비교**에 쓴다.
- **[[value-maxing]] · [[token-minimization-trap]]** — *토큰 제한은 틀렸다* 는 [[token-minimization-trap]]의 벤더판. 다만 처방이 다르다: IBM 편은 **결과를 측정하라**, Kimchi는 **단가를 내려 무제한을 가능하게 하라**(같은 결과에 더 싼 모델).
- **[[overspending-underusing-loop]]** — Uber CTO의 *"넉 달에 1년 치"* 는 그 페이지의 *"1년 치 토큰 예산을 한 분기에"* 의 실명(⚠️ 미확인) 사례. Coinbase(기본 모델 교체 → 지출이 토큰에서 갈라짐)와 **같은 모양의 곡선**(토큰↑·비용↓)을 자사 차트로 보인다.
- **[[cloud-agent-delegation]]** — Cursor *"노트북을 닫아도"* 와 같은 문장. Kimchi는 **Studio로 팀 공유**를 그 위에 얹는다.
- **[[risk-proportional-human-review]]** — 스테이징에서 사람이 멈춘다(*"At least at this point"*). 위험 비례가 아니라 **환경 경계(staging/prod)** 로 사람을 둔 사례.

### 갈리는 것

> ⚠️ **Contradiction: 토큰 무제한 vs 결과 측정.** [[value-maxing]]은 토큰맥싱과 토큰 최소화를 **둘 다** 토큰을 주 지표로 삼는 함정이라 본다. Kimchi는 *"make the tokens unlimited"* 를 목표로 걸고 성과를 **토큰 증가율 대비 비용 증가율**로 보고한다 — 결과 지표(배포·재작업)는 *"same outcome"* 한 마디뿐이다. **비용을 내리는 것은 토큰맥싱을 지속 가능하게 만들 뿐, 결과 측정을 대신하지 않는다**는 반론이 이 위키 안에 이미 있다(⚠️ 위키의 대조, 화자는 다루지 않음).

> ⚠️ **Contradiction(약): 모델 선택을 하네스에 맡기는 근거.** 화자는 *사람은 새 모델을 평가하는 데 느리다*를 근거로 든다. [[automatic-model-routing]]의 미해결(*"임계값을 누가·무엇으로 보정하는가"*)은 여기서도 열려 있다 — 6월 12일 전환이 **품질 유지 하의 비용 최적화**였다는 증거는 차트의 *"same outcome"* 문구뿐이다.

## 해소하지 않고 표시만 한 것

- **두 화자의 실명** — "Laura"(성별 단서 en-orig *he* / `en` *she*), "Zilvinas"(en-orig 철자 7종). 설명란 미기재.
- **Gemini 3 Flash 작업당 비용** $75 vs $705, MiniMax 2.7 토큰 단가 단위, 대학 연구의 이름.
- **사내 성과 산수**(1.5×1.5 = 2.25 vs 2.5 vs 3)와 기준선 산정법, *cloud* = Claude 여부.
- **채점자·채점 기준**(B의 의미), 점수 → 모델 선택 되먹임의 메커니즘.
- **"py mono SSDK"** = pi-mono 여부. **Studio·Teleport의 오픈소스 여부.** 부스 *"U4"* vs *"UZ4"*.
- 인도 회사·Uber CTO 트윗의 출처, [[tech-bridge-trusted-throughput]]의 5억 달러 일화와 같은 사건인지.

## 등장 개체

- 인물: "Laura"([[cast-ai]] 공동 창업자·사장, 페이지 없음 — 실명 미확정) · "Zilvinas"([[kimchi]] 엔지니어링 리드, 페이지 없음) · Uber CTO(이름 미발화)
- 조직: [[cast-ai]] (신규) · [[anthropic]] · Google([[google-cloud]] — Teleport 실행 위치) · Uber · [[ai-engineer]](설명란 링크, 부스)
- 제품·모델: [[kimchi]] (신규 — 하네스·Ferment·Teleport·Studio) · [[claude-code]](*"cloud code"*) · [[minimax-m3]](*"Minimat 3"*) · MiniMax 2.7 · Kimi 2.6 · Gemini 3 Flash · pi-mono SDK(⚠️ 추정) · Kubernetes
- 개념: [[automatic-model-routing]] · [[model-mixing-economics]] · [[true-cost-to-perfect-answer]] · [[value-maxing]] · [[token-minimization-trap]] · [[overspending-underusing-loop]] · [[generator-evaluator-pattern]] · [[token-roles]] · [[cloud-agent-delegation]] · [[verification-bottleneck]] · [[intent-alignment]] · [[spec-driven-development]] · [[risk-proportional-human-review]] · [[production-trace-eval-flywheel]] · [[plan-to-ticket-pipeline]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=31XD1O74pks> (17:39, `upload_date` 2026-10-07)
- raw: `01.raw/articles/2026-10-07_토큰 제한을 멈추세요 - 하네스가 최적의 모델을 직접 고르게 해보세요.md`
- 설명란 링크: <https://kimchi.dev/> · <https://github.com/getkimchi/kimchi> · <https://cast.ai> · <https://ai.engineer> (⚠️ 열어 보지 않았다)
- 같은 주제: [[tech-bridge-factory-software-factory]] · [[tech-bridge-tokenmaxxing-to-valuemaxxing]] · [[tech-bridge-tokens-should-have-jobs]] · [[tech-bridge-trusted-throughput]] · [[tech-bridge-mousepower-measuring-agents]] · [[tech-bridge-cursor-legacy-refactoring]] · [[tech-bridge-death-of-code-review]] · [[tech-bridge-minimax-m3-long-context]]
- [[tech-bridge]] · [[cast-ai]] · [[kimchi]]
