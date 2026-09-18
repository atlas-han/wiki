---
title: 레거시 코드 현대화 (Legacy Code Modernization)
type: engineering
category: pattern
tags: [legacy, modernization, migration, architecture, cicd, technical-debt, agents]
aliases: [레거시 현대화, 현대화의 세 축]
related: [technical-debt, legacy-skills-gap, syntactically-correct-behaviorally-wrong, risk-proportional-human-review, greenfield-vs-brownfield-agent-risk, refactoring, ai-native-sdlc]
first-seen: tech-bridge-legacy-code-modernization-ai
sources: [tech-bridge-legacy-code-modernization-ai]
created: 2026-09-18
updated: 2026-09-18
---

# 레거시 코드 현대화

**레거시 코드는 여전히 돌아가지만 아무도 완전히 이해하지 못하는 핵심 인프라이고, 현대화는 그것을 새 언어로 번역하는 일이 아니라 아키텍처·기술·프로세스를 점진적으로 바꾸는 일이다.** [[anna-gutowska|Anna Gutowska]]([[ibm|IBM]])가 [[tech-bridge-legacy-code-modernization-ai]]에서 정리했다.

## 정의 — 오래됨이 아니라 이해의 부재

> **레거시 코드는 여전히 작동하지만 유지 관리 측면에서 상당한 복잡성을 수반하는 소프트웨어입니다.** (…) **구식 프로그래밍 언어**, **노후화되었거나 지원되지 않는 인프라**, **자동화된 테스트 부족**, **문서 부재**. (00:53~01:13)

> **문서화되지 않아 아무도 완전히 이해하지 못하는 중요한 도메인별 논리**가 포함되어 있기도 합니다. (01:16~01:23)

> **변경할 때마다 위험 부담이 느껴지기 때문에 아무도 손대고 싶어하지 않습니다.** (01:29~01:34)

네 속성 중 **뒤의 둘(테스트 없음·문서 없음)이 결정적**이다 — 앞의 둘(옛 언어·옛 인프라)은 위험이 아니라 비용이고, 위험은 *바꿨을 때 무엇이 깨지는지 알 수 없다* 는 데서 온다.

## 왜 지금 더 나빠지는가

| 추세 | 내용 |
|---|---|
| **사람** | 옛 시스템을 아는 개발자가 은퇴하고 신입은 다른 스택을 배운다 → [[legacy-skills-gap]] |
| **생산성** | 부채·유지보수·디버깅이 새 것을 만드는 시간을 먹는다 |
| **보안** | 패치·규정 준수 불가, *"기다리는 해가 길어질수록 취약점 표면은 더 커집니다"* (03:31~03:33) |

셋째가 [[technical-debt]]에 없던 차원이다 — 부채의 이자가 **변경 비용**만이 아니라 **보안 노출**로도 붙는다.

## AI가 들어오는 두 자리, 그리고 에이전트

| 단계 | 옛 방식 | AI |
|---|---|---|
| **발견** | *"몇 달씩"* 코드를 읽는다 — 문서와 원저자가 없으므로 | 코드베이스 전체를 읽어 **모듈 기능·데이터 흐름·도메인 로직 위치**를 요약, *"몇 달 → 몇 주"* (04:15~04:36) ⚠️ 근거 없음 |
| **번역** | 구성 요소를 **하나씩 손으로**, *"안 깨지길 바라며"* | COBOL→Java · C→Python · 배치→이벤트 기반/서버리스, *"논리와 의도는 유지"* (04:38~04:56) |
| **에이전트** | — | 분석 → 계획 → 번역 → **테스트 작성** → 문서화를 *"최소한의 사람 개입으로 순차적으로"* (05:12~05:26) |

발견 단계는 이 위키가 도구 층위에서 이미 가진 것의 일반 서술이다 — [[tech-bridge-cursor-legacy-refactoring]]의 `/canvas`, [[code-knowledge-graph]], [[file-discovery-tax]]. 에이전트 단계는 [[tech-bridge-cursor-legacy-refactoring]]의 네 단계(감사 → 계획 → 티켓 → 위임)와 같은 구조를 **제품 없이** 말한 것이다.

## 현대화 ≠ 번역 — 세 축

> 목표는 **수십 년간 축적된 핵심 논리를 유지하면서 시스템을 더 쉽게 발전시킬 수 있도록** 하는 것입니다. (05:59~06:04)

| 축 | 에서 | 로 | 얻는 것 |
|---|---|---|---|
| **아키텍처** | 긴밀히 결합된 모놀리스 | 독립 서비스 | *"전체 플랫폼을 중단하지 않고 업데이트·확장"* |
| **기술** | 옛 언어·프레임워크·온프레미스 | 현대 플랫폼 | 보안 업데이트 · 클라우드 통합 · 최신 도구 |
| **개발 프로세스** | 수개월 수동 테스트, 연 몇 회 출시 | 자동 테스트 + 지속 배포 | *"더 작고 안전한 변경을 더 자주"* |

> **핵심은 현대화는 기존 프로세스를 유지하면서 그 아래에서 기술이 발전하는 점진적인 과정이라는 점입니다.** (07:21~07:29)

셋째 축이 [[ai-native-sdlc]]·[[trusted-throughput]]이 말해 온 처방과 같고, 이 소스는 그것을 **현대화의 목적지**로 둔다 — 즉 레거시를 옮기는 이유 중 하나가 *자주 안전하게 바꿀 수 있는 상태* 가 되기 위해서다. ⚠️ **세 축의 순서·의존은 없다.**

## 한계와 처방

> AI 모델은 **매우 복잡하게 얽힌 도메인별 논리**에 어려움을 겪을 수 있습니다. 또한 **문법적으로는 올바르지만 동작상으로는 잘못된 번역**을 생성할 수도 있습니다. (07:34~07:51) → [[syntactically-correct-behaviorally-wrong]]

> **기존의 취약점을 자동으로 제거하거나 안전한 코드를 보장할 것으로 기대해서는 안 됩니다.** (07:57~08:05) → [[shift-left-security]]

> 효과는 **모델 자체뿐만 아니라 (…) 테스트, 사람 검토 및 검증을 통합하는 잘 설계된 워크플로**에도 달려 있습니다. (08:07~08:23)

> **AI를 자동화의 승수(force multiplier)로** (…) **가장 큰 위험을 수반하는 결정에 경험 많은 엔지니어들이 가까이** (08:26~08:39) → [[risk-proportional-human-review]]

## [[greenfield-vs-brownfield-agent-risk]]와의 관계

[[lauren-tan]]은 *브라운필드가 안전하다 — **이미 잘 세팅돼 있다면***이라고 했다. 이 페이지의 레거시 정의(테스트 없음·문서 없음·이해 없음)는 **그 조건을 갖추지 못한 브라운필드**다. 두 소스는 모순이 아니라 **가드레일의 유무**로 갈린다 — 옛 코드가 위험한지는 나이가 아니라 가드레일이 정한다는 결론에 양쪽이 각자 도달한다.

## 표시해 둔 것

> ⚠️ **수치 근거 없음** — *몇 달 → 몇 주*, *시간의 절반*. **도구·제품·사례 0개.** *"의도는 유지된다"*(번역)와 *"동작이 틀릴 수 있다"*(한계)가 같은 영상 안에서 정리되지 않는다. **"가장 큰 위험을 수반하는 결정"의 예시가 없다.**

## References

- [[tech-bridge-legacy-code-modernization-ai]] · [[anna-gutowska]] · [[ibm]]
- 관련: [[technical-debt]] · [[legacy-skills-gap]] · [[syntactically-correct-behaviorally-wrong]] · [[risk-proportional-human-review]] · [[greenfield-vs-brownfield-agent-risk]] · [[tech-bridge-cursor-legacy-refactoring]] · [[refactoring]] · [[ai-native-sdlc]]
