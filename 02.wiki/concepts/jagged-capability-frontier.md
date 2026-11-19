---
title: 들쭉날쭉한 역량 경계 (Jagged Frontier)
type: concept
category: theory
tags: [capability, evaluation, astra, agi, unevenness]
related: [agi-definition, all-or-nothing-accuracy, skill-evals, ai-slop, openai-astra, capability-detour, differential-capability-limitation, demo-collaboration-gap]
first-seen: tech-bridge-brockman-agi-era-defender-window
sources: [tech-bridge-brockman-agi-era-defender-window, tech-bridge-claude-fable-5-2-announcement, tech-bridge-karpathy-hackertube-two-hours-five-words, tech-bridge-gpt-6-2-astra-launch-day-reactions]
created: 2026-09-20
updated: 2026-11-19
---

# 들쭉날쭉한 역량 경계 (Jagged Frontier)

**모델의 역량이 도메인마다 고르지 않게 앞서고 뒤처지는 상태.** [[greg-brockman|Greg Brockman]]이 [[tech-bridge-brockman-agi-era-defender-window]]에서 [[openai-astra|Astra]]의 남은 한계를 설명하며 쓴다.

> 누군가 트위터에 올린 그래프를 봤는데 **들쭉날쭉한 프론티어(jagged frontier)** 같은 것이었고, **우리가 정말 있어야 할 곳은 전 범위에 걸쳐 훨씬 더 고른 상태**입니다. (39:00~39:16)

> ⚠️ 출처는 *"누군가 트위터에 올린 그래프"* 뿐이다. 이 위키는 원 출처를 확인하지 못했다.

## 왜 이 위키에 필요한가

이 개념이 **AGI 논쟁의 형태를 바꾼다**:

> **AGI는 시점(point in time)이라기보다는 일종의 흐릿한 스펙트럼(fuzzy spectrum)으로 드러났다고 생각합니다.** (38:26~38:45)

**"들쭉날쭉하다"는 것이 곧 "시점이 없다"는 것**이다 — 축마다 다른 시점에 넘어가므로 단일한 문턱이 성립하지 않는다. → [[agi-definition]]

그래서 이 페이지는 [[agi-definition]]에 **네 번째 입장의 메커니즘**을 제공한다. [[andrew-ng]]는 정의를 높게 잡아 *decades*, [[sam-altman]]은 용어가 무의미, [[jensen-huang]]은 도달 후에도 남는 일 — 여기서는 **경계의 모양 자체가 점이 아니다.**

## 구체적으로 어디가 뒤처지는가

> 예를 들어 **글쓰기가 그렇습니다. 꽤 괜찮은 글입니다. [슬롭(slop)]이 아닌 건 이번이 처음이에요.** — **하지만 훌륭한 글은 아닙니다.** (38:47~39:00)

> **몇몇 영역에서 조금만 다듬으면 환상적일 것 같은데 딱 거기까지는 아직 못 갔다고 느낍니다.** (39:00~39:16)

**[[openai-astra]] 페이지가 2026-09-06 이후 처음으로 구체적인 한계를 받는 자리**이고, **[[ai-slop]]이 모델 제작사 쪽에서 평가 어휘로 쓰인 첫 사례**다 — 이 위키에서 *슬롭* 은 09-12 [[taste-labs]]의 **측정 대상**이거나 09-14 [[jonathan-kelley|Kelley]]의 **불만**이었다.

> ⚠️ **ko 자막이 이 문장을 파괴한다** — *"경사가 없는 건 이번이 처음이에요"*. en-orig의 *"not sloping"* 자체가 *slop* 의 오인식이고 ko가 그것을 기울기로 읽었다. **한쪽만 읽으면 품질 평가가 사라진다.**

## 이 위키에서의 좌표

| 페이지 | 다루는 것 |
|---|---|
| [[all-or-nothing-accuracy]] | **한 과제 안**에서 100%가 아니면 실패 |
| **이 페이지** | **과제 사이**에서 고르지 않음 |
| [[skill-evals]] | 그 불균일을 어떻게 잴 것인가 |
| [[capability-detour]] | 뒤처진 축을 우회하는 실무 대응 |

**[[capability-detour]](09-14, 펠리컨 SVG가 안 되면 PNG→벡터화)가 이 개념의 현장 판본**이다 — 들쭉날쭉함을 인정하고 **뾰족한 부분을 골라 쓰는 것**.

그리고 화자의 처방은 그 반대다 — *"전 범위에 걸쳐 훨씬 더 고른 상태"*. **사용자는 우회하고 제작자는 평탄화하려 한다.**

## ⚠️ 유보

- **측정이 없다.** 어느 축이 얼마나 앞서고 뒤처지는지 수치가 없고, *"글쓰기"* 하나만 예로 든다.
- **원 그래프의 출처 불명.**
- *"이런 도약을 한 모델은 우리가 정말 본 적이 없다"*(39:16~39:33)는 **자기 보고**다.

## References

- [[tech-bridge-brockman-agi-era-defender-window]] — first-seen
- [[greg-brockman]] · [[openai-astra]]
- 관련: [[agi-definition]] · [[all-or-nothing-accuracy]] · [[skill-evals]] · [[ai-slop]] · [[capability-detour]]

## 평균 10%의 안쪽 — Fable 5.2 표 (2026-11-11 · [[tech-bridge-claude-fable-5-2-announcement]])

[[fable-5-2|Fable 5.2]]와 [[claude-opus-5-5|Opus 5.5]]의 차이는 항목마다 다르다(해설 전달). 코딩은 45.5 → 49.1인데 로봇 제어는 39.4 → 64.9, Remote Labor Index는 21.3 → 41.3이다. 업무 자동화는 Gemini 4 Carbon이, 한 지식 업무 Elo는 Opus 5.5가 앞선다. 해설의 결론: *"평균 10%라는 말은 어디를 보느냐에 따라 맞기도 하고 틀리기도 합니다."*(02:12~02:17)

⭐ 같은 발표에 **의도한 함몰**도 있다. AI R&D를 앞당길 두 능력은 일부러 Opus 5.5 수준에 묶었다 → [[differential-capability-limitation]]. 표의 낮은 칸이 *못 한 것* 인지 *안 키운 것* 인지는 표만 보고 알 수 없다(위키의 읽기).

## 2026-11-19 — 들쭉날쭉함이 사용 격차의 이유로 ([[tech-bridge-karpathy-hackertube-two-hours-five-words]])

Karpathy의 10월 *냅킨 계산* 글(한국어 해설 전달, ⚠️ 원 글 미열람)이 AI를 깊이 쓰는 0.2%와 나머지가 벌어지는 이유 셋 가운데 둘째로 든다. 실력은 *"디지털이고 검증할 수 있고 돈이 되는 분야에서"*(01:53~01:55) 먼저 왔고 수학과 코드가 그렇다(01:53~01:58, 동사는 ASR 판독 보류). 나머지 둘은 야망(*"한 문단짜리 답을 묻는 질문으로는 시스템이 거의 힘을 쓰지 않습니다."*(01:47~01:49))과 접근(무료 · 유료 · 연구소 내부)이다.

이 페이지의 앞선 용법은 *모델의 한계* 를 말하는 것이었다(Brockman — 고르게 올라와야 한다). 여기서는 같은 성질이 **사람들이 보는 세상을 가르는 원인** 으로 쓰인다 — 어느 봉우리 위에서 일하느냐에 따라 모델에 대한 인상이 달라진다. 봉우리가 서는 조건 셋(디지털 · 검증 가능 · 수익)을 적은 것은 이 소스가 처음이다.

## 2026-11-19 — 바깥 사용자가 같은 말을 쓴다: GPT-6.2 Astra ([[tech-bridge-gpt-6-2-astra-launch-day-reactions]])

이 개념은 [[greg-brockman|Brockman]]이 Astra를 두고 쓴 말로 이 위키에 들어왔다(09-20, 제작사의 자기 평가). GPT-6.2 [[openai-astra|Astra]] 출시 첫날, 와튼 스쿨의 Ethan Mollick 교수가 같은 낱말로 평했다고 해설이 전한다: *"들쭉날쭉하고 이상하다. 다른 모델보다 다루기 어렵다. 하지만 야심찬 프로젝트를 맡기면 잘 해낸다고 썼습니다."*(01:32~01:38) ⚠️ 한국어 해설의 번역이고 원문의 낱말(*jagged* 인지)은 위키가 확인하지 않았다.

출시 첫날의 지형(모두 사용자 자기 보고):

| 앞선 쪽 | 뒤처진 쪽 |
|---|---|
| 3D · 게임(*세계 최고 수준* — [[theo|Theo]]) · 영상 편집 · 사람이 결과물만 보고 고르는 3D 평가 1등 | 긴 작업에서 멈춤 · 설명의 가독성 · 제자리 돌기(Theo) |
| 컴퓨터 사용 · 코드 품질(Theo의 칭찬) | 글쓰기 — 지나친 간결함(Every) |
| 한 번에 뽑아내는 결과물 | 변주 — 다른 프롬프트에서 같은 이름의 레벨(*벨웨더*) |

09-20에 Brockman이 든 뒤처진 곳이 *글쓰기* 였고, 두 달 뒤 바깥 팀(Every)이 든 것도 글쓰기다 — 다만 이유가 다르다(09-20 *훌륭하지는 않다* / 이번 *너무 압축한다*). 뒤처진 쪽이 **도메인이 아니라 일의 길이와 방식** 으로 갈린다는 것이 이 편의 새 조각이다. → [[demo-collaboration-gap]]
