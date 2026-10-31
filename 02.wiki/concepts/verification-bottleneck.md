---
title: 검증 병목 (Verification Bottleneck)
type: concept
category: framing
tags: [code-review, verification, throughput, bottleneck, agents]
aliases: [병목은 검증으로 옮겨갔다, 코드 리뷰 병목]
related: [mergeability-gap, automated-code-review, verification-cost-asymmetry, agent-verification-skill, behavior-validated-trust, trusted-throughput, agent-trust-curve, hard-vs-soft-enforcement, generator-evaluator-pattern, structure-sensitive-tests, agent-attention-management, agent-change-evidence, agent-plus-program-analysis, review-wip-limit, cross-model-prior-intersection, three-level-agent-review]
first-seen: tech-bridge-mousepower-measuring-agents
sources: [tech-bridge-mousepower-measuring-agents, tech-bridge-lauren-tan-trusting-agents, tech-bridge-ambitious-software-agent-era, tech-bridge-pstack-third-party-review, tech-bridge-graft-code-knowledge-graph, tech-bridge-shift-left-security-ai-code, tech-bridge-death-of-code-review, tech-bridge-dx-ai-impact-trends, tech-bridge-lauren-tan-agent-dev-workflow, tech-bridge-pocock-pr-bottleneck, tech-bridge-rails-harness-engineering, tech-bridge-sourcegraph-codebase-visibility, tech-bridge-kimchi-cost-per-task-harness, tech-bridge-agentcraft-strategy-game, tech-bridge-prompt-to-production, tech-bridge-lauren-tan-pocock-podcast-full, tech-bridge-gitar-agentic-pr-validation, tech-bridge-horthy-state-of-software-factory, tech-bridge-g2i-generation-cheap-evaluation-expensive, tech-bridge-atlassian-build-your-own-sdlc, tech-bridge-just-in-time-ontology, tech-bridge-three-level-agent-review, tech-bridge-top-1-percent-ai-habits, tech-bridge-stripe-collison-cherny-ai-dev-workflow, tech-bridge-laurie-voss-product-engineer, tech-bridge-anthropic-30k-merges-verification]
created: 2026-09-13
updated: 2026-10-31
---

# 검증 병목

**코드 생성이 싸지면서 병목이 생성에서 검증으로 옮겨갔다**는 진단. 2026-09-12에 업로드된 두 소스가 **서로를 언급하지 않으면서 같은 진단에 도달**했다.

## 진단

> **우리 모두가 천 개의 pull request에 치여 죽고 있습니다.** **코딩을 풀었다고 주장하는 사람이 있는 [[anthropic|Anthropic]]조차 코드 리뷰는 풀지 못했다고 인정**했습니다. — [[tech-bridge-mousepower-measuring-agents]]

> **병목이 검증 쪽으로 옮겨가면서 대규모로 가치를 측정하고 같은 속도로 품질을 판정할 방법이 없습니다.**

같은 상태를 개인의 경험으로 말한 것:

> 검증 스킬 없이 개발하면 — **검증자는 여러분 자신이고, 여러분이 병목**입니다. (…) **병렬화할 방법이 전혀 없죠.** — [[tech-bridge-lauren-tan-trusting-agents]]

## 두 개의 답

| | **작업을 고른다** | **역량을 짓는다** |
|---|---|---|
| 소스 | [[tech-bridge-mousepower-measuring-agents]] | [[tech-bridge-lauren-tan-trusting-agents]] |
| 처방 | 검증이 실행만큼 비싼 작업은 **하지 않는다** → [[task-entropy-matrix]] | 검증을 **스킬로 만들어 에이전트에게 넘긴다** → [[agent-verification-skill]] |
| 그다음 | **검증하는 에이전트**를 만든다 | 제약을 **CI로 하드 강제**해 검증을 애초에 줄인다 → [[hard-vs-soft-enforcement]] |
| 화자의 위치 | 판매자(고객의 작업을 고를 수 없다) | 코드베이스 소유자(자기 환경을 바꿀 수 있다) |

→ [[verification-cost-asymmetry]]

## 왜 코드 리뷰는 풀릴 것처럼 느껴지는가

Mousepower 편이 **Noah Hine**(철자 미확정)의 글을 인용해 답한다:

> **문화로서 코드 리뷰는 공유된 가정에 대한 수렴이 아주 좋다** — 모두가 측정에 수렴할 수 있으면 **대규모 측정이 가능해지고 그것이 명확한 루브릭**이 됩니다. 이제 할 일은 **그 가정들을 에이전트 시대에 맞게 적응시키는 것**입니다.

> **컴퓨트 속도의 실행에서 컴퓨트 속도의 측정으로.**

Lauren Tan 쪽의 답은 그 적응의 구체적 형태다 — **사람이 PR 댓글로 강제하던 가정을 CI 실패로 옮긴다.**

## 위키의 다른 페이지와 맞닿는 자리

- **[[behavior-validated-trust]]** — *증거가 작성자를 대체한다* 는 프레이밍의 **처리량 판본**. 증거를 만드는 비용이 병목이다.
- **[[trusted-throughput]]** — 그 지표가 *신뢰하는 결과물* 을 세는데, **신뢰를 붙이는 단계가 바로 이 병목**이다.
- **[[tech-bridge-knowledge-work-agent-infrastructure]]**(Composio) — *"코딩 에이전트만 폭발한 이유는 검증 인프라가 있었기 때문"* 이라는 주장과 정확히 이어진다. 그 인프라조차 **리뷰 단계에서는 아직 부족하다**는 것이 이 페이지의 내용이다.
- **[[tech-bridge-ai-era-code-quality]]**(IBM) — *"완벽한 코드로도 부족하다"* 와 같은 자리. 시스템 수준 품질은 리뷰로 확인되는데 리뷰가 확장되지 않는다.


## 2026-09-15 — 검증 앞에 있는 다른 병목, 그리고 디자인으로의 확장

이날 들어온 두 소스가 이 페이지의 양쪽을 건드린다.

- [[tech-bridge-graft-code-knowledge-graph]]는 **변경 *전*의 병목**을 가리킨다 — [[file-discovery-tax|탐색세]]. 이 페이지가 말하는 병목(변경 *후*의 검증)과 **경쟁하지 않고 작업의 앞뒤를 각각** 차지한다.
- [[tech-bridge-one-designer-plus-ai]]는 검증 병목이 **디자인 조직에서도 성립**함을 보여 준다 — 140곳 스폰서 배너의 **누락 검사**를 에이전트에게 넘긴다 → [[agent-visual-qa]].

두 번째는 **작성자 = 검증자** 구도의 네 번째 사례이기도 하다(배너를 만든 사람이 검수도 시킨다).

## References

- [[tech-bridge-mousepower-measuring-agents]] · [[tech-bridge-lauren-tan-trusting-agents]] · [[verification-cost-asymmetry]] · [[agent-verification-skill]] · [[behavior-validated-trust]] · [[trusted-throughput]] · [[hard-vs-soft-enforcement]]


## 세 번째 답 — 일을 쪼갠다 (2026-09-14 추가)

[[tech-bridge-ambitious-software-agent-era]]가 **검증 작업 자체를 둘로 가른다** → [[test-harness-vs-test-authoring]].

| 답 | 소스 | 처방 |
|---|---|---|
| **작업을 고른다** | [[tech-bridge-mousepower-measuring-agents]] (09-12) | 검증이 비싼 작업은 에이전트에게 주지 마라 |
| **역량을 짓는다** | [[tech-bridge-lauren-tan-trusting-agents]] (09-12) | 검증을 스킬로 만들어 에이전트에게 넘겨라 |
| **일을 쪼갠다** | [[tech-bridge-ambitious-software-agent-era]] (09-13) | **무엇을 검증할지는 사람이, 검증 장치(퍼징 하네스)는 에이전트가** |

> **어떤 API에 대해서든 테스트를 쉽게 쓸 수 있지만, **인간과 마찬가지로 올바른 테스트를 쓰는 데는 실패**합니다.** (…) **코딩 에이전트는 이런 [퍼징] 하네스를 만드는 데 탁월합니다.**

**세 번째가 고유한 점**: 에이전트에게 넘기는 것이 **판정이 아니라 도구**다. 2026-09-09 이래 이 위키가 반복 표시해 온 **평가자의 독립성 문제**(작성자=검증자)를 **구조적으로 피한다** — 퍼징 하네스는 의견을 내지 않고 **크래시를 낼 뿐**이다.

⚠️ **대가가 있다.** 같은 소스가 **엔드투엔드 테스트에서는 에이전트도 고전한다**고 인정하고(*"zed를 열어 보지 않고서는"*), [[agent-verification-skill]](에이전트가 앱을 실제로 띄운다)과 **긴장 관계**에 있다. **두 접근을 비교한 소스는 아직 없다.**

## 검증이 실제로 무엇을 잡았는가 (2026-09-14 추가)

[[tech-bridge-pstack-third-party-review]]에 **관측된 사례**가 하나 있다.

> **E 단계에서 검증 테스트를 전부 하고 감사로 마무리합니다. 바로 이래서 검증이 중요합니다 — **에이전트가 세부 일부를 환각했다는 걸 스스로 깨달았습니다. 시스템이 허위 주장 세 건을 잡아 고칠 수 있었습니다.**** (07:49~08:03)

**이 위키가 기록한 검증 사례 중 "무엇이 몇 건 잡혔는지"가 나온 첫 사례**다. ⚠️ 다만 **세 건의 내용이 없고, 놓친 것이 있었는지도 알 수 없다.**

→ [[test-harness-vs-test-authoring]] · [[agent-arena]] · [[agent-swarm]] · [[minimizing-reader-load]]

## 보안 쪽에서 나타난 같은 병목 (2026-09-17)

[[tech-bridge-shift-left-security-ai-code]]가 사후 보안 검토의 실패를 **이 페이지와 같은 구조**로 진단한다.

> 보안이 프로세스 마지막 단계에서 **사후적으로 추가(retrofit)** 되는 방식으로만 이루어진다면 **품질이 저하되고 전체 프로세스가 완전히 멈춰 섭니다.**

> **코드 생성이 몇 초 만에 이루어질 수 있는 상황에서, 마지막까지 기다리는 것은 병목을 만들고 위험을 키웁니다.**

**두 방향으로 깨진다** — 검토가 형식이 되거나(품질 저하), 검토가 처리량을 못 따라간다(정체). 그리고 양이 늘면 상황이 나빠진다:

> **코드가 많을수록 기능이 많아지고 복잡성도 커집니다. 그리고 복잡성은 보안의 적입니다.** / **속도만으로는 가치를 만들어내지 못합니다. 신뢰가 만듭니다.**

[[trusted-throughput]]과 짝을 이루되 방향이 반대다 — 그쪽은 *처리량의 값은 신뢰에서 온다*, 이쪽은 **처리량 자체가 검증 표면을 키운다.**

⚠️ 소스가 내놓는 해법은 **자동화**(프론티어 모델을 쓴 취약점 탐지)인데, **AI가 만든 코드를 AI가 검증하는 구성의 독립성을 논의하지 않는다** — 이 위키가 [[embedded-external-evaluators]]·[[skill-evals]]에서 반복해 기록한 *작성자=검증자* 문제가 여기서도 열린 채로 남는다.

→ [[shift-left-security]] · [[continuous-security-validation]]

## 네 번째 답 — 리뷰를 시스템으로 재건한다, 그리고 첫 정량 근거 (2026-10-03 · [[tech-bridge-death-of-code-review]])

[[laurie-voss|Laurie Voss]]([[arize-ai|Arize AI]])가 이 페이지의 진단에 **처음으로 숫자를 붙였다** — 모두 화자의 2차 인용이다.

| 근거 | 진술 | en-orig |
|---|---|---|
| 경제학자 3인, GitHub 개발자 10만+ | 자율 에이전트를 켠 개발자 *"wrote 741% more code but only 30% more software shipped"*, 저자들은 *"blunt that review was the bottleneck"* | 01:22~01:54 |
| Cisco 연구(약 20년 전) | 한 번에 400줄, 시간당 450줄을 넘으면 결함 발견이 무너진다 → 1만 줄 에이전트 PR = *"three or four working days"* | 03:30~04:05 |

**"더 열심히 리뷰"는 산수상 안 된다** — 그리고 리뷰를 빼 본 곳(OpenAI 2월 글, Carlini, Bun)은 모두 리뷰를 **지운 게 아니라 사람이 지은 시스템으로 옮겼다**(*"They didn't delete review, they moved it."* 17:21~17:23).

| 답 | 소스 | 처방 |
|---|---|---|
| 작업을 고른다 | 마우스파워 (09-12) | 검증이 비싼 작업은 주지 마라 |
| 역량을 짓는다 | Lauren Tan (09-12) | 검증을 스킬로 |
| 일을 쪼갠다 | Jonathan Kelley (09-13) | 무엇을 검증할지는 사람, 장치는 에이전트 |
| **리뷰를 재건한다** | **Voss (10-03)** | ***"stop reviewing PRs"*(23:19~23:21)** — 사람은 PR이 아니라 **리뷰 하네스**(좋음의 정의·회사 맥락·도메인 지식)를 짓는다 |

네 번째 답이 고유한 점: 사람이 **루프 *안*(in)이 아니라 루프 *위*(on)** 에 선다 — 그리고 테스트 통과가 머지 가능을 보장하지 않기 때문에(METR 약 절반, FrontierCode 88% vs 29%) 그 하네스가 *테스트 이상* 을 봐야 한다. → [[mergeability-gap]] · [[automated-code-review]]

⚠️ 같은 발표가 **Dex Horthy의 철회**(*"Please please read the code. We tried not reading the code for like six months. It did not end well."* 18:48~18:54)를 근거로 들면서 처방은 *"stop reviewing PRs"* 다. 두 주장을 화해시키는 말은 없다 — 위키의 독해로는 *아무도 안 보는 것* 과 *보는 층을 올리는 것* 의 차이.

## "생성은 애초에 병목이 아니었다" — 집계 데이터, 그러나 다른 병목 (2026-10-03 · [[tech-bridge-dx-ai-impact-trends]])

[[getdx|DX]]의 [[justin-reock|Justin Reock]]: *"code generation was never the bottleneck in the first place, right? Even if engineers are getting like 100% accurate instant code coming from the models, which they are not, you would still only be attacking anywhere from maybe 14 to 16% of the overall value stream."*(14:48~15:03) PR 처리량 증가는 **중앙값 7.7%, 평균 13%, 상위 70%대 — *"Nobody hit 2x"***(15:19~15:32). 근거는 Goldratt: *"an hour saved on something that isn't the bottleneck is worthless"*(16:02~16:05). ⚠️ 전부 DX 플랫폼 데이터, 14~16%의 출처 미발화.

**이 페이지를 지지하는 쪽** — 같은 데이터의 품질 지표가 검증 병목의 증상이다:

- 평균 PR 크기 **44 → 72줄**(06:56~07:02), 점진적 전달 체감 **−10%**(08:12~08:14) → 리뷰 표면이 커진다 → [[minimizing-reader-load]]
- 변경 확신 **−6%** vs 유지보수성 **+약 4%** — *"I trust the outputs less. I'm more afraid now of breaking things than I was a year ago."*(06:35~06:41) → [[perceived-vs-actual-productivity]]
- Zapier의 주 약 3,000건 자동 1차 리뷰 — 피상적 항목만, 사람은 여전히 루프에(17:28~17:52, 화자 전언) → [[automated-code-review]]

> ⚠️ **Contradiction: 다음 병목은 검증인가, 조직 마찰인가.** 이 페이지는 병목이 *생성 → 검증* 으로 옮겨갔다고 본다. Reock은 AI의 시간 절약을 갉아먹는 것으로 **검증이 아니라** *"meeting heavy days and context switching and other sources of interruption, the cumulative effects of the dev environment and friction"*(15:45~15:53)을 꼽고, 사례도 스탠드업 축소·온보딩·인시던트 컨텍스트(Zapier·Spotify)다. 자기 데이터(PR ↑, 확신 ↓)는 검증 병목을 가리키는데 결론에서는 그것을 말하지 않는다 — **같은 데이터의 두 읽기.** 위키의 독해: 둘은 배타적이지 않다. *생성이 병목이 아니었다*는 데는 모두 동의하고, 그다음 병목이 **코드 경로 안(리뷰)이냐 밖(조직)이냐**가 갈린다.

## 표본을 보고 환경을 고친다 (2026-10-09 · [[tech-bridge-lauren-tan-agent-dev-workflow]])

[[lauren-tan]]의 대담 발췌가 *"사람은 그 많은 변경을 어떻게 검토하나"* 에 답한다 — **전수가 아니라 표본**:

> *"as a quality supervisor on a factory, you can't look at every single item. You sample, right? You take you, you you go in there every day and you look at the quality of the pull requests, you look at the code that the agents are writing, and you scanize[=scrutinize] it very rigorously and think about all the inefficiencies, the bad patterns that the agent are doing"* (09:12~09:37)

해설(ko 09:40~09:49): *"문제 하나를 고치고 끝내는 대신 다음에도 같은 문제가 생길 환경인지 돌아보는 겁니다. 스킬과 타입, 제약을 조정하면서 사람이 개입하는 지점을 줄여 갑니다."*

- [[tech-bridge-death-of-code-review|Voss]]의 *"stop reviewing PRs"* 와 **전수 리뷰를 버린다는 점은 같고**, 남는 사람의 일이 다르다 — Voss는 **리뷰 시스템**을 짓고, Lauren은 표본에서 본 것으로 **환경**(스킬·타입·제약 — [[hard-vs-soft-enforcement]])을 고친다.
- ⚠️ 표본 크기·빈도·선택 기준은 없다. [[risk-proportional-human-review]]처럼 **어디를 볼지 위험으로 고르는** 장치가 없다.
- ⚠️ 해설만의 요약(발췌 음성 없음): 비슷한 제보를 묶는 **조정자 역할**, 나쁜 패턴을 **곧바로 고치지 않고 문서에 모아** 공통 원인을 찾기(ko 08:09~08:28) — 원본 대담 미확인.

## 네 번째 답을 실행 단위로 — 싼 층 둘을 깔고 사람은 one-way door만 (2026-10-09 · [[tech-bridge-pocock-pr-bottleneck]])

[[matt-pocock|Matt Pocock]]: PR 병목은 AI 이전부터 있었고(*"huge numbers of PRs just laying around that no one's bothered to review"* 00:12~00:18) AI가 키웠다. 답은 사람 리뷰를 없애는 것이 아니라 **빠르게** 하는 것 — *"to make human review faster by leaning on those first two phases"*(03:47~03:50): 자동 검사(CPU) → 자동 리뷰(토큰) → 사람 리뷰. 그리고 사람 리뷰 자체를 **위험도로 거른다** — *"You really don't need to review every single two-way door. Every single one-way door you do."*(22:06~22:12)

Voss 편의 *네 번째 답*(리뷰를 시스템으로 재건)과 같은 방향이지만, Voss가 *"stop reviewing PRs"* 라 한 데 비해 Pocock은 **PR 리뷰를 남기고 그것을 사람 친화적으로** 만든다(merge danger 요약, 다이어그램). → [[automated-code-review]] · [[risk-proportional-human-review]] · [[structure-sensitive-tests]]

## 1시간 생성, 이틀 다듬기 — 개인 단위의 같은 병목 (2026-10-09 · [[tech-bridge-rails-harness-engineering]])

[[joel-quenneville|Joël Quenneville]]의 출발 일화: 2일로 잡은 기능이 에이전트로 약 1시간 만에 동작했지만 다듬고 리뷰하는 데 이틀 — *"I did two days worth of work in two days"*(01:46~01:49), *"one hour building code and then two days playing whack-a-ole[=mole] with (…) slop"*(02:03~02:12). Voss 편의 741% vs 30%를 **한 사람의 하루**로 겪은 것. 그가 거절하는 해법은 PR을 그대로 올려 *"shifted that burden onto everyone else. Don't do that."*(02:31~02:36) — 병목을 동료 리뷰어에게 넘기는 것. 그의 답은 이 페이지의 네 답 어디에도 정확히 맞지 않는 **다섯 번째 — 생성의 바닥을 올려 검증할 양을 줄인다**(→ 아래 통합 표)(*"raise the floor on what the AI gives me so that I'm not spending two days reviewing it"* 02:41~02:49): 결정론적 도구·훅·좁은 리뷰 스킬. ⚠️ 측정 없음 — 바닥을 올린 뒤 이틀이 얼마로 줄었는지 말하지 않는다.

## 리뷰 이전의 병목 — 가시성 (2026-10-09 · [[tech-bridge-sourcegraph-codebase-visibility]])

[[dan-adler|Dan Adler]]([[sourcegraph|Sourcegraph]])는 리뷰 피로를 인정한다 — *"this flood of AI generated code that we now have to review (…) and we're exhausted by it"*(02:02~02:09). 그러나 코드 리뷰 에이전트·코드베이스 건강 측정 도구·더 나은 모델을 *"sandbags"* 와 *"local maxima"*(02:22~02:31)로 내리고, 병목을 **리뷰 이전**에 둔다: 에이전트(와 리뷰어)가 수만 저장소를 **보지 못한다**(*"You can't gp[=grep] what you literally cannot see."* 07:33~07:36).

[[file-discovery-tax]]가 *변경 전* 단일 저장소의 탐색 비용이었다면, 이것은 **변경 전 저장소 사이의 가시성**이다. ⚠️ 측정치 없음, 화자는 가시성 인프라 벤더 → [[code-knowledge-graph]] · [[large-scale-code-changes]]

## diff가 아니라 의도와 스펙을 — 비기술 인력의 PR (2026-10-09 · [[tech-bridge-kimchi-cost-per-task-harness]])

[[kimchi|Kimchi]]의 Zilvinas: *"what we believe is that reading code is not enough anymore"*(10:48~10:52). 이유에 새 변수가 붙는다 — 변경량 증가에 더해 *"as you keep bringing like a little bit of a less technical personnel onto your pipelines"*(11:06~11:12). PM이나 사장이 2,000줄 PR을 들고 오면 *"you need to actually review not just the differences but the actual intent which he wanted to achieve and the specifications which he provided to the coding agent"*(11:19~11:30). → [[intent-alignment]] · [[spec-driven-development]]

답은 **두 층**이다: Ferment의 점수 게이트(B 이상)와 스테이징에서의 사람 정지(*"some little human (…) before going to the production"*, 10:11~10:18), 그리고 Studio에서 **계획 단계 리뷰**. ⚠️ 의도 리뷰를 실제로 어떻게 하는지는 시연되지 않는다.

## 병목은 리뷰보다 넓다 — 주의 비용과 인터페이스 (2026-10-09 · [[tech-bridge-agentcraft-strategy-game]])

[[ido-salomon|Ido Salomon]]([[agentcraft|AgentCraft]])도 *"we are the bottleneck"*(01:01~01:02)에서 출발하지만 병목을 **리뷰 하나가 아니라** *"steer them, direct them, review them"*(00:47~00:53) 전체의 **주의·기력**으로 본다. 답은 리뷰 처리량이 아니라 **인터페이스** — 상태 패널·지도·히트맵, RTS식 *"the nearest thing that actually needed your attention"*(04:45~04:49) 점프, 할 일 생성(퀘스트), 자율 실행, 영상·사진 *"visual evidence"* 리뷰(07:22~07:28), 사람 협업. → [[agent-attention-management]] (신규)

답의 표에 넣으면: **주의를 라우팅한다** — 모두 보지 말고 **필요한 곳으로 점프**, 리뷰는 시각 증거로 압축, 단순판에선 과정 보기를 선택 사항으로(→ 아래 통합 표).

⚠️ 단순판의 *"I don't really care perhaps about the way, I can see it if I want to"*(12:05~12:09)는 Voss가 인용한 *"Please please read the code"*(18:48~18:54)와 정면으로 긴장한다 — 화자는 이를 다루지 않는다. 당사자 데모, 측정 없음.

## 또 하나의 답 — 에이전트가 증거를 낸다 (2026-10-09 · [[tech-bridge-prompt-to-production]])

[[ibm|IBM Technology]] 계열 해설(발표자 무명)이 이 페이지의 진단을 **가장 짧게** 말한다 — 측정치 없이 가상 예시 하나로:

> *"AI can scale execution dramatically faster than humans can scale verification. If an agent updates five files, that's no sweat. (…) If it updates 500 files (…) I can't realistically review every change."* (04:33~04:52) → *"the bottleneck becomes our confidence that the solution's outcomes are successful"* (04:55~05:00)

| 답 | 소스 | 처방 |
|---|---|---|
| 작업을 고른다 | 마우스파워 (09-12) | 검증이 비싼 작업은 주지 마라 |
| 역량을 짓는다 | Lauren Tan (09-12) | 검증을 스킬로 |
| 일을 쪼갠다 | Jonathan Kelley (09-13) | 무엇을 검증할지는 사람, 장치는 에이전트 |
| 리뷰를 재건한다 | Voss (10-03) | *"stop reviewing PRs"* — 리뷰 하네스 |
| 바닥을 올린다 | Quenneville (10-05) | 결정론적 도구·훅·좁은 리뷰 스킬로 생성 품질을 올려 검증할 양을 줄인다 (위 섹션) |
| 주의를 라우팅한다 | Salomon (10-07) | 필요한 곳으로 점프, 시각 증거로 압축 → [[agent-attention-management]] (위 섹션) |
| **증거를 받는다** | **IBM 계열 (10-07)** | *"AI (…) should generate evidence"*(05:31~05:36) — 사람은 diff 대신 **다섯 질문의 답**(무엇·왜·무엇이 깨질 수 있나·하류 영향·목표 달성)을 본다 → [[agent-change-evidence]] |

> 통합 메모(2026-10-09): 이번 회차의 세 소스(Quenneville·Salomon·IBM 계열)가 각자 "다섯 번째 답"의 자리를 주장했다 — 위 표는 업로드 순으로 합친 것이다. Pocock(10-05) 편은 스스로 네 번째 답의 변주로 자리 잡고, Lauren Tan(10-03)·Sourcegraph(10-06)·Kimchi(10-07) 편은 새 행을 주장하지 않는다.

> ⚠️ **Contradiction(추가): 실행은 병목이었나.** 이 소스는 *"For years, software development was limited by execution"*(04:08~04:13)이라 한다 — 위 [[tech-bridge-dx-ai-impact-trends|Reock]]의 *"code generation was never the bottleneck"* 과 정면으로 갈린다. 다만 이 소스의 *execution* 은 *"Writing code, migrating systems, and testing"*(04:13~04:16)이고, **같은 영상 안에서** 병목을 *"coordinating all of the changes around it"*(03:55~04:01) · *"the hardest part, coordination"*(06:27~06:29)으로도 부른다. 화자 자신이 실행 → 조율 → 확신 세 이름을 쓴다. 해소하지 않는다.

## 거꾸로 푼다 — "에이전트가 자기 코드를 머지하려면?" (2026-10-10 · [[tech-bridge-lauren-tan-pocock-podcast-full]])

[[lauren-tan|Lauren Tan]]이 [[tech-bridge-lauren-tan-agent-dev-workflow|해설 영상]]의 원 대담 풀버전에서 이 병목을 **출발 질문**으로 삼았다고 말한다. ⚠️ 당사자 진술, 독립 확인 없음.

- ⭐ *"the big unlock for me for getting to 2,000 PRs is starting from the question and working backwards of how do I get to the point where my agent can merge its own code?"*(38:32~38:45) — 사람들이 *"How did you review that?"* 라고 묻는 그 자리에서 시작한다.
- **답 = 검증 + 환경**: *"verification plus the environment, right? It's these the combination of these two things that allow me to step away"*(52:43~52:49). 검증은 [[pstack|Pstack]] *full autopilot* — PR마다 verifier 에이전트가 앱을 실제로 돌려 퍼징하고 스스로 고친다(51:42~52:21). 사람은 **머지 이후** 커밋 히스토리로 본다(52:49~52:52).
- **표본, 그리고 고치는 대상은 환경** — *"you cannot be tasting every single dish"*(48:34~48:38) → 공장 품질 감독관처럼 표본을 *"very rigorously"* 보고(48:47~49:13), *"course correct the environment, right? Not not that single agent"*(49:17~49:22). 일회성이면 그대로 두고, 여러 에이전트가 같은 우회책을 퍼뜨리면 스킬·제약·린트·타입을 고친다(49:26~49:59).
- **사람이 병목인 자리를 계속 묻는다** — *"where am I the bottleneck in this process? Why do my agents need me, you know, to answer this question?"*(36:56~37:03), 답은 *"not by hallucinating, not by guessing, but actually real data"*(37:09~37:13) — 바깥 루프([[grokbot]]).
- ⚠️ **한계를 본인이 말한다** — 검증하기 어려운 영역의 one-way door엔 *"I don't really have the answer to"*(56:29~56:34). 자동 머지 후 회귀·되돌림 비율은 제시되지 않는다. → [[action-reversibility]] · [[trusted-throughput]]

## CI까지 한 에이전트로 — "slow down" vs "rubber stamp" (2026-10-14 · [[tech-bridge-gitar-agentic-pr-validation]])

[[ali-reza|Ali-Reza]]([[gitar|Gitar]] → [[sonar|Sonar]])는 병목에 **두 나쁜 선택**이라는 이름을 붙인다: *"Either you slow down and ask developers to review every PR very carefully or you rubber stamp PRs and you risk incidents in production."*(03:09~03:16) 원인은 *"more PRs than before, uh, thanks to AI, and bigger PRs"*(02:48~02:53)이고, 그 결과 *"your costs in your development life cycle are kind of shifting to the right"*(02:56~03:00).

- 답은 *"Of course, it's more AI."*(03:27~03:31) 리뷰만이 아니라 **CI 실패 분석·flaky 탐지·자동 수정·자동 승인·머지까지** 한 에이전트 파이프라인으로 묶는다. 이 페이지의 기존 답들이 대부분 리뷰를 다시 짜는 쪽이었던 것과 다르다.
- 사람이 어디에 남는지는 말하지 않는다. 자동 승인 조건은 *"you can define rules and conditions"*(05:18~05:29)로 사용자에게 넘긴다. 자동 머지 후 회귀율도 없다. Lauren Tan 섹션이 지적한 공백과 같은 자리다.
- ⚠️ 벤더 발표이고 수치가 없다.

## PR을 기다리지 않는 리뷰 — 철회의 당사자 (2026-10-15 · [[tech-bridge-horthy-state-of-software-factory]])

Voss가 인용한 철회(*"Please please read the code"*)의 당사자 [[dex-horthy|Dex Horthy]]가 직접 근거를 낸다: agentic형 공장에서 빌드는 *"minutes or hours"*, 리뷰는 *"still takes hours or days"*(04:31~04:37), agentic 코드 리뷰로 당겨도 *"it may still be the bottleneck"*(04:43~04:47). 그의 답은 셋 — ① 계획을 앞에(*"20 minutes 30 minutes up front can save you hours during review"* 09:19~09:24, [[expected-pain-planning]]) ② 에이전트에게 back pressure([[back-pressure]]) ③ ⭐ *"every agent running anywhere as it's writing code the diffs are streaming to the cloud. So we can do code review uh without waiting for pull request."*(15:22~15:31 — 자사 제품, ⚠️ 당사자 진술). 근거로 든 5월 리포트(*"code review uh uh quality is way down (…) incidents per PR is way up"* 01:58~02:08)는 **이름·수치 미발화**.

## "생성은 싸고 평가는 비싸다" — 리뷰 면을 줄이는 답 (2026-10-15 · [[tech-bridge-g2i-generation-cheap-evaluation-expensive]])

[[gabriel-martinez|Gabriel Martinez]]: *"Generation is cheap, but evaluation is expensive. If AI produces more than humans can possibly evaluate, it has not accelerated the team, it has created a bottleneck."*(10:05~10:17) 기제는 **모호함을 넘기는 것**이다. 10줄짜리 범위를 받아 20페이지 문서로 돌려주면(09:19~09:26) *"the real work has just moved to the reviewer."*(10:00~10:02)

답은 리뷰 자동화가 아니라 **리뷰할 면을 줄이는 것**이다. 작은 원자적 변경(10:52~10:58), 다이어그램·선언적 코드로 만든 [[compressed-review-surface|압축된 리뷰 표면]](12:31~12:57), 관례(13:46~13:58)가 그 수단이다. 하루 전 업로드된 [[tech-bridge-gitar-agentic-pr-validation|Gitar 편]]의 *"Of course, it's more AI"*(03:27~03:31)와 정반대 방향이다. 다만 Martinez도 자사 에이전트 도구(ORC)로 발표를 맺는다.

## 유량을 리뷰 용량에 맞춘다 — "where things go to die" (2026-10-17 · [[tech-bridge-atlassian-build-your-own-sdlc]])

[[andrei-bocan|Andrei Bocan]]([[atlassian|Atlassian]] AutoDev): *"the reviewing step is where things go to die. Um because people again are uh busy with other things."*(45:32~45:40) 답은 리뷰 자동화가 아니라 **흐름 제어**다. 1인당 주 3~5 PR 설정(41:52~42:01), WIP 한도(43:50~43:58), 티켓·주 단위 비용 한도(44:18~44:28)를 두고, Slack으로 적절한 때에 리뷰어를 호출한다(45:43~46:00). → [[review-wip-limit]]. *"nobody's going to approve a PR that's like change half your code base"*(41:32~41:37)이라 기존 코드를 고칠 때도 PR을 점진적으로 낸다.

## 검증에 매긴 가격 — 첫 답의 약 4배 (2026-10-18 · [[tech-bridge-just-in-time-ontology]])

[[tech-bridge-g2i-generation-cheap-evaluation-expensive|G2i]]의 *"Generation is cheap, but evaluation is expensive"*에 데이터 파이프라인 쪽 **비율**이 붙는다: 검증 $545 vs 첫 답 $128(12:26~12:36, ⚠️ 자기 보고). 화자는 이것을 병목이 아니라 **예산 항목**으로 다룬다. 미리 정한 $800 안에서 second opinion·불일치 해소·감사를 돌렸고, *"now that the pipeline is built and verified, we expect the audit budget for the next state to be close to zero."*(12:40~12:45, ⚠️ 예측) 검증을 줄이는 길은 리뷰 자동화(Gitar)나 리뷰 면 축소(G2i)가 아니라 **한 번 검증한 파이프라인의 재사용**이다. → [[just-in-time-ontology]] · [[cross-model-prior-intersection]]

## "사람이 덜 읽게"가 아니라 "사람이 안 읽게" (2026-10-20 · [[tech-bridge-three-level-agent-review]])

[[corey-gallon|Corey Gallon]](⚠️ 이름 *추정*): *"In these cases, each review took minutes, not hours, and the agents do the checking, not me. At the scale we operate, checking it myself isn't an option."*(03:48~03:57) 첫 회계 에이전트가 *"I recommend spot checking a few of these transactions"*라고 돌려준 것을 *"This put the burden of reviewing the agent's work back on us, which is a non-starter."*(07:14~07:26)라 부른다. 병목의 답을 리뷰 면 축소가 아니라 **검토 주체 교체**(세 단계 에이전트 검토)로 둔다. ⚠️ 사람이 놓친 오류와 비교한 데이터는 없다. → [[three-level-agent-review]]

## 사용자 한 사람의 검증 — "같은 기준으로 비교하라" (2026-10-21 · [[tech-bridge-top-1-percent-ai-habits]])

코드 리뷰 밖, 개인 업무 단위의 판본이다. Tech Bridge 내레이션(더빙): *"When you delegate a small part of your work, you have concrete things to verify. You can check if the necessary content is included, if there are errors, and how long it takes to edit. By comparing subsequent results using the same criteria, it becomes easier to judge if it's helpful for your work."*(05:49~06:04) 기준 셋(포함 여부 · 오류 · **고치는 시간**)과 고정 기준 비교는 팀 단위 eval의 최소형이다. 같은 편은 AI의 비판을 받아도 *"check if there is a basis for the rebuttal"*(05:15~05:18)이라 하여, 검증 대상을 생성물뿐 아니라 **AI의 평가**로 넓힌다([[sycophancy]]).

## 생성 시각과 수용 시각 — 간격을 재는 한 쌍 (2026-10-23 · [[tech-bridge-stripe-collison-cherny-ai-dev-workflow]])

- 진단의 분해(해설): *"AI가 코드를 작성한 시점과 우리가 그 코드를 배포할 수 있는 시점 사이에는 간격이 있습니다"* — 요구사항 적합 · 테스트 충분성 · 다른 변경과의 통합(00:59~01:10). 간격을 두고 생성만 빨라지면 *"검토를 기다리는 변경이 쌓일 수 있습니다."*
- 측정 권고(해설): *"코드가 처음 나온 시간과 사람이 검토해서 받아들인 시간을 함께 기록해 보십시오. 프롬프트 수정, 테스트, 실패 해결, 병합 충돌 정리에 쓴 시간을 보면 처음 고른 우선순위가 맞았는지 판단할 수 있습니다."*(08:52~09:06) 진단표: 환경이 뒤섞이면 분리 · 같은 검사를 사람이 반복하면 자동화 · 합칠 때 깨지면 병렬 계획부터.
- 테스트 통과 ≠ 요구 충족: *"로그인 버튼이 잘 눌리는 것과 다른 사람의 계정으로 들어갈 수 없는 것은 서로 다른 확인 항목입니다."*(04:35~04:39)
- ⚠️ 전부 Tech Bridge 해설 권고다 — [[stripe|Stripe]]의 수치나 측정 결과는 자막에 없다.

## 검증 다음의 병목 — 리뷰 → 운영 → 보안 → 문제 정의 (2026-10-27 · [[tech-bridge-laurie-voss-product-engineer]])

[[laurie-voss|Voss]]의 두 번째 강연(발췌)은 이 페이지의 전제를 한 단계 연장한다. 제약 이론(귀속 미상의 *"his big idea"*)에서 두 가지를 가져온다. 하나는 *"speeding things up does not work unless the thing that you were speeding up is the bottleneck"*(00:54~01:00), 다른 하나는 *"when you fix the bottleneck it doesn't go away, it just moves"*(01:11~01:15)다.

화자는 병목이 옮겨 갈 순서를 이렇게 본다.

1. **코드 리뷰**: 12개월 안에 *"real progress"*
2. **운영**: 배포와 확장
3. **보안**: 2와 3을 합쳐 *"5 and 10 years"*
4. **문제를 기술하고 해결의 기준을 정하는 일**: *"that is where it stays"*(03:40~03:48)

이 페이지의 다른 소스들이 검증을 **종착점**으로 봤다면, 이 편은 검증을 **경유지**로 본다.

## 병합 실패율 · 검증 불가 체감 — 그리고 Anthropic의 답 (2026-10-31 · [[tech-bridge-anthropic-30k-merges-verification]])

진행 쪽([[manish-kapur]] 추정)이 두 통계를 읽는다(둘 다 출처 링크 없음, 미확인): CircleCI 2,800만 워크플로에서 처리량 약 59% 증가에도 *"three in 10 attempts to merge that code into production are failing"*(00:29~00:32), 그리고 개발자 76%가 *"code is being produced at a speed that is impossible for them to verify it"*(02:08~02:09). [[addy-osmani|Addy Osmani]]의 답은 이 페이지의 *에이전트가 증거를 낸다* 쪽이다: Claude 1차 리뷰가 *"try the experience out similar to a real user"*(04:22~04:24)하고, *"people are responsible for checking on the agent's evidence"*(05:14~05:17). 다음 개선 지점도 검증이다 — *"the next gains are going to come from a combination of us really nailing verification, right? As well as model quality."*(05:46~05:52) 처방이 막연하다는 자각이 붙는다: *"if you tell people yeah, just like verify the work, you know, their next question is what does that even mean"*(06:05~06:09). 진행 쪽 정리: *"Fast to write is not fast to ship."*(10:37) → [[agent-change-evidence]] · [[layered-verification-every-loop]]
