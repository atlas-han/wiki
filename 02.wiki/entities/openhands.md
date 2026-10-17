---
title: OpenHands
type: entity
category: org
tags: [coding-agents, open-source, agent-platform, agent-sandboxing, harness, control-plane]
aliases: [OpenHands, Open Hands, OpenHands Agent Canvas, Agent Canvas]
links:
  - "https://openhands.dev"
  - "https://github.com/OpenHands/OpenHands"
sources: [tech-bridge-openhands-sandboxing-coding-agents]
created: 2026-10-17
updated: 2026-10-17
---

# OpenHands

MIT 라이선스 코딩 에이전트에서 출발해 *"a platform for running coding agents"*로 넓힌 조직이자 제품이다. CEO는 [[robert-brennan|Robert Brennan]]이다. 자기 규정은 이렇다. *"we started Open Hands as an MIT-licensed coding agent. Uh, and I would say now we've we've evolved really to a a platform for running coding agents. Everything from the harness to the infrastructure to the control plane to actually like monitor these agents at scale."*(00:31~00:43, [[tech-bridge-openhands-sandboxing-coding-agents]]) 창업은 *"a little over two years ago"*(00:18~00:19)다. 이 위키 첫 등장이다. 링크는 설명란에서 가져왔고 열어 보지 않았다.

## 출발점 — 대화마다 Docker 컨테이너

*"This is actually the uh way we originally launched Open Hands was as an interface where every time you started a new conversation with the agent, we'd spin up a brand new Docker container. The agent would get its own its own container."*(05:36~05:46) [[agent-sandboxing]]의 전략 1(로컬 Docker)이 이 회사의 첫 제품 형태였다는 당사자 진술이다.

## Agent Canvas

- *"a quick plug for OpenHands Agent Canvas. This is a way you know, really to run with any type of sandbox. You can run it with cloud code[=Claude Code] or code X[=Codex] or the OpenHands harness."*(12:54~13:05)
- *"by default if you saw it on your laptop, it's like running cloud code with dangerously skip permissions. But with one quick toggle, you can start running things in Docker containers. Another toggle, you can start running it in a remote VM. Another toggle, you can run it inside of Kubernetes."*(13:07~13:20)
- 목적은 *"pick the right environment for the job"*(13:20~13:23)이다. 로컬 사본으로 빠르게 반복할 때와 이벤트로 몇 시간 백그라운드에 돌릴 때를 가른다.
- ⚠️ 인터페이스, 토글 사이에 유지되는 상태, 가격, 고객, 수치는 발화되지 않는다. 당사자 발표다.

## 위키의 다른 페이지와

- 하네스·인프라·control plane을 한 회사가 다 갖는다는 자기 규정이다. [[agent-platform-layers]]와 비교할 것.
- 다른 회사의 하네스(Claude Code·Codex)를 바꿔 끼운다. [[embedded-agent-harness]]와 같은 방향이다.
- 로컬과 클라우드를 토글로 오간다. [[cloud-agent-delegation]]의 Rauch "양방향"과 같은 그림이다.

## References

- [[tech-bridge-openhands-sandboxing-coding-agents]] · [[robert-brennan]] · [[agent-sandboxing]]
