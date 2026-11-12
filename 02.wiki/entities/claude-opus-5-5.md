---
title: Claude Opus 5.5
type: entity
category: model
tags: [anthropic, claude, opus, flagship, secondhand-claims]
aliases: [Opus 5.5, 오푸스 5.5]
sources: [tech-bridge-white-house-superintelligence-panel, tech-bridge-claude-duet-proactive-assistant, tech-bridge-nick-saraev-kimi-k3-1-vs-opus-5-5, tech-bridge-nick-saraev-gpt-6-1-terra-vs-opus-5-5, tech-bridge-nick-saraev-karpathy-ai-habits, tech-bridge-lance-martin-old-prompts-make-claude-worse, tech-bridge-claude-fable-5-2-announcement, tech-bridge-chase-ai-fable-5-2-prompting-rules]
links: []
created: 2026-10-09
updated: 2026-11-12
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
