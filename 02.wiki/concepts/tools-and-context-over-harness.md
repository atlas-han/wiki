---
title: 하네스는 고정하고 도구와 컨텍스트에 투자하라 (Tools and Context over Harness)
type: concept
category: pattern
tags: [harness, tools, context, model-upgrade, scaffolding, sunk-cost]
aliases: [하네스를 만들지 않는다, 도구와 컨텍스트라는 두 인터페이스, over-scaffolding]
related: [harness-pruning, ride-the-optimization-trajectory, harness-engineering, agent-harness-design, shift-left-interventions, context-engineering, executable-standards, agent-skills]
first-seen: tech-bridge-lopopolo-agent-harness
sources: [tech-bridge-lopopolo-agent-harness]
created: 2026-09-23
updated: 2026-09-23
---

# 하네스는 고정하고 도구와 컨텍스트에 투자하라

**하네스(Antigravity·Claude Code 같은 것)는 고정값으로 두고 최신 모델을 즉시 갈아 끼우며, 엔지니어링 노력은 모든 하네스가 공유하는 최소 표면 위의 도구와 컨텍스트에만 쌓는다 — 그 부분은 모델이 바뀌어도 낡지 않기 때문이다.** [[ryan-lopopolo|Ryan Lopopolo]]가 [[tech-bridge-lopopolo-agent-harness]]에서.

> **저는 하네스를 만들어 본 적이 없습니다.** 음, 제 생각에는 **제가 '하네스 엔지니어링'이라고 부르는 것에 대한 명칭 자체가 좀 오해의 소지가 있는 것 같습니다.** 저는 당신의 에이전트 시스템에서 **[Antigravity]와 같은 요소를 항상 고정된 상태로 유지해 왔습니다.** 신제품이 출시되자마자 가장 좋은 모델을 구입하세요. (14:47~15:04)

## 논증

1. **모든 하네스의 공통 표면은 작다** — *"모든 하네스는 기본적으로 파일 읽기, [grep] 및 임의 명령 실행 도구를 제공합니다."*(16:00~16:07)
2. 그러므로 **그 표면 위에 쌓은 것(도구·문서)은 하네스를 바꿔도, 모델을 바꿔도 따라온다** — *"도구와 컨텍스트의 품질 향상에 모든 노력을 집중하면 최신 모델이 출시될 때마다 자유롭게 도입할 수 있으며"*(16:12~16:14), [결코 낡지 않을 시스템의 한 부분에 레버리지를 계속 쌓게 됩니다](16:18~16:24, ko가 흐린 문장을 en-orig로 보정).
3. 반대로 **모델 주위에 쌓은 스캐폴딩은 모델이 좋아지면 족쇄가 된다** — *"주변에 지나치게 많은 지원 체계를 구축하면, 실력이 향상될수록 불필요하게 그들의 발전을 제약하게 됩니다. 그리고 이런 물건들을 버리기 싫다는 생각 때문에 **일종의 매몰 비용 오류**에 빠지게 됩니다."*(16:26~16:36)
4. 도구가 잘 먹히는 이유 — *"모범 사례 도구들이 **학습 데이터에 매우 잘 반영되어 있기 때문**입니다."*(07:10~07:16) PromQL 같은 익숙한 형태로 문제를 접고, CLI로 *"추론을 결정론으로 전환"* 한다(07:42~07:48).

맺음에서 같은 말을 **두 인터페이스**로 요약한다 — *"도구와 컨텍스트를 중심으로 하는 이러한 두 가지 유형의 확장 가능한 인터페이스에 집중하는 것"*(18:36~18:43). 그리고 *"점점 더 강력한 도구들이 일종의 **기억 역할**을 하고, 당신이 생각하는 좋은 모습이 무엇인지 **강화하는 역할**"*(19:01~19:07).

## ⭐ 이 위키의 하네스 시간축 위에서

| | 모델이 좋아질 때 하네스는 | 투자 대상 |
|---|---|---|
| [[harness-pruning]] (Anthropic CC 팀) | **지운다** — 결함 보완 기능이 dead weight | 하네스 자체(만들고 덜어낸다) |
| [[ride-the-optimization-trajectory]] ([[jo-bergum\|Bergum]]) | **얹는다** — 랩이 최적화하는 방향 위에 | bash·도구 사용 형태의 작업 설계 |
| **이 페이지** | **건드리지 않는다** — 고정 | **도구·컨텍스트** |

**세 입장은 같은 전제(모델은 계속 좋아지고 하네스의 가정은 낡는다)에서 출발한다.** 이 페이지는 가장 급진적이다 — **지울 것을 애초에 만들지 않는다.** 그리고 [[ride-the-optimization-trajectory]]와는 **근거까지 같다**(학습 데이터에 잘 반영된 도구). ⚠️ **세 소스는 서로를 모른다.**

[[harness-engineering]]의 Cole Medin 3계층(Base LLM / Tool Harness / **AI Layer**)으로 옮기면 **Tool Harness는 고르고 AI Layer만 만진다**는 뜻이 된다 — 명칭은 달라도 **같은 분업**이다.

## ⚠️ 유보

- **"결코 낡지 않는다"는 근거 없는 단언이다.** 문서가 거의 즉시 낡는다는 것이 [[executable-standards]]의 출발점이다. Lopopolo가 문서 구조를 **테스트로 강제**하는 예(08:28~08:38)를 드는데 이 페이지의 논증과 **연결하지 않는다.**
- **같은 에피소드의 반대 입장** — 빌리: *"직접 하네스를 제작하는 것은 [뭔가] 고장 났을 때 내부적으로 어떤 일이 일어나는지 이해하는 방법"*(19:53~19:56). 에피소드는 조정하지 않는다.
- **하네스가 정말 교체 가능한가** — 스킬·AGENTS.md는 하네스를 넘나들지만(→ [[google-skills]]의 *하네스 무관*), 훅·권한 설정·서브에이전트 정의는 **하네스마다 다르다.** Lopopolo의 "고정"이 **한 하네스에 머문다**는 뜻인지 **어느 것이든 상관없다**는 뜻인지 불분명하다.
- **당사자성** — 화자는 하네스를 파는 회사(Google, [[antigravity|Antigravity]])에 있다. 다만 이 논증은 **특정 하네스를 사라고 하지 않는다**는 점에서 3부의 제품 소개와 결이 다르다.

## References

- [[tech-bridge-lopopolo-agent-harness]] · [[ryan-lopopolo]]
- 같은 전제, 다른 처방: [[harness-pruning]] · [[ride-the-optimization-trajectory]]
- 계보: [[harness-engineering]] · [[agent-harness-design]] · [[context-engineering]] · [[shift-left-interventions]]
- 긴장: [[executable-standards]] · [[linear-vs-closed-loop-harness]]
