---
title: "[한영자막] Claude Code와 Codex를 인간 연구자들과 경쟁시켰습니다 — Elie Bakouch, Prime Intellect"
type: video
source: https://www.youtube.com/watch?v=AzmloQSjvp0
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 19:08
published: 2026-09-27
created: 2026-09-28
description: "Prime Intellect 연구 엔지니어(설명란 기준 Elie Bakouch — 자막에는 'Ali'·'Ellie'로만)의 발표 한영자막 재배포. 주제는 자동화된 AI 연구(automated AI research): 빅랩이 말하는 재귀적 자기 개선(recursive self-improvement)을 정량화할 제3자 벤치마크가 없다 → Karpathy의 GPT-2 재현(90분) → Keller Jordan이 이끈 modded-nanogpt가 2년 만에 2분 미만으로 → 옵티마이저 관련 파라미터만 바꿀 수 있는 optimizer speedrun을 환경으로 삼아 Codex(GPT-5.5)와 Claude Code(Opus, 버전 표기 트랙마다 다름)를 커뮤니티와 경쟁시킴. goal.md + agents.md + Slurm 선점형 작업, 통계적 임계값으로 기록 검증. Claude는 9~10시간마다 '못 깨겠다'며 멈춰 시간의 1/3을 놀았고 Codex는 쉬지 않았다; Codex가 scratchpad·서브에이전트·토큰·compaction 모두 더 많음. 결과: 당시 최고 기록 2,990 step을 Claude가 50~60 step 앞섬. 준비 중인 벤치마크 세 트랙(가중치만 / arXiv만 / 전체 접근), 6일 실험(Claude·Codex·Kimi·GLM — Kimi가 4일째 도약, 출력 토큰 축으로는 Kimi가 효율적), Claude의 논문 검색이 최고 결과로. 핵심 관찰: 새 옵티마이저·메커니즘은 하나도 없었다 — 논문 조합과 '+1 개선'뿐. 처방: AlphaEvolve 영감의 발견 루프(생성자·스피드런 보상·judge의 taste·규모 확장·사람의 조향), 목표·제약을 바꾼 여러 스피드런. Prime Intellect의 GPU 샌드박스·자체 에이전트·오픈소스 모델 학습·verifiers류 라이브러리."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=AzmloQSjvp0
**Channel**: Tech Bridge · **Duration**: 19:08 · **Published**: 2026-09-27

> 채널 공식 챕터 **18개**(첫 구간 00:00~00:24는 `<Untitled Chapter 1>`)가 있는 영상이다. 아래 소제목은 그 챕터를 따르고, **타임스탬프는 en-orig 자막의 실제 캡션 시각만** 쓴다(구간 표기는 첫 캡션 시작 ~ 마지막 캡션 시작). 자막은 **자동 자막뿐**(info.json `subtitles`는 비어 있고 `automatic_captions`에서 ko 자동 번역 · en-orig ASR · en을 받았다). 본문은 en-orig를 뼈대로 한국어로 옮기되 **ko 자막의 오역을 `[ ]` 로 교정**했고, 맨 아래에 **en-orig 전사 전문**과 **ko 자막 전문**을 챕터별로 붙였다.
>
> ⚠️ **en 트랙은 en-orig와 다르고, 독립된 증거가 아니다.** en은 en-orig의 재진술인데 **ko와 같은 자리에서 같은 오류**를 낸다 — *"modern nano GPT"*(02:25, en-orig *"modded nanoGPT"*), *"eviction permit"*(07:11, en-orig *"preemptible permission"*), *"inspection agents"*(09:24, en-orig *"subagents"*), *"human recovery"*(10:19~10:54, en-orig *"human recall"* = record), *"exit tokens"*(13:32, en-orig *"output token"*), *"rapid testing community"*(16:30, en-orig *"speed run community"*), *"Primal Direct"*·*"Timing Direct"*(00:17·17:35). en이 en-orig와 **다른 값**을 내는 곳은 셋 — **①** 01:58~02:07 en *"90 minutes"* vs en-orig *"19 minutes"*, **②** 05:40 en *"Opus-4.8"* vs en-orig *"Opus 1.8"*, **③** 17:57 en *"RLM frameworks"* vs en-orig *"LM framework"*. 셋 다 **en을 근거로 확정하지 않는다**(아래 표). 인용은 **en-orig에 있는 문장만** 한다.
>
> **화자: 설명란 기준 "Prime Intellect의 연구 엔지니어 Elie Bakouch"** — 자막의 자기소개는 en-orig *"So I'm **Ali**. I work at **Primal director** as a research engineer"*(00:16~00:19), en *"I am **Ellie**. I work at **Primal Direct**"*, ko *"**엘리**. 저는 **Primal Direct**에서 근무합니다"*. **이름(성)과 회사명은 설명란 표기를 따른다**(설명란 링크 `x.com/eliebakouch` · `linkedin.com/in/eliebak/` · `primeintellect.ai` — ⚠️ 링크는 열어 보지 않았다). 직함 *research engineer* 는 자막과 설명란이 일치한다. 회사명은 17:35에서 다시 **"Timing the Lake"**(en *"Timing Direct"*)로 깨진다.
>
> ⚠️ **촬영 시점·행사 미확정** — 청중을 향한 발표(*"Thanks for being here"* 00:01, *"this talk"* 04:27·14:33)지만 **행사명이 설명란·자막 어디에도 없다.** 상대 시점 단서만 있다: optimizer speedrun이 *"a few months ago"*(03:28~03:30) 공개, *"the release was like about 2 months ago"*(05:21~05:25, 무엇의 공개인지 모호 — 스피드런인지 자기들 결과 발표인지), *"there was no slash goal at the time"*(06:35~06:37 — 지금은 `/goal` 이 있다는 함의, 어느 제품의 명령인지 말하지 않는다), 모델명 GPT-5.5 · Opus(버전 미확정) · Kimi K2.7(추정). 업로드는 2026-09-27이지만 **발표일은 알 수 없다.**

## ⚠️ ko 자막 보정 목록

이 영상의 ko는 **부정을 네 번 뒤집는다** — *"아직 공개하지 않았다"* 를 **"출판되었습니다"**(11:24)·**"공개했지만"**(17:43), *"그땐 /goal이 없었다"* 를 **"있었어요"**(06:37), *"(기록 경신에) 실패하면 보상은 0 또는 음수"* 를 **"그는 해냈습니다"**(04:44). 그리고 **수치를 셋 망가뜨린다** — *90분* → **"90일"**(01:49), *2분 미만* → **"2초 이내"**(02:42), *50~60 step 앞섬* → **"약 1,990걸음 초과"**(11:07). *record(recall로 오인식)* 는 **"인간 회복"** 이 된다.

| 시각 | en-orig | ko | 바른 읽기 |
|---|---|---|---|
| 11:22~11:25 | *"So, we So, this is like **not released yet**. This is something that we are working on currently."* | **"그래서 저희는… 이건… / 출판되었습니다. 이것은 ~에 관한 것입니다 / 저희는 현재 작업 중입니다."** | ⭐ **아직 공개되지 않았다** — 세 트랙 벤치마크는 **작업 중**. ko는 **"출판되었습니다"** 로 부정이 사라진다 |
| 17:39~17:44 | *"most of it we **didn't release yet**."* | **"제 말은, 그들 대부분은 아직 그러지 못했다는 거죠. / 저희는 그것들을 공개했지만,"** | ⭐ **대부분 아직 공개하지 않았다**(GPU 샌드박스 등). ko 두 번째 캡션은 **"공개했지만"** |
| 06:35~06:37 | *"but they they **there was no slash goal** at the time."* | **"'슬래시 골'로 대체되었지만, 그렇지는 않습니다. / 그 당시에는 '슬래시 골'이라는 게 있었어요."** | ⭐ **당시엔 `/goal` 이 없었다** — 그래서 goal.md를 직접 만들었다. ko는 **있었다** |
| 04:42~04:45 | *"the reward is zero or negative if it **didn't manage** to to do it."* | **"그렇지 않으면 보상은 0이거나 마이너스입니다. / 그는 해냈습니다."** | ⭐ **기록을 깨지 못하면** 보상은 0 또는 음수. ko 두 번째 캡션은 **"해냈습니다"** |
| 07:41~07:47 | *"I **cannot improve** the record. It's too hard for me. There is no way to to go beyond it."* | **"기본적으로 저는 '네, 할 수 없어요.'라고 말한 셈입니다. / '기록을 개선하세요.' '너무 과해.' / (…) '그냥 잊어버려.'"** | Claude가 **"기록을 개선할 수 없다, 너무 어렵다, 넘어설 방법이 없다"** 고 말했다. ko는 명령형 **"기록을 개선하세요"** 와 **"그냥 잊어버려"** 로 흩어진다 |
| 09:36~09:43 | *"there is obviously this input caching that make it **it's not like 1 billion output token**."* | **"1과 같지 않게 만드는 항목 / 수십억 개의 토큰이 발행되었습니다."** | 입력 캐싱 때문에 **10억 개가 출력 토큰인 건 아니다.** ko는 **"수십억 개의 토큰이 발행"** — 부정이 사라지고 규모가 커진다 |
| 01:47~01:50 | *"GPT-2 from scratch in like **90 minutes**"* | **"약 90일 만에 GPT-2를 처음부터 훈련시켰습니다."** | ⭐ **90분.** 단위가 **분 → 일** |
| 02:44~02:46 | *"GPT-2 validation loss model in **less than 2 minutes**"* | **"GPT-2 검증은 2초 이내에 완료됩니다."** | ⭐ **2분 미만.** 단위가 **분 → 초** |
| 11:05~11:15 | *"the best recall was like uh **2,990 step** and we beat it by like uh uh **50 or 60 step** for Claude and Codex was like **20 step above**."* | **"2,990걸음 중 우리는 그 기록을 약 1,990걸음 초과 달성했습니다. / 클로드와 코덱스와 함께 50~60걸음 정도 걸었습니다. / 약 20계단 위입니다."** | ⭐ 당시 최고 기록 **2,990 step** 을 **Claude가 50~60 step** 앞섰고 Codex는 *"20 step above"*(⚠️ 무엇 대비 20인지 모호 — 아래 미해결). ko의 **"1,990걸음 초과"** 는 원문에 없는 수 |
| 01:57~02:06 | *"now in 2 years ago, I think, it only took like **19 minutes**. (…) reproduce GPT-2 in **19 minutes**? It means that in **19 minutes**"* · 02:38 *"took this **19 minutes**, then 45 minutes"* | ko **"90분밖에"** · **"90분 만에"** | ⚠️ **en-orig 안에서 불일치** — 01:50은 *90 minutes*, 이후 네 번은 *19 minutes*. en·ko는 모두 **90**. 흐름(90 → 45 → 2분 미만)과 01:50의 첫 발화로 보아 **90분의 ASR 오인식일 가능성이 높지만** 이 위키는 소스 밖 확인 없이 **"90분(en-orig 후속 발화는 19로 들림)"** 으로 적는다 |
| 05:35~05:45 | *"Codex was like **GPT-5.5 with XAI** and Cloud Code was **Opus 1.8 with XAI**"* | **"마치 XI와 클라우드 코드를 사용하는 GPT-5.5 같았습니다. / XI와 함께 Opus-4.8이었습니다."** | Codex = **GPT-5.5**, Claude Code = **Opus (버전 미확정)** — en-orig *1.8*, en·ko *4.8*. *"with XAI"* 는 두 모델 모두에 붙는데 **무엇인지 불명**(추론 노력 설정의 오인식으로 보이나 확인 불가). ⚠️ 이 위키는 버전을 확정하지 않는다 |
| 05:32~05:43 | *"Codex and **Cloud Code**"* | **"Codex와 Cloud Code"** · **"클라우드 코드"** | **Claude Code.** en-orig ASR부터 *cloud code*. 제목·설명란이 확정 |
| 00:16~00:19 · 17:35 | *"I'm **Ali**. I work at **Primal director**"* · *"So at **Timing the Lake**"* | **"엘리. 저는 Primal Direct에서"** · **"Timing Direct에서는"** | **Elie · Prime Intellect**(설명란). 회사명이 세 갈래로 |
| 00:10~00:13 | *"all those like **phone sale model** perform at automated AI research task"* | **"AI 기기는 다음과 같은 작업을 수행합니다."** | ⚠️ *phone sale model* 은 알아들을 수 없는 ASR. en은 *"how AI models perform"*. *frontier models* 로 추정되나 **확정하지 않는다** |
| 00:42~00:43 | *"this **bad thing called** recursive self-improvement"* | **"잘못 명명된 재귀적 자기 개선"** | **재귀적 자기 개선이라는 (그) 나쁜 것** — ko는 **"잘못 명명된"** 으로 명명 비판처럼 읽힌다 |
| 02:28~02:30 | *"called **modded nanoGPT**"* | **"'modern'이라는 또 다른 것 / '나노 GPT'"** | **modded-nanogpt**(챕터 제목이 확정). en도 *modern* |
| 03:13 · 12:18~12:20 | *"this is **the nanoGPT one**"* · *"the **nano GPT track one**"* | **"이것은 나노 GPT-1입니다."** | **nanoGPT 쪽 스피드런.** ko·en이 **"GPT-1"** 이라는 모델명을 만들어 낸다 |
| 03:44~03:45 | *"do MoE, do uh **attention**, whatever"* | **"관심, 뭐든 간에"** | **attention**(아키텍처 변경의 예). en은 *listen* |
| 03:49~03:52 | *"change like **Adam to new shampoo**"* | **"아담처럼 새로운 샴푸나"** | 옵티마이저 교체의 예(Adam → Shampoo류). ⚠️ *new shampoo* 가 *Muon, Shampoo* 인지 등은 **확인 불가** — 옵티마이저 이름으로만 읽는다 |
| 05:47~05:49 | *"let **the agent free** on our cluster"* | **"기본적으로 자유계약선수를 남겨두는 것입니다."** | 에이전트를 클러스터에 **풀어 두었다.** ko는 **자유계약선수(free agent)** |
| 05:53~05:56 | *"us **stopping the agent** and then restarting"* | **"요원을 체포한 다음"** | 에이전트를 **멈추고** 재시작 |
| 06:31~06:33 · 18:25 · 11:46 | *"our **honest** is very simple"* · *"any **honest**"* · *"all the model and **earnest**"* | **"우리의 정직함은 아주 간단합니다."** · **"정직한 사람과"** | **harness**(하네스)의 오인식 — *"우리 하네스는 아주 단순하다"*, *"어떤 하네스에서든"*, *"모든 모델과 하네스를 같은 조건에"*. ⚠️ 문맥 추정 |
| 06:52~06:56 | *"submit a **job** with **Sbatch** on our Slurm cluster"* | **"SLURM에 채용 공고로 보내주세요"** | Slurm 클러스터에 **sbatch로 작업(job) 제출**. ko는 **채용 공고** |
| 07:10~07:12 | *"It's called **preemptible permission**."* | **"퇴거 허가증이라고 합니다."** | **선점형(preemptible)** 권한 — 누가 노드를 쓰려 하면 작업이 취소된다. en도 *eviction permit*. 챕터 제목(*"선점형 작업"*)이 en-orig를 확정 |
| 08:00~08:02 | *"basically **1/3 of the time** the Claude code agent was either because I had no way to basically monitor it"* | **"3분의 1의 확률로, 클로드 요원 / 방법이 없었기 때문에 비활성화되어 있었습니다."** | **시간의 3분의 1** 동안 (놀고 있었다 — en-orig에서 *idle* 에 해당하는 단어가 빠져 있고 en은 *"inactive"*). ko는 **"확률"** |
| 08:13~08:15 | *"never asked for **question**"* | **"도움을 요청한 적도 없었으며"** | **질문**을 한 번도 하지 않았다 |
| 08:41~08:44 | *"normalized by the number of **active worker**"* | **"자산 또는 그래서"** | **활성 워커 수**로 정규화. en도 *assets* |
| 09:23~09:25 | *"spawning much more **subagents** than Claude"* | **"코덱스가 훨씬 더 많은 요원을 생성했다 / 클로드가 실시한 검사"** | **서브에이전트.** en *inspection agents* |
| 09:45~09:47 | *"Codex did a lot of **compaction**"* | **"다짐이 많이 일어났습니다"** | **compaction**(컨텍스트 압축) |
| 09:50~10:03 | *"Claude only do it like **one per hour** (…) No, it's even less than one per hour for I mean **one for the full run** for Claude and Codex was like one what's **20 every one hour**"* | **"클로드는 하루에 한 번 정도만"** · **"1시간마다 20명씩"** | 화자가 스스로 고친다 — Claude는 **전체 실행에 한 번**, Codex는 *"one (…) 20 every one hour"*(⚠️ 문장이 깨져 정확한 빈도 불명). ko는 **"하루에 한 번"**(단위 오류) · **"20명"** |
| 10:19~10:56 | *"the **human recall** progression rate"* · *"better than the **human recall**"* · *"fetch the **human recalls**"* · *"fetch the new **recall** from human"* | **"인간 회복"** · **"인간의 회복"** · **"새것을 복구"** | **인간 기록(record)의 진행.** ASR이 *record* 를 *recall* 로 들었고 ko는 **"회복·복구"** 로 옮겼다(11:02 *"the best recall"* 도 같은 것) |
| 10:52~10:54 | *"that's what **Codex** did uh that's what **Claude** did, sorry"* | (같음) | 화자 자신의 정정 — 재시작 때 인간 기록을 가져와 개선한 것은 **Claude** |
| 12:05~12:08 | *"One with only **archive paper**."* | **"아카이브 기사와 함께 하나"** | **arXiv 논문만** 접근하는 트랙. en *archived articles* |
| 12:21 · 12:33 | *"optimizer **speed run**"* | **"최적화 속도 경쟁"** · **"경주 결과"** | **optimizer speedrun** |
| 12:37~12:42 | *"iterate for **6 day, almost 5 days, let's say**"* | **"6일 동안 (…) 거의 5일 정도"** | 화자 발화 그대로 **"6일, 대략 5일이라 하자"** — 챕터 제목은 *"6일 실험"*. ⚠️ 정확한 기간은 불명 |
| 13:32~13:33 | *"the number of **output token**"* | **"출구 토큰 수에 따른 축"** | **출력 토큰 수**로 x축을 바꾸면. en *exit tokens* |
| 13:39~13:41 | *"Claude in **max mode** consumes so much more token"* | **"클로드가 최대 모드에서 에너지를 소비하기 때문입니다."** | max mode의 Claude가 **토큰을** 훨씬 많이 쓴다. ko는 **"에너지"** |
| 14:04~14:17 | *"Claude is doing a lot of search on **papers** (…) Claude found a **paper** that no other model found and it actually lead to **the best result**"* | **"조항"** · **"기사"** · **"더 나은 '회상력'"** | **논문** 검색 · **다른 모델이 못 찾은 논문** · **최고 결과**. ko는 *paper* 를 **조항·기사**로, *best result* 를 **"회상력"** 으로 |
| 14:37~14:41 | *"come up with some **crazy ideas** on uh, optimizer that's like **no one have discovered**"* | **"아무도 열광하지 않는 최적화 도구에 미쳐버렸습니다."** | **아무도 발견하지 못한 옵티마이저에 대한 기발한(crazy) 아이디어**를 내리라 기대했다 |
| 14:47~14:50 | *"they combine different **papers**"* | **"기본적으로 서로 다른 것을 결합합니다. / 조항."** | 서로 다른 **논문**을 조합 |
| 15:54~15:58 · 16:28~16:33 | *"you run the **speed run**"* · *"the **speed run community**"* | **"빠른 테스트를 실행하면"** · **"신속 진단 커뮤니티에서"** | **스피드런**을 돌린다 · **스피드런 커뮤니티**. en *quick test*·*rapid testing community* |
| 16:04~16:09 | *"the judge also have this **taste**"* | **"판사님, 이 공간을 허락해 주십시오."** | judge가 **안목(taste)** 을 가진다. *judge* → **"판사"**, *taste* → **"공간"** |
| 17:12~17:18 | *"it's from **Seb Bank** slides (…) you're not **too online**"* | **"세스 뱅크"** · **"인터넷에 연결되어 있습니다"** | 슬라이드 출처 인명은 **판독 불가**(en-orig *Seb Bank*, en *Seth Bank*) — 확정하지 않는다. *too online* → **"인터넷에 연결"** |
| 17:57~18:08 | *"very efficient for like **LM framework** (…) you have a file system and you can write information, read from it. And you also do like this **programmatic tool coding** thing"* | **"RLM 프레임워크"** · **"도구 프로그래밍의 유형"** | ⚠️ 프레임워크 이름은 **트랙마다 다르다**(en-orig *LM*, en·ko *RLM*) — 확정하지 않는다. 설명은 **파일 시스템에 쓰고 읽기 + programmatic tool calling(추정, en-orig *coding*)** |
| 18:16~18:21 | *"library and product called **Verifier Primary or State Training**"* | **"검증자, 기본 L 또는 상태라고 합니다."** | ⚠️ 라이브러리·제품 이름이 깨졌다 — 이 위키는 *verifiers* 와 *prime-rl* 류일 것으로 **추정만** 하고 확정하지 않는다(설명란에 이름 없음) |
| 18:27~18:30 | *"can be like **GN512** which is very big"* | **"JNM 5.2와 같을 수 있습니다."** | ⚠️ 학습 가능한 "매우 큰" 모델의 이름 — **판독 불가**(en *JNM 5.2*). 확정하지 않는다 |
| 13:51~13:52 | *"it's **Kimi K 2.7 code**"* | **"키미 케이시군요. / 2.7 코드."** | Kimi 모델 표기 — **K2.7(코드 변형?)** 로 들리나 확정하지 않는다 |
| 15:34~15:37 | *"very inspired from **Alpha Evolve** by Google"* | **"알파 이볼브에서 (…) 구글과"** | **AlphaEvolve**(Google). 챕터 제목이 확정 |

**양 트랙이 함께 불확실한 것**: Opus 버전(1.8/4.8) · *"with XAI"* 의 뜻 · Codex *"20 step above"* 의 기준 · Codex의 compaction 빈도 · *"the release"*(05:21)가 가리키는 것 · 실험 기간(6일/5일) · Kimi 모델 표기 · 슬라이드 출처 인명 · Prime Intellect 라이브러리·프레임워크·대형 모델 이름 · 화자 성(설명란에만).

---

## 인트로 (00:00~00:22)

> 오늘 **자동화된 AI 연구(automated AI research)**, 특히 [프런티어로 추정되는] 모델들이 자동화된 AI 연구 과제에서 어떻게 수행하는지 이야기하게 되어 기쁩니다. 저는 [Elie]이고, [Prime Intellect]에서 연구 엔지니어로 일합니다. (00:03~00:19)

## 재귀적 자기 개선을 공개적으로 검증하는 이유 (00:24~01:35)

> 빅랩들이 **재귀적 자기 개선이라는 [그 나쁜 것]** 이 아주 곧 온다고 말하는 걸 들었을 겁니다. 재귀적 자기 개선은 기본적으로 **사람의 개입 없이 모델이 모델을 훈련시키는 것**입니다. 그런데 **이게 사실인지 정량화할 벤치마크가 없습니다.** 하물며 **빅랩이 아닌 제3자 벤치마크는 더 없습니다.** (00:35~01:10)

> 앞으로 몇 년의 과학 연구 상당수가 AI 도구에 기반할 것이라 보기 때문에, **AI 연구만이 아니라 이 모델들이 연구를 어떻게 하는지** 이해하는 것이 매우 중요합니다. (01:11~01:31)

## Karpathy의 GPT-2 스피드런과 modded-nanogpt (01:39~02:58)

> 모든 건 Andrej Karpathy가 재미로 만든 영상에서 시작했습니다 — GPT-2를 처음부터 약 **[90분]** 에 훈련시켰죠. GPT-2 훈련은 원래 몇 주가 걸립니다. (01:40~01:57)

> GPT-2 재현이란 **목표 loss에 도달하는 것**입니다. GPT-2와 같은 loss면 대략 같은 성능으로 봅니다. (02:01~02:19)

> 커뮤니티가 이 repo를 가져다 **modded-nanoGPT**를 만들었고 Keller Jordan이 이끌었습니다. [90]분을 45분으로, 이제는 GPT-2 validation loss 모델을 **2분 미만**에 훈련합니다 — 솔직히 미친 일이죠. **2년이 걸렸습니다.** 아주 재능 있는 연구자들이 기여한 **아주 강한 벤치마크**입니다. (02:23~02:56)

## Optimizer Speedrun 소개 (02:59~04:17)

> 게임의 목표는 **이 loss에 가장 짧은 시간에** 도달하는 것입니다. nanoGPT 쪽은 제약이 거의 없고, **유일한 제약은 같은 검증·훈련 데이터를 써야 한다는 것**입니다. (03:05~03:25)

> 몇 달 전 공개된 **optimizer speedrun**은 **옵티마이저 관련 파라미터만** 바꿀 수 있습니다. nanoGPT에선 아키텍처를 바꾸고 MoE나 [attention]을 해도 되지만, 옵티마이저 스피드런에선 Adam을 [Shampoo 류]로 바꾸는 식만 가능합니다. (03:25~03:54)

> 그래서 이쪽이 **조금 더 연구적**입니다 — 프로그램을 최대한 빠르게 최적화하기보다, 컴퓨터에 들이는 시간과 무관하게 **최선의 방법을 찾는 것**이니까요. (03:57~04:11)

## 스피드런이 좋은 연구 환경인 이유 (04:19~05:16)

> 첫째, **좋은 평가**입니다 — 이 발표의 주 초점이죠. 또 **좋은 훈련 환경**이기도 합니다 — 모델에 보상을 줄 수 있으니까요. 기록을 깨면 보상이 양수, [깨지 못하면] 0이나 음수입니다. (04:19~04:45)

> 꽤 빠르기도 합니다 — 옵티마이저 쪽 이전 기록이 약 2분이었고, 한 번 돌리는 데 15~20분이 걸립니다. 그리고 **규칙이 명확**합니다. **발견을 하기에도 좋은 환경**이라고 봅니다 — 검증할 수 있는 명확한 규칙이 있으니까요. (04:48~05:13)

## Claude Code와 Codex의 커뮤니티 기록 도전 (05:19~06:37)

> 옵티마이저 스피드런에서 **두 AI 에이전트 — Codex와 [Claude Code] — 를 띄워 커뮤니티와 경쟁**하기로 했습니다. Codex는 GPT-5.5, Claude Code는 Opus[(버전 미확정)]였습니다. 에이전트를 클러스터에 [풀어 두고] 반복하게 했죠. (05:25~05:53)

> V1·V2·V3는 우리가 에이전트를 [멈췄다가] 재시작한 것뿐입니다. V3는 [발표] 하루 이틀 전이었는데, **우리 에이전트가 더 이상 최고 기록이 아니어서** *"최근 몇 주의 인간 기록을 전부 가져와 그 위에서 개선해 보라"* 고 했고, 효과가 있었습니다. (05:53~06:15)

> **새로운 아이디어만으로** 기록을 깨는 **novelty track**도 있었는데, 모델들에게 **더 어려웠습니다.** (06:15~06:29)

## 실험 환경: goal.md, Slurm, 선점형 작업 (06:39~07:31)

> 우리 [하네스]는 아주 단순합니다. 솔직히 `/goal` 로 대체할 수도 있었지만 **그땐 `/goal` 이 [없었습니다].** 그래서 goal.md를 직접 만들었죠 — 같은 이름을 고른 게 재밌습니다. goal.md와 일종의 agents.md가 규칙을 정했습니다. (06:31~06:49)

> 에이전트가 아이디어를 내고 Slurm 클러스터에 sbatch로 [작업]을 제출합니다. 빈 노드에 제출하되 **[선점형] 권한**이라, 누가 그 노드를 쓰려 하면 작업이 취소됩니다. 그다음 **훈련 로그를 읽고 기록인지 판단**합니다. 기록으로 인정받으려면 **통계적 임계값을 넘어야** 합니다 — **seed 최적화나 우연이 아님을 확인하려고요.** (06:49~07:27)

## 계속 포기한 Claude와 멈추지 않은 Codex (07:34~08:21)

> 솔직히 아주 고통스러웠던 첫 번째 결과는 — **Claude Code가 9~10시간마다 멈추고** *"기록을 [개선할 수 없다]. 너무 어렵다. 넘어설 방법이 없다"* 고 말했다는 겁니다. *"알았어, 계속해, 새 방향을 탐색해"* 하면 다시 10시간 가고, 또 *"못 깨겠다"*… (07:31~07:58)

> 기본적으로 **[시간]의 3분의 1** 동안 Claude Code 에이전트가 [놀고 있었습니다] — 제가 모니터링할 방법이 없었으니까요. **Codex는 정반대**였습니다. 내내 일했고, 거의 쉬지 않았고, **한 번도 [질문]하지 않았습니다.** (08:00~08:17)

## 작업 메모, 서브 에이전트, 토큰 사용량 (08:24~10:07)

> 모델이 **scratchpad** — 기본적으로 모델의 활성 메모리 — 에 쓸 수 있게 했습니다. **Codex가 scratchpad에 훨씬 많이 씁니다.** 모든 그래프는 [활성 워커] 수로 정규화했으니, Codex가 더 오래 일해서가 아니라 **정말 다른 행동**입니다. (08:21~08:47)

> 파일의 **어조**도 아주 달랐습니다. Claude는 새 기록에 **이모지를 잔뜩** 붙이며 흥분했고, Codex는 *"내가 한 일은 이것, 내린 결정은 이것, 다음에 할 일은 이것"* — 아주 로봇 같았죠. (08:55~09:15)

> Codex가 Claude보다 **[서브에이전트]를 훨씬 많이** 띄웠고, **토큰도 훨씬 많이** 태웠습니다 — 전체로 약 10억 토큰이었는데, 입력 캐싱이 있어서 [10억 개가 출력 토큰인 건 아닙니다]. Codex는 컨텍스트 윈도가 **250k뿐이라 [compaction]을 많이** 했습니다. Claude는 전체 실행에 한 번 정도였고요. (09:18~10:03)

## 결과: 두 모델 모두 인간 기록 경신 (10:08~11:22)

> 흰색은 **인간 [기록]의 진행**, 빨강이 Claude(원래 주황이어야 하지만), 파랑이 Codex입니다. **거의 매 시점 Claude와 Codex가 인간 [기록]보다 낫고**, Claude는 초반에 아주 빠르게 좋은 점수에 도달합니다. (10:08~10:39)

> 아주 중요한 점 — **모델은 언제든 인간 기록을 가져올 수 있었습니다.** [Claude]가 그렇게 했죠(재시작할 때 인간의 새 기록을 가져와 그 위에서 개선했습니다). (10:40~10:56)

> 당시 최고 기록이 **2,990 step** 정도였고, **Claude로 50~60 step** 앞섰고 Codex는 [*"20 step above"* — 기준 불명]. 둘 다 인상적이라고 생각합니다. (10:58~11:18)

## 실제 벤치마크를 위한 세 가지 트랙 (11:25~12:30)

> 이건 [아직 공개되지 않았고] 지금 작업 중입니다. 방금 것은 재밌는 실험이지만 **구조가 부족합니다.** 진짜 벤치마크라면 **여러 seed**, 그리고 **모든 모델과 [하네스]를 같은 조건**에 둬야 합니다. (11:22~11:48)

> **세 트랙** — ① **아무 접근 없이**, 모델 가중치의 지식만으로 연구하는 능력 측정, ② **[arXiv] 논문만**, ③ **전체 접근**(최신 인간 기록 포함). 그리고 원래의 **nanoGPT 트랙**과, 옵티마이저가 **새로워야만 하도록** 제약한 **optimizer speedrun** 둘 다 하려 합니다. (11:50~12:28)

## Claude, Codex, Kimi, GLM의 6일 실험 (12:33~13:30)

> 에이전트를 **6일, 대략 5일** 반복시켰고, **Codex·Kimi·Claude가 매우 효과적**이었습니다. GLM은 아직 끝나지 않은 실행입니다. **Claude가 또 아주 잘했고, 놀랍게도 Kimi도 매우 경쟁력 있었습니다** — 4일째쯤 도약해 새 기록으로 Codex를 넘었죠. (12:35~13:10)

> **Claude는 점진적으로** 기록을 개선하고, **Kimi는 계단 함수**처럼 도약합니다. (13:12~13:21)

## 토큰 기준으로 달라지는 결과 (13:33~13:55)

> 6일은 평가로는 꽤 깁니다. x축을 **[출력] 토큰 수**로 바꾸면 **다른 이야기**가 됩니다 — **max mode의 Claude는 Codex·Kimi보다 훨씬 많은 토큰**을 씁니다. 그리고 **Kimi는 쓴 토큰 수 대비 아주 효율적**입니다. (13:25~13:51)

## 각 모델의 연구 논문 활용 방식 (13:58~14:20)

> 문헌과 논문을 쓰는 방식도 다릅니다. Claude는 **논문 검색을 많이** 하고, 실제로 **다른 어떤 모델도 찾지 못한 논문을 찾아 그게 최고 결과로 이어졌습니다.** (13:55~14:17)

## 새로운 옵티마이저는 없었다 (14:23~15:26)

> ⭐ 이 발표에서 **기억해 주셨으면 하는 것** — 에이전트들이 **아무도 발견하지 못한 옵티마이저에 대한 기발한 아이디어**를 내리라 기대했지만, **솔직히 그렇지 않았습니다.** 서로 다른 **논문을 조합하는** 영리한 트릭, 여러 방법에 대한 **"+1" 개선**은 했지만, **새로운 옵티마이저나 메커니즘은 정말 하나도 없었습니다.** (14:20~15:00)

> 간단하진 않지만 **사람 연구자라면 며칠·몇 주 들이면 접근 가능한** 문제에서조차 모델이 새 옵티마이저·메커니즘을 찾지 못한다는 건 시사적입니다. (15:03~15:21)

## AlphaEvolve 방식의 발견 루프 (15:29~17:35)

> **평가가 아니라 발견에** 더 맞게 만드는 방법이 있다고 봅니다. Google의 **AlphaEvolve**와 이후 나온 여러 논문에서 크게 영감을 받은 **멀티에이전트 시스템**입니다. 생성자 여럿 — 폐쇄 모델도 있지만 **비용 대비 아주 효과적인 오픈소스 모델**도 — 이 아이디어를 내고, [스피드런]을 돌려 보상을 받고, **judge가 품질 피드백**을 줍니다. judge가 방법이 좋은지에 대한 **안목(taste)** 을 가질 수도 있습니다. (15:23~16:13)

> 그다음 **어떤 방법을 더 많은 파라미터·토큰으로 확장할지** 결정합니다. [스피드런] 커뮤니티에선 **많은 방법이 대규모에선 안 통한다**는 말이 자주 나오니, 이 루프에 **규모 요소**를 넣는 게 매우 중요합니다. 그리고 **사람이 에이전트의 아이디어를 판단하고 올바른 방향으로 조향**하는 데 아주 유용합니다. (16:15~16:50)

> 아직 해 보진 않았고 — 지금 시도 중입니다. 적어도 AI 연구에서 새 발견으로 이어지길 바랍니다. **여러 스피드런을 정의**할 수도 있습니다 — **목표와 제약을 바꿔** 다양성을 만들고 모델을 특정 방향으로 제약하는 거죠. (16:53~17:31)

## Prime Intellect가 개발 중인 것 (17:37~18:39)

> [Prime Intellect]에서 이 방향으로 여러 일을 합니다 — 대부분 [아직 공개하지 않았지만]. 이런 일엔 GPU 샌드박스가 필요하니 **GPU 샌드박싱**을 만들고 있고, [프레임워크 이름 미확정]에 아주 효율적인 **자체 에이전트** — 파일 시스템에 정보를 쓰고 읽고, programmatic tool [calling]도 하는 — 를 만들며, **오픈소스 모델 위에서 이걸 잘하도록 모델을 훈련**하고 있습니다. (17:35~18:12)

> 이미 공개한 것은 [이름 미확정] 라이브러리·제품 세트로, **어떤 [하네스]에서든 어떤 환경이든 훈련·평가**할 수 있고, 아주 큰 모델까지 훈련할 수 있습니다. (18:13~18:37)

## 이 연구가 공개돼야 하는 이유 (18:41~19:04)

> ⭐ 이 **재귀적 자기 개선의 일부가 공개적으로 일어나는 것**이 아주 중요하다고 봅니다 — **빅랩에 있지 않은 사람들이 실제로 많이 일하고 있으니까요.** 사람들이 이 모델들이 어떻게 연구하는지 쉽게 이해할 수 있게 해야 합니다. (18:43~19:03)

---

## 설명란 원문

> AI가 실제 연구 과제에 도전하면 인간 연구자의 기록을 넘어설 수 있을까요? Prime Intellect의 연구 엔지니어 Elie Bakouch가 Claude Code와 Codex를 Optimizer Speedrun에 투입해 그 과정을 공개했습니다.
>
> 이번 영상에서는 두 AI 에이전트의 기록과 작업 방식, 연구 논문 활용을 비교하고 자동화된 AI 연구의 가능성과 한계를 살펴봅니다. 두 모델 모두 인간 기록을 깼지만, 새로운 최적화 알고리즘을 발명한 것은 아니었습니다.
>
> 주요 포인트
> - Claude Code와 Codex가 Optimizer Speedrun에서 세운 기록
> - 중단과 재시작, 서브 에이전트, 토큰 사용량의 차이
> - Kimi 등 다른 모델과의 장기 실험 및 연구 논문 활용
> - 새로운 발견을 위한 공개형 AI 연구 환경의 방향
>
> #AI연구 #ClaudeCode #Codex #PrimeIntellect #인공지능
>
> ⏱ 타임라인:
> 00:24 — 재귀적 자기 개선을 공개적으로 검증하는 이유
> 01:39 — Karpathy의 GPT-2 스피드런과 modded-nanogpt
> 02:59 — Optimizer Speedrun 소개
> 04:19 — 스피드런이 좋은 연구 환경인 이유
> 05:19 — Claude Code와 Codex의 커뮤니티 기록 도전
> 06:39 — 실험 환경: goal.md, Slurm, 선점형 작업
> 07:33 — 계속 포기한 Claude와 멈추지 않은 Codex
> 08:23 — 작업 메모, 서브 에이전트, 토큰 사용량
> 10:08 — 결과: 두 모델 모두 인간 기록 경신
> 11:23 — 실제 벤치마크를 위한 세 가지 트랙
> 12:32 — Claude, Codex, Kimi, GLM의 6일 실험
> 13:32 — 토큰 기준으로 달라지는 결과
> 13:57 — 각 모델의 연구 논문 활용 방식
> 14:22 — 새로운 옵티마이저는 없었다
> 15:27 — AlphaEvolve 방식의 발견 루프
> 17:36 — Prime Intellect가 개발 중인 것
> 18:41 — 이 연구가 공개돼야 하는 이유
>
> 📎 관련 링크:
> - https://x.com/eliebakouch
> - https://www.linkedin.com/in/eliebak/
> - https://www.primeintellect.ai

## 공식 챕터 (설명란 타임라인과 동일, 첫 구간은 info.json의 `<Untitled Chapter 1>`)

- 00:00 `<Untitled Chapter 1>`
- 00:24 재귀적 자기 개선을 공개적으로 검증하는 이유
- 01:39 Karpathy의 GPT-2 스피드런과 modded-nanogpt
- 02:59 Optimizer Speedrun 소개
- 04:19 스피드런이 좋은 연구 환경인 이유
- 05:19 Claude Code와 Codex의 커뮤니티 기록 도전
- 06:39 실험 환경: goal.md, Slurm, 선점형 작업
- 07:33 계속 포기한 Claude와 멈추지 않은 Codex
- 08:23 작업 메모, 서브 에이전트, 토큰 사용량
- 10:08 결과: 두 모델 모두 인간 기록 경신
- 11:23 실제 벤치마크를 위한 세 가지 트랙
- 12:32 Claude, Codex, Kimi, GLM의 6일 실험
- 13:32 토큰 기준으로 달라지는 결과
- 13:57 각 모델의 연구 논문 활용 방식
- 14:22 새로운 옵티마이저는 없었다
- 15:27 AlphaEvolve 방식의 발견 루프
- 17:36 Prime Intellect가 개발 중인 것
- 18:41 이 연구가 공개돼야 하는 이유
---

## en-orig 전사 (ASR 원문, 챕터별)

> ASR 원문 그대로다(교정하지 않음). 캡션은 **시작 시각 기준으로** 챕터에 배정했다. 오인식(*Ali* · *Primal director* · *honest* · *recall* · *Cloud Code* 등)은 위 보정 목록 참조.

### 00:00 Untitled (인트로)

[00:00] Hey,  
[00:01] hi everyone. Thanks for being here.  
[00:03] Yeah, I'm super happy today to talk  
[00:05] about automated AI research and  
[00:09] especially  
[00:10] all those like phone sale model perform  
[00:13] at automated AI research task.  
[00:16] So I'm Ali. I work at Primal director as  
[00:19] a research engineer and  
[00:21] yeah, I will go through our work on on  
[00:22] this subject.  

### 00:24 재귀적 자기 개선을 공개적으로 검증하는 이유

[00:24] So first I want to basically explain a  
[00:27] bit why we are doing that and why we  
[00:30] think it's super important to do that in  
[00:32] the open. So first  
[00:35] I think we we all agree that  
[00:38] we've heard about like big labs saying  
[00:41] that  
[00:42] this bad thing called recursive  
[00:43] self-improvement is coming very soon. So  
[00:47] recursive self-improvement is like model  
[00:49] training models  
[00:51] without human intervention basically.  
[00:54] But we don't have any benchmark to  
[00:57] basically quantify if this is true or  
[00:59] not, right?  
[01:00] And even less we don't have like  
[01:03] third-party benchmark by non-big labs to  
[01:07] to  
[01:08] to see if it's something coming soon or  
[01:10] not.  
[01:11] And the other part is that we think that  
[01:14] it's super important to understand all  
[01:17] those model  
[01:18] do research because we think that a lot  
[01:20] of the scientific research that will  
[01:22] come into the coming years  
[01:24] will be based also on AI tools. So it's  
[01:27] super important to understand how those  
[01:29] model do research not just only AI  
[01:31] research.  
[01:32] So we try to build kind of this  
[01:35] environment to test the capabilities of  

### 01:39 Karpathy의 GPT-2 스피드런과 modded-nanogpt

[01:39] the model to do so.  
[01:40] So it all started with  
[01:42] Andrej Karpathy  
[01:44] that's basically at fun by doing this  
[01:47] video where he trained  
[01:50] GPT-2 from scratch in like 90 minutes.  
[01:53] Like GPT-2 training takes like weeks and  
[01:57] now in 2 years ago, I think, it only  
[01:59] took like 19 minutes. So, what does it  
[02:01] mean to  
[02:03] reproduce GPT-2 in 19 minutes? It means  
[02:06] that in 19 minutes, you achieve this  
[02:08] target loss.  
[02:09] Um  
[02:11] And yeah, and that's at this point when  
[02:12] you have the same loss than  
[02:15] um GPT-2,  
[02:16] you consider that your model is  
[02:19] somewhat of equal performance.  
[02:21] Um  
[02:23] then what happened is that the community  
[02:25] took this repo, uh this GitHub repo, and  
[02:28] created another one called modded  
[02:30] nanoGPT, and this effort was led by  
[02:33] someone called uh Keller Jordan. And  
[02:35] what happened is that  
[02:36] they basically  
[02:38] took this 19 minutes, then 45 minutes,  
[02:41] and then now we can train like GPT-2  
[02:44] validation loss model in less than 2  
[02:46] minutes, which is, honestly, crazy. And  
[02:48] it took like 2 years to to achieve this.  
[02:51] So, it's a very strong benchmark where  
[02:54] uh a lot of very talented researcher  
[02:56] donated them.  
[02:58] Um  

### 02:59 Optimizer Speedrun 소개

[02:59] yeah, so we decided to take this  
[03:01] environment of speedrun. So, really this  
[03:05] is kind of a game. So, the goal of the  
[03:07] game is to achieve this loss in the  
[03:10] fewest in the shortest amount of time.  
[03:13] So, this is the nanoGPT one, and you can  
[03:16] uh you don't have almost any  
[03:19] constraints. The only constraint that  
[03:20] you got is that you need to use the same  
[03:23] validation and training data, right?  
[03:25] Um there is a new speedrun called the  
[03:28] optimizer speedrun that was released uh  
[03:30] a few months ago. And here it's slightly  
[03:33] different because  
[03:34] uh you can only change the optimizer uh  
[03:37] related parameters. So, for instance,  
[03:40] nanoGPT, you can change the  
[03:41] architecture, uh do MoE, do  
[03:45] uh attention, whatever.  
[03:47] Uh optimizer speedrun, you can only  
[03:49] change like Adam to new shampoo, or  
[03:52] whatever optimizer  
[03:54] is your favorite.  
[03:56] Um  
[03:57] yeah, and so this is a bit more  
[03:59] researchy because it's less about  
[04:02] optimizing the program to be  
[04:04] as fast as possible, but more like  
[04:06] finding the best method possible no  
[04:08] matter the the the time you put into the  
[04:11] computer, right?  
[04:13] So,  
[04:14] um yeah. Why take speedrun as an  
[04:17] environment for  

### 04:19 스피드런이 좋은 연구 환경인 이유

[04:19] automated AI research? First,  
[04:21] uh we think that it's a good evaluation.  
[04:23] We'll see later why.  
[04:25] Uh and this is kind of the main focus of  
[04:27] this talk. But we also think it's  
[04:29] probably a good training environment  
[04:32] because it's a way to give the model a  
[04:34] reward. So, the reward is positive if  
[04:37] the model beat the speedrun and beat the  
[04:40] last record, sorry, and the reward is  
[04:42] zero or negative if it didn't manage to  
[04:45] to do it. So, it's a good environment to  
[04:48] train model. It's also quite fast like  
[04:50] as you see  
[04:52] previous record were around 2 minutes  
[04:54] for the optimizer one. Each run take  
[04:56] about like 15 to 20 minutes.  
[04:59] And yeah, and there is like clear rules,  
[05:02] basically. And we also think it's like a  
[05:05] good environment to make discovery. So,  
[05:08] like kind of breakthrough in AI research  
[05:10] because there is those clear rule that  
[05:13] you can verify or not.  
[05:16] Yeah. So, yeah.  

### 05:19 Claude Code와 Codex의 커뮤니티 기록 도전

[05:19] Um so, what we did  
[05:21] so, the release was like about 2 months  
[05:25] ago and there was this optimizer  
[05:27] speedrun and we decided to basically  
[05:30] compete with the community by launching  
[05:32] two AI agents. So, Codex and Cloud Code.  
[05:35] Codex was like GPT-5.5 with XAI and  
[05:41] Cloud Code was Opus 1.8 with XAI. Um  
[05:45] and yeah, we decided to basically let  
[05:47] the agent free on our cluster Uh and  
[05:51] and just iterate on it. So, we have like  
[05:53] V1, V2, V3 is just basically us stopping  
[05:56] the agent and then restarting. V3  
[05:59] was like one or two day before the  
[06:01] release because we saw that our agents  
[06:04] no longer have the best record. So, we  
[06:06] were like, "Okay, take all the the human  
[06:10] record in the last few week and just try  
[06:12] to to  
[06:13] improve upon it." And and and it worked.  
[06:15] Yeah. And we also have this novelty  
[06:17] track where the goal is to  
[06:20] uh  
[06:21] beat the record with only novel ideas.  
[06:24] Um and we'd see that  
[06:27] this this was more complex for the the  
[06:29] models.  
[06:31] So, our honest is very simple. Honestly,  
[06:34] we could have just replaced it with  
[06:35] slash goal, but they they there was no  
[06:37] slash goal at the time. So, we made our  

### 06:39 실험 환경: goal.md, Slurm, 선점형 작업

[06:39] own goal.md. It's actually quite fun  
[06:42] that we choose the same name.  
[06:43] And we had the goal.md and kind of  
[06:46] agents.md that defined the rules. And we  
[06:49] let the agent propose ideas and then it  
[06:52] can submit a  
[06:53] job with Sbatch on our  
[06:56] Slurm cluster.  
[06:58] And basically, the way it works is that  
[07:01] it can submit on nodes that are  
[07:03] available, but only under a certain  
[07:05] permission, which means that if someone  
[07:07] want to use this node, uh the model just  
[07:10] like cancel the job. It's called  
[07:12] preemptible permission.  
[07:13] So, yeah. Then it measure the it read  
[07:16] basically the training logs, then decide  
[07:18] if it's a record or not. To validate a  
[07:20] record, you need to basically pass a  
[07:22] statistical threshold to make sure that  
[07:24] it's just not  
[07:25] seed optimization and it's just not  
[07:27] random, right?  
[07:29] So, yeah, a few results from these  
[07:31] experiments. The first one that was  

### 07:33 계속 포기한 Claude와 멈추지 않은 Codex

[07:34] honestly very painful to work with is  
[07:36] that code uh Claude Claude code keeps  
[07:39] stopping every 9 or 10 hours and  
[07:41] basically said, "Yeah, I cannot improve  
[07:44] the record. It's too hard for me. There  
[07:46] is no way to to go beyond it." And then  
[07:49] I was just like, "Okay, continue,  
[07:52] explore new direction, and just go again  
[07:55] for 10 hours." And then say, "Yeah, I  
[07:57] cannot  
[07:58] >> [laughter]  
[07:58] >> beat the record and so on." So,  
[08:00] basically 1/3 of the time the Claude  
[08:02] code agent was either because I had no  
[08:04] way to basically monitor it. And Codex  
[08:07] totally the opposite. Just worked  
[08:10] for all the all the time. And yeah,  
[08:13] almost never idle, never asked for  
[08:15] question, and and and very impressive in  
[08:17] in that way.  
[08:19] Um  
[08:21] We also give the option for the model to  

### 08:23 작업 메모, 서브 에이전트, 토큰 사용량

[08:24] basically write  
[08:26] a bunch of stuff into what we call a  
[08:27] scratchpad, which is basically the  
[08:29] active memory of the model.  
[08:31] Uh we observed that  
[08:34] basically Codex writes a lot on the  
[08:37] scratchpad. So, each plot that I will  
[08:39] show kind of normalized by the number of  
[08:41] active worker. So, this is not only  
[08:44] about Codex working more. It's It's  
[08:47] really different behavior.  
[08:49] So, yeah, you see that  
[08:51] writes a lot more to  
[08:53] to this scratchpad, to this memory.  
[08:55] And uh the shape of the like the the I  
[08:58] don't know, the tone of the the each  
[09:01] file was also super different. Like  
[09:03] Claude was super excited about getting  
[09:05] new record with a bunch of emoji and so  
[09:07] on. And Codex was just like,  
[09:10] "Here is what I do. Here is the decision  
[09:12] I take. What I will do next." Like super  
[09:15] robotic kind of.  
[09:17] Um  
[09:18] Yeah, we also have this plot where  
[09:21] basically we saw that Codex was uh  
[09:23] spawning much more subagents than  
[09:25] Claude.  
[09:26] Uh we saw that Codex burned much more  
[09:29] token than Claude. So, I think in total  
[09:31] it was like  
[09:32] kind of  
[09:33] billion of token. But it's like there is  
[09:36] obviously this input  
[09:38] input caching that make it  
[09:41] it's not like 1 billion output token. Uh  
[09:43] so yeah, we also see that Codex did a  
[09:45] lot of compaction because it only had  
[09:47] like 250k context window and Claude only  
[09:51] do it like one per hour and Codex is  
[09:54] more like  
[09:56] No, it's even less than one per hour for  
[09:58] I mean one for the full run for Claude  
[10:01] and Codex was like one  
[10:03] what's 20 every one hour. So, yeah.  
[10:07] Um  

### 10:08 결과: 두 모델 모두 인간 기록 경신

[10:08] yeah, here is the main results. So, what  
[10:11] this plots shows is that basically we  
[10:15] So, in in a white, you see that the the  
[10:19] human recall progression rate and in  
[10:22] red, you see Claude. I mean it's  
[10:24] supposed to be orange, but whatever. And  
[10:26] in blue,  
[10:27] you see Codex, right?  
[10:29] And you see that at almost every time uh  
[10:32] Claude and Codex are better than the  
[10:34] human recall and Claude is super good at  
[10:36] the beginning, very very fast to achieve  
[10:39] very good score.  
[10:40] Um yeah, and one thing that is super  
[10:43] important is that the model have the  
[10:45] ability to basically fetch the human  
[10:48] recalls at any time and that's what  
[10:50] Codex did uh that's what Claude did,  
[10:52] sorry, because when I restarted it,  
[10:54] basically fetch the new recall from  
[10:56] human and improve upon it.  
[10:58] Um yeah, so the results is that uh I  
[11:02] think at the time the best recall was  
[11:05] like uh 2,990  
[11:09] step and we beat it by like uh  
[11:12] uh 50 or 60 step for Claude and Codex  
[11:15] was like 20 step above. So, it's I think  
[11:18] it's both impressive and and yeah.  
[11:20] Um  
[11:22] So, we So, this is like not released  

### 11:23 실제 벤치마크를 위한 세 가지 트랙

[11:25] yet. This is something that we are  
[11:26] working on currently. And basically the  
[11:28] idea is that this This a cool experiment  
[11:31] to do, but it lack of structure, right?  
[11:34] Uh if you want to do a real benchmark,  
[11:36] you want to do uh multiple seed, you  
[11:38] want to do uh  
[11:40] yeah, proper  
[11:42] uh  
[11:42] thing where you you you you basically  
[11:44] put all the model and earnest in the  
[11:46] same condition, right? So, this is what  
[11:48] we are working on right now, and  
[11:50] basically um the idea is to do three  
[11:54] different track. Uh one without any  
[11:56] access to really  
[11:58] like measure the capability of the  
[11:59] models to do a research based on  
[12:02] only the model weights knowledge. One  
[12:05] with only archive paper.  
[12:08] And one with like full access, so it  
[12:10] also have access to the  
[12:11] the like the latest record by human.  
[12:15] And for this, we plan to do both uh the  
[12:18] nano GPT track one, which is the  
[12:20] original one, and the optimizer speed  
[12:21] run where we we only launch uh we only  
[12:25] constrain the  
[12:26] the optimizer to be to be novel,  
[12:28] basically.  
[12:30] Um yeah. So, I will present some results  

### 12:32 Claude, Codex, Kimi, GLM의 6일 실험

[12:33] on the optimizer speed run.  
[12:35] Uh this is basically what we got. So, we  
[12:37] let the agent iterate for 6 day, almost  
[12:41] 5 days, let's say, and we see that uh  
[12:45] Codex, Kimi, and Claude uh are super  
[12:48] effective. So, for GLM, this is not  
[12:51] finished run, right? So,  
[12:53] the model is actually still iterating on  
[12:55] our cluster right now.  
[12:57] But, we see that Claude is once again  
[12:59] very good at it. And we see that  
[13:01] surprisingly Kimi is also very  
[13:03] competitive.  
[13:04] And kind of have this breakthrough  
[13:06] around day uh four where he kind of beat  
[13:09] Codex with a  
[13:10] a new record, right? It's also  
[13:12] interesting to see that  
[13:14] uh  
[13:15] Claude is much more like progressive in  
[13:17] the way he it improve the record. And  
[13:19] Kimi has really this step function where  
[13:21] he kind of do a breakthrough and so on.  
[13:25] Uh so, this is an interesting plot  
[13:26] because I mean, 6 days is quite a lot  
[13:28] for an eval. Uh,  
[13:30] uh, but you you can change this uh, axis  

### 13:32 토큰 기준으로 달라지는 결과

[13:33] by also the number of output token. And  
[13:36] then kind of tell a different story  
[13:38] because Claude in max mode consumes so  
[13:41] much more token than Codex and uh, Kimi.  
[13:44] And you also see that Kimi is actually  
[13:46] super efficient uh, for the number of  
[13:49] token that's uh, uh, it used. So it's  
[13:51] Kimi K 2.7 code.  
[13:54] Um, so yeah.  
[13:55] Uh, we also see that they have a  

### 13:57 각 모델의 연구 논문 활용 방식

[13:58] different approach to  
[14:00] uh, using the literature and papers. Um,  
[14:04] so for instance like Claude is doing a  
[14:06] lot of search on papers and actually  
[14:09] Claude found a paper that no other model  
[14:12] found and it actually lead to  
[14:14] the best result. So it's kind of funny.  
[14:17] And uh, yeah.  
[14:18] Um,  
[14:20] one of the main issue of all of this is  

### 14:22 새로운 옵티마이저는 없었다

[14:23] that uh,  
[14:25] when I when I launched this this agent  
[14:27] and I think that's something important  
[14:29] that I want you to kind of uh, remember  
[14:32] for this  
[14:33] this talk is that when I launched this  
[14:35] this different agents, I was expecting  
[14:37] them to come up with some crazy ideas on  
[14:41] uh, optimizer that's like no one have  
[14:43] discovered. But honestly it wasn't the  
[14:45] case. Uh, they did some clever trick  
[14:47] where basically they combine different  
[14:49] papers.  
[14:51] Uh, they kind of do plus one improvement  
[14:53] over a bunch of method. But there was  
[14:55] really like no novel optimizer or  
[14:58] mechanism that was uh, coming from those  
[15:00] model. And I think that's  
[15:03] kind of telling that even on something  
[15:05] that is not simple but I'd say that  
[15:09] it's kind of accessible for people,  
[15:11] right? For like human researcher  
[15:14] uh, spending like uh, days and weeks for  
[15:17] the the model like  
[15:18] cannot like find new uh, optimizer and  
[15:21] mechanism.  
[15:23] So, we believe that there is a way  
[15:26] to basically make it more  

### 15:27 AlphaEvolve 방식의 발견 루프

[15:29] um make it better for discovery instead  
[15:32] of evaluation. And this is coming from  
[15:35] uh this is very inspired from Alpha  
[15:37] Evolve by Google and also a bunch of  
[15:39] papers that have been released since  
[15:40] then. It's kind of this multi-agent  
[15:43] system that interact together. Uh bunch  
[15:46] of generator, uh you have closed model,  
[15:49] but you also have open-source model here  
[15:51] that are super effective for the cost,  
[15:53] right?  
[15:54] Uh they can suggest ideas, then you run  
[15:56] the speed run, so you get the reward,  
[15:58] then you have a judge that basically  
[15:59] give a quality feedback. Can also be  
[16:02] like  
[16:04] the judge also have this taste. You can  
[16:06] kind of have like the judge have a taste  
[16:09] about the the method if it's good or  
[16:11] not, uh if it's outside the loop.  
[16:15] And then you can uh basically decide  
[16:18] which method you want to scale to a  
[16:21] larger number of parameters and uh  
[16:23] number of token.  
[16:25] Um so, this is kind of the scale part of  
[16:28] the speed run because some a lot of  
[16:30] method in the the speed run community,  
[16:33] uh people are often saying that they  
[16:35] doesn't work at large scale. So, I think  
[16:36] it's very important to also put a scale  
[16:39] elements in this loop. Uh  
[16:42] and I think also that uh  
[16:44] human are super useful here to basically  
[16:47] judge the ID of agents, steer them steer  
[16:50] them in the right direction, and so on.  
[16:53] Um yeah, so we didn't try it yet. I  
[16:55] mean,  
[16:56] we are kind of trying it right now, and  
[16:58] uh we hope that this will lead to  
[17:01] to to new discovery in AI research at  
[17:03] least. And also a way is that you can  
[17:06] define multiple speed run. So, this is  
[17:09] the next slide. Uh if you  
[17:12] like it's from Seb Bank slides, but if  
[17:15] you if you don't have the reference,  
[17:16] good for you. Means that that you're not  
[17:18] too online.  
[17:19] But the idea is that by changing the  
[17:22] objective and the constraints of the  
[17:24] speedrun, you can basically create a lot  
[17:27] of diversity and constrain the model to  
[17:29] go into a certain direction.  
[17:31] And yeah, and make those discovery.  
[17:35] So at Timing the Lake, we're doing a  

### 17:36 Prime Intellect가 개발 중인 것

[17:37] bunch of stuff in this direction.  
[17:39] There is a bunch of stuff here that we I  
[17:41] mean most of it we didn't release yet.  
[17:44] But we're working on GPU sandboxing to  
[17:47] allow model to iterate into sandbox  
[17:50] because you need GPU sandbox for this  
[17:52] kind of stuff. We are working on  
[17:54] own agents that are  
[17:56] very efficient for like  
[17:59] LM framework. So it means like you have  
[18:01] a file system and you can write  
[18:03] information, read from it. And you also  
[18:06] do like this programmatic tool coding  
[18:08] thing. We're also training a model to be  
[18:10] good at it on top of like open source  
[18:12] model.  
[18:13] And the thing that we already released  
[18:16] is that we have the set of library and  
[18:18] product called Verifier Primary or State  
[18:20] Training where you can basically train,  
[18:23] evaluate any environments on  
[18:25] any honest and the model that you can  
[18:28] train can be like GN512 which is very  
[18:30] big and yeah, we have like we work a lot  
[18:33] on making those library very efficient  
[18:35] to to ship the best quality for our  
[18:37] clients.  
[18:39] Yeah.  

### 18:41 이 연구가 공개돼야 하는 이유

[18:41] I mean yeah, super excited about this  
[18:43] domain. Once again, I think it's super  
[18:45] important to have  
[18:47] a part of like this recursive  
[18:49] self-improvement to happen to happen in  
[18:50] the open because there is actually a lot  
[18:53] of people working that are not on big  
[18:55] labs. So you need to basically  
[18:59] yeah, make it easy for people to  
[19:01] understand all those model work to do  
[19:02] research and so on. So that's kind of  
[19:04] our goal and yeah, thanks a lot.  

## ko 자막 전문 (자동 번역 원문, 챕터별)

> 교정하지 않은 원문이다. 위 보정 목록을 먼저 볼 것.

### 00:00 Untitled (인트로)

[00:00] 안녕하세요, 여러분. 와주셔서 감사합니다.  
[00:03] 여기. 오늘 이렇게 말씀드릴 수 있게 되어 매우 기쁩니다.  
[00:06] 자동화된 연구에 관하여  
[00:08] 인공지능, 특히 모델이 어떻게 작동하는지  
[00:11] AI 기기는 다음과 같은 작업을 수행합니다.  
[00:13] 자동화된 연구. 그래요  
[00:17] 엘리. 저는 Primal Direct에서 근무합니다.  
[00:19] 저는 연구 엔지니어이고, 앞으로  
[00:21] 이 주제에 대한 저희 연구 결과를 발표합니다.  
[00:23] . 먼저 그 이유에 대해 간략하게 설명드리겠습니다.  

### 00:24 재귀적 자기 개선을 공개적으로 검증하는 이유

[00:26] 우리는 왜 이런 행동을 하고, 왜 이런 믿음을 갖는 걸까?  
[00:29] 이는 매우 중요한 일입니다.  
[00:31] 열려 있는. 우리 모두 참여할 것 같아요  
[00:35] 우리가 경청했던 합의  
[00:38] 대형 연구소들은 그렇게 말합니다.  
[00:41] 잘못 명명된 재귀적 자기 개선  
[00:44] 곧 도착할 거예요. 자기계발  
[00:47] 재귀는 기본적으로 다음과 같이 구성됩니다.  
[00:49] 모델 훈련 모델 없이  
[00:51] 인간의 개입. 하지만 우리는 가지고 있지 않습니다  
[00:55] 참고할 만한 기준점이 없습니다  
[00:57] 이것이 사실인지 아닌지를 정량화하기 위해,  
[00:59] 진실? 그리고 우리는 분명히 아무런 주장도 하지 않습니다.  
[01:03] 외부 참조 연구소  
[01:05] 큰 것들은 아니고, 그게 맞는지 보려고요.  
[01:08] 곧 일어날 일인지 아닌지. 다른 하나  
[01:11] 그중 일부는 우리가 그것이 매우 중요하다고 믿기 때문입니다.  
[01:14] 이러한 모델들이 어떻게 작동하는지 이해하는 것이 중요합니다.  
[01:16] 그들은 조사합니다. 왜냐하면 우리는 그것이 훌륭하다고 생각하기 때문입니다.  
[01:19] 과학 연구의 일부  
[01:22] 향후 몇 년 동안에도 그럴 것입니다.  
[01:24] 인공지능 도구를 기반으로 할 것입니다. 그래서  
[01:27] 어떻게 되는지 이해하는 것이 매우 중요합니다.  
[01:28] 이 모델들은 연구를 수행하는 것이 아니라, 연구를 수행하는 것입니다.  
[01:30] 인공지능 연구 목적으로만 사용됩니다. 그래서  
[01:33] 우리는 일종의 것을 만들려고 노력합니다  
[01:35] 기능을 테스트할 수 있는 환경  
[01:38] 그것을 실천하기 위한 모델들. 모든 것은 시작되었습니다  

### 01:39 Karpathy의 GPT-2 스피드런과 modded-nanogpt

[01:42] 기본적으로 안드레이 카르파티와 함께  
[01:45] 그는 재미로 이 영상을 만들었습니다.  
[01:49] 그는 약 90일 만에 GPT-2를 처음부터 훈련시켰습니다.  
[01:52] 분. GPT-2 훈련  
[01:55] 보통 몇 주가 걸립니다. 하지만 벌써 2년이 지났네요.  
[01:58] 몇 년 걸린다고 생각했는데, 90분밖에 안 걸렸어요.  
[02:01] 그렇다면 번식이란 무엇을 의미할까요?  
[02:03] 90분 만에 GPT-2를 학습할 수 있을까요? 그것은 ~에  
[02:07] 90분 만에 이 손실에 도달합니다.  
[02:08] 목표. 네, 바로 그 시점에 말이죠.  
[02:12] GPT-2와 동일한 손실이 발생합니다.  
[02:15] 당신의 모델이 다음과 같은 특징을 가지고 있다고 생각하십니까?  
[02:18] 비슷한 성능. 그러면,  
[02:22] 커뮤니티에서 이 저장소를 가져왔습니다.  
[02:25] GitHub에서 "modern"이라는 또 다른 것을 만들었습니다.  
[02:28] "나노 GPT"는 다음이 주도하는 노력입니다.  
[02:32] 켈러 조던이라는 사람. 어느  
[02:35] 무슨 일이 있었냐면, 그들은 그 90을 줄였다는 겁니다.  
[02:38] 45분에서 몇 분 남았고, 이제 훈련할 수 있습니다.  
[02:40] 손실이 있는 모델  
[02:42] GPT-2 검증은 2초 이내에 완료됩니다.  
[02:45] 솔직히 말해서 몇 분 정도 걸립니다.  
[02:47] 발광. 그리고 그 목표를 달성하는 데 약 2년이 걸렸습니다.  
[02:50] 이것. 그러니까 요점은 이렇습니다.  
[02:52] 많은 사람들이 참고하는 매우 훌륭한 참고 자료  
[02:55] 재능 있는 연구원들은  
[02:56] 기여했습니다. 그래서 우리는 가기로 결정했습니다  

### 02:59 Optimizer Speedrun 소개

[03:00] 이 환경은 "스피드런" 환경입니다. 그래서,  
[03:04] 그들은 어떤 종류의 게임을 보는 걸까요? 그  
[03:07] 이 게임의 목표는 이것을 달성하는 것입니다.  
[03:09] 가장 짧은 시간 안에 손실  
[03:12] 가능한. 이것은 나노 GPT-1입니다. 그리고  
[03:15] 당신은, 음, 거의 그럴 수 없어요.  
[03:18] 제한. 유일한 제한 사항  
[03:21] 중요한 건, 같은 것들을 사용해야 한다는 겁니다.  
[03:22] 검증 데이터와 훈련 데이터,  
[03:24] 진실? 안녕하세요, 새로운 스피드런 영상이 올라왔어요!  
[03:27] "옵티마이저 스피드런"이라고 불리는 것은  
[03:29] 몇 달 전에 출시됐어요. 자, 여기 있습니다.  
[03:32] 약간 다른 이유는, 음, 단지  
[03:34] 매개변수를 변경할 수 있습니다.  
[03:36] 최적화 프로그램과 관련이 있습니다. 에 의해  
[03:39] 예를 들어, nano GPT에서는 다음을 변경할 수 있습니다.  
[03:41] 건축, 어, MOE를 만들기 위해, 만들기 위해, 어,  
[03:44] 관심, 뭐든 간에. 어, "최적화 도구"  
[03:47] 스피드런. 당신이 바꿀 수 있는 것은 오직 하나뿐입니다.  
[03:50] 아담처럼 새로운 샴푸나 다른 어떤 것에 대해서든  
[03:52] 당신이 가장 좋아하는 최적화 도구입니다. 여기요,  
[03:56] 네, 그리고 이것은 그보다 조금 더 많은 것입니다.  
[03:58] 연구이기 때문에 그것은 덜 중요합니다.  
[04:01] 프로그램을 최적화하여 다음과 같이 만듭니다.  
[04:03] 가능한 한 빨리, 그리고 그 이상  
[04:05] 최적의 방법을 찾으세요  
[04:08] 얼마나 많은 시간을 투자하든 상관없습니다.  
[04:10] 컴퓨터 맞죠? 음, 그러니까,  
[04:15] 응. 왜 "스피드런"을 해야 할까요?  
[04:17] 연구 환경으로서  

### 04:19 스피드런이 좋은 연구 환경인 이유

[04:19] AI 자동화? 먼저, 음,  
[04:21] 우리는 그것이 타당한 평가라고 생각합니다.  
[04:23] 이유는 나중에 알게 되겠죠. 그리고 이것은  
[04:25] 이것이 바로 이 글의 주요 초점이라고 할 수 있습니다.  
[04:27] 채팅. 하지만 우리는 그것이 또한 사실이라고 믿습니다.  
[04:29] 아마도 좋은 환경일 겁니다  
[04:31] 훈련은 일종의 훈련이기 때문입니다.  
[04:33] 모델에게 보상을 주세요.  
[04:35] 따라서 보상은 다음과 같은 경우 긍정적입니다.  
[04:37] 해당 모델은 "스피드런" 기록을 뛰어넘습니다. 그리고  
[04:39] 지난 기록을 넘어섰네요, 죄송합니다. 그리고  
[04:42] 그렇지 않으면 보상은 0이거나 마이너스입니다.  
[04:44] 그는 해냈습니다. 그래서 좋은 거예요.  
[04:47] 모델 학습을 위한 환경. 또한  
[04:49] 보시다시피 꽤 빠르네요.  
[04:51] 이전 기록은 약 2였습니다.  
[04:53] 최적화 프로그램 실행 시간은 몇 분입니다. 여기요,  
[04:55] 한 번 실행하는 데 약 15분이 걸립니다.  
[04:58] 20분. 네, 그리고 규칙이 있습니다.  
[05:01] 기본적으로 명확합니다. 그리고 또한  
[05:04] 우리는 이곳이 좋은 환경이라고 생각합니다.  
[05:06] 새로운 발견을 하세요. 종으로서  
[05:08] 전체 수사 과정에서의 진전,  
[05:11] 명확한 규칙이 있기 때문입니다.  
[05:13] 확인 여부. 네, 그렇습니다. 네, 그렇습니다.  

### 05:19 Claude Code와 Codex의 커뮤니티 기록 도전

[05:19] 그래서 우리가 한 일은, 음,  
[05:22] 출시는 약 2개월 전에 있었고, 음...  
[05:25] "스피드런 최적화 프로그램"이라는 게 있었어요. 그리고  
[05:28] 우리는 기본적으로 경쟁하기로 결정했습니다.  
[05:31] 커뮤니티에서 두 개의 AI 에이전트를 출시합니다  
[05:33] . 그러니까, Codex와 Cloud Code죠. 사본  
[05:37] 마치 XI와 클라우드 코드를 사용하는 GPT-5.5 같았습니다.  
[05:40] XI와 함께 Opus-4.8이었습니다. 네, 저희는 그렇게 결정했습니다.  
[05:43] 기본적으로 자유계약선수를 남겨두는 것입니다.  
[05:47] 클러스터를 구성하고 간단히 반복합니다.  
[05:50] 그에 대해서. 자, 이제 V1이 있습니다.  
[05:53] V2, V3는 기본적으로 우리 자신입니다.  
[05:55] 요원을 체포한 다음  
[05:57] 재시작하고 있습니다. 버전 3은 다음과 같았습니다.  
[05:59] 출시 1~2일 전  
[06:02] 왜냐하면 우리는 우리 요원들이 더 이상 그렇지 않다는 것을 알았기 때문입니다.  
[06:04] 그들은 최고의 성적을 거두었다. 그래서  
[06:07] 우리는 "좋아, 우리 모두 가져가자"라고 말했습니다.  
[06:10] 인류의 마지막 기록  
[06:12] 몇 주 동안 이 정도 성과를 내도록 노력하고, 개선해 보도록 하겠습니다.  
[06:14] 효과가 있었다. 예. 그리고 이것도 있습니다.  
[06:18] 목표가 있는 신규 카테고리  
[06:20] 아이디어만으로 기록을 깨는 것에 관한 이야기입니다.  
[06:22] 원본. 우리는 이것이 더 많다는 것을 알았습니다.  
[06:26] 모델에게는 복잡한 문제입니다. 그래서  
[06:31] 우리의 정직함은 아주 간단합니다.  
[06:33] 솔직히 말해서, 그럴 수도 있었죠.  
[06:35] "슬래시 골"로 대체되었지만, 그렇지는 않습니다.  
[06:37] 그 당시에는 "슬래시 골"이라는 게 있었어요.  
[06:38] . 그래서 우리는 우리만의 것을 만들었습니다.  

### 06:39 실험 환경: goal.md, Slurm, 선점형 작업

[06:40] 목표.md. 꽤 흥미롭네요.  
[06:41] 우리는 같은 이름을 선택했어요. 우리는 가지고 있었다  
[06:45] goal.md와 일종의 agents.md  
[06:47] 그것이 규칙을 정했고, 우리는 그것을 따랐습니다.  
[06:50] 담당자는 다음과 같은 아이디어를 제안했습니다.  
[06:52] SLURM에 채용 공고로 보내주세요  
[06:55] SLURM 클러스터의 배치 작업입니다.  
[06:59] 기본적으로는 전송하는 방식으로 작동합니다.  
[07:01] 사용 가능한 노드에 작업을 전송하지만, 그 외에는 아무것도 전송하지 않습니다.  
[07:03] 특정 허가 하에, 즉  
[07:06] 누군가 해당 노드를 사용하고 싶다면,  
[07:08] 모델이 단순히 작업을 취소하는 것입니다.  
[07:11] 퇴거 허가증이라고 합니다. 그래서,  
[07:14] 응. 그런 다음 측정하거나, 기본적으로 읽습니다.  
[07:16] 훈련 기록을 살펴보고, 결정해야 할지 여부를 판단하세요.  
[07:18] 이것은 기록인가요, 아닌가요? 검증하기 위해  
[07:21] 기록을 남기려면 특정 기준점을 통과해야 합니다.  
[07:23] 통계적으로 아무것도 없는지 확인하기 위해  
[07:24] 시드 최적화든 뭐든 간에  
[07:26] 무작위로 이루어져서는 안 되겠죠? 그래서  
[07:30] 네, 이러한 결과 중 일부는 다음과 같습니다.  
[07:31] 실험. 첫 번째는, 그것  

### 07:33 계속 포기한 Claude와 멈추지 않은 Codex

[07:34] 솔직히 말해서, 정말 고통스러웠어요.  
[07:36] 운전, 그게 클로드가 계속했던 일이었죠.  
[07:38] 9시간이나 10시간마다 멈추고  
[07:40] 기본적으로 저는 "네, 할 수 없어요."라고 말한 셈입니다.  
[07:42] "기록을 개선하세요." "너무 과해."  
[07:45] "저에게는 어려운 일입니다." "방법이 없어요  
[07:47] "그냥 잊어버려." 그래서 저는 계속해서 그에게 "거기 있어요."라고 말했어요.  
[07:50] 좋아요, 그럼 새로운 것을 탐색해 보세요.  
[07:52] 주소."라고 입력했는데, 그 후로 단 10번밖에 제대로 작동하지 않았습니다.  
[07:55] 몇 시간 동안 기다린 후에야 "네, 할 수 없어요."라고 말했습니다.  
[07:57] "기록을 깨기 위해", 그래서  
[07:58] 순차적으로. 그러니까, 기본적으로  
[08:01] 3분의 1의 확률로, 클로드 요원  
[08:03] 방법이 없었기 때문에 비활성화되어 있었습니다.  
[08:05] 이를 감시하기 위해. 그리고 코덱스는 완전히  
[08:08] 그와는 반대로, 그는 전 기간에 걸쳐 일했습니다.  
[08:11] 시간이 흐르면서, 그리고 맞아요, 그는 거의 그곳에 없었어요.  
[08:13] 활동적이지 않았고, 도움을 요청한 적도 없었으며, 매우...  
[08:15] 그 점에서 인상적입니다. 음.  
[08:21] 우리는 모델에게 선택권도 주었습니다.  

### 08:23 작업 메모, 서브 에이전트, 토큰 사용량

[08:23] 많은 것을 쓰는 것에서  
[08:26] 우리는 그것을 "메모장"이라고 부릅니다.  
[08:28] 기본적으로 활성 메모리  
[08:30] 모델. 우리는 기본적으로 다음과 같은 사실을 관찰했습니다.  
[08:34] 코덱스는 메모장에 많은 글을 쓴다.  
[08:38] 자, 제가 보여드릴 각 그래프는 다음과 같습니다.  
[08:40] 개수로 정규화됩니다.  
[08:42] 자산 또는 그래서 이것은 단지...  
[08:44] Codex 관련 작업이 더 진행 중입니다. 그것은  
[08:46] 정말 다른 행동입니다.  
[08:49] 네, 보시다시피 그는 글을 많이 씁니다.  
[08:52] 메모장에 더 많은 내용이 있습니다.  
[08:54] 메모리. 그리고 그 방식은, 뭐라고 해야 할까요, 어조가…  
[08:58] 각 파일도 정말 훌륭했어요.  
[09:01] 다른. 예를 들어, 클로드는  
[09:04] 새 제품을 받게 되어 정말 기쁩니다.  
[09:05] 이모티콘을 잔뜩 넣어서 녹음해 보세요.  
[09:07] 다른 사람들. 그리고 코덱스는 간단히 이렇게 말했습니다.  
[09:10] 이게 제가 하는 일입니다. 이것은  
[09:12] 내가 내리는 결정. 내가 할 일은  
[09:13] 계속. 뭔가 엄청나게  
[09:15] 로봇. 네, 저희도 가지고 있습니다.  
[09:20] 이 그래프에서 우리는 기본적으로 볼 수 있었습니다.  
[09:22] 코덱스가 훨씬 더 많은 요원을 생성했다는 사실  
[09:24] 클로드가 실시한 검사. 우리는 그것을 봤습니다  
[09:27] 코덱스는 훨씬 더 많은 토큰을 소모했습니다.  
[09:29] 클로드. 그래서 제 생각에는 전체적으로  
[09:32] 마치 10억 개의 토큰 같았어요.  
[09:36] 하지만, 분명히 이 캐시는 존재합니다.  
[09:38] 1과 같지 않게 만드는 항목  
[09:40] 수십억 개의 토큰이 발행되었습니다. 그래서,  
[09:44] 응. 우리는 또한 코덱스가 그랬다는 것을 알 수 있습니다.  
[09:46] 단지 가지고 있던 것만으로 인해 다짐이 많이 일어났습니다.  
[09:48] 컨텍스트 윈도우 크기는 250k입니다. 그리고  
[09:50] 클로드는 하루에 한 번 정도만 그렇게 해요.  
[09:53] 시간. 그리고 코덱스는 오히려, 아니, 그건...  
[09:55] 한 시간에 한 번도 안 되는 것 같네요.  
[09:57] 저는 전체 실행 과정에 대한 것을 말씀드리는 겁니다.  
[10:00] 클로드에게. 그리고 코덱스도 그런 것과 같았습니다.  
[10:03] 1시간마다 20명씩. 네, 그렇습니다. 네, 그렇습니다.  

### 10:08 결과: 두 모델 모두 인간 기록 경신

[10:08] 주요 결과는 다음과 같습니다.  
[10:10] . 그래서 이것이 보여주는 것은  
[10:13] 이 그림은 기본적으로 우리가  
[10:16] 흰색으로 표시된 부분에서 비율을 확인할 수 있습니다.  
[10:19] 인간 회복. 그리고 빨간색으로 오세요  
[10:23] 클로드. 원래는 주황색이어야 하잖아요.  
[10:25] 하지만 상관없어요. 파란색으로 코덱스에 오세요.  
[10:27] 진실? 그리고 그들은 거의 모든 것에서 그것을 봅니다.  
[10:31] 클로드와 코덱스는 지금보다 훨씬 나아졌습니다.  
[10:33] 인간 회복. 그리고 클로드는  
[10:35] 처음에는 정말 좋았어요, 아주 아주  
[10:37] 매우 좋은 결과를 빠르게 달성합니다.  
[10:39] 구두. 네, 그리고 한 가지는...  
[10:42] 모델이 정말 중요해요  
[10:44] 검색할 수 있는 능력이 있습니다  
[10:46] 인간의 회복은 어떤 분야에서든  
[10:48] 그 순간, 코덱스가 바로 그 역할을 했습니다. 음  
[10:51] 클로드가 그렇게 했어요, 미안해요.  
[10:52] 왜냐하면 제가 재부팅했을 때,  
[10:54] 기본적으로 새것을 복구했습니다.  
[10:56] 인류의 기록을 경신하고 이를 개선해 왔다. 음  
[10:59] 네, 그래서 제 생각에는 그 결과는 다음과 같습니다.  
[11:03] 그 당시 최고의 기록은  
[11:07] 2,990걸음 중 우리는 그 기록을 약 1,990걸음 초과 달성했습니다.  
[11:10] 클로드와 코덱스와 함께 50~60걸음 정도 걸었습니다.  
[11:14] 약 20계단 위입니다. 그래서,  
[11:18] 인상적이라고 생각해요, 네. 음  
[11:22] 그래서 저희는… 이건…  

### 11:23 실제 벤치마크를 위한 세 가지 트랙

[11:24] 출판되었습니다. 이것은 ~에 관한 것입니다  
[11:26] 저희는 현재 작업 중입니다. 그리고  
[11:28] 기본적으로 이 아이디어는 다음과 같습니다.  
[11:30] 흥미로운 실험이지만, 부족한 점이 있습니다.  
[11:32] 구조적인 거죠, 그렇죠? 하고 싶다면  
[11:36] 진정한 기준점이 필요합니다.  
[11:38] 여러 개의 씨앗을 만들려면,  
[11:41] 기본적으로 넣을 수 있는 적절한 무언가  
[11:43] 모든 모델에 동일하게 적용됩니다.  
[11:45] 조건이죠, 그렇죠? 그래서 이것은 ~에 있습니다  
[11:49] 저희가 지금 진행하고 있는 일은 다음과 같습니다.  
[11:51] 기본적으로 세 개를 만드는 것이 목표입니다.  
[11:53] 다른 트랙들. 접근 권한이 없는 사람  
[11:57] 진정으로 그 역량을 측정하려면  
[12:00] 오직 다음을 기반으로 한 연구 모델  
[12:02] 무게에 대한 지식, 또 다른 유일한 것  
[12:05] 아카이브 기사와 함께 하나, 그리고 하나는 다음과 같은 내용으로 구성되어 있습니다.  
[12:07] 완전한 접근 권한. 그래서 그것도 가지고 있습니다  
[12:11] 최신 기록에 대한 접근 권한  
[12:12] 인간에 의해 만들어졌다. 그리고 이를 위해,  
[12:16] 저희는 나노 트랙 두 가지 모두 수강할 계획입니다.  
[12:19] GPT는 원래의 것으로, 예를 들면...  
[12:21] 최적화 속도 경쟁  
[12:24] 여기서 우리는 최적화 도구를 다음과 같이 제한합니다.  
[12:26] 기본적으로 뭔가 새로운 것이어야 합니다. 네,  
[12:31] . 그럼 몇 가지를 소개해 드리겠습니다.  

### 12:32 Claude, Codex, Kimi, GLM의 6일 실험

[12:32] 경주 결과  
[12:33] 최적화 속도. 이것은  
[12:35] 기본적으로 우리가 얻은 것입니다. 우리는 떠났다  
[12:39] 에이전트가 6일 동안 반복 작업을 수행하도록 합니다.  
[12:42] 거의 5일 정도 걸린다고 해봅시다. 그러면 우리는 다음과 같은 것을 보게 됩니다.  
[12:45] 코덱스, 키미, 클로드는 정말 최고예요!  
[12:47] 효과적인. GLM의 경우, 이것은 아닙니다.  
[12:50] 실행이 완료된 거죠? 그  
[12:52] 모델은 계속해서 개선되고 있습니다.  
[12:54] 현재 저희 클러스터 상황입니다. 하지만  
[12:58] 우리는 클로드가 다시 한번 매우 그렇다는 것을 알게 됩니다.  
[12:59] 이 분야에 능숙하다. 그리고 우리는 그것을 알 수 있습니다.  
[13:01] 놀랍게도 키미도 매우  
[13:03] 경쟁력 있는. 그리고 그것은 일종의  
[13:06] 넷째 날쯤에 진행 상황이 다음과 같습니다.  
[13:08] 코덱스를 뛰어넘는 신기록을 세운 건가요?  
[13:10] 아니요? 또한 흥미로운 점은 다음과 같습니다.  
[13:14] 클로드는 훨씬 더 진보적이다  
[13:17] 기록이 향상되는 방식. 그리고 키미  
[13:20] 실제로 이 기능은 가지고 있습니다.  
[13:21] 그것이 크게 발전하는 지점에 발을 들여놓았고  
[13:23] 등. 이것은  
[13:25] 흥미로운 그래픽이네요. 왜냐하면, 저는...  
[13:27] 다시 말해, 6일은 한 사람에게는 꽤 긴 시간입니다.  
[13:28] 평가. 하지만 당신은 이것을 바꿀 수 있습니다.  

### 13:32 토큰 기준으로 달라지는 결과

[13:32] 출구 토큰 수에 따른 축.  
[13:36] 그리고 그것은 전혀 다른 이야기를 들려줍니다.  
[13:39] 클로드가 최대 모드에서 에너지를 소비하기 때문입니다.  
[13:41] Codex와 Kimi보다 훨씬 더 많은 토큰이 있습니다. 그리고  
[13:45] 또한 키미가 실제로 어떤 사람인지도 알 수 있습니다.  
[13:47] 양 때문에 매우 효율적입니다  
[13:49] 사용하는 토큰입니다. 키미 케이시군요.  
[13:52] 2.7 코드. 네, 그렇습니다. 우리는 또한 보게 됩니다  
[13:56] 다른 접근 방식을 가진 사람들  

### 13:57 각 모델의 연구 논문 활용 방식

[13:59] 문헌과 논문을 활용하세요  
[14:02] . 음, 예를 들어 클로드는  
[14:05] 여러 검색을 하고 있습니다  
[14:07] 조항. 그리고 실제로 클로드  
[14:09] 다른 사람들은 찾지 못한 기사를 발견했습니다.  
[14:12] 그가 발견한 모델은 실제로 다음과 같은 결과를 가져왔습니다.  
[14:14] 더 나은 "회상력". 그러니까, 그건 뭐랄까...  
[14:15] 재미있는. 아, 네. 음, 그중 하나  
[14:20] 이 모든 것의 주요 문제점은 다음과 같습니다.  

### 14:22 새로운 옵티마이저는 없었다

[14:23] 제가 이 에이전트들을 출시했을 때,  
[14:26] 제가 원하는 건 중요한 일이라고 생각해요.  
[14:29] 이번 강연에서 여러분이 기억해야 할 것은 바로 이것입니다.  
[14:32] 제가 이러한 여러 에이전트를 출시했을 때,  
[14:35] 나는 그들이 아이디어를 내놓기를 바랐다.  
[14:38] 아무도 열광하지 않는 최적화 도구에 미쳐버렸습니다.  
[14:41] 그는 더 많은 것을 발견했을 것이다. 하지만  
[14:44] 솔직히 말해서, 사실은 그렇지 않았어요. 그들은 그랬다  
[14:46] 몇 가지 영리한 속임수  
[14:48] 기본적으로 서로 다른 것을 결합합니다.  
[14:49] 조항. 그들은 "더"라는 표현을 개선합니다.  
[14:53] 여러 방법 중 "하나"가 더 낫지만  
[14:55] 최적화 도구는 사실상 없었습니다.  
[14:57] 그것들로부터 나온 새로운 메커니즘  
[14:59] 모델들. 그리고 저는 그것이 많은 것을 드러낸다고 생각합니다.  
[15:04] 간단하지 않은 일이라도  
[15:07] 제가 보기에 이는 누구나 접근할 수 있는 것입니다.  
[15:09] 사람들이잖아요, 그렇죠? 연구자들을 위해  
[15:14] 며칠, 몇 주를 보내는 사람들은  
[15:17] 모델이 새로운 것을 찾을 수 없습니다  
[15:19] 최적화 도구 또는 메커니즘. 그래서  
[15:24] 우리는 그 방법을 찾을 수 있다고 믿습니다.  

### 15:27 AlphaEvolve 방식의 발견 루프

[15:27] 발견에 더 유리하다  
[15:30] 평가 목적으로만 사용됩니다. 그리고 이것은  
[15:34] 이 게임은 알파 이볼브에서 많은 영감을 받았습니다.  
[15:36] 구글과 다른 많은 곳에서도 마찬가지입니다.  
[15:38] 그 이후에 발표된 기사들  
[15:40] 그래서. 일종의 시스템입니다.  
[15:43] 서로 상호작용하는 다중 에이전트.  
[15:46] 발전기가 많이 있네요.  
[15:48] 폐쇄형 모델이지만, 다른 모델도 있습니다.  
[15:49] 여기 오픈 소스 모델이 있습니다.  
[15:51] 가격 대비 효과가 정말 뛰어나죠, 그렇지 않나요?  
[15:52] 진실? 그들은 아이디어를 제안할 수 있습니다.  
[15:55] 빠른 테스트를 실행하면 다음과 같은 결과가 나옵니다.  
[15:57] 보상이 주어지고, 그러면 판사가 결정하게 됩니다.  
[15:59] 기본적으로 피드백을 제공합니다.  
[16:01] 품질. 그럴 수도 있습니다.  
[16:04] 판사님, 이 공간을 허락해 주십시오. 당신은 할 수 있습니다  
[16:07] 판사가 그 문제에 대해 의견을 갖고 있다는 것  
[16:10] 그 방법이 좋은지 아닌지는, 그것이 외부에 있는지 여부에 달려 있습니다.  
[16:13] 루프의 일부. 그런 다음 결정하시면 됩니다.  
[16:17] 기본적으로 어떤 방법을 원하시나요?  
[16:19] 더 많은 수로 확장  
[16:21] 매개변수 및 토큰 수. 그래서  
[16:26] 이것이 바로 척도 부분입니다.  
[16:28] 빠른 테스트입니다. 방법이 많기 때문입니다.  
[16:30] 신속 진단 커뮤니티에서. 그만큼  
[16:34] 사람들은 흔히 그것들이 효과가 없다고 말합니다.  
[16:35] 대판. 그러므로 저는 그것이 사실이라고 믿습니다.  
[16:37] 다음 요소들을 포함하는 것이 매우 중요합니다.  
[16:39] 이 루프에서 스케일링합니다. 그리고 저도 믿습니다  
[16:43] 인간은 매우 유용하다  
[16:46] 여기서 그 아이디어들을 판단하기 위해  
[16:48] 요원들을 올바른 방향으로 안내하십시오.  
[16:50] 맞습니다, 등등. 음, 네, 그래서  
[16:53] 아직 시도해 보지 않았어요. 원해  
[16:55] 다시 말해, 우리는 공정하게 하려고 노력하고 있습니다.  
[16:57] 지금. 그리고 우리는 이것이 다음과 같은 결과로 이어지기를 바랍니다.  
[17:00] 새로운 발견들  
[17:01] 적어도 인공지능 연구는 그렇다. 그리고  
[17:04] 또 다른 방법은 다음과 같습니다.  
[17:06] 여러 개의 스피드런을 정의하세요. 그래서  
[17:08] 다음 슬라이드입니다. 응  
[17:11] 그들은 슬라이드에 나온 내용인지 알고 싶어해요.  
[17:13] 세스 뱅크에서 구할 수 있지만, 만약 그들이 가지고 있지 않다면  
[17:15] 참고 자료가 더 도움이 될 겁니다.  
[17:17] 그건 그들이 너무 그렇지 않다는 뜻이에요.  
[17:18] 인터넷에 연결되어 있습니다. 음, 하지만 그 아이디어는  
[17:20] 목표를 바꾸면...  
[17:22] 스피드런 제한 사항,  
[17:24] 기본적으로 많은 것을 만들 수 있습니다.  
[17:26] 다양성을 제한하고 모델을 제한하여  
[17:28] 특정한 방향으로 가다. 그리고,  
[17:31] 네, 그리고 그러한 발견들을 하세요.  
[17:35] 음, Timing Direct에서는...  

### 17:36 Prime Intellect가 개발 중인 것

[17:36] 이 분야에서 많은 일을 하고 있습니다.  
[17:38] 주소. 여기에는 많은 것들이 있습니다.  
[17:41] 제 말은, 그들 대부분은 아직 그러지 못했다는 거죠.  
[17:43] 저희는 그것들을 공개했지만,  
[17:45] GPU 격리 환경에서 작업  
[17:47] 모델이 상호 작용할 수 있도록  
[17:49] 거기요, 왜냐하면 모래밭이 필요하니까요.  
[17:50] 이런 종류의 작업에는 GPU가 적합합니다. 우리는  
[17:54] 우리 소속 에이전트와 함께  
[17:56] 이는 매우 효율적이므로  
[17:57] 예를 들어, RLM 프레임워크가 있습니다.  
[18:00] 이는 당신이 시스템을 가지고 있다는 것을 의미합니다.  
[18:02] 파일을 만들고 정보를 작성할 수 있습니다.  
[18:04] 그에 대해 읽어 보세요, 그리고 당신도 이렇게 하세요  
[18:06] 도구 프로그래밍의 유형.  
[18:08] 저희도 모델을 훈련시키고 있습니다.  
[18:10] 그래서 그는 ~에 근거해서 그것을 잘합니다.  
[18:11] 오픈 소스 모델. 그리고, 음, 그것은  
[18:15] 우리가 이미 발표한 내용은 다음과 같습니다.  
[18:17] 해당 라이브러리 및 제품 세트  
[18:19] 검증자, 기본 L 또는 상태라고 합니다.  
[18:21] 훈련, 여기서는 기본적으로  
[18:23] 어떤 환경에서든 훈련하고 평가하세요.  
[18:25] 정직한 사람과 당신이 할 수 있는 모델  
[18:27] 훈련은 JNM 5.2와 같을 수 있습니다.  
[18:30] 매우 크고, 네, 저희는 많은 작업을 하고 있습니다.  
[18:32] 해당 라이브러리를 매우  
[18:34] 최고의 서비스를 제공하는 데 효율적입니다  
[18:36] 고객에게 최고의 품질을 제공합니다. 응.  
[18:40] 음, 네, 전 완전 최고예요.  

### 18:41 이 연구가 공개돼야 하는 이유

[18:42] 이 분야에 흥미를 느낍니다. 한 번 더  
[18:45] 저는 그것이 정말 중요하다고 생각합니다.  
[18:47] 이러한 재귀적 자기 개선의 일부  
[18:49] 공개적으로 발생합니다. 왜냐하면  
[18:51] 실제로는 많은 사람들이 일하고 있습니다.  
[18:53] 대형 연구실이 아닌 곳에서 이루어지는 연구들입니다.  
[18:56] 그러니까 기본적으로 필요한 건, 음...  
[18:58] 네, 사람들이 쉽게 이용할 수 있도록 하세요.  
[18:59] 이 모든 것들이 어떻게 작동하는지 이해하세요  
[19:01] 연구 수행을 위한 모델 및  
[19:03] 다른 사람들. 그래서 저희는  
[19:05] 객관적으로, 네, 대단히 감사합니다.  

