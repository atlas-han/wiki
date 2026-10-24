---
title: 최소 권한 커넥터 (Least-Privilege Connectors)
type: concept
category: pattern
tags: [security, permissions, connectors, least-privilege, agents]
aliases: [읽기 전용으로 시작한다, least privilege]
related: [secure-tool-evolution, confused-deputy-attack, bound-parameters, credential-injection-outside-sandbox, sentinel-agent, build-time-vs-runtime-tools, agent-sandboxing]
first-seen: tech-bridge-zuckerberg-muse-personal-agent
sources: [tech-bridge-zuckerberg-muse-personal-agent, tech-bridge-zuckerberg-muse-in-daily-use, tech-bridge-jensen-huang-korea-society-gala, tech-bridge-alexandr-wang-muse-launch, tech-bridge-tailscale-aperture-ai-without-lock-in, tech-bridge-openhands-sandboxing-coding-agents, tech-bridge-jediah-katz-harness-whats-left, tech-bridge-claude-duet-proactive-assistant]
created: 2026-09-14
updated: 2026-10-24
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

## 세 번째 서술 — "권한은 능력이 자격을 갖춘 만큼" (2026-10-09 · [[tech-bridge-jensen-huang-korea-society-gala]])

[[jensen-huang|Jensen Huang]]: *"the only information, the only tools, the only rights you will give to AI are the ones that it deserves because its capabilities deserve it. And so the first thing that you do with an AI is you say, I give you no rights. (…) minimal rights, minimal access, minimal everything. based on the job that I want you to do and your capabilities, I would give you more rights, more tools, more access."*(17:23~17:51)

Zuckerberg 편의 *"읽기 전용으로 시작한다"* 와 같은 출발점(0에서 시작)이고, **확대 조건을 명시**한다 — **일(job)과 능력(capabilities)**. 커넥터 단위가 아니라 *정보·도구·권리* 전체를 한 말로 묶는다. ⚠️ 능력을 무엇으로 재는지는 없다. 행동 증거로 넓히는 [[agent-trust-curve]]와 비교.

## 네 번째 서술 — Meta 공식 소개의 2차 요약 (2026-10-15 · [[tech-bridge-alexandr-wang-muse-launch]])

Tech Bridge 해설이 Meta의 Muse 소개를 이렇게 요약한다. *"Muse is designed to use a browser on a separate virtual machine and ask for user confirmation before sending emails or making purchases. It is a structure where users also define the access permissions for required apps."*(07:48~07:57, 해설). Zuckerberg 편의 *"이메일은 읽기 전용으로 시작"*·*"로그인·결제·민감 정보 전송은 매번 승인"* 과 같은 원칙이다. ⚠️ 화자 발화가 아니라 해설이 Meta 자료를 요약한 것이고, 이 위키는 원 자료를 열어 보지 않았다.

## 팀 신원별 커넥터 권한 — 게이트웨이에서 (2026-10-17 · [[tech-bridge-tailscale-aperture-ai-without-lock-in]])

[[remy-guercio|Remy Guercio]]([[tailscale|Tailscale]]): *"the marketing team, you know, they get access to Google Calendar and Gmail, but the engineering team will also get access to GitHub."*(13:31~13:36) 같은 엔지니어링 안에서도 쓰기와 읽기 전용을 나눈다(13:42~13:47). [[ai-gateway]]는 커넥터 권한을 에이전트가 아니라 **사람·팀 신원**에 묶는다. 커넥터는 chat UI가 아니라 게이트웨이에서 설정된다(15:26~15:34). ⚠️ 벤더 진술이고 화면 데모를 전제한다.

## 실행 환경 층 — 샌드박스와 blast radius (2026-10-17 · [[tech-bridge-openhands-sandboxing-coding-agents]])

[[robert-brennan|Robert Brennan]]([[openhands|OpenHands]]): *"a paradigm that we actually know well from, you know, pre-agent security days, the principle of least privilege, right? The idea is that both agents and humans should only have access to the things that they need in order to do their job"*(04:41~04:53). 예는 *"the GitHub repo that it's editing, and maybe a couple secrets"*(05:00~05:04)다. 근거 어휘는 blast radius다(*"we limit the blast radius by limiting how much the agent has access to"* 05:23~05:27).

앞의 서술들이 **커넥터·도구·신원** 단위로 권한을 좁혔다면, 이쪽은 **실행 환경** 단위다. 새로 더하는 것은 **co-location 문제**다. 한 VM에 모은 에이전트들은 *"all have access to the same stuff"*(09:04~09:06)라서, 코드 리뷰 봇이 Datadog 봇의 메모리를 고칠 수 있다(09:19~09:23). 최소 권한은 사용자와 에이전트 사이만이 아니라 **에이전트와 에이전트 사이**에도 걸린다. → [[agent-sandboxing]]

## 2026-10-24 — "API 키 파일을 통째로" · 비밀을 보지 않는 비서

- [[tech-bridge-jediah-katz-harness-whats-left]]: [[jediah-katz|Jediah Katz]] *"a simple harness with just bash and all your … API keys in a file can solve coding tasks, but you probably don't want to give all your API keys in a file to the model. … [at] companies where we want to have permissions that are scoped down to specific agents and specific people"*(06:05~06:29). 해설: *"AI가 일을 잘 끝냈는지와 필요한 권한만 썼는지는 함께 살펴봐야 해요."* 모델이 좋아져도 **지워지지 않는** 하네스 층으로 분류된다.
- [[tech-bridge-claude-duet-proactive-assistant]]: [[claude-duet|Claude Duet]]은 *"never directly sees your passwords or any of your sign[-in] tokens"*, 카드 번호·신분증 공유를 거부하는 검사를 추가(발췌, 화자 미상). 해설: *"문제가 절대 생기지 않는다는 보증으로 받아들이면 안 돼요."* → [[credential-injection-outside-sandbox]]와 같은 방향(⚠️ 구현 미확인).
