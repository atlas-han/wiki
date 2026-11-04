---
title: "리뷰 모델 뒤집기 — 코드를 쓴 모델과 다른 모델에게 리뷰시킨다 (Review Model Inversion)"
type: concept
category: pattern
tags: [automated-code-review, model-diversity, correlated-errors, generator-evaluator, coding-agents, greptile, vendor-claim]
aliases: [model inversion, 모델 뒤집기, 모델 교차 리뷰, flip models, cross-model code review, invert the model]
related: [automated-code-review, cross-model-prior-intersection, generator-evaluator-pattern, three-level-agent-review, model-mixing-economics, cross-lab-peer-review, production-trace-eval-flywheel]
first-seen: tech-bridge-greptile-daksh-gupta-build-review-agent
sources: [tech-bridge-greptile-daksh-gupta-build-review-agent]
created: 2026-11-04
updated: 2026-11-04
---

# 리뷰 모델 뒤집기 (Review Model Inversion)

**같은 모델이 쓰고 같은 모델이 리뷰하면 두 단계에서 같은 방식으로 실패하므로, 작성에 쓴 모델을 알아내 다른 계열의 모델에게 리뷰를 맡긴다.** [[daksh-gupta|Daksh Gupta]](설명란 근거, [[greptile|Greptile]])가 [[tech-bridge-greptile-daksh-gupta-build-review-agent]]에서 "model inversion"이라고 부른다.

> *"they fail in the same ways during review that they do during code generation. And so, you'll want to invert the model. If you've used cloud[=Claude] code to write the code, you'll want to use a GPT model to review it"*(07:09~07:16)

> ⚠️ **"model inversion"은 ML 보안의 *model inversion attack*(모델에서 학습 데이터를 복원하는 공격)과 이름이 겹친다**(이 구분은 위키의 일반 지식이고, 발표자는 언급하지 않는다). 이 페이지는 혼동을 피하려 "리뷰 모델 뒤집기"로 적는다.

## 주장

- **모델마다 내는 버그가 다르다** — *"the types of bugs produced by cloud[=Claude] models or codex models are actually quite different from each other."*(06:38~06:42)
  - *"cloud[=Claude] models are something like three times more likely to produce one-off errors than GBT[=GPT] models."*(06:45~06:51)
  - *"GBT[=GPT] models on the other hand are significantly more likely to produce off[=auth] bypasses than cloud[=Claude] models."*(06:51~06:55)
  - 원인: *"these are all just artifacts of the post training as far as I understand."*(06:55~06:58) 본인이 유보를 붙였다.
- **효과** — ⚠️ *"We found that there's a 10% higher cache[=catch] rate if you flip models."*(08:06~08:08) 권고: *"we highly recommend that you use some type of model inversion in your process."*(08:20~08:23)

## 작성 모델을 어떻게 아는가

⭐ 이 페이지에서 가장 바로 쓸 수 있는 부분이다. 리뷰 시스템은 PR을 누가 썼는지 알아야 뒤집을 수 있다.

| 경로 | en-orig |
|---|---|
| 도구의 지문 — Codex | *"codecs[=Codex] will name branches in a codec[=codex]/branch name format"*(07:32~07:34) |
| 도구의 지문 — Claude | *"claude is going to write a co-authored by claude in the PR description and commit message."*(07:37~07:39) |
| 지문의 범위 | *"about 80% of the times this will be true."*(07:41~07:42) ⚠️ 발표자의 어림값 |
| 나머지 | 사람이 브랜치를 직접 만들었거나 다른 도구를 썼을 때는 *"some type of heristic[=heuristic]"*(07:51~07:53), 사내 카탈로그(07:56~07:59), *"telemetry that's coming out of your dev machines"*(08:00~08:02) |

⚠️ 지문은 약한 신호다. 공동 저작 표시는 사람이 커밋을 고치면 사라질 수 있다(위키의 해석, 발화 아님). 발표자도 *"quite tricky for the last 20."*(07:24)라고 인정한다.

## 위키의 다른 페이지와

- [[cross-model-prior-intersection]] — 이 페이지의 **이론적 짝**이다. [[hrishi-olickel|Olickel]]은 계열이 다른 모델의 불일치에 검증을 몰았고, 대상이 데이터였다. 여기는 대상이 코드이고, 일치 · 불일치를 보지 않고 **작성자와 다른 모델 하나**를 리뷰어로 둔다.
- [[generator-evaluator-pattern]] — 그 페이지가 반복해 물은 *채점자의 독립성*(같은 모델인가)에 **모델 계열**이라는 답 하나를 준다. Claude Code 팀의 *별도 리뷰어*(11-02 [[automated-code-review]])는 맥락의 분리다. 모델을 바꾸라는 말은 그 기록에 없다.
- [[three-level-agent-review]] — Corey Gallon(이름 추정)의 Level 2는 **같은 지시**를 받은 에이전트 둘이고 모델 다양성을 말하지 않는다. 축이 다르다.
- [[model-mixing-economics]] — 지금까지 모델 혼합의 이유는 대부분 **비용**이었다. 여기서는 **상관된 실패를 깨는 것**이 이유다. 같은 영상의 뒷부분은 비용 쪽 혼합도 말한다. 두 혼합이 충돌할 때(싼 모델이 리뷰를 맡아도 되는가)의 우선순위는 말하지 않는다.
- [[cross-lab-peer-review]] — *경쟁사가 숙제를 채점한다* 는 같은 직관을 **회사 단위 안전 검증**에 쓴다. 메커니즘과 강제력이 달라 같은 패턴으로 묶지 않는다.

## ⚠️ 유보

- **10%가 무엇의 10%인지 모른다.** 상대값인지 퍼센트포인트인지, 모델 쌍 · 버그 등급 · 표본 · 기간이 없다. 발표자는 바로 이어서 *"That means that there's a 10% higher chance that something will go wrong if you're not using model inversion"*(08:14~08:18)라고 하는데, **탐지율 차이와 사고 확률 차이는 같은 수가 아니다.**
- **거꾸로 비교한 수치가 없다.** 3배와 *"significantly"* 는 Claude · GPT 작성 버그의 차이이고, 어느 조합의 리뷰가 어떤 유형을 더 잡는지는 발화되지 않는다. 뒤집기의 효과가 **두 방향에서 대칭인지** 알 수 없다.
- 모델 버전이 하나도 없다. *"post training"* 이 원인이라면 버전마다 달라질 수 있는데, 수치의 유효 기간을 말하지 않는다.
- *"one-off errors"* 는 off-by-one의 ASR 또는 말버릇 추정이고 확정이 아니다. ⚠️ `en`은 `"unique errors"`(06:50) · `"omissions"`(06:55)로, 처방 이름은 `"model versioning"`(08:19)으로 바꾸고, ko는 *"버전 관리"*(08:17)로 옮긴다. 자막으로 읽으면 이 개념이 보이지 않는다.
- 발표자는 리뷰 제품 회사의 공동창업자이고, 모델을 가로질러 고르는 일은 그 제품이 대신해 주는 일이다. 다른 쪽의 독립 측정은 위키에 없다.

## References

- [[tech-bridge-greptile-daksh-gupta-build-review-agent]] §5 — first-seen
- [[daksh-gupta]] · [[greptile]] · [[automated-code-review]] · [[cross-model-prior-intersection]] · [[generator-evaluator-pattern]]
