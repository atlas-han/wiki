---
title: 최소 권한 커넥터 (Least-Privilege Connectors)
type: concept
category: pattern
tags: [security, permissions, connectors, least-privilege, agents]
aliases: [읽기 전용으로 시작한다, least privilege]
related: [secure-tool-evolution, confused-deputy-attack, bound-parameters, credential-injection-outside-sandbox, sentinel-agent, build-time-vs-runtime-tools]
first-seen: tech-bridge-zuckerberg-muse-personal-agent
sources: [tech-bridge-zuckerberg-muse-personal-agent, tech-bridge-zuckerberg-muse-in-daily-use]
created: 2026-09-14
updated: 2026-09-17
---

# 최소 권한 커넥터

**에이전트를 외부 서비스에 연결할 때 읽기 전용에서 시작하고, 필요할 때만 권한을 올린다.**

> 어떤 사람들은 **연결하면 곧바로 모든 것에 접근**하게 설계하지만, **우리 접근은 "이메일에 연결하면 **읽기 전용으로 시작**한다"** 입니다. **보내게 하고 싶으면 따로 요청하면 됩니다.** — [[tech-bridge-zuckerberg-muse-personal-agent]] (35:38~36:02)

> **우리의 핵심 설계 원칙은 **최소 권한(least privilege)** 입니다. 각 단계에서 필요한 **최소 권한만 갖고, 필요할 때만 더합니다.** 이건 제품 설계에서 아주 근본적입니다.** (36:03~36:23)

함께 놓인 것이 **보안 자격증명 저장소**다:

> **신용카드·비밀번호·일회용 카드 번호를 열린 채로 둘 이유가 없습니다. **에이전트는 그걸 알아서는 안 됩니다.** 로그인해 달라고 요청했을 때 필요한 만큼만 접근할 수 있고 그 외에는 아니어야 합니다.** (34:11~34:31)

→ [[credential-injection-outside-sandbox]]

## 같은 원칙이 두 층에서 확인됐다

2026-09-10 [[tech-bridge-build-time-vs-runtime-tools|Google Cloud 편]]이 **데이터베이스 앞의 에이전트**에 대해 같은 사다리를 제시했다 — *슈퍼유저 → 제로 트러스트*, 그리고 [[bound-parameters]](JWT 클레임으로 범위를 묶기).

**이 위키에서 같은 보안 원칙이 인프라 층과 소비자 제품 층 양쪽에서 확인된 첫 사례다.** 어휘까지 같다(*least privilege*).

| | [[tech-bridge-build-time-vs-runtime-tools]] | **이 개념** |
|---|---|---|
| 대상 | 데이터베이스 | 이메일·메시징·건강 정보·광고 시스템 |
| 사용자 | 개발자 | **일반 소비자** |
| 승격 방법 | 도구 정의·바운드 파라미터 | **사용자에게 따로 요청** |
| 근거 | [[confused-deputy-attack]] · [[lethal-trifecta]] | 신뢰 확보(제품 논리) |

**승격 방법이 다르다는 것이 소비자 층의 어려움을 드러낸다** — 개발자는 설정 파일을 읽지만 소비자는 **매번 뜨는 확인창을 읽어야 한다.** 소스는 이 부담을 인정한다:

> **특히 이런 제품을 처음 써 보는 분이 대부분일 테니 복잡하게 느껴질 수 있습니다.** (36:03~36:06)

## 열려 있는 것

- ⚠️ **권한 승격의 UX가 실제로 어떻게 생겼는지 없다.**
- ⚠️ **"항상 허용"의 위험이 다뤄지지 않는다.** 소스는 그 선택지가 있다고만 말하고(*"이런 종류는 일반적으로 괜찮다"*), **그것이 최소 권한을 무력화하는 경로**라는 점은 논의하지 않는다.
- ⚠️ **읽기 전용도 충분히 위험할 수 있다** — 읽은 내용이 [[prompt-injection|인젝션]]의 경로이고([[lethal-trifecta]]), 유출의 원천이다. 소스는 쓰기 권한만 제한 대상으로 본다.

## References

- [[tech-bridge-zuckerberg-muse-personal-agent]] · [[muse]] · [[meta]]
- 관련: [[secure-tool-evolution]] · [[confused-deputy-attack]] · [[bound-parameters]] · [[credential-injection-outside-sandbox]] · [[sentinel-agent]] · [[confidential-vm]] · [[build-time-vs-runtime-tools]] · [[lethal-trifecta]]

## 두 번째 서술과 두 방향의 최소 노출 (2026-09-17)

[[tech-bridge-zuckerberg-muse-in-daily-use]]가 같은 원칙을 같은 예로 반복한다.

> **새 시스템에 연결할 때 — 이메일이든 뭐든 — 가능한 한 최소 권한(least privilege)으로 기본 설정됩니다.** 뭔가에 연결하고 싶다고 해서 **콘텐츠를 편집할 쓰기 권한까지 꼭 줄 필요는 없습니다.** (19:49~20:01)

> **근본 아키텍처와 설계가 기본적으로 가능한 한 최소의 권한을 주고, 하려는 일을 완료하는 데 필요한 최소의 정보만 노출하는 것입니다.** (20:08~20:21)

이번 편이 더하는 것은 **원칙이 두 방향으로 적용된다**는 점이다:

| 방향 | 장치 | 무엇을 감추나 |
|---|---|---|
| **에이전트를 향해** | 자격증명 저장소 | 카드 번호·비밀번호를 **에이전트가 모른다** |
| **거래 상대를 향해** | [[one-time-virtual-card\|일회용 가상 카드]] | 실제 카드 번호를 **판매자가 못 본다** |

같은 문단이 근거까지 준다 — *"이게 에이전트를 갖는 것의 가치 중 하나입니다 — **에이전트는 그 추가 수고를 마다하지 않습니다.**"* **최소 권한이 지켜지지 않는 이유가 기술이 아니라 마찰이었다면, 에이전트는 그 마찰을 치른다.**

⚠️ ko 자막이 *"right access"*(en-orig ASR of **write access**)를 쓰기 권한으로 명시하지 못했다.
