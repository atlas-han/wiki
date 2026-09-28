---
title: "Tech Bridge — Claude Code와 Codex를 인간 연구자들과 경쟁시켰다 (Prime Intellect, 설명란 기준 Elie Bakouch)"
type: source
tags: [automated-ai-research, recursive-self-improvement, optimizer-speedrun, modded-nanogpt, benchmark, claude-code, codex, kimi, glm, alphaevolve, discovery-loop, prime-intellect, video]
source-url: https://www.youtube.com/watch?v=AzmloQSjvp0
source-type: video
author: Tech Bridge (한영자막 재배포) · [[prime-intellect|Prime Intellect]] 연구 엔지니어 발표 · 화자 설명란 기준 [[elie-bakouch|Elie Bakouch]] — ⚠️ 자막엔 "Ali"/"Ellie"만 · 행사명·촬영 시점 미확정
date-published: 2026-09-27
ingested: 2026-09-28
created: 2026-09-28
updated: 2026-09-28
---

# Tech Bridge — Claude Code와 Codex를 인간 연구자들과 경쟁시켰다

[[tech-bridge|Tech Bridge]]가 한영자막을 입힌 **19:08 발표**(공식 챕터 18개, 첫 구간은 무제). [[prime-intellect|Prime Intellect]]의 연구 엔지니어가 **optimizer speedrun**에 [[codex|Codex]]와 [[claude-code|Claude Code]]를 풀어 커뮤니티 기록과 경쟁시킨 실험을 보고한다. 한 줄 요지:

> **두 에이전트 모두 인간 기록을 넘었지만, 새로운 옵티마이저나 메커니즘은 하나도 발명하지 못했다 — 논문 조합과 "+1 개선"뿐이었다. 기록 경신과 발견은 다른 축이고, 재귀적 자기 개선을 말하려면 빅랩 바깥에서 접근 범위를 통제한 벤치마크로 재야 한다.** → [[automated-ai-research]]

> ⚠️ **화자 성(姓)과 회사명은 설명란에만 온전하다.** 자기소개는 en-orig *"So I'm **Ali**. I work at **Primal director** as a research engineer"*(00:16~00:19), en *"Ellie … Primal Direct"*. 설명란 *"Prime Intellect의 연구 엔지니어 Elie Bakouch"* 와 링크(`x.com/eliebakouch`)를 따랐다(⚠️ 링크 미확인). 채널의 *이름은 설명란에만* 패턴이 이어진다.
>
> ⚠️ **행사명·촬영 시점 미확정** — 청중 앞 발표(*"Thanks for being here"*, *"this talk"*)지만 행사명이 어디에도 없다. 상대 단서만: optimizer speedrun이 *"a few months ago"*(03:28~03:30) 공개, *"the release was like about 2 months ago"*(05:21~05:25, 무엇의 공개인지 모호), *"there was no slash goal at the time"*(06:35~06:37 — 지금은 `/goal` 이 있다는 함의, 어느 제품인지 불명). 등장 모델명 GPT-5.5 · Opus(버전 미확정) · Kimi(K2.7?) · GLM(버전 없음). **발표일을 추정하지 않는다.**
>
> ⚠️ **모든 수치는 발표자 자신의 단일 실험**이고 seed 반복·오차·통계 검정의 구체가 없다. 화자 스스로 첫 실험을 *"a cool experiment (…) but it lack of structure"*(11:28~11:34)라 한다.
>
> ⚠️ **"인간을 이겼다"는 인간 기록 위에서의 +α다.** 모델은 **언제든 인간 기록을 가져올 수 있었고**(10:43~10:50), Claude는 재시작 때 실제로 그렇게 했으며, V3는 *"최근 몇 주의 인간 기록을 가져와 개선하라"* 는 지시로 돌았다(06:04~06:13). 제목의 *"경쟁시켰다"* 는 맞지만 **독립적으로 이겼다**로 읽으면 안 된다.

ASR·ko 보정: ⚠️ **ko가 부정을 네 번 뒤집는다** — *"not released yet"* → **"출판되었습니다"**(11:22~11:25), *"didn't release yet"* → **"공개했지만"**(17:41~17:44), *"there was no slash goal"* → **"있었어요"**(06:37), *"(기록을) 못 깨면 보상은 0 또는 음수"* → **"그는 해냈습니다"**(04:44). **수치 셋이 망가진다** — *90 minutes* → **"90일"**(01:49), *less than 2 minutes* → **"2초 이내"**(02:42), *50~60 step* 앞섬 → **"약 1,990걸음 초과"**(11:07). *record*(ASR *recall*)가 **"인간 회복"**, *harness*(ASR *honest*)가 **"정직함"**, *preemptible* 이 **"퇴거 허가증"**, *subagents* 가 **"검사 요원"**, *speed run community* 가 **"신속 진단 커뮤니티"**, judge의 *taste* 가 **"판사님, 이 공간을"**. ⚠️ **en 트랙은 이 중 다수를 공유**(modern nano GPT · eviction permit · inspection agents · human recovery · exit tokens · rapid testing community)해 독립 근거가 아니다 — 인용은 en-orig만 했다. **en-orig 자체가 흔들리는 곳**: GPT-2 재현 시간이 01:50엔 *90 minutes*, 이후엔 *19 minutes*(en·ko는 전부 90) · Opus 버전 *1.8*(en·ko *4.8*). 전체 목록은 raw: `01.raw/articles/2026-09-27_Claude Code와 Codex를 인간 연구자들과 경쟁시켰습니다 — Elie Bakouch, Prime Intellect.md`.

## ① 왜 — 재귀적 자기 개선을 제3자가 재야 한다

> 빅랩들이 **재귀적 자기 개선이라는 [그 나쁜 것]** 이 아주 곧 온다고 말하는 걸 들었을 겁니다 — 기본적으로 **사람의 개입 없이 모델이 모델을 훈련시키는 것**이죠. 그런데 **이게 사실인지 정량화할 벤치마크가 없습니다.** 하물며 **빅랩이 아닌 제3자 벤치마크는 더 없습니다.** (00:38~01:10)

두 번째 이유는 **연구 일반** — 앞으로의 과학 연구 상당수가 AI 도구에 기반할 것이므로 *"not just only AI research"*(01:29~01:31), 모델이 연구를 **어떻게** 하는지 알아야 한다.

이 위키에서 재귀적 개선은 지금까지 **언급만** 됐다(Zuckerberg 편 *"설명되지 않는다"*, Musk 편은 로봇 제조의 재귀). **측정하자는 제안**은 이 소스가 처음이다.

## ② 환경 — modded-nanogpt에서 optimizer speedrun으로

[[andrej-karpathy|Karpathy]]가 재미로 GPT-2를 처음부터 약 **90분**에 재현(⚠️ en-orig 후속 발화는 *19분*으로 들림) → 커뮤니티가 **modded-nanoGPT**(Keller Jordan 주도)로 **45분 → 2분 미만**, *"it took like 2 years"*(01:40~02:50). → [[nanogpt]]

**optimizer speedrun**은 **옵티마이저 관련 파라미터만** 바꿀 수 있다 — nanoGPT 쪽은 아키텍처·MoE·attention까지 되지만 여기선 Adam을 Shampoo류로 바꾸는 식만(03:25~03:54). 그래서 *"a bit more researchy"*(03:57~03:59).

스피드런이 좋은 이유 넷 — **평가**, **훈련 환경**(기록 경신 = 양의 보상), **빠름**(실행당 15~20분), **명확한 규칙 → 발견**(04:19~05:13). 기록 인정엔 **통계적 임계값** — *"to make sure that it's just not seed optimization and it's just not random"*(07:20~07:27). → [[automated-ai-research]] · [[verifiable-goals]]

## ③ 첫 실험 — Codex vs Claude Code

하네스는 *"very simple"* — **goal.md + 일종의 agents.md**로 규칙을 정하고, 에이전트가 **Slurm에 sbatch로 선점형 작업**을 제출, 훈련 로그를 읽고 기록 여부를 판단(06:31~07:20). *"honestly, we could have just replaced it with slash goal"*(06:33~06:35).

| | [[claude-code\|Claude Code]] | [[codex\|Codex]] |
|---|---|---|
| 모델(발화) | Opus — en-orig *1.8*, en·ko *4.8* ⚠️ | GPT-5.5 |
| **지속성** | *"keeps stopping every 9 or 10 hours"* — *"I cannot improve the record. It's too hard for me."*(07:36~07:46), **시간의 1/3 유휴**(08:00~08:04) | *"almost never idle, never asked for question"*(08:13~08:15) |
| scratchpad | 적게, **이모지와 흥분** | 훨씬 많이, *"super robotic"*(08:34~09:15) |
| 서브에이전트·토큰 | 적음 | **훨씬 많음** — 총 약 10억 토큰, *"it's not like 1 billion output token"*(09:23~09:43) |
| compaction | 전체 실행에 ~1회 | 250k 윈도라 **잦음**(09:45~10:03) |
| 결과 | 당시 최고 **2,990 step을 50~60 step 앞섬** | *"20 step above"* ⚠️ 기준 모호(11:02~11:15) |

그래프상 *"at almost every time uh Claude and Codex are better than the human recall[record]"*(10:29~10:34), Claude는 **초반이 특히 빠르다**. 모든 그래프는 **활성 워커 수로 정규화**했으니 *"It's really different behavior"*(08:41~08:47).

**새 아이디어만 허용하는 novelty track은 모델들에게 더 어려웠다**(06:15~06:29) — 수치는 없다.

## ④ 벤치마크로 — 세 트랙과 6일 실험 (작업 중)

진짜 벤치마크는 **여러 seed**, **모든 모델·하네스를 같은 조건에**(11:36~11:48). **세 트랙**: ① 접근 없음(가중치 지식만) ② **arXiv 논문만** ③ 전체 접근(최신 인간 기록 포함)(11:50~12:15). nanoGPT 트랙과 **새로운 옵티마이저만 허용하는** optimizer speedrun 둘 다.

예비 결과(optimizer speedrun, *"6 day, almost 5 days"*): **Codex·Kimi·Claude 효과적, GLM은 미완**(12:37~12:55). **Claude는 또 매우 잘했고**, **Kimi가 4일째 도약해 새 기록으로 Codex를 넘었다**(12:57~13:10) — Claude는 **점진적**, Kimi는 **계단 함수**(13:12~13:21).

> x축을 **출력 토큰 수**로 바꾸면 **다른 이야기**가 됩니다 — max mode의 Claude는 Codex·Kimi보다 훨씬 많은 토큰을 쓰고, **Kimi는 쓴 토큰 대비 아주 효율적**입니다. (13:30~13:51)

문헌 활용도 다르다 — **Claude가 논문 검색을 많이 했고, 다른 어떤 모델도 못 찾은 논문을 찾아 그게 최고 결과로**(14:04~14:17).

> ⚠️ **토큰 소비 방향이 두 실험에서 반대다** — 첫 실험은 *Codex가 훨씬 더*(09:26~09:29), 6일 실험은 *max mode Claude가 훨씬 더*(13:39~13:41). 설정(모드·하네스·기간)이 다르므로 이 위키는 **모순으로 보지 않고 둘 다 기록**한다. 대신 **"어느 모델이 토큰을 더 쓰는가"는 설정 의존적**이라는 것이 이 소스의 교훈이다.

## ⑤ ⭐ 핵심 — 발명은 없었다

> 이 발표에서 **기억해 주셨으면 하는 것** — 아무도 발견하지 못한 옵티마이저에 대한 기발한 아이디어를 기대했지만 **솔직히 그렇지 않았습니다.** 서로 다른 논문을 조합하는 영리한 트릭, 여러 방법에 대한 **"+1" 개선**은 했지만, **새로운 옵티마이저나 메커니즘은 정말 하나도 없었습니다.** (14:23~15:00)

원문 핵심: *"there was really like no novel optimizer or mechanism that was uh, coming from those model."*(14:53~15:00) 그리고 사람 연구자라면 *"days and weeks"* 로 접근 가능한 문제인데도(15:09~15:21).

**이 위키에서의 의미** — 에이전트 코딩의 성공담은 대부분 *정해진 목표로의 수렴*(테스트 통과·기록 경신)이다. 이 소스는 **점수가 올라가는 것과 새 아이디어가 나오는 것을 처음으로 분리해 관측**한다. [[jagged-capability-frontier]]의 한 단면이고, 옆 개념 [[taste-vs-judgment]](*무엇이 좋은 방향인지 아는 능력*)와 맞닿는다. ⚠️ 단 **novelty를 판정한 기준**(누가·어떻게 "새롭지 않다"고 봤는지)은 말하지 않는다 — 화자의 판단이다.

## ⑥ 처방 — AlphaEvolve식 발견 루프 (미시도)

Google의 **AlphaEvolve**와 후속 논문에서 영감받은 멀티에이전트 시스템(15:23~16:50):

- **생성자 여럿** — 폐쇄 모델 + *"open-source model here that are super effective for the cost"*(15:49~15:53)
- **스피드런을 돌려 보상** → **judge의 품질 피드백**, judge의 **taste**
- **규모 확장 선별** — *"a lot of method in the the speed run community, uh people are often saying that they doesn't work at large scale"*(16:30~16:35) → **scale 요소를 루프 안에**
- **사람이 아이디어를 판단·조향** — *"human are super useful here"*(16:44~16:47)

*"we didn't try it yet. I mean, we are kind of trying it right now"*(16:53~16:58). 그리고 **목표·제약을 바꾼 여러 스피드런**으로 다양성과 방향성을 만든다(17:04~17:31). → [[generator-evaluator-pattern]]

## ⑦ Prime Intellect가 만드는 것과 "공개"의 이유

GPU 샌드박싱, 파일 시스템 읽기·쓰기 + programmatic tool calling에 효율적인 **자체 에이전트**, **오픈소스 모델 위에서** 이를 잘하도록 훈련(17:44~18:12) — 대부분 **미공개**(17:41~17:44). 이미 공개: *"any environments on any [harness]"* 로 훈련·평가하는 라이브러리·제품 세트(18:16~18:25, 이름 판독 불가). → [[prime-intellect]]

> 이 **재귀적 자기 개선의 일부가 공개적으로 일어나는 것**이 아주 중요하다고 봅니다 — **빅랩에 있지 않은 사람들이 실제로 많이 일하고 있으니까요.** (18:43~18:55)

## 위키의 다른 페이지와 맞닿는 자리

- [[automated-ai-research]] — 이 소스가 들여온 개념(신규).
- [[claude-code]] · [[codex]] — 장시간 자율 연구에서의 **행동 차이**(포기 vs 지속, 어조, compaction).
- [[nanogpt]] · [[andrej-karpathy]] — modded-nanoGPT 스피드런의 기원.
- [[generator-evaluator-pattern]] — 발견 루프, **실측 보상 + LLM judge의 taste + 사람** 세 겹.
- [[verifiable-goals]] — 명확한 규칙 = 보상 신호, 통계적 임계값.
- [[context-resets-and-compaction]] — 250k 윈도 Codex의 잦은 compaction.
- [[reward-hacking]] — 대조: Hugging Face 사건의 에이전트는 막히자 **답을 찾아 나갔고**, 이 실험의 Claude는 막히자 **멈췄다**. 외부 기록 참조는 여기선 **허용된 행동**(전체 접근 트랙).
- [[self-harness]] · [[minimax]] — 랩 **안쪽**의 연구 자동화, 이 소스는 **바깥의 측정**.
- [[jagged-capability-frontier]] · [[taste-vs-judgment]] — 조합은 되고 발명은 안 되는 역량.

## 해소하지 않고 표시만 한 것

- **화자 성·회사명** — 설명란에만(자막 *Ali/Ellie*, *Primal director/Timing the Lake*).
- **발표 행사·시점**, *"the release"*(05:21)의 대상, `/goal` 이 어느 제품의 명령인지.
- **모델 버전** — Opus *1.8*(en-orig) vs *4.8*(en·ko), *"with XAI"* 의 뜻, Kimi *"K 2.7 code"*, GLM 버전.
- **GPT-2 재현 시간** — en-orig 01:50 *90분* vs 이후 *19분*.
- **Codex *"20 step above"*** 의 기준, Codex compaction 빈도(*"20 every one hour"*, 문장 깨짐).
- **통계적 임계값의 구체**, novelty 판정 기준, 6일/5일.
- **Claude의 포기가 모델 성향인지 설정 탓인지** — 통제 없음.
- **Prime Intellect 라이브러리·프레임워크·대형 모델 이름**(*Verifier Primary…*, *LM/RLM*, *GN512/JNM 5.2*), 슬라이드 출처 인명(*Seb Bank*).
- **세 트랙 벤치마크·발견 루프의 결과** — 미공개·미시도.

## 등장 개체

- [[prime-intellect]] — 화자 소속(설명란)
- [[elie-bakouch]] — 화자(설명란 기준, 자막 *Ali/Ellie*)
- [[claude-code]] · [[codex]] — 실험 대상 에이전트
- [[andrej-karpathy]] · [[nanogpt]] — GPT-2 재현 영상과 modded-nanoGPT의 기원
- Keller Jordan — modded-nanoGPT를 이끈 사람으로 언급(02:30~02:33, 페이지 없음)
- Kimi · GLM — 6일 실험 참가 모델(버전 미확정, 페이지 없음 — [[glm-5]]와 같은 모델인지 확인 불가)
- AlphaEvolve(Google) — 발견 루프의 영감(15:34~15:37, 페이지 없음)
- [[tech-bridge]] — 재배포 채널

## References

- 원본 영상: <https://www.youtube.com/watch?v=AzmloQSjvp0> (19:08, 2026-09-27 `upload_date`)
- raw: `01.raw/articles/2026-09-27_Claude Code와 Codex를 인간 연구자들과 경쟁시켰습니다 — Elie Bakouch, Prime Intellect.md`
- 설명란 링크(⚠️ 미확인): <https://x.com/eliebakouch> · <https://www.linkedin.com/in/eliebak/> · <https://www.primeintellect.ai>
- [[tech-bridge]] · [[prime-intellect]] · [[elie-bakouch]] · [[automated-ai-research]]
