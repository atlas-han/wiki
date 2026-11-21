---
title: Claude Opus 5.5
type: entity
category: model
tags: [anthropic, claude, opus, flagship, secondhand-claims]
aliases: [Opus 5.5, 오푸스 5.5]
sources: [tech-bridge-white-house-superintelligence-panel, tech-bridge-claude-duet-proactive-assistant, tech-bridge-nick-saraev-kimi-k3-1-vs-opus-5-5, tech-bridge-nick-saraev-gpt-6-1-terra-vs-opus-5-5, tech-bridge-nick-saraev-karpathy-ai-habits, tech-bridge-lance-martin-old-prompts-make-claude-worse, tech-bridge-claude-fable-5-2-announcement, tech-bridge-chase-ai-fable-5-2-prompting-rules, tech-bridge-addy-osmani-which-claude-model, tech-bridge-lydia-hallie-rethinking-claude-code-best-practices, tech-bridge-theo-fable-vs-opus-when-to-use, tech-bridge-ryan-carson-managing-20-agents, tech-bridge-fable-5-2-start-with-opus, tech-bridge-gpt-6-2-astra-launch-day-reactions, tech-bridge-zechner-ronacher-verification-is-overrated]
links: []
created: 2026-10-09
updated: 2026-11-21
---

# Claude Opus 5.5

[[anthropic|Anthropic]]의 Claude Opus 계열 모델. 이 위키에서는 [[tech-bridge-white-house-superintelligence-panel]]에서 진행자가 *"you announced Opus 5.5 in the last several days"*(17:58~18:01)라 하고 공동 창업자 [[tom-brown|Tom Brown]]이 설명하는 것으로 처음 등장한다.

> ⚠️ **이 페이지에는 1차 자료가 없다.** 발표일·벤치마크·가격·컨텍스트 길이는 어느 소스에도 없다. *"며칠 전 발표"* 는 진행자의 말이고 패널 녹화일 자체가 미확정(2026년, 10-03 이전)이다. 이 위키에서 직전 세대로 불린 이름은 [[fable-5-1]] 표의 *"Opus 5"*(2026-09-14 ingest, 진행자 서술)뿐이다 — **4.7 → 5 → 5.5 사이의 1차 기록이 없다.**

## 소스에서 확인되는 것

| 출처 | 진술 |
|---|---|
| [[tech-bridge-white-house-superintelligence-panel]] (18:18~18:37, Brown) | *"continues the normal progress (…) more IQ points (…) with each model release"* |
| 같음 (18:37~18:46) | 이전 모델보다 **더 긴 작업을 위임**할 수 있다 |
| 같음 (18:56~19:10) | 모델이 쓰는 소프트웨어가 많아져 제품이 *"higher quality, cheaper over time"* |
| 같음 (22:06~22:13, 진행자) | *"hopefully Opus 56 tells Tom, don't take that left"* — ⚠️ **"56"이 5.6(다음 버전 농담)인지 미판독** |

## 자막 주의

- en-orig 18:18 *"Opus 55"* = 5.5(같은 문장 앞뒤). ko 22:06 *"Opus 56"* → **"작품 56"**(Opus의 사전적 뜻).
- 같은 무대에서 [[jensen-huang|Huang]]이 *"Claude"* 로 리서치한다고 말했는데(19:59~20:04) ko는 **"클라우드"** — 모델 버전은 말하지 않는다.

## 위치

- 이 위키의 이전 Opus 페이지: [[claude-opus-4-7]] (2026-05). 5.x 세대의 페이지는 이것이 처음이다.

## 2026-11-08 — medium effort 기본 + Sonnet 위임 (Karpathy 습관, [[tech-bridge-nick-saraev-karpathy-ai-habits]])

Saraev 전달: Karpathy는 Opus 5.5를 *"exclusively on medium effort as his default. He does not use max effort."*(00:52~00:54) 그리고 Opus 5.5 medium이 Sonnet 서브에이전트들에게 위임하는 구조를 좋아한다. *Land or water?* 실험을 *"most of the world's knowledge is now compressed in the neurons of these models like Opus 5.5"*(03:13~03:17)의 예로 든다. ⚠️ 2차 전달, 비교 측정 없음.

## 4.8 → 5.5 교체만으로 비용 약 18% ↓ (2026-11-09 · [[tech-bridge-lance-martin-old-prompts-make-claude-worse]])

[[lance-martin|Lance Martin]] 워크숍 해설(⚠️ 벤더 자기 실험의 2차 전달): *"오퍼스 4.8에서 5.5로 해도 비용이 18%쯤 줄었는데 오디서를 한번 돌리자 9%가 더 줄었습니다."*(01:58~02:02) → [[prompt-debt]]. 이 페이지의 가격 기록 가운데 **Anthropic 쪽 숫자**는 이것이 처음이다(단, 단가가 아니라 한 과제의 상대 비용). ⚠️ 같은 영상 04:40의 *오퍼스 5.0 낮은 노력*과 같은 모델인지 모른다 — ASR · 더빙 모두 *5.0*이다.

## References

- [[tech-bridge-white-house-superintelligence-panel]] · [[tom-brown]] · [[anthropic]]

## Claude Duet의 판단 모델? (2026-10-24 · [[tech-bridge-claude-duet-proactive-assistant]])

발췌(화자 미상): *"also said that op 5.5 and that's a model that's going to decide what needs [?] with you first."* — [[claude-duet|Claude Duet]]이 무엇을 먼저 알릴지 정하는 모델로 읽힌다. ⚠️ *op 5.5* → Opus 5.5는 ASR 판독, 앞부분 무캡션.

## 첫 실사용 비교 — Kimi K3.1 Pro와 같은 프롬프트 데모 6종 (2026-11-01 · [[tech-bridge-nick-saraev-kimi-k3-1-vs-opus-5-5]])

[[nick-saraev|Nick Saraev]](추정, 설명란 · 태그 근거)가 [[claude-code|Claude Code]] max effort로 돌린 Opus 5.5를 [[kimi|Kimi K3.1 Pro]](Kimi Code)와 비교한다. 이 페이지 **첫 사용 결과 소스**다(이전은 발표 언급 · 2차 진술뿐).

- 평균 제작 시간 *"47 minutes and 2 seconds"*(01:04~01:06) vs Kimi 29분 41초.
- **완성도는 대체로 앞선다**: 키보드 *"greater visual fidelity"*(02:26~02:29), 랜딩 페이지의 상어 · 3D(대신 *"the page is a lot slower"* 05:17~05:19), 도시 속 타워 · 애니메이션, 액션 게임 *"10 out of 10 would play this game again"*(08:08~08:12).
- ⭐ **두 번 작동하지 않았다**: 키보드 첫 빌드 *"it's not loading"*(02:08) → 수정 요청, 마인크래프트 *"My character is incapable of moving forward"*(06:59~07:01). 화자 집계 *"Opus 5.5 uh so screwed up twice on this uh list of eight demos"*(07:13~07:19), 원인 추측 *"it just didn't I don't know, proof its work"*(07:21~07:24) — *"although I did run it on max mode"*(07:22~07:25). → [[agent-verification-skill]]
- 가격: *"Opus 5.5 is double the cost"*(09:48~09:50) — Kimi $2/$10 per 1M의 두 배라는 화자 진술. ⚠️ **이 페이지의 가격 1차 자료는 여전히 없다**(어느 단가의 두 배인지도 미발화, 실행은 플랜 기반).

> ⚠️ 한 제작자의 주관적 비교, 프롬프트 · 채점 기준 비공개, 8개 중 6개 데모만 영상에 나온다. 하네스(Claude Code)와 묶인 결과다. ko는 이 영상에서도 Opus를 **"작품"** 으로 옮긴다.

## 두 번째 비교 — GPT-6.1 Terra와 같은 프롬프트 데모 5종 · 벤치마크 그래프 (2026-11-02 · [[tech-bridge-nick-saraev-gpt-6-1-terra-vs-opus-5-5]])

같은 화자([[nick-saraev|Nick Saraev]] 추정)가 하루 뒤 같은 형식으로 [[openai-terra|GPT-6.1 Terra]]([[codex|Codex]])와 비교한다.

- 평균 제작 시간 *"43 minutes and 52 seconds"*(00:53~00:57) vs Terra 23분 43초, 출력 토큰은 Terra의 약 3배, 비용 약 12배(화자 진술). ⚠️ Kimi 편의 평균 47분 2초와 다른 것은 데모 세트 차이로 보인다.
- ⭐ **상위 복잡도에서 앞선다**: *"3D complexity in particular, Opus 5.5 just wiped the floor with Terra on."*(06:11~06:18) · *"at the higher levels of all of this, Opus 5.5 reigns supreme."*(06:27~06:31) · *"on upper echelons of quality, you know, it doesn't really hold a candle to Opus 5.5, especially in some design applications."*(11:28~11:35)
- **이번엔 명확한 작동 실패가 없다.** 시계 페이지에서 *"not seeing the watch on the right hand side. Don't know if that's intentional or if maybe something is broken."*(05:34~05:42) 한 번뿐이고 곧 *"far higher quality"* 로 평가한다. Kimi 편의 *"screwed up twice"* 와 대조 — ⚠️ 1회씩의 비교라 경향으로 묶지 않는다.
- 지구본 데모에서는 화자가 Terra 쪽 디자인을 더 좋아했고(01:58~02:06), 폭풍 시뮬레이션은 *"didn't really do that good of a job either"*(03:08~03:13).
- **그래프상 위치(화자가 읽은 값, ⚠️ 출처 미표기)**: Agents' Last Exam 비용 대비 점수에서 Terra를 이기는 유일한 모델 — *"The only situation in which it gets beat is by Opus 5.5."*(09:49~09:54) — 대신 작업당 약 $9 vs Terra 약 $1(09:58~10:02). → [[cost-vs-score-frontier]]

> ⚠️ 이 페이지의 **가격 1차 자료는 여전히 없다.** "약 12배"(데모 달러 사용량)와 "약 9배"(그래프 작업당 비용)는 서로 다른 화자 진술이고, Kimi 편의 *"double the cost"*(단가표)와도 단위가 다르다.

## Fable 5.2 발표의 기준선 · 권장 기본값 (2026-11-11 · [[tech-bridge-claude-fable-5-2-announcement]])

[[fable-5-2|Fable 5.2]] 발표문(해설 전달)에서 Opus 5.5는 **비교의 기준선**이자 **권장 기본값**이다.

- 리뷰어(Nick Saraev)의 평가: *"바로 아래 모델인 오퍼스 5.5와 비교하면 대략 10% 차이라는 거죠."*(01:28~01:30) 표에는 Opus 5.5가 앞서는 항목도 있다(한 지식 업무 Elo).
- 페르마의 마지막 정리 형식화에서 *"같은 조건에 오퍼스 5.5는 30시간이 지나도 27%에서 멈췄습니다."*(05:22~05:26)
- ⭐ 권고: *"대부분의 코딩과 지식 작업은 5스 [음악] 5. 시작하라고 권합니다. 가장 강한 일상형 모델이라는 표현까지 쓰죠."*(07:05~07:11)[=오퍼스 5.5로] Fable 안전장치에 걸린 요청도 *"이전 오퍼스 모델이"*(07:28~07:31) 대신 답한다(버전 미발화).
- ⚠️ 영어 더빙은 이 영상 초반에 Opus 5.5를 `Opus 3.0`으로 말한다(01:30 · 02:08).

## Fable 5.2 high의 비교 기준으로 (2026-11-12 · [[tech-bridge-chase-ai-fable-5-2-prompting-rules]])

[[chase-ai|Chase AI]]가 읽은 Frontier Code 2.0 표: Fable 5.2 high 45.3% · $6.72가 Opus 5.5 extra high보다 높고 Opus 5.5 max($12.82)와 거의 같다 — *"we're getting Opus 5.5 max performance at half the cost."*(01:39~01:42) 그래서 *Opus로 될 일이면 Fable을 낮은 강도로 돌릴 이유가 없다* — *"I could probably get this done with Opus."*(02:11~02:13) → [[reasoning-effort-levels]]

## 2026-11-13 — 가격  /  (해설 전달) · 기본값 medium · 스레드 모델 ([[tech-bridge-addy-osmani-which-claude-model]] · [[tech-bridge-lydia-hallie-rethinking-claude-code-best-practices]])

[[addy-osmani|Addy Osmani]]의 모델 선택 가이드 해설이 이 페이지에 없던 **가격** 을 준다(⚠️ 해설 전달, 원 글 · 공식 문서 미열람): 입력 $4 · 출력 $20 / 100만 토큰, 컨텍스트 100만, 캐시 읽기 100만 토큰당 20센트(Fable 5.2와 같음). Kimi 편의 *"Opus 5.5 is double the cost"*(Kimi $2/$10 기준)와 산술이 맞는다.

- *"먼저 결론부터 말하면 잘 모르겠을 때는 오퍼스 5.5를 에포트 미디엄으로 시작하면 됩니다."*(00:25~00:29) Claude Code 기본 모델 · API 기본 effort medium. 맞는 일: 여러 PR에 걸친 기능 개발 · 일상 디버깅 · 컴퓨터 사용 · 복잡한 재무 모델 문서.
- SWE-bench Pro(high 기준): medium −2.5p · 비용 70%, low −8p · 1/3, extra high +1.4p · 2.5배. Frontier Code 2.0 max 45.5%(11-10 발표문 해설의 *45.5* 와 같은 값). Terminal-Bench 3.0 high 58.9%로 Fable 5.1 max 58.0%를 토큰 절반으로 앞섬. 전부 low + 실패만 high 재실행 ≈ 97% · 17센트 vs 전부 high 95.3% · 29센트 → [[true-cost-to-perfect-answer]].
- 혼합: Opus 지휘 + Sonnet 5.5 워커가 단독보다 약 1/3 저렴 · 성능 비슷. Fable 5.1 어드바이저를 붙이면 약 1.7 오르고 비용 2.1배. 도구 사용 강제 시 400 오류, 항상 생각을 켠 채 동작 → [[model-mixing-economics]].
- 같은 날 [[lydia-hallie|Lydia Hallie]] 발표 해설: 올해 초 Opus 4.5보다 *의도와 코드베이스를 훨씬 잘 이해해* 중간 조종이 줄었다. 리디아의 구성은 지휘 세션 Fable · 작업 스레드 Opus 5.5.

## 2026-11-16 — 모범생 · 앨런: Theo의 기본 모델 ([[tech-bridge-theo-fable-vs-opus-when-to-use]])

[[theo|Theo]] 해설(⚠️ 원 영상 미열람): **시작은 Opus** — 공식 가이드와 같은 결론이지만 effort는 medium이 아니라 **high** 추천. SWE-bench Pro(medium −2.5p · 비용 70%, xhigh +1.4p · 2.5배)와 Frontier Code 2.0 max 45.5%는 11-12 가이드 해설과 같은 값으로 다시 나온다.

- **기질**: 시킨 일은 끝까지, 두세 번 확인 — *대신 시킨 일 자체는 의심하지 않는다*, 가만 두면 기능 · 스펙이 부푼다. 보완 한 줄 *좋은 생각 같으면 하고 아니면 다른 방법을 제안해라*. 리뷰어로는 *작은 PR에도 댓글 여덟 개* 인 앨런. → [[model-temperament-routing]]
- **속도** 112 tok/s(Theo 측정), Fable 5.2 106과 거의 같다.
- **구독 효율**: 월 200달러 요금제로 API 값 약 14,600~15,000달러 치(Theo 계정 3달 · 110만 요청) — Fable의 약 5배. → [[bring-your-own-subscription]]
- 검증 가능한 일(TypeScript → Rust 재작성)은 Opus로 충분. Opus의 선택지가 뻔하거나 같은 자리를 맴돌 때 Fable로.

## 2026-11-17 — *엔지니어링 매니저* 자리의 모델 ([[tech-bridge-ryan-carson-managing-20-agents]])

[[ryan-carson|Ryan Carson]]의 9월 글(해설 인용): *"엔지니어링 매니저는 오퍼스 5.5, 여기에 데빈과 리니어, 그리고 로컬 개발은 전혀 하지 않는다."*(02:01~02:05) — 코드를 쓰지 않고 빌더 에이전트를 배정 · 확인하는 매니저 세션에 Opus 5.5를 둔다는 뜻으로 읽힌다(위키 해석, 10월 발표 시점에도 같은지는 미확인).

## 2026-11-18 — *먼저 쓸 모델* 의 자리 굳히기 ([[tech-bridge-fable-5-2-start-with-opus]])

종합 해설이 Opus 5.5를 기본 출발점으로 다시 세운다: *"대부분의 일은 오퍼스 5.5, 기본 노력 수준인 미디엄에서 시작하라."*(01:30~01:34) 부족하면 검증 수단 → effort 한 단계 → 그다음에야 큰 모델. Fable로 넘어가는 때는 *"오퍼스를 하이까지 올려도 모자랄 때, 그리고 오래 혼자 돌려 둘 때입니다."*(02:14~02:18) 지휘자 자리에서도 쓰인다 — 소스 코드 2,200만 토큰 결함 탐색에서 Opus 지휘 + Sonnet 일꾼이 Opus 단독보다 1/3쯤 싸고 점수는 비슷했다(11-13 가이드 해설과 같은 사례). Claude Code의 Explore 서브에이전트가 세션 모델을 따를 때 *"API 기준 상한은 오퍼스입니다."*(04:10~04:12) ⚠️ 해설 전달, 원 문서 미열람.

## 2026-11-19 — GPT-6.2 Astra를 써 본 사람들의 기준 모델 ([[tech-bridge-gpt-6-2-astra-launch-day-reactions]])

GPT-6.2 [[openai-astra|Astra]] 반응 모음(⚠️ 해설 전달 + 원음 발췌 하나)에서 불만을 말하는 두 사람이 Opus를 맞은편에 세운다.

- [[theo|Theo]] — 컴퓨터 한 대에서만 작업이 느린 이유를 묻자 Astra는 패키지 관리자의 내부 동작을 네 문단 늘어놓았다. *"같은 질문에 클로드 오퍼스 5.5에 답은 한 줄이었습니다."*(02:38~02:41) — *SSD가 느려져요.*
- 개발 유튜버 vogel(원음) — 사내 장난감 프로젝트에서 Astra가 리뷰와 재확인에 계속 걸리자 Opus로 바꿨다: *"Opus understood that the goal was to get it out there"*(05:17~05:20)<!--k--> *"it feels better to use Opus because it feels like it's on your team"*(05:28~05:32)<!--k--> ⚠️ vogel은 버전을 말하지 않는다(*Opus*).
- Every의 자체 코딩 벤치마크: Astra 39점쯤, *클로드 모델들* 40~41점(어느 모델인지는 말하지 않음).

둘 다 점수가 아니라 **목표를 읽는 방식** 의 비교다 — 무엇을 답하면 되는지, 이 일의 끝이 어디인지. ⚠️ 두 사람의 일화이고 과제는 각각 하나다.

## 2026-11-21 — 에이전트 제작자의 평: *감독 없이 훨씬 오래* ([[tech-bridge-zechner-ronacher-verification-is-overrated]])

[[matt-pocock|Matt Pocock]]이 [[pi-coding-agent|Pi]]를 만드는 두 사람에게 던진 첫 질문이 *"오퍼스 5.5 이후로 뭐가 달라졌나?"*(00:49~00:51) 였다(한국어 해설의 전달).

- [[armin-ronacher|Armin Ronacher]]: *"어떤 종류의 일은 이제 감독 없이 훨씬 오래 맡겨둘 수 있게 됐다고 답합니다."*(00:53~00:57)
- *거짓말을 덜 한다* 는 평가가 한 구절로 전해진다: *"거짓말을 덜 한다는 말 끝에 마리오가 예전 모습이라며 꺼낸 게 처음에 그 밤샘 실험입니다."*(01:46~01:50) → [[reward-hacking]]
- 한계는 그대로라는 쪽: *"정답이 없고 경험이나 감이 필요한 모호한 일은 형편없다. 목표까지 길이 곧게 뻗은 일은 믿을 수 있다."*(04:04~04:08)([[mario-zechner|Mario Zechner]]) 그리고 *"모델이 나올 때마다 무엇을 맡겨도 되고 무엇을 안 되는지 다시 배운다고 합니다."*(04:24~04:29)

⚠️ 두 사람의 답 원음(01:04~01:46)은 두 트랙 모두 무캡션이라 위 문장들은 내레이션의 요약이다. 모호한 일 · 곧은 일의 구분이 Opus 5.5에 한정한 말인지 에이전트 일반에 대한 말인지는 캡션으로 가릴 수 없다. 수치 없음.
