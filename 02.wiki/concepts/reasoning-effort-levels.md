---
title: "추론 강도 (Reasoning Effort Levels) — 강도로 바꿀 것과 프롬프트로 바꿀 것"
type: concept
category: technique
tags: [reasoning-effort, effort-level, cost, benchmark, fable-5-2, claude-code, api, prompt-engineering]
aliases: [effort level, reasoning effort, 추론 강도, effort setting, low/medium/high/xhigh/max, extra high, xhigh]
related: [prompt-debt, ultracode, model-mixing-economics, token-roles, fable-5-2, claude-opus-5-5, model-temperament-routing]
first-seen: tech-bridge-chase-ai-fable-5-2-prompting-rules
sources: [tech-bridge-chase-ai-fable-5-2-prompting-rules, tech-bridge-addy-osmani-which-claude-model, tech-bridge-theo-fable-vs-opus-when-to-use, tech-bridge-fable-5-2-start-with-opus, tech-bridge-pocock-networkchuck-what-to-learn-instead-of-languages]
created: 2026-11-12
updated: 2026-11-24
---

# 추론 강도 (Reasoning Effort Levels)

**모델이 답하기 전에 얼마나 생각할지를 정하는 설정(low · medium · high · extra high · max).** [[fable-5-2|Fable 5.2]] 같은 상위 모델에서 이 다이얼이 **비용 대비 성능** 을 가장 크게 바꾼다는 주장과, 강도로는 **바뀌지 않는 것** 의 목록이 [[tech-bridge-chase-ai-fable-5-2-prompting-rules]]([[chase-ai|Chase AI]])에서 나왔다.

> ⚠️ **한 실무자가 공식 가이드 · 시스템 카드 · 벤치마크 표를 읽어 준 것이다.** 위키는 원 문서를 열지 않았다. 기본값(API high · Claude Code medium)은 영상 시점의 진술이고 바뀔 수 있다.

## 강도가 바꾸는 것

| 무엇 | 화자의 진술 |
|---|---|
| 비용 대비 성능 | medium → high에서 *"our biggest jump in terms of performance per dollar"*(01:02~01:07). Frontier Code 2.0: high 45.3% · $6.72 ≈ Opus 5.5 max($12.82), medium 37.6% · $2.48 |
| 생각의 양 | *"how much it's going to think is going to be a function of your effort level."*(05:44~05:45) |
| 완주율 | low · medium에서 조기 종료가 두드러지고 위로 갈수록 준다(03:45~03:55) |
| 서브에이전트 자발성 | extra high · max에서 자기 작업을 검사하는 서브에이전트를 스스로 띄운다(08:09~08:19) → [[ultracode]] |
| 위쪽 끝의 수익 | max는 대체로 피하라 — 값은 많이 내고 점수가 extra high보다 낮을 때도 있다(02:23~02:32) |

## 강도가 바꾸지 않는 것 — 프롬프트의 몫

- **생각을 할지 말지.** Fable 5.1에서는 *"Don't deliberate"* 가 통했지만 5.2는 *"It is always going to think."*(05:41) — 줄이려면 강도를 내린다.
- **말투와 길이.** *"This is not something that can be affected by the effort level."*(09:32~09:36) low에서 짧아지길 기대하지 말고 프롬프트 · CLAUDE.md에 적는다.

## 고르는 규칙 (화자)

1. 그 일을 [[claude-opus-5-5|Opus 5.5]]로 할 수 있으면 Fable을 low · medium으로 돌릴 이유가 없다 — Opus를 쓴다.
2. Fable이 필요한 일(어렵거나 긴 에이전트 작업)이면 **high에서 시작**, 모자라면 extra high.
3. max는 예외로.

→ 위키의 읽기: *모델 선택* 과 *강도 선택* 이 한 축이 된다. 낮은 강도의 상위 모델은 높은 강도의 하위 모델과 경쟁한다 — [[model-mixing-economics]] · [[token-roles]]의 *역할별로 모델을 섞는다* 에 **강도라는 둘째 다이얼** 이 붙는다.

## 미해결

- 같은 표의 다른 벤치마크 · 과제에서도 high가 *가성비 꼭짓점* 인지. 화자는 *"across a number of different benchmarks"* 라고만 한다.
- [[tech-bridge-claude-fable-5-2-announcement]]의 Frontier Code 점수(49.1)와 이 소스의 45.3%(high)가 같은 표인지.

## References

- [[tech-bridge-chase-ai-fable-5-2-prompting-rules]] — 규칙 1 · 5 · 8 · 10
- [[tech-bridge-claude-fable-5-2-announcement]] — *하이 설정으로도 오퍼스의 최고 점수와 비슷 · 비용 절반*(발표문 해설)

## 2026-11-13 — 벤더 가이드: *모델보다 effort 먼저* ([[tech-bridge-addy-osmani-which-claude-model]])

두 번째 소스. [[addy-osmani|Addy Osmani]]의 모델 선택 가이드 해설(⚠️ 원 글 · effort 문서 미열람)이 effort를 **모델 선택의 첫 다이얼** 로 놓는다: *"모델을 바꾸기 전에 에포트부터 조정을 하는 것입니다."*(02:31~02:34) 단, *"다만 에포트를 올려도 [음악] 모델에 없는 지식이나 능력이 생기지는 않습니다."*(02:37~02:41) 올리면 더 오래 생각 · 도구를 더 호출 · 자기 결과를 더 검증하고, effort와 지연 시간은 대략 비례한다.

| 기본 effort(해설) | API | Claude Code |
|---|---|---|
| Haiku 5.5 · Opus 5.5 | medium | medium |
| Sonnet 5.5 · Fable 5.2 | high | medium |

- Opus 5.5 SWE-bench Pro(high 기준): medium −2.5p · 비용 70% / low −8p · 1/3 / extra high +1.4p · 2.5배 → high를 넘겨야 하면 *"한 단계 위 모델을 더 낮은 에포트로 시험해 봐야 합니다."*(03:13~03:17)
- 막힐 때의 순서: ① 스스로 검증할 수단 ② effort 한 단계 ③ 한 단계 위 모델 · 더 낮은 effort. 자동 검증이 되면 **전부 low → 실패만 high**(Opus 5.5 ≈ 97% · 17센트 vs 전부 high 95.3% · 29센트) → [[true-cost-to-perfect-answer]].
- Haiku 4.5 → 5.5 이전 시 budget tokens를 effort 수준으로 바꿔야 한다. Opus · Fable은 항상 생각을 켠 채 동작한다.
- 이 페이지의 열린 질문(11-10 발표문 해설 49.1 vs Chase AI 45.3%)에 한 조각: 이 가이드도 Fable 5.2 **high** 45.3%를 적는다. 49.1은 다른 effort 값일 수 있다(⚠️ 위키의 추정).

## 2026-11-16 — 실무자의 등급표: high가 꼭짓점, max는 엉뚱해진다 ([[tech-bridge-theo-fable-vs-opus-when-to-use]])

[[theo|Theo]]의 Opus effort 등급표(X 게시물, 해설 전달): 맨 위 high · 맨 아래 max. medium은 *조금 일찍 멈추고 확인을 덜 한다*, max는 *쉬운 일에도 억지로 오래 생각하게 만들어 오히려 엉뚱한 일을 벌인다*. 공식 기본값(medium)과 달리 **high를 추천** 한다. 공식 가이드의 *high를 넘기려면 effort 대신 모델을 한 단계 올려 낮은 effort로* 와 합치면 — **effort 사다리의 꼭대기는 max가 아니라 *다음 모델의 낮은 effort*** 라는 같은 결론을 벤더 수치(Frontier Code 2.0 Opus max 45.5% ≈ Fable high 45.3%)와 실무자 체감이 각각 준다. ⚠️ 등급표 원문 미열람, Theo 개인 평.

## 2026-11-18 — medium에서 시작 vs medium에서 일찍 멈춘다 ([[tech-bridge-fable-5-2-start-with-opus]])

종합 해설에서 두 문서의 권고가 맞닿는다. 가이드는 *Opus 5.5 medium에서 시작*, 프롬프트 문서는 [[fable-5-2|Fable 5.2]]가 길고 단계 많은 일에서 끝내기 전에 턴을 마치는 일이 low · medium에서 더 잦다고 한다 — *"그런데 클로드 코드의 기본 값이 바로 그 미디엄이라는 게 문제입니다."*(05:03~05:05) 해설의 화해는 조건부다: 평소는 medium, **오래 혼자 돌릴 일 앞에서만 high**(또는 medium + *멈추지 말라* 문단 — 조기 종료 절반, 출력 토큰 +30%쯤).

- high 위는 권하지 않는다 — 성능 향상의 대부분은 high에서. high 이상에서는 인사 한마디에도 생각부터 하므로 느려진 턴만 내린다. extra high는 점수 조금 · 토큰 훨씬 많이. *"하이를 넘으면 한 단계가 더 큰 모델 하나 값일 수 있습니다."*(05:52~05:54)
- 사다리의 첫 칸이 다시 확인된다: effort보다 먼저 **스스로 확인할 수단**(테스트 · 빌드).
- 위 11-16 절의 [[theo|Theo]](*high를 기본으로*)와는 여전히 다르다 — 벤더는 *긴 자율 실행* 이라는 조건을 붙인다. ⚠️ 해설 전달.

## 2026-11-24 — 높은 단계의 자리: 조사 · 성능 측정 · 디버깅 · 자기 검증 ([[tech-bridge-pocock-networkchuck-what-to-learn-instead-of-languages]])

[[matt-pocock|Matt Pocock]]의 NetworkChuck 대담 해설(내레이션 전달). 챕터 제목은 *"최선을 다해"가 AI를 멍청하게 만든다* 이다.

- 진행자의 설정: *"진행자 척은 AI가 매번 최선을 다하길 바라서 노력 수준을 최고에 가깝게 둔다고 했습니다."*(05:18~05:23)
- ⚠️ **이에 대한 Pocock의 답(05:30~06:01)은 두 트랙 모두 무캡션이다.** 높은 강도가 왜 해로운지의 논거는 이 위키에 들어오지 않았다 — 설명란은 *"최선을 다해"라고 시키면 오히려 멍청해지는 이유* 라고만 적는다.
- 남은 것은 배치다: *"높은 단계는 조사나 성능 측정, 디버깅처럼"*(06:04~06:07) 여러 번 시도해야 하는 일에 맞는다고 하고, 검증 쪽에서 다시 나온다 — *"높은 노력 단계를 쓰는 곳도 바로 여깁니다. 앱을 실제로 클릭해 보고 성능을 재면서 자기 작업을 검증할 때요."*(09:16~09:21)
- 탐색에는 필요 없다는 쪽: *"맞는 파일을 읽으면 되죠."*(06:03~06:04)

11-16 절(*max는 엉뚱해진다*)과 같은 방향의 실무자 진술이 하나 더해졌으나, 근거 문장이 비어 있어 독립된 논거로 세지 않는다. 그가 11-21 업로드 편에서 쓴 설정은 중간이었다.
