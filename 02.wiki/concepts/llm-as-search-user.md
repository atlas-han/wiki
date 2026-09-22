---
title: LLM이라는 새로운 검색 사용자 (The LLM as Search User)
type: concept
category: framing
tags: [retrieval, query-formulation, bm25, agentic-search, workload]
aliases: [새로운 사용자, new user, 쿼리 구성]
related: [agentic-search, bm25, retrieval-not-reasoning-bottleneck, ir-evaluation-obsolescence, retrieval-primitive-repertoire, code-as-atypical-knowledge]
first-seen: tech-bridge-bm25-agentic-search
sources: [tech-bridge-bm25-agentic-search, tech-bridge-exa-perfect-search-for-agents]
created: 2026-09-21
updated: 2026-09-22
---

# LLM이라는 새로운 검색 사용자

**검색 기술이 바뀐 게 아니라 검색을 쓰는 쪽이 바뀌었다.** 30년 된 함수가 갑자기 강해 보이는 이유는 **그 앞에 앉은 사용자가 교체됐기 때문**이다.

> **BM25는 변하지 않았어요. 점수 계산 방식은 동일하지만, 여기서 달라진 점은 사용자가 더 강력한 권한을 갖게 되었다는 것입니다.** — [[jo-bergum]], [[tech-bridge-bm25-agentic-search]] (03:19~03:28)

## 무엇이 달라졌나

| | 사람 사용자 | **LLM 사용자** |
|---|---|---|
| 쿼리 길이 | **몇 개 용어** — AOL 쿼리 로그도, 최근 로그도 그렇다 | **아주 긴 쿼리를 순식간에** |
| 아는 것 | 자기가 찾는 것 | **개체·회사·날짜** 등 **매개변수에 내재된 일반 지식** |
| 구문 | 대부분 안 쓴다 | **`site:` 연산자·구문 등을 웹 검색에서 학습해 쓴다** |
| 읽기 | 파란 링크 10개를 훑는다 | **결과를 읽고 쿼리를 재구성한다** |
| 횟수 | 한두 번 | **사람이 할 수 있는 것보다 훨씬 많이** |

> **[LLM]은 폭넓은 일반 지식을 갖추고 있습니다. 개체에 대해서도 알고, 회사에 대해서도 알고, 날짜에 대해서도 알고, 많은 것을 알고 있죠.** 그리고 **매개변수 모델에 내재된 그러한 암묵적인 지식을 활용함으로써, 그들은 본질적으로 검색에 매우 능숙해집니다.** (03:31~03:46)

> ⚠️ **ko 자막이 이 문장의 *LLM* 을 "법학 석사 과정 학생들"로 옮긴다**(03:31). **발표의 테제를 담은 자리**라 한쪽만 읽으면 뜻이 사라진다. → [[tech-bridge-bm25-agentic-search]]

## 근거 — 실제 궤적을 뜯어봤다

> 우리는 **[GPT-5]가 어떻게 쿼리를 구성하는지 알아보기 위해 이러한 궤적을 조사하는 데 시간을 좀 할애했습니다.** (08:24~08:35)

그리고 **AOL 쿼리 로그**와 대조한다 — AOL이 *"실수로 사람들이 웹에서 무엇을 검색하는지에 대한 대규모 샘플을 공개해 버린"* 그 데이터셋(08:45~09:02).

> 그리고 [그 쿼리들은] 꽤 **짧았어요**. 최근의 검색 로그도 살펴봤는데, **사용자들의 검색 패턴은 여전히 몇 가지 용어만으로 이루어져 있습니다.** (09:05~09:12)

> **이것은 새로운 유형의 작업 부하(workload)입니다.** (09:33)

> ⚠️ **분석 결과가 소스에 없다.** *"많은 흥미로운 점들을 발견했습니다"* 라고만 하고 **무엇을 발견했는지는 블로그로 넘긴다**(08:36~08:43). 쿼리 길이 분포·연산자 사용률 같은 **수치가 하나도 제시되지 않는다.**

## 왜 이것이 낡은 도구를 되살리는가

사용자가 강해지면 **도구는 단순한 편이 낫다**는 역전이 일어난다.

> [새 사용자는] **쿼리를 재구성할 수 있고, 다양한 일반 지식을 보유하고 있어 `grep`이나 BM25와 같은 간단한 도구를 더욱 강력하게 만들어 줍니다.** (16:39~16:50)

**이 위키가 지금까지 도구를 논한 방식과 방향이 반대다.** [[agent-tool-design-practices]]·[[build-a-lever]]·[[adaptive-response-format]]은 전부 **도구를 모델에 맞춰 정교하게 다듬는** 쪽이었다. 여기서는 **모델이 강해졌으니 도구는 프리미티브로 남고 조합을 모델에 맡긴다.**

→ [[ride-the-optimization-trajectory]] · [[corpus-as-filesystem-workspace]]

## ⚠️ 반대 관측 — 사용자가 강해진 것이 언제나 좋지는 않다

같은 날 [[benjamin-clavie|Clavié]]는 **같은 사실의 부작용**을 지목한다:

> 자주 보게 되는 한 가지는 **에이전트가 [`grep`] 쿼리를 쓰려고 한다는 것입니다. [`grep`]은 학습 데이터 어디에나 있고 BM25도 데이터 어디에나 있으니까요. 그리고 그게 항상 필요한 것은 아닙니다.** — [[tech-bridge-knowledge-agents-not-coding-agents]] (16:02~16:17)

**같은 "학습 데이터에서 온 검색 습관"이 한쪽에서는 강점이고 다른 쪽에서는 편향이다.** 텍스트 코퍼스에서는 모델의 `grep` 본능이 맞고, PDF에서는 **틀린 도구로 손이 간다.** → [[retrieval-primitive-repertoire]]

## 평가가 따라 무너진다

> 이전에는 (…) 단순히 **파란색 링크 10개**를 보고 (…) 몇 가지 지표를 계산하는 식이었죠. **이제 그런 문제들이 많이 사라지고 있는데, 에이전트가 사람이 할 수 있는 것보다 훨씬 더 많은 쿼리를 입력할 수 있다는 점에서 강력해졌기 때문입니다.** (04:13~04:32)

→ [[ir-evaluation-obsolescence]]


## ⭐ "사용자가 바뀌었다"의 두 번째 읽기 (2026-09-22 추가)

이 페이지는 **AOL 쿼리 로그 대조**(사람은 예나 지금이나 몇 단어를 친다) 위에 서 있고, 결론은 **사용자가 더 강력해졌다**는 것이다. **하루 뒤 들어온 소스가 같은 관측에 다른 해석을 붙인다.**

> *"싱가포르에서 AI 검색을 연구하는 모든 사람과 그들이 쓴 블로그 글이나 논문을 찾아 줘."* — **장담컨대 여러분은 이런 걸 구글에 쳐 본 적이 없을 겁니다. 안 될 걸 아니까요.** — [[will-bryk]], [[tech-bridge-exa-perfect-search-for-agents]] (03:05~03:16)

→ **[[suppressed-query-demand]]**

**사람이 짧게 치는 것은 그것이 사람의 자연스러운 크기여서가 아니라, 긴 쿼리가 안 통하는 걸 학습했기 때문일 수 있다.** 그렇다면 *사용자가 바뀌었다* 는 **제약이 풀렸다** 로도 읽힌다.

⚠️ **두 읽기는 배타적이지 않고 어느 쪽도 증거가 없다** — [[jo-bergum|Bergum]]은 로그를 갖고 있지만 **왜 짧은지**를 묻지 않았고, [[will-bryk|Bryk]]은 *"장담컨대"* 가 전부다. **구분이 중요한 이유는 사람용 검색의 수요 추정치가 전부 하한이 되기 때문이다.**

## References

- [[tech-bridge-bm25-agentic-search]] · [[jo-bergum]] · [[hornet]] · [[tech-bridge-exa-perfect-search-for-agents]]
- 개념: [[agentic-search]] · [[bm25]] · [[ir-evaluation-obsolescence]] · [[ride-the-optimization-trajectory]] · [[corpus-as-filesystem-workspace]] · [[retrieval-primitive-repertoire]]
- 방향이 반대인 곳: [[agent-tool-design-practices]] · [[build-a-lever]] · [[adaptive-response-format]]
