---
title: "코딩 에이전트 플랫폼의 네 층 (Compute · Dev Environment · Harness · Control Plane)"
type: concept
category: architecture
tags: [platform, compute, sandbox, dev-environment, harness, control-plane, dispatch, system-of-record, software-forge, buy-vs-build]
aliases: [SDLC 4개 레이어, 네 층, control plane, software forge, system of record for sessions]
related: [harness-as-platform, model-harness-knowledge-stack, multiplayer-agent-context, human-plumbing, harness-engineering, trace-to-memory-loop, software-factory]
first-seen: tech-bridge-horthy-state-of-software-factory
sources: [tech-bridge-horthy-state-of-software-factory]
created: 2026-10-16
updated: 2026-10-16
---

# 코딩 에이전트 플랫폼의 네 층

**에이전트로 소프트웨어를 만드는 조직이 갖춰야 할 층 넷 — 에이전트를 돌릴 compute, 에이전트가 자기 작업을 테스트할 dev environment, harness, 그리고 일을 배분하고 세션·계획을 함께 다루는 control plane. 각 층은 사거나 만든다.** [[dex-horthy|Dex Horthy]]([[humanlayer|HumanLayer]])가 [[tech-bridge-horthy-state-of-software-factory]]에서 제시. *"Each of these layers you can buy or build."*(14:52~14:53)

| 층 | 발화 |
|---|---|
| compute | *"we have some spare pods in our Kubernetes cluster (…) or you can go buy Daytona or E2B or whatever it is"*(14:23~14:33) |
| dev environment | *"How do you get your language set up? Your runtime? Your preview environments? Do I need to connect to internal services in our VPC in order to even run a dev environment so an agent can test its work?"*(14:33~14:43) |
| harness | *"of course, the harness, which you can buy or build. There's a ton of options here."*(14:43~14:47) |
| control plane | *"How do I dispatch work? How do I collaborate on sessions and plans?"*(14:49~14:52) |

## 왜 control plane인가 — 새 software forge

- 비유: git 패치를 메일링 리스트로 돌리던 시절 → GitHub(*"the protocol is is decentralized, but we have a centralized place to do this"* 13:25~13:30).
- *"now there's other parts of the SDLC that I think are first class. So, you have session traces, you have architecture docs"*(13:28~13:35) — 지금은 Slack·Teams 복사·붙여넣기로 나른다(13:35~13:50).
- ⭐ *"we need a place where our sessions and plans and prompts and all this stuff kind of lives in in a centralized sort of system of record."*(13:53~14:01)

## 위키에서의 자리

- [[harness-as-platform]] — Uber는 harness를 플랫폼 팀이 소유. 네 층 그림에서는 harness가 **한 층**일 뿐이고, 그 위에 control plane이 있다.
- [[model-harness-knowledge-stack]] — 모델·하네스·지식 3층과 축이 다르다(그쪽은 에이전트의 내부, 이쪽은 조직의 인프라).
- [[multiplayer-agent-context]] · [[human-plumbing]] — control plane이 없을 때 사람이 세션 사이의 배관이 된다.
- [[trace-to-memory-loop]] — 세션 트레이스를 SDLC의 first-class 산출물로 보관하는 장소.

## ⚠️ 유보

- **벤더의 틀**: 화자의 회사가 control plane을 판다(*"we're kind of working very closely in this control plane"* 14:53~14:58). 슬라이드의 *"hour-long deep dive"*(14:12~14:15)는 이 영상에 없다. ko는 *compute layer* 를 **"망토"**, *dispatch* 를 **"끝내다"** 로 옮긴다.

## References

- [[tech-bridge-horthy-state-of-software-factory]]
