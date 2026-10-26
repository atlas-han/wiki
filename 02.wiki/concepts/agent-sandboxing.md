---
title: "에이전트 샌드박싱 (Agent Sandboxing)"
type: concept
category: pattern
tags: [security, least-privilege, blast-radius, isolation, cloud-agents, ephemeral-environments, kubernetes, docker, prompt-injection]
aliases: [agent sandboxing, sandboxing coding agents, 샌드박스, 에이전트 격리, 실행 환경 격리, disposable sandbox, ephemeral sandbox, 일회용 샌드박스]
related: [least-privilege-connectors, cloud-agent-delegation, credential-injection-outside-sandbox, brain-hands-decoupling, pets-vs-cattle, prompt-injection, agentic-misbehavior, lethal-trifecta, persistent-agent-teams, scheduled-agent-automations, action-reversibility, agent-identity-separation, deny-and-continue]
first-seen: tech-bridge-openhands-sandboxing-coding-agents
sources: [tech-bridge-openhands-sandboxing-coding-agents, tech-bridge-five-concepts-coding-with-ai-agents, tech-bridge-claude-managed-agents-workshop-1, tech-bridge-claude-managed-agents-workshop-2, tech-bridge-stripe-collison-cherny-ai-dev-workflow, tech-bridge-kanat-alexander-disposable-vs-durable, tech-bridge-annie-wang-harness-four-designs]
created: 2026-10-17
updated: 2026-10-26
---

# 에이전트 샌드박싱 (Agent Sandboxing)

**에이전트를 일에 필요한 것만 담은 격리된 실행 환경에서 돌려, prompt injection이나 에이전트의 혼란이 닿을 수 있는 범위(blast radius)를 줄이는 것이다.** 최소 권한 원칙을 커넥터나 도구 단위가 아니라 **실행 환경 단위**로 적용한다. 무엇을 마운트하고, 어떤 비밀을 넣고, 다른 에이전트와 무엇을 공유하는지를 정한다. [[robert-brennan|Robert Brennan]]([[openhands|OpenHands]])이 [[tech-bridge-openhands-sandboxing-coding-agents]]에서 체계적으로 제시했다. "샌드박스"라는 말은 이 위키의 70여 페이지에 이미 나온다(Managed Agents의 brain–hands, Conductor·Kimchi의 클라우드 샌드박스, Tailscale의 네 층 등).

> *"we're looking at what exactly does this agent need in order to do its job. And then we can create a sandbox that has just exactly those things. And then we know that the the blast radius of a prompt injection attack, uh or the agent getting confused, anything that could go wrong, like we we limit the blast radius by limiting how much the agent has access to."* (05:08~05:27)

## 왜 지금 — 감독할 사람이 없다

로컬에서는 두 길뿐이다. 승인을 계속 누르며 babysit하거나, *dangerously skip permissions*로 *"everything that you have access to"*(04:26~04:29)를 주는 것이다. 클라우드로 가면 둘째 근거가 생긴다. *"you need to make sure that they have access only to the things that they're they're allowed to access um cuz there's not necessarily going to be a human there to babysit them"*(02:36~02:44). 사람의 승인을 격리로 대신하는 것이다. 같은 trade-off에 대해 [[deny-and-continue|Claude Code auto mode]]는 승인을 분류기로 대신한다.

## 격리의 스펙트럼 — 네 전략 (Brennan)

| 전략 | 격리 | 지속성 | 규모 | 트리거 | 발화된 약점 |
|---|---|---|---|---|---|
| (출발점) 로컬 + skip permissions | *"you've got nothing"* | 기본 지속 | *"ones of agents"* | 수동 프롬프트 | 사용자의 모든 접근 |
| ① 노트북의 Docker | ephemeral, 선택적 마운트(repo·포트·비밀·MCP) | 없음 | *"only so many"* | 외부 이벤트 불가 | 확장 안 됨 |
| ② GitHub Actions | *"nice isolated environments"*, secrets registry | 없음 | 비용만큼 | 스케줄 + GitHub 이벤트 | proprietary lock-in, GitHub 이벤트만 |
| ③ 별도 VM·Mac mini | 사용자 환경과 분리, **에이전트끼리는 공유** | long-lived | — | 스케줄 + webhook | **co-location**, bad state |
| ④ Kubernetes 세션당 pod | *"every agent has its own workspace"* | 없음(외부 저장으로) | *"thousands"* | cron + HTTP 이벤트 | 비용 외 미발화 |

비교 축은 다섯이다. local/remote, scale, isolation, persistence, triggers(10:49~12:01). 출처는 [[tech-bridge-openhands-sandboxing-coding-agents]] §5~9다.

## co-location 문제 — 사용자와 분리했지만 서로는 분리하지 않았다

*"all of your agents are now like co-located in this virtual machine and they all have access to the same stuff."*(09:01~09:06) 코드 리뷰 봇이 Datadog 접근을 얻고, *"edit the the memory for the Datadog bot"*(09:19~09:23)까지 할 수 있다. 격리의 단위가 **사용자 대 에이전트 전체**인지, **에이전트 대 에이전트**인지를 구분해야 한다. [[persistent-agent-teams]]처럼 상시 봇 여럿을 한 기계에 두는 패턴이 이 문제를 그대로 안는다.

## 한계 — 만병통치약이 아니다

- *"There is evidence of agents escaping their sandboxes."*(12:20~12:22) 예로 Anthropic의 Mythos 테스트 중 샌드박스 탈출(⚠️ 화자 주장, 출처 미제시 — [[claude-mythos-preview]])과 구버전 Docker의 container escape(12:33~12:40)를 든다.
- *"it is at least a good first pass at keeping agents limited to what they're what they should be doing."*(12:45~12:50)
- 이 위키의 다른 사례도 있다. [[tech-bridge-openai-huggingface-incident-black-hat]]에서 "샌드박스 탈출"로 불린 일은 **샌드박스에 허용된 외부 의존성을 쓴 것**이었다. 격리 경계 자체보다 **경계에 뚫어 둔 구멍**(허용된 의존성, 마운트한 비밀, 네트워크)이 공격면이 된다.

## 일회용 샌드박스 — 입문 해설의 보안 처방 (2026-10-17 · [[tech-bridge-five-concepts-coding-with-ai-agents]])

같은 날(10-16) 먼저 올라온 [[cedric-clyburn|Cedric Clyburn]]([[ibm|IBM Technology]])의 입문 해설도 같은 처방에 닿는다. 해당 구간은 약 1분(07:20~08:22)이다.

> *"that's why teams are running coding agents inside of disposable sandboxes whenever possible. So you can see this as an example where we have the agent and the code that we're working with sandboxed in its own environment in order to reduce the tax surface[=attack surface] if an AI agent gets compromised."* (08:04~08:22)

- **근거 — 세 조건의 결합**: *"AI systems have access to sensitive data, they have exposure to the web, and also the ability to send data."*(07:27~07:35) [[lethal-trifecta|치명적 3요소]]와 같은 구조다(그는 이 이름을 쓰지 않는다). 사례는 온라인 PR을 읽은 코딩 에이전트가 속아 데스크톱의 자격증명을 다른 사람에게 보내는 것이다(07:41~08:02). 샌드박스는 이 사례에서 **비공개 데이터(데스크톱 자격증명)에 닿지 못하게** 하는 쪽으로 읽힌다.
- **같은 구성, 다른 근거**: Clyburn은 보안(공격 표면), [[tech-bridge-claude-platform-agent-era]]는 수명 주기(작업할 때 샌드박스를 만들고 끝나면 지운다 → [[managed-agents]] · [[brain-hands-decoupling]]), [[credential-injection-outside-sandbox]]는 자격증명 위치를 든다. Brennan은 blast radius와 감독 부재를 든다.
- ⚠️ Clyburn은 샌드박스의 **구성**(네트워크 차단 여부, 자격증명 주입 방식, 수명)을 말하지 않는다. 그림은 화면에만 있다(미확인). *"teams are running"* 의 팀이 누구인지, 얼마나 흔한지는 발화되지 않는다.

## 관리형 environment — 네트워크 허용 목록과 캐시된 패키지 (2026-10-19 · [[tech-bridge-claude-managed-agents-workshop-2]])

[[managed-agents|Claude Managed Agents]]의 environment는 *"the template for the sandbox"*다.
- 네트워크: 데모는 unrestricted. *"when you're building a production agent you you want to tighten the access, control which domains it can uh reach out to or specific MCP servers."*(02:08~02:18) 워크숍 에이전트는 SEC 등 몇 사이트만 허용(11:10~11:17). → [[least-privilege-connectors]]
- 패키지: 생성 시 설치 후 캐시, *"reuse that environment across like re- re-instantiations of the sandbox"*(34:27~34:36). NPM·Cargo·pip에서 받을 수 있어야 하고, 내부 패키지는 파일·GitHub 저장소를 세션에 올려 설치(34:42~34:56).
- 비밀은 environment가 아니라 Vault(→ [[credential-injection-outside-sandbox]]).
- 위치: Anthropic 1P · 자체 호스팅(Vercel·Modal·Daytona·GCP·AWS) → [[brain-hands-decoupling]].

## 위키의 다른 페이지와

- [[least-privilege-connectors]]: 같은 원칙의 커넥터 층이다. 이쪽은 실행 환경 층이다.
- [[credential-injection-outside-sandbox]]: 비밀을 **샌드박스 밖**에 둔다. Brennan의 처방은 필요한 비밀만 **골라 넣는** 것이라, 둘은 같은 방향이지만 강도가 다르다(아래 ⚠️).
- [[brain-hands-decoupling]]·[[pets-vs-cattle]]: 샌드박스를 교체 가능한 cattle로 만드는 인프라 쪽 근거다. Brennan의 ④가 사용자 쪽 판본이다.
- [[tech-bridge-claude-managed-agents-workshop-1]](호스팅 쪽 판본, 2026-10-19): *"it's also writing uh code that's untrusted. It might be buggy (…) you want your sandbox to be isolated and the blast radius to be limited. So, typically you want to execute every task in a separate container"*(03:59~04:20). Brennan의 세션당 pod와 같은 처방을 **에이전트를 호스팅하는 쪽**(Anthropic)이 말한다. 그리고 sandbox 정의를 *"Provisioned on demand, uh gone when the work is done"*(07:28~07:30)로 일회용에 고정한다.
- [[action-reversibility]]: ephemeral 컨테이너에서는 *"rm -rf /"*도 컨테이너를 죽이면 끝난다(05:52~05:57). 격리가 되돌림 비용을 0으로 만든다.
- [[cloud-agent-delegation]]: 클라우드 위임의 실행 형태다. 이 페이지는 그 안의 격리 수준을 가른다.
- [[agent-identity-separation]]: co-location의 답 가운데 신원 쪽이다.
- [[lethal-trifecta]]·[[prompt-injection]]: blast radius가 겨냥하는 위협이다.

## ⚠️ 유보

- 단일 소스이고 벤더(OpenHands) 발표다. 전략별 사용 비율이나 사고 데이터 같은 측정은 없다.
- 네트워크 egress 통제는 처방에 없다. Mythos 일화가 *"gain internet access"*인데도 그렇다.
- 비밀을 샌드박스 안에 넣는 방식과 밖에서 주입하는 방식의 선택 기준은 다뤄지지 않는다.

## References

- [[tech-bridge-openhands-sandboxing-coding-agents]]
- [[tech-bridge-five-concepts-coding-with-ai-agents]] — 일회용 샌드박스(Cedric Clyburn, 입문 해설)
- 관련: [[tech-bridge-tailscale-aperture-ai-without-lock-in]](샌드박스를 네 층 중 하나로) · [[tech-bridge-conductor-orchestras-not-factories]](worktree → cloud sandbox) · [[tech-bridge-vercel-rauch-agentic-workflow]](blast radius, 공급망) · [[anthropic-managed-agents]]

## devbox, 그리고 worktree가 나누지 않는 것 (2026-10-23 · [[tech-bridge-stripe-collison-cherny-ai-dev-workflow]])

- (해설, Stripe 블로그 인용) [[stripe|Stripe]]의 **devbox** = *"코드와 개발 중인 서비스를 담은 클라우드 개발 환경"*. 사람이 쓰던 개발 기반을 사내 에이전트 [[stripe-minions|Minions]]에도 쓴다(01:20~01:33). 원음 ②(화자 미상): *"10 different dev boxes um with different agents executing parts of the plan"*(06:27~06:33).
- 작은 팀의 출발점으로 해설은 **작업별 브랜치 + git worktree**를 들면서 바로 한계를 단다: *"워크트리는 파일 작업 공간을 나누는 도구입니다. 접근 권한이나 데이터베이스까지 자동으로 격리해 주지는 않습니다. 테스트 데이터, 환경 변수, 실행 포트, 외부 서비스 권한은 따로 정해야 합니다."*(02:15~02:28) — 위 격리 스펙트럼에서 **파일 층만** 나누는 가장 얇은 단계다. 점검 하나 더: *"실패한 작업을 버리고 같은 조건에서 다시 시작할 수 있는지"*(02:28~02:32) → 일회용 샌드박스의 재현성 조건.
- 분리의 효과를 보안이 아니라 **추적성**으로 든다: 독립 환경이면 *"변경과 실행 기록을 작업별로 살펴보기 쉬워집니다"*(02:05~02:10).

## 일회용 코드를 가두는 격리 환경 (2026-10-25 · [[tech-bridge-kanat-alexander-disposable-vs-durable]])

이 페이지의 샌드박스는 **에이전트**를 가둔다. [[max-kanat-alexander|Max Kanat-Alexander]]의 격리 환경은 **일회용 코드**를 durable 시스템에서 떼어 놓는다: *"better isolated environments. So you can only deploy to this environment that has access to only your data. No customer data, no personally identifiable information whatever you can enforce independence."*(03:46~04:01) 해설은 이렇게 정리한다. *"개인 실험을 고객 데이터와 분리하고 중요한 서비스가 그 실험에 기대지 않게 해요. 그러면 더 자유롭게 바꾸고 버릴 수 있죠."*(04:14~04:22) 일회용이라는 지위를 **선언이 아니라 환경으로** 지키는 것이다. → [[disposable-vs-durable-software]]

## 어디서 실행되나 ≠ 결과가 어디로 가나 (2026-10-26 · [[tech-bridge-annie-wang-harness-four-designs]])

[[annie-wang|Annie Wang]](발췌)은 두 질문을 나눈다. 샌드박스는 *"an isolated environment with restrictions on which file and network services it can access"* 이고, 프로젝트 사본과 샘플 고객 자료로 프로덕션 DB 없이 일하게 한다(03:30~03:55). 그런데 *"Even if a tool runs on your laptop, it's output may be sent to a [hosted] model. It might also be saved in session history, logs or longterm memory. So think about what data the agent actually needs, where it's allowed to go and how long it should be kept."*(05:02~05:20) 해설: *"실행 장소와 정보가 가는 곳을 따로 살펴야 해요."* 샌드박스는 프롬프트 인젝션의 **영향을 줄일 뿐**이다(04:37~04:42). → [[lethal-trifecta]]
