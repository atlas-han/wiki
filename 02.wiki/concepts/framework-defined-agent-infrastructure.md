---
title: 프레임워크 정의 에이전트 인프라 (Framework-Defined Agent Infrastructure)
type: concept
category: pattern
tags: [framework, convention-over-configuration, file-system, agent-runtime, vercel]
aliases: [에이전트를 위한 Next.js, 컨벤션 기반 에이전트 선언]
related: [eve-framework, nextjs, file-system-agent, agent-harness-design, build-time-vs-runtime-tools]
first-seen: tech-bridge-vercel-eve-filesystem-agent
sources: [tech-bridge-vercel-eve-filesystem-agent]
created: 2026-09-19
updated: 2026-09-19
---

# 프레임워크 정의 에이전트 인프라

**에이전트를 코드로 조립하는 대신 파일 시스템 컨벤션으로 선언하고, 런타임 배치(내구성·격리·모델·연결)는 프레임워크가 결정하게 하는 설계.** [[tech-bridge-vercel-eve-filesystem-agent]]에서 [[andrew-qu|Andrew Qu]]가 [[nextjs|Next.js]]의 *framework defined infrastructure* 를 에이전트로 옮기며 제안했다. 구현이 [[eve-framework|Eve]]다.

## 원형 — 웹에서 이미 한 일

> 이 프레임워크는 **파일 시스템, 즉 프레임워크 정의 인프라**라는 개념을 창안했습니다. **파일 위치를 걱정할 필요 없이 올바른 규칙(convention)에 따라 파일을 작성하기만 하면 프레임워크가 자동으로 위치를 지정합니다.** **페이지는 CDN으로, 서버리스 함수는 [거기로], 캐싱은 중간 위치로** 이동합니다. (11:53~12:11)

핵심은 **선언이 곧 배치**다. 개발자는 *무엇인지* 만 말하고 *어디에 어떻게 놓일지* 는 말하지 않는다.

## 에이전트로 옮기면

> **에이전트 구축도 이처럼 간단해야 한다**고 생각했습니다. **스킬 폴더, 도구 폴더, 채널 폴더만 만들고 간단하게 선언하면 프레임워크가 모든 것을 정확하게 인식해야 합니다.** (12:11~12:28)

| 선언 | 프레임워크가 결정하는 것 |
|---|---|
| `skills/` | 언제 어떤 스킬이 컨텍스트에 들어가는가 |
| `tools/` | 도구 등록·호출 규약 |
| `channels/` | 입출력 경로 |

그리고 **런타임의 네 요구**가 배치의 대상이 된다:

> 에이전트는 **런타임과 채널**을 가지고 있습니다. 그리고 런타임에는 **내구성(durability)** 이 있어야 합니다. **격리된 환경에서 실행**해야 하고, **다양한 모델을 호출**해야 하며, **연결(connections)** 도 필요합니다. (12:47~13:05)

이 넷이 각각 오픈소스 어댑터(Docker · Postgres · OpenAI 응답 API)나 Vercel 제품(샌드박스 · 워크플로 · Connect)으로 채워진다. → [[eve-framework]]

## 왜 이 주장이 나왔는가 — 포크의 문제

> 에이전트를 구축하는 **모든 단계에서, Vercel의 누군가가 … 제 D0 에이전트를 기반으로(fork) 자신만의 에이전트를 만들려고 시도**했습니다. 그리고 **매 단계마다 기존에 알려지지 않았던 더 나은 방법**을 발견했습니다. 그래서 사람들이 **단순히 프롬프트에서 시작하거나 처음부터 최고의 원칙을 재창조할 필요 없이, 최신 인사이트부터 시작할 수 있다면 어떨까** 생각했습니다. (11:16~11:51)

**동기가 성능이 아니라 지식 전파다.** [[agent-architecture-progression|네 단계]]를 각자 다시 걷는 대신 도착점에서 시작하게 하려는 것이고, 프레임워크는 그 **교훈의 저장 형식**이다.

이것은 이 위키의 [[agent-harness-design]]과 같은 문제를 다른 쪽에서 잡는다. 하네스 설계는 *하네스가 모델의 한계를 가정하고 그 가정이 낡는다* 를 경계하는데([[harness-pruning]]), 프레임워크는 **가정을 컨벤션으로 굳혀 배포**한다. ⚠️ **같은 낡음의 위험을 더 넓게 퍼뜨리는 구조**인데 소스는 이 긴장을 다루지 않는다.

## ⚠️ 유보

- **컨벤션의 실제 규격이 없다** — 폴더 이름 셋만 나온다.
- **채널이 무엇인지** 열거되지 않는다.
- **탈출구**(컨벤션이 맞지 않을 때 무엇을 할 수 있는가)가 없다. 웹 프레임워크의 오래된 논점인데 다루지 않는다.
- 위의 **낡음 위험** — 프레임워크에 굳은 가정이 모델 향상으로 사문화될 때 어떻게 걷어내는가.
- **보안 모델이 없다.** 격리는 샌드박스뿐이고 [[agent-governance-layers]]에 해당하는 층이 서술되지 않는다.
- 파일 시스템이 **두 층에서 두 번** 쓰이는데(런타임 탐색 바닥 / 빌드타임 선언 문법) 소스가 이 구분을 하지 않는다. [[build-time-vs-runtime-tools]]의 축으로 보면 명백히 다른 시간대다.

## References

- [[tech-bridge-vercel-eve-filesystem-agent]] — first-seen
- [[eve-framework]] · [[nextjs]] · [[vercel]] · [[andrew-qu]]
- 관련: [[file-system-agent]] · [[agent-architecture-progression]] · [[agent-harness-design]] · [[harness-pruning]] · [[agent-skills]] · [[build-time-vs-runtime-tools]]
