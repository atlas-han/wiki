---
title: Trusted Throughput
type: concept
category: pattern
tags: [productivity-metrics, token-economics, code-review, ci, goodhart, roi]
related: [verifiable-goals, agent-org-adoption, frontier-engineering, generator-evaluator-pattern, outcome-engineering, token-roles, context-resets-and-compaction, intelligence-as-infrastructure, compute-constrained-growth, value-maxing, token-minimization-trap, effort-output-outcome-mission]
first-seen: tech-bridge-trusted-throughput
sources: [tech-bridge-trusted-throughput, tech-bridge-claude-platform-agent-era, tech-bridge-flutter-ai-workflow, tech-bridge-jensen-huang-g20-agi, tech-bridge-altman-astra-hardware, tech-bridge-ai-era-code-quality, tech-bridge-knowledge-work-agent-infrastructure, tech-bridge-mousepower-measuring-agents, tech-bridge-lauren-tan-trusting-agents, tech-bridge-tokenmaxxing-to-valuemaxxing, tech-bridge-lauren-tan-2000-prs, tech-bridge-lauren-tan-agent-dev-workflow, tech-bridge-kent-beck-craft-augmented-development, tech-bridge-gitar-agentic-pr-validation, tech-bridge-g2i-generation-cheap-evaluation-expensive, tech-bridge-factory-bug-report-to-production, tech-bridge-anthropic-30k-merges-verification]
created: 2026-09-02
updated: 2026-10-31
---

# Trusted Throughput

**Trusted throughput**은 [[mingsheng-hong|Mingsheng Hong]]([[ironclad|Ironclad]] VP of Engineering, AI)이 [[tech-bridge-trusted-throughput|강연]]에서 제시한 지표 프레이밍으로, AI 도입 이후 조직이 최적화해야 할 대상을 *토큰 사용량*이나 *코드 생산량*이 아니라 **내부 엔지니어링·경영진과 외부 고객 모두가 신뢰하는 고품질 결과물의 처리량**으로 정의한다.

> 여기서 목표는 토큰 지출을 최소화하거나 실제로 줄이는 것이 아닙니다. (…) **'긴축(austerity)'에 관한 것이 아니라** 토큰 사용에 대한 **ROI를 향상**시키는 것에 관한 것입니다.

> ⚠️ 이 용어는 한 조직의 **현장 coinage**다. 업계 표준 용어가 아니며, 아래 연결은 이 위키의 기존 개념과의 해석적 매핑이다.

## 논증의 축: 토큰은 LOC다

이 프레이밍 전체가 하나의 비유 위에 서 있다.

> [LOC를] 속도를 측정하는 **핵심 목표**로 삼는 것은 현명하지 않을 것입니다. (…) 생산적이고 고품질의 작업을 원한다면 **코드를 제거하는 것이 훨씬 더 좋다**고 주장할 수도 있으니까요.

> LOC는 중요한 지표이지만, 직접적으로 최적화해야 할 대상은 아닙니다. **토큰 사용량과 지출도 마찬가지입니다.**

즉 [[verifiable-goals]]가 경고한 Goodhart 문제를 토큰 경제에 옮긴 것이다. 실제 사고 사례가 근거로 제시된다 — Amazon에서 자발적으로 만들어진 전사 토큰 대시보드가 리더보드처럼 작동해 **엔지니어들이 사용량 극대화를 경쟁**하기 시작했다.

## 대시보드는 연기 감지기다

> 우리는 사용량 대시보드를 **연기 감지기**와 같은 것으로 생각합니다.

방향이 통념과 반대라는 점이 핵심이다.

| 통념 | 이 프레이밍 |
|---|---|
| 많이 쓰는 사람 = 잘 활용 | **거의 안 쓰는 국소적 집단**이 조사할 신호 (도입 격차) |
| 순위를 매겨 보상 | 사용량 극대화의 **간접적 동기조차** 만들지 않음 |

검토 목적은 두 가지로 좁혀진다 — (A) **도입 격차**, (B) **예상치 못한 급증**. 단, 팀마다 AI 활용 방식이 다르므로(플랫폼 인프라 팀 vs UI 팀) **맥락을 고려한** 비교여야 한다.

## 지표의 진화 경로

실패한 단계를 포함해 공개된 것이 실무적 가치다.

| 단계 | 지표 | 왜 버렸나 |
|---|---|---|
| 1 | 코드 라인 수 | 가치의 대리 지표로 부적절 |
| 2 | **열린** PR 수 | "결국 우리는 **출시한 코드**로 평가받는다" |
| 3 | **병합된** PR 수 | "병합 PR이 모두 동일하지 않다" |
| 4 | **복잡도 가중치가 적용된 병합 PR** | 현재 (완성형 아님) |

3단계의 반례 — 동시성 버그를 잡는 **10줄 PR** vs 가치를 별로 더하지 않는 **수천 줄의 보일러플레이트**.

복잡도 점수는 **LLM 1~2개에 잘 만든 프롬프트를 넣어 티셔츠 사이즈로 채점**해 얻는다. 즉 [[generator-evaluator-pattern]]을 코드가 아니라 **생산성 계측 자체**에 적용한다.

## 정성적 정의: 세 버킷

| 버킷 | 내용 |
|---|---|
| 객관적 검사 | 테스트 커버리지, 사전 정의된 보안 검사, 안전 배포 시 **카나리** |
| 주관적 인간 판단 | 코드 리뷰·디자인 리뷰 — 품질·명확성·유지보수성·아키텍처 적합성 |
| 고객 반응 | 프로덕션 **롤백** 여부, 사용성·불편·버그 **티켓** |

세 버킷이 모두 필요하다는 것이 요점이다. 자동 검사만으로는 아키텍처 적합성이 잡히지 않고, 내부 리뷰만으로는 고객 반응이 잡히지 않는다.

## 병목의 이동: 생성 → 리뷰·CI

AI 코드 생성이 PR 생성량을 급증시키면서 병목이 **리뷰와 병합**으로 옮겨간다.

### 안티패턴

CI 과부하에 대한 자연스러운 대응이 오히려 위험하다.

> "엔지니어들이 **PR 분할을 중단**하고, 그냥 큰 PR을 한꺼번에 검토 및 제출하는 방식을 택하자"

산술은 이해된다 — 회귀 테스트가 **1시간**이면 10개로 쪼갤 때 **10시간**이다. 하지만 사람 검토 부담이 커지고 **주의력이 분산되어 검토 품질이 떨어진다.**

### 처방: AI가 1차 방어선

- 코딩 스타일·테스트 커버리지 같은 **간단한 사항** → AI 검토
- 저자가 그 단계를 끝낸 **뒤에야** 사람에게 전달
- 사람은 **아키텍처·보안 설계·주관적 심층 판단**에 집중

> 그래서 최종적으로는 우리 엔지니어링 팀이 **책임을 질 수 있게** 됩니다.

### CI 품질이 토큰 비용이 된다

이 개념의 가장 비직관적인 연결 고리다. flaky 테스트를 방치하면 엔지니어는 **수동 재실행**을 하거나 **AI 에이전트에게 반복 재시도를 시켜 토큰을 낭비**한다. 즉 **토큰 낭비의 원인이 모델이 아니라 CI 품질**일 수 있다.

측정 지표:

- **PR 제출 준비 완료 → 실제 제출까지의 대기 시간**
  > CI 실행에 한 시간이 걸린다면, PR 제출에는 두세 시간이 걸릴까요? 그런 경우라면 **위험 신호**입니다.
- PR이 테스트를 통과하기까지의 **재시도 횟수**

## 토큰 효율 기법

- **제한된 에이전트 루프** — 루프 단계 수를 제한해 통제 불능 시 낭비 방지. [[ralph-wiggum-method]]의 무한 루프와 정확히 반대 방향의 안전장치
- **프롬프트 캐싱** — 고정 시스템 프롬프트를 위, 가변 콘텐츠를 아래
- **컨텍스트 가지치기** — 요약을 조직의 **습관**으로 만든다
  > 토큰 사용 효율성을 높일 뿐만 아니라 **AI 출력의 품질도 향상**시킵니다

## Build vs. buy

> IDE나 CI 인프라처럼 **차별화 요소가 아닌 부분은 구매**하고 싶습니다.

내부에서 만드는 것은 **자기 상황에 특화된 프롬프트 플레이북**이고 팀 전체가 재사용·개선한다 — [[agent-skills]] 레지스트리와 같은 구조를 프롬프트 자산에 적용한 것.

## 공급자 쪽에서의 수렴

[[tech-bridge-claude-platform-agent-era|Claude Platform 팀]]이 같은 주에 반대편(공급자)에서 같은 결론에 도달했다.

> 사람들은 문제를 해결하기 위한 메커니즘으로 **모델**을 찾는 경향이 있는데 (…) 비용에 대한 이야기는 들었지만, **도대체 무엇을 하려고 했던 건가요?**

> 때로는 역설적이게도 **더 크고 비싼 모델을 사용하는 것이 더 나은 선택**일 수도 있습니다. (…) 모든 토큰이 정확하다면 낭비되는 것이 전혀 없고

> 이런 종류의 **토큰 경제학은 불행히도 현실과 다소 동떨어져** 있는 것 같습니다.

구매자와 공급자가 독립적으로 **"토큰 단가는 잘못된 최적화 대상"**에 합의한 셈이다. 다만 각자의 인센티브가 그 결론과 정렬돼 있다는 점은 감안해야 한다.

## 관련

- [[verifiable-goals]] — Goodhart 경고의 원류. trusted throughput은 그것을 3중 검증으로 구현
- [[agent-org-adoption]] · [[frontier-engineering]] — *도입*을 다룬다면 이쪽은 **도입 이후 무엇을 계측할 것인가**
- [[generator-evaluator-pattern]] — 지표 산출과 리뷰 파이프라인 양쪽에 적용
- [[token-roles]] — 같은 문제("토큰 단가가 답이 아니다")에 대한 공급자 쪽 처방
- [[outcome-engineering]] — 결과를 정의하고 에이전트와 함께 만든다는 인접 프레이밍

## 개인 수준의 대응물: 게임화된 토큰 (2026-09-02)

Amazon 리더보드 일화가 조직에서 생긴 Goodhart라면, [[ivanna-kacevica|Ivanna Kaceviča]]([[tech-bridge-flutter-ai-workflow]])는 같은 현상을 **개인 안에서** 솔직하게 보고한다.

> 룰렛 게임은 별로 안 좋아해요. 저는 **토큰을 다 써버리는 걸** 좋아해요. (…) 세 대의 기계 모두에서 제 한계를 모두 소진할 때까지 작업을 계속합니다.

> 토큰이 다 떨어지기 전에 아직 남아 있다는 이 느낌은, 제 생각엔 일종의 심리적인 현상인 것 같아요. — 진행자: "게임화된 거예요."

차이는 발표자가 이것을 **문제로 규정하지 않는다**는 점이다 — *"지나치게 생산적인 사람이 된 것 같아서 속도를 좀 줄여야 할 것 같아요"*라는 농담으로 처리한다. 이 페이지의 처방(대시보드는 연기 감지기, 조사 신호는 *안 쓰는 쪽*)이 개인 수준에서는 아직 없다. 두 소스를 나란히 두면 **한도(limit)가 곧 목표가 되는** 구조는 조직이든 개인이든 같고, 다른 것은 그것을 문제로 볼 인센티브뿐이다.

## 판매자 층의 토큰 — kWh 비유 (2026-09-06)

이 페이지(구매자: 토큰=LOC)와 [[token-roles]](모델 공급자: 토큰=역할)에 세 번째 층이 붙었다. [[jensen-huang|Jensen Huang]]([[tech-bridge-jensen-huang-g20-agi]]):

> 세계는 **에너지**라는 새로운 개념을 발견하고 그것을 **킬로와트시당 달러**로 환산하여 화폐 가치를 매겼습니다. 오늘날에는 **백만 토큰당 달러**로 계산됩니다. **같은 개념이에요.**

| 층 | 토큰의 정의 | 최적화 방향 |
|---|---|---|
| 구매자 (이 페이지) | LOC — 연기 감지기 | 총량이 아니라 **ROI** |
| 모델 공급자 ([[token-roles]]) | 역할 — advising·grading·dreaming | 단가가 아니라 **정확한 토큰** |
| 하드웨어 공급자 ([[intelligence-as-infrastructure]]) | 상품 단위 — kWh의 후계 | **더 많이** |

그리고 [[sam-altman]]([[tech-bridge-altman-astra-hardware]])이 총량의 추세를 준다 — *"효율성 향상을 찾을 때마다 전 세계 토큰 수요가 계속 급증해서 그걸 다 잡아먹어 버리죠."* → [[compute-constrained-growth]]

이 페이지의 처방(*"토큰 단가는 잘못된 최적화 대상"*)은 세 층 어디서도 부정되지 않는다. 다만 하드웨어 층에서는 그것이 *"그러니 더 써라"* 로 읽힌다는 점을 기록해 둔다 — Amazon 리더보드 일화가 경고한 바로 그 방향이다.

## 같은 구조가 두 자리에서 반복된다 (2026-09-08)

이날 두 소스가 이 페이지의 핵심 구조 — **가드레일은 속도를 늦추는 것이 아니라 안전한 확장을 가능하게 한다** — 를 각기 다른 층위에서 반복한다.

**개발 프로세스에서** ([[tech-bridge-ai-era-code-quality]]):

> 이러한 자동 가드레일은 일관성을 높이는 것 이상의 일을 합니다. **보안, 컴플라이언스, 엔지니어링 표준이 팀 전체에 걸쳐 일관되게 강제되도록 보장함으로써 조직이 AI 도입을 안전하게 확장하도록 돕습니다. 거버넌스가 사후 고려가 아니라 워크플로의 일부가 됩니다.**

→ [[executable-standards]]

**에이전트 런타임에서** ([[tech-bridge-knowledge-work-agent-infrastructure]]):

> 거버넌스는 **하나의 게이트가 아니라 여러 개이고, 각각은 노출되는 폭발 반경에 따라 크기가 다릅니다. 안전한 부분에서는 아무것도 에이전트를 느리게 하지 않습니다.**

> **그 선이 촘촘할수록 에이전트를 더 믿고 마음껏 풀어놓을 수 있습니다.**

→ [[agent-governance-layers]]

**세 소스가 같은 형태의 주장을 한다는 것이 이 페이지의 논지를 강화한다** — [[mingsheng-hong]]이 조직 운영에서, IBM이 개발 프로세스에서, [[karan-vaidya]]가 에이전트 런타임에서. 셋 다 *신뢰를 만드는 장치가 처리량의 조건* 이라고 말하고, 셋 다 **그 장치가 균일한 게이트가 아니라 위험에 비례한 게이트여야 한다**고 말한다.

> ⚠️ 세 소스 모두 **가드레일 자체의 비용을 정량화하지 않는다.** 모든 커밋 검증·상시 정적 분석·모든 파괴적 행동의 샌드박스 경유가 무엇을 얼마나 느리게 하는지 어느 쪽도 답하지 않는다.

## 같은 단어, 다른 층 — 마우스파워 편 (2026-09-12)

[[tech-bridge-mousepower-measuring-agents]]가 이 페이지와 **같은 단어에서 만난다.** 이 페이지의 원 소스([[ironclad|Ironclad]])는 *"'긴축(austerity)'에 관한 것이 아니라 토큰 사용에 대한 ROI를 향상시키는 것"* 이라고 했는데, [[maximillian-piras]]는 **긴축을 악순환의 한 국면**으로 그린다:

> **토큰 맥싱으로 스스로를 긴축(austerity)으로 몰아넣고, 그러다 루프에서 이탈했다가, FOMO가 다시 차오르면 재시도**하는 악순환이죠.

→ [[overspending-underusing-loop]]

토큰에 대한 처방도 같다:

> 토큰은 **내부 시스템의 측정값으로는 유용**하지만 **결국 산출물일 뿐**이고 (…) **우리가 산 토큰으로 버그를 몇 개 잡았나? 지원 요청을 몇 개 닫았나?**

**차이는 청중이다.** 이 페이지의 지표는 **조직이 스스로에게** 쓰는 것이고, 마우스파워 편은 **판매자가 고객에게 가치를 전달하는 문제**를 다룬다. 그래서 한 조건이 추가된다 — ***"측정은 그것을 쓰는 고객의 멘탈 모델에 맞아야 한다."*** → [[agent-roi-measurement]] · [[mousepower]]

**토큰 리더보드**가 이 페이지의 Goodhart 경고에 붙는 구체적 사례로 등장한다.

## ⚠️ Goodhart의 실례 — PR 수 (2026-09-12 Lauren Tan 편)

[[tech-bridge-lauren-tan-trusting-agents]]의 자기 보고 수치(**지난달 PR 1,000건 · 이번 달 12일 시점 800건 · 하룻밤 20건 자동 병합**)는 **이 페이지가 경고한 지표의 모양 그 자체**다. 화자도 먼저 인정한다 — *"이 코드 중 실제로 좋은 게 얼마나 되냐고 물으실 겁니다. 충분히 물을 만한 질문입니다."*

다만 그쪽의 답은 **처리량이 아니라 신뢰**다 → [[agent-trust-curve]]. 그리고 **평균 PR 크기는 본인이 모른다**고 답했다 — 분모가 없는 분자다.

## References

- [[tech-bridge-trusted-throughput]] — [[mingsheng-hong]] ([[ironclad]]), 2026-09-01
- [[tech-bridge-claude-platform-agent-era]] — Anthropic Claude Platform 팀, 2026-09-01
- [[tech-bridge-jensen-huang-g20-agi]] · [[tech-bridge-altman-astra-hardware]] — 판매자 층의 토큰 (2026-09-06)

## 대시보드는 조작된다 — IBM 컨설팅의 증언 (2026-09-24 · [[tech-bridge-tokenmaxxing-to-valuemaxxing]])

> **[진짜] 지표[가] 부족[한 상황에서] 팀들은 [사용량 대시보드]를 만들었[고], 사람들[은 그것을 조작(game)하는 법을] 금방 익혔습니다.** 곧 **사용[량]이 가치의 [대리] 지표가 되었습니다.** — IBM 컨설팅 SVP *Neil Dar*(ASR 철자, 설명란 미확정) 인용 (01:32~01:46)

이 페이지 원 소스의 Amazon 리더보드 사례가 **일반화된 증언**으로 다시 나왔다. 처방도 같다 — *"목표는 인공지능[을 덜] 사용하[는 것이 아니라], 인공지능을 더 효과적으로 활용하[는 것]"*(06:25~06:30) = 이 페이지의 *"'긴축'에 관한 것이 아니라 ROI"*. 새로 붙은 것은 둘이다: **긴축 쪽의 실패 메커니즘**([[token-minimization-trap]] — 컨텍스트 절감 → 재작업)과 **플랫폼 리더의 인센티브**(*"[볼륨 대신] 가치를 측정해야 하고, 효율성[에] 보상"*, 06:51~06:55). ⚠️ ko가 *dashboards* → **"패널"**, *game* → **"조종"**, *instead of* **누락**으로 이 문장들의 Goodhart 의미를 흐렸다. → [[value-maxing]]

## 수치는 두 배, 유보는 사라졌다 (2026-09-26 · [[tech-bridge-lauren-tan-2000-prs]])

[[lauren-tan]]의 녹화 발표: *"지난달 **PR 2,000개**를 프로덕션에 반영"*(00:07~00:16) — 09-12 워크숍의 *지난달 1,000 · 12일 시점 ~800* 의 두 배다. 화자는 *"목표가 아니었다"*(04:24~04:31)고 하지만, 워크숍에 있던 **유보**(평균 PR 크기 모름, 맹목적 신뢰 경계, 무제한 토큰 인정)는 **녹화 발표에 하나도 없다.** 이 페이지의 기준으로 읽으면 **PR 수는 여전히 throughput이지 trusted throughput의 증거가 아니다** — 회귀·되돌림·리뷰 부담의 수치가 없다. → [[agent-trust-curve]]

## 세 번째 값 2,500 — 그리고 유보의 복귀 (2026-10-09 · [[tech-bridge-lauren-tan-agent-dev-workflow]])

Tech Bridge 해설 영상이 *"X에서는 … 한 달에 2,500개의 PR을 프로덕션에 반영했다고 소개했습니다"*(ko 00:11~00:17)라고 **내레이터의 입으로** 전한다. **본인 발화가 아니고, 달이 없고, 출처는 X 프로필**이다(이 위키는 열어 보지 않았다). 해설 스스로 *"2,500개의 새 기능을 만들었다는 뜻은 아닙니다"*(00:22~00:26)라고 단서를 단다 — **PR 수 ≠ 산출이라는 이 페이지의 경고를 채널이 먼저 말한 첫 사례.**

자기 보고 계열: 09-12 *지난달 1,000* → 09-25 *지난달 2,000* → **X 프로필 2,500/월**. 반면 같은 영상의 대담 발췌에서 본인은 *"it's very hard to get to this point. I don't want to sell this as (…) something that you can just do easily"*(10:12~10:21)라고 말한다 — 09-25에 사라졌던 유보가 **대담 형식에서는 남아 있다.**

## LOC·PR 수의 자리 — 노력과 산출 (2026-10-09 · [[tech-bridge-kent-beck-craft-augmented-development]])

[[kent-beck|Kent Beck]]이 [[effort-output-outcome-mission|노력 → 산출 → 결과 → 미션]] 사슬로 이 페이지의 경고에 위치를 준다: *"The Genie produced 200,000 lines of code. That's a measure of effort. It has nothing to do with the mission."*(46:00~46:07), *"lines of code (…) somehow it's back PR count"*(47:10~47:22). Goodhart는 더 나쁘다 — *"I think Goodart was an optimist. (…) people will twist the entire system out of shape."*(48:41~48:52)

## 토큰 리더보드에 대한 풍자 (2026-10-15 · [[tech-bridge-g2i-generation-cheap-evaluation-expensive]])

*"we've completely forgotten that lines of code is a garbage metric for productivity, but then we decided that it's different than deciding the engineer who burns the most tokens must be producing the most."*(10:41~10:51) [[gabriel-martinez|Gabriel Martinez]]는 "토큰은 LOC다"를 풍자로 말한다. 그가 제시하는 보상 대상은 *"producing value, elegant, well-factored, pragmatic system design, and around clarity of test and evaluation harnesses"*(08:24~08:31)다. 지표는 제안하지 않는다.

## flaky 테스트 — 고치게 하는가, 재시도로 덮는가 (2026-10-14 · [[tech-bridge-gitar-agentic-pr-validation]])

[[gitar|Gitar]]는 flaky 테스트를 두 방향으로 다룬다. ① 플랫폼 팀에 CI 실패 분류를 준다: *"Are these flakiness issues that you can that you need to address by improving the reliability of the tests or are there infrastructure issues"*(07:04~07:12). ② 동시에 *"you can even set up rules that automatically retry flaky tests if you want. That's a very popular feature."*(04:41~04:47) ②는 이 페이지가 경고한 증상(에이전트의 반복 재시도가 낭비하는 토큰)을 자동화하는 쪽일 수도 있다. 화자는 이 긴장을 다루지 않는다.

PR 분류(*"what amount of PRs are going to feature development versus fixing issues, chores, refactors"* 07:37~07:44)는 PR 수·LOC 계열 지표와 이웃하지만, 양이 아니라 **구성**을 본다. 분류 정확도는 미발화다.

## Goodhart의 명시적 인용과 지표 이름 다섯 (2026-10-17 · [[tech-bridge-factory-bug-report-to-production]])

*"Token leaderboards at big companies just encourage profligate spending. It's Goodhart's law in real time. If you decide to measure token usage, engineers are going to optimize for token usage, and then it's no longer a good metric."*(16:32~16:49) [[davis-palmie|Davis Palmie]]([[factory-ai|Factory]])는 *"It's about who can get the highest leverage outcomes from that spent."*(16:54~16:58)이라고 하고, Factory가 보는 지표를 이름으로 든다: *"signal to production time, human intervention count, median time to repair, shelf life of code, and cost per PR. These are real tangible outcomes."*(17:02~17:13)

이 페이지의 논증(토큰은 LOC다, 대시보드는 조작된다)에 **벤더 쪽의 명시적 Goodhart 인용**이 더해진다. *human intervention count* 는 Tessl의 *manual takeovers* 와 같은 계열로 사람의 개입을 센다. ⚠️ 다섯 지표 모두 이름만 있고 정의·값·사례가 없다. ko는 *signal to production time* 을 "이제 시작할 시간이에요 / 생산에 대한 신호"(17:01~17:03)로, *median* 을 "mean"으로 옮긴다(ko·`en` 공유).

## "하루 3만 건" — 누가 말했고 누가 확인하지 않았나 (2026-10-31 · [[tech-bridge-anthropic-30k-merges-verification]])

영상 제목의 숫자는 진행 쪽([[manish-kapur]] 추정) 발화다: *"They are merging about 30,000 code changes every single day. They used to do about 3,000 or so, 2,500 or so code changes just a few months back. They've scaled from 2,500 code changes to 3,000 30,000 code changes per day."*(03:27~03:41) — 스스로 3,000 → 30,000으로 고친다. [[addy-osmani|Addy Osmani]]([[anthropic|Anthropic]] 쪽)의 숫자는 *"about 2,500 changes all the way back in May"*(03:50~03:53, **기간 단위 미발화**)와 Claude.ai 개편 때 *"about 3,000 pull requests in a very short space of time"*(04:03~04:05)뿐이고 3만은 되풀이하지 않는다. 설명란의 Anthropic 글(redesigning-source-control)이 출처일 수 있으나 열어 보지 않았다(미확인). ⚠️ 이 페이지의 경고대로 *변경 수 ≠ 산출*: 같은 대담이 *"Fast to write is not fast to ship"*(10:37)으로 끝나고, CircleCI 통계(처리량 +59%, 병합 시도 10건 중 3건 실패, 00:20~00:32)가 처리량과 병합 성공이 따로 움직인다는 반례로 인용된다.
