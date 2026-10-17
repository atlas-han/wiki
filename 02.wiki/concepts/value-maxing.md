---
title: 밸류맥싱 (Value Maxing) — 토큰맥싱과 토큰 최소화 너머
type: concept
category: framing
tags: [token-economics, metrics, value-maxing, tokenmaxxing, goodhart, roi, adoption]
aliases: [밸류맥싱, valuemaxxing, value maxing, 토큰맥싱, tokenmaxxing, token maxing, 토큰 최소화]
related: [token-minimization-trap, trusted-throughput, overspending-underusing-loop, agent-roi-measurement, true-cost-to-perfect-answer, token-roles, model-mixing-economics, context-engineering, mousepower]
first-seen: tech-bridge-tokenmaxxing-to-valuemaxxing
sources: [tech-bridge-tokenmaxxing-to-valuemaxxing, tech-bridge-introspection-loop-is-the-product, tech-bridge-conductor-orchestras-not-factories, tech-bridge-kimchi-cost-per-task-harness, tech-bridge-brockman-start-building-before-ready, tech-bridge-tailscale-aperture-ai-without-lock-in]
created: 2026-09-24
updated: 2026-10-17
---

# 밸류맥싱 (Value Maxing)

**토큰 소비를 최대화하는 것(토큰맥싱)도 최소화하는 것(토큰 최소화)도 같은 함정이고 — 둘 다 토큰을 주요 지표로 가정한다 — 최적화 대상은 토큰이 만든 결과라는 프레이밍.** [[ibm|IBM Technology]] 계열 해설([[tech-bridge-tokenmaxxing-to-valuemaxxing]])이 정리했고, 용어는 *"Nebius의 CRO인 Mark Boroditsky가 만든 용어"*(04:23~04:30)라고 귀속한다.

> ⚠️ **용어의 귀속과 철자는 영상의 주장이다**(ASR만, 설명란이 이름을 확정하지 않음). 설명란 표기는 **Valuemaxxing**. 업계 표준 용어가 아니라 **현장 coinage** — [[trusted-throughput]]·[[outcome-engineering]]과 같은 지위.

## 세 국면

| 국면 | 믿음 | 지표 | 소스의 판정 |
|---|---|---|---|
| **토큰맥싱** | *"활동량이 많을수록 가치도 커진다"*(01:22~01:24) | 사용자 수·토큰 소비 = **참여(engagement)의 대리** | *"[도입] 신호로서[는 효과가 있었다]"*(01:27) — 그러나 대시보드는 **곧 조작된다** |
| **토큰 최소화** | 비용이 문제니 토큰을 줄인다 | 여전히 토큰 | *"토큰 [맥싱]과 같은 함정"*(03:20~03:22) → [[token-minimization-trap]] |
| **밸류맥싱** | 결과가 추가 토큰을 정당화한다 | 배포·개발자 시간·재작업·취약점 | *"다음 장은 가치"*(07:59~08:02) |

핵심 문장:

> **둘 다 토큰 소비[가] 중요한 주요 지표[라고] 가정합니다. 그 어느 것도 운영 결과를 측정하지 않습니다.** (03:24~03:32)

## 토큰맥싱이 망가지는 지점 — 에이전틱 AI

> **[더] 유능한 [에이전트]들은 당연히 더 많은 토큰을 소비했습니다.** 하지만 **토큰 소비만으로는 활동과 측정 가능한 결과를 구분할 수 없었다.** (02:12~02:23)

채팅 시대에는 *많이 쓴다 ≈ 도입됐다* 가 쓸 만한 근사였다. 에이전트가 계획·저장소 분석·도구 호출·테스트·시스템 간 조율(01:55~02:12)을 하면서 **토큰이 일의 양이 아니라 탐색·재시도·실패까지 포함한 활동량**이 되고, 근사가 깨진다. Goodhart 증언은 IBM 컨설팅 SVP(*Neil Dar* — ASR 철자)의 것이다: *"[진짜] 지표[가] 부족[한 상황에서] 팀들은 [사용량 대시보드]를 만들었[고], 사람들[은 그것을 조작하는 법을] 금방 익혔습니다"*(01:34~01:44).

## 결과를 묻는 질문

> **[배포가] 얼마나 완료되었습니까? 개발자 시간[이] 얼마나 절약되었나요? 재작업이 얼마나 [회피되었나요]? 얼마나 많은 취약점을 [해결했습니까]?** (04:44~04:55)

두 가지를 판단하는 데 쓴다 — AI가 측정 가능한 결과를 만드는지, **추가(incremental) 토큰 사용이 정당한지**(04:57~05:05). 즉 밸류맥싱은 긴축이 아니다: *"목표는 인공지능[을 덜] 사용하[는 것이 아니라], 인공지능을 더 효과적으로 활용하[는 것]"*(06:25~06:30).

⚠️ **ko는 이 질문 넷 중 셋의 방향을 바꿨다**(*회피된* → *필요했던* 재작업, *해결된* → *방지한* 취약점, *절약된 시간* → *걸린 시간*). 자막만 본 시청자는 **비용 지표**로 읽는다.

## 따라 나오는 명제 — 시스템 > 모델

> **결과가 토큰보다 더 중요[하다면], 시스템이 모델들보다 더 중요해집니다.** (05:43~05:48)

모델 접근이 차별화 요소가 아니게 되면 차이는 **컨텍스트 관리 · 워크플로 오케스트레이션 · 거버넌스 · 최적화**에서 난다(05:32~05:41). 그래서 *모델 오케스트레이션 > 모델 선택* — IDC 예측(2028년까지 선도적 대규모 AI 배포의 70%가 멀티 모델, 05:53~06:05, ⚠️ 출처 없음). → [[model-mixing-economics]] · [[model-harness-knowledge-stack]] · [[tools-and-context-over-harness]]

## 분담 — 개발자 · 플랫폼 리더 · 플랫폼

- **개발자**: AI 효율성은 *"새로운 [엔지니어링] 기술"* — 클라우드 리소스·[데이터베이스]·앱 성능처럼 다룬다. **컨텍스트 위생 · 실행 전 계획 · 비용-결과 트레이드오프 이해**(06:12~06:41).
- **플랫폼 리더**: 비용과 결과 **둘 다의 가시성**, *[볼륨 대신] 가치 측정*, **효율성에 보상**(06:44~06:58). → [[trusted-throughput]]의 *"리더보드 금지"* 와 같은 방향의 인센티브 설계.
- **플랫폼**: 관리 제어(예산·거버넌스·가시성) · 분석(소비 → 운영 결과) · 워크플로·[스킬]·도구 통합(07:19~07:50). ⚠️ **벤더가 자기 층을 해법에 넣는 자리** — 제품명은 없다.

## 이 위키의 다른 토큰 경제 프레이밍과

| | 무엇을 재나 | 긴축에 대해 |
|---|---|---|
| [[trusted-throughput]] (Ironclad) | 신뢰받는 결과의 처리량 · 복잡도 가중 병합 PR | *"'긴축'에 관한 것이 아니라 ROI"* |
| [[overspending-underusing-loop]] (Piras) | (척도 미정) | 긴축은 **순환의 한 국면** |
| [[agent-roi-measurement]] (Piras) | *"버그 몇 개? 지원 요청 몇 개?"* | — |
| [[true-cost-to-perfect-answer]] (Anthropic) | 완벽한 답 하나까지의 토큰 | 실행당 비용 최소화는 착시 |
| **밸류맥싱 (IBM 계열)** | 배포·시간·재작업·취약점 | **최소화 = 맥싱과 같은 함정** |

⭐ **다섯 소스가 같은 결론이고, 이 페이지만 *최소화* 를 명시적 함정으로 이름 붙였다.** ⚠️ 동시에 다섯 소스 모두 **측정된 전후 사례가 없다**(Ironclad의 지표 진화 경로가 가장 가깝다). 그리고 판매자·벤더 쪽 화자는 **토큰 지출이 줄지 않기를 바랄 자리**에 있다 — 수렴을 독립 증거로 세지 않는다.

> ⚠️ Contradiction: [[overspending-underusing-loop]](Piras, 09-12)는 맥싱 ↔ 긴축의 **순환**을, 이 소스는 맥싱 → 최소화 → 가치의 **단계적 진행**(*"첫 번째 장은 [도입], 다음 장은 가치"*, 07:57~08:02)을 그린다. 어느 쪽도 조직 사례로 뒷받침하지 않는다 — 위키는 판정하지 않는다.

## 남은 공백

- **귀속 문제** — *배포 몇 건* 을 **어느 토큰이** 만들었는지 나누는 법을 말하지 않는다. [[agent-roi-measurement]]가 남긴 공백과 같다.
- 네 질문의 **측정 방법·기준선** 없음. Ironclad의 *복잡도 가중치*([[trusted-throughput]])나 Piras의 [[mousepower]] 같은 **단위 설계**가 없다.

## References

- [[tech-bridge-tokenmaxxing-to-valuemaxxing]] · [[ibm]]
- [[token-minimization-trap]] · [[trusted-throughput]] · [[overspending-underusing-loop]] · [[agent-roi-measurement]] · [[true-cost-to-perfect-answer]] · [[token-roles]] · [[model-mixing-economics]] · [[outcome-engineering]]

## 분모를 명시한 짝 — valued work per watt (2026-09-30 · [[tech-bridge-introspection-loop-is-the-product]])

[[roland-gavrilescu|Roland Gavrilescu]]: *"how much value am I getting per watt? Um how do I measure the value is the first step, and how do I know I'm getting a good deal on that value is the second."*(09:38~09:49). **가치를 먼저**라는 순서는 이 페이지와 같고, 분모(와트, 맺음말에선 Claude Code 대비 **가격 차이** 17:31~17:38)를 명시한다는 점이 다르다. 가치의 측정은 제작자 taste + 사용자 A/B로 넘긴다. ⚠️ 와트를 재는 방법은 없다. → [[valued-work-per-watt]]

## "우리는 토큰맥서가 아니다" — 평판의 부정 (2026-10-02 · [[tech-bridge-conductor-orchestras-not-factories]])

멀티 에이전트 앱 [[conductor|Conductor]]의 [[charlie-holtz|Charlie Holtz]]: *"a lot of people assume that we are pure token maxers and we are like ripping through like 30,000 line PRs, but we're actually not."*(05:18~05:27) 에이전트를 가장 많이 돌릴 것 같은 회사가 **토큰맥싱을 평판 위험으로** 다루고, 대안으로 [[slop-free-zone|엄격 구역/느슨한 구역]]을 든다. ⚠️ ko는 *30,000 line PRs*를 **"3만 건의 구매 요청(PR)"** 으로 옮겨 단위(줄 → 건)가 바뀌었다.

## "토큰을 무제한으로" — 벤더의 반대편 처방 (2026-10-09 · [[tech-bridge-kimchi-cost-per-task-harness]])

[[cast-ai|Cast AI]]의 [[kimchi|Kimchi]] 발표는 토큰 **최소화**를 같은 이유로 거부한다: 사용 제한은 *"you have an hour battery and you can only charge once (…) a day"*(01:36~01:42), *"We at Kimchi think this is wrong. Our jobs as manager is to do the opposite is to ensure that we want to make the tokens unlimited and inexpensive."*(01:45~02:04) — [[token-minimization-trap]]의 벤더판.

> ⚠️ **Contradiction: 처방이 갈린다.** 이 페이지는 토큰맥싱·토큰 최소화가 **둘 다** 토큰을 주 지표로 삼는다고 보고 *결과를 측정하라*고 한다. Kimchi는 *토큰 단가를 내려 무제한을 지속 가능하게 하라*고 하고, 성과를 **토큰 증가 대비 비용 감소**(토큰 1.5배↑·비용 1.5배↓)로 보고한다 — 결과 지표는 차트의 *"same outcome"*(05:04) 한 마디뿐이다. 위키의 독해: 단가 최적화는 토큰맥싱을 **싸게** 만들 뿐 결과 측정을 대신하지 않는다. 다만 Kimchi가 모델 선택 기준으로 **작업당 비용 + 산출물 점수**를 쓴다는 점은 *토큰이 아니라 결과* 쪽으로 한 발 옮긴 것이다.

## 프론티어 랩 내부의 입장 — "주 목표는 아니지만 좋은 대리 지표" (2026-10-11 · [[tech-bridge-brockman-start-building-before-ready]])

> *"there was this era of token maxing, right? Where it's just like people are just blindly saying[=throwing] more tokens at it, which is clearly not a primary objective. But it is a good proxy metric. If you're not trying to optimize tokens, you're probably going to then see improved productivity correlated with increased number of tokens. And we really do see it. We have leaderboards"* (21:52~22:09) · [[greg-brockman]]

IBM 해설의 첫 국면(토큰맥싱 → 대시보드가 곧 조작된다)을 **알면서 유지하는 쪽**이다. 조건은 *토큰을 최적화 대상으로 삼지 않을 때만* 이다. 굿하트 경고를 받아들이면서 **리더보드는 운영한다.** 처방의 무게는 양이 아니라 겨냥에 있다. *"the people who really point compute at the right problem (…) and then are willing to push the that token budget high, we're really seeing this like sort of outsized impact"* (23:30~23:45). ⚠️ 모델을 파는 회사의 사장이 말한 것이고, 리더보드의 지표와 사용 방식은 미공개다. 앞의 "우리는 토큰맥서가 아니다"(Conductor)와 "토큰을 무제한으로"(Kimchi) 사이, **대리 지표로서의 토큰맥싱**이라는 세 번째 자리다.

⚠️ ASR *"saying three or more tokens"* 를 *"throwing more tokens"* 로 판독했다. ko는 이를 **"토큰 세 개 이상"** 으로 옮겼다.

## 셋째 이름 "ROI 맥싱" — 가치 증명 + 선택권 (2026-10-17 · [[tech-bridge-tailscale-aperture-ai-without-lock-in]])

[[remy-guercio|Remy Guercio]]([[tailscale|Tailscale]]): *"We're not going to be token maxing. We're going to be ROI maxing."*(05:05~05:08) 정의는 *"when I say ROI maxing, I don't just mean cutting costs, right? I mean actually proving some sort of value to the thing that you're doing."*(05:15~05:24)이다. 여기에 **선택권**을 더한다: *"ROI maxing really is all about maximizing choice to prevent lock-in"*(17:40~17:48). 비용 구조가 사내 확산의 상한을 정한다는 논증도 이 위키에서 처음이다(*"You can't actually expand AI usage into the company if that's the only way you can use AI."* 05:37~05:42).

토큰맥싱을 부정하며 시작하지 않는다는 점이 IBM 해설과 다르다. 지난 12개월은 *"it's really made truly agentic coding possible"*(01:21~01:23)였다. 문제는 비용과 *"wasted tokens by default"*(02:07~02:12), 그리고 수직 통합이다.

⚠️ 가치를 *어떻게* 증명하는지는 발화되지 않는다. 처방은 자사 제품 범주([[ai-gateway]])로 귀결되는 벤더 발표다. ko는 *"I don't just mean cutting costs"* 를 **"비용 절감을 말씀하시는 거죠?"**(05:17)라는 되물음으로 바꾼다.
