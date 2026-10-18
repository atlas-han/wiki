---
title: Vercel
type: entity
category: org
tags: [platform, web-infra, agent-infra, ai-sdk, nextjs]
links:
  - "https://vercel.com"
sources: [tech-bridge-vercel-eve-filesystem-agent, tech-bridge-vercel-rauch-agentic-workflow, tech-bridge-fireworks-train-to-deploy-open-models]
created: 2026-09-19
updated: 2026-10-18
---

# Vercel

[[nextjs|Next.js]]를 만든 웹 플랫폼 기업. 본 위키에는 **[[tech-bridge-vercel-eve-filesystem-agent]]** 로 처음 들어왔다 — [[andrew-qu|Andrew Qu]](소프트웨어 총괄)의 발표.

## 자기 규정

> Vercel은 **사람들이 미래를 만들어갈 수 있도록 에이전트 기반 인프라를 구축하는 플랫폼**입니다. 저희는 웹 업계에서 사람들이 **인프라 구축에 신경 쓰지 않고도** 웹사이트와 웹 앱을 출시할 수 있도록 돕는 일을 시작했습니다. (00:17~00:34)

> 사람들은 처음에는 **페이지를 만드는 것**부터 시작했지만, 이제는 **에이전트를 만들고 싶어하는 것** 같습니다. (00:36~00:54)

**페이지 → 에이전트**라는 전환을 회사 서사의 축으로 놓는다. 그 전환을 [[nextjs|Next.js]]가 웹에서 한 일([[framework-defined-agent-infrastructure|프레임워크 정의 인프라]])의 반복으로 제시한다.

## 제품 (소스가 언급한 것)

| 제품 | 역할 |
|---|---|
| **AI SDK** | 공급자별 코드 *"300~400줄"* 대신 **한 줄**로 모델 교체, 동일 모델 인터페이스. 모델 대체·안전한 코드 실행·대기 중 과금·내구성/재개 |
| **[[eve-framework\|Eve]]** | 파일 시스템 컨벤션으로 에이전트를 조립하는 프레임워크 (2주 전 런던 행사에서 공개) |
| **Vercel 워크플로** | Eve 런타임의 **내구성(durability)** |
| **샌드박스** | 안전한 실행 — [[file-system-agent]]의 바닥이 되는 곳 |
| **Vercel Connect** | 연결용 **단기 OIDC 토큰** 생성 |
| **skills.sh** | *"에이전트 스킬을 찾고 직접 실행하는 가장 인기 있는 방법"* → [[agent-skills]] |

⚠️ 전부 **자기 진술**이다. skills.sh의 *"가장 인기 있는"* 에는 근거가 없다.

## 사내 에이전트 도입

- **D0** — 데이터 사이언스 에이전트. 세 번의 아키텍처를 거쳐 [[file-system-agent]]에 닿았다 → [[agent-architecture-progression]]
- 하루 **수천 건**의 쿼리, 증류된 스킬 **약 100개** → [[query-to-skill-distillation]]
- 사내 **약 20개**의 product-market fit 에이전트 — 마케팅 회고 · 법무 계약 레드라인 · 데이터 쿼리
- 발표자 자신이 쓴 블로그가 *"그 주 vercel.com 트래픽의 70%"*

⚠️ 수치는 전부 자기 진술이고 조건이 없다.

## 이 위키에서의 좌표

**자기 제품이 아닌 것을 돌파구로 지목한 판매자 소스**다 — [[claude-code|Claude Code]]와 [[claude-opus-4-5|Opus 4.5]]가 *"우리가 손으로 키운 에이전트에 비하면 거의 AGI"* 라고 말한다. 그 인정 위에 자사 프레임워크를 얹는 구조다.

⚠️ 발표 전체에서 **보안·권한·[[prompt-injection]]을 한 번도 다루지 않는다** — 시맨틱 레이어 전체를 샌드박스에 붓는 구조인데도 그렇다.

## CEO 본인의 1인칭 (2026-10-12 · [[tech-bridge-vercel-rauch-agentic-workflow]])

[[guillermo-rauch|Guillermo Rauch]](CEO — 이름은 제목·설명란에만)가 David Ondrej(⚠️ 추정) 인터뷰 발췌에서 자기 작업 방식을 보인다. 이 위키의 **두 번째 Vercel 소스**이고 첫 CEO 발화다.

| 제품 (이 소스) | 역할 |
|---|---|
| **[[fx]]** | Vercel Labs의 코딩 CLI — 셸처럼 부팅, 6MB/11MB, 임베드 가능 |
| **fx0** | fx 위의 앱 생성 데모(HTML → 샌드박스 Next.js → Eve 에이전트), 오픈소스 예정이라 함 |
| **[[v0]]** | 하네스에 *"like 90% of the engineering time"* 을 쓴 앱 생성 제품(회고) |
| **Vercel Sandbox** | brain and hands의 *손* — *"the tool that we're giving it is the Vercel sandbox"*(05:51~05:56) |
| *drives* | ⚠️ ASR — 신규 인프라로 보임, 정체 미확인. 에이전트에게 깨 보게 했다(03:23~03:33) |

권장 아키텍처: *"the architecture that we recommend at Vercel is that you run the harness and then you give it tools."*(05:44~05:51) → [[brain-hands-decoupling]]. 보안 서사: 샌드박스로 공급망 공격을 *"eradicate"* 할 수도 있다(12:48~12:56, 화자 *"bold statement"*).

⚠️ 09-19 소스에 대해 이 페이지가 적었던 *"보안·권한·prompt injection을 한 번도 다루지 않는다"* 는 Andrew Qu 발표에 대한 것이다 — 이번 소스는 보안을 **판매 논점**으로 전면에 둔다(엔터프라이즈 신뢰, 샌드박스 격리). 단 prompt injection은 이번에도 나오지 않는다.

## 추론 벤더의 고객 사례로 (2026-10-18 · [[tech-bridge-fireworks-train-to-deploy-open-models]])

[[fireworks-ai|Fireworks AI]]가 Vercel을 고객으로 든다: *"We helped them actually fine tune and also host the model on our platform and they see a 40x latency improvement."*(03:58~04:06) 커널 최적화 예시도 Vercel이다 — 입력·출력 토큰 수, prompt cache hit rate, latency 목표를 주면 CUDA 커널까지 맞춘다(05:41~06:08). ⚠️ 어느 모델·제품인지, 40배의 기준선은 발화되지 않았다. 벤더 측 진술이다.

## References

- [[tech-bridge-vercel-eve-filesystem-agent]] · [[andrew-qu]] · [[eve-framework]] · [[nextjs]]
- [[tech-bridge-vercel-rauch-agentic-workflow]] · [[guillermo-rauch]] · [[fx]] · [[v0]]
- 관련: [[file-system-agent]] · [[framework-defined-agent-infrastructure]] · [[query-to-skill-distillation]] · [[company-knowledge-moat]] · [[agent-skills]]
