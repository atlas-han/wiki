---
title: "Tech Bridge — 샌드박스는 선택이 아닙니다 (Robert Brennan · OpenHands): 로컬 Docker → GitHub Actions → VM·Mac mini → Kubernetes, 최소 권한으로 blast radius를 줄이되 샌드박스는 만병통치약이 아니다"
type: source
tags: [agent-sandboxing, least-privilege, blast-radius, prompt-injection, dangerously-skip-permissions, cloud-agents, docker, github-actions, vendor-lock-in, virtual-machine, mac-mini, co-location, kubernetes, ephemeral-environments, persistence, triggers, scheduled-agents, event-driven-agents, multi-agent, sdlc-automation, container-escape, sandbox-escape, mythos, vendor-pitch, openhands, video]
source-url: https://www.youtube.com/watch?v=VOToAHcnhyA
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 Robert Brennan([[openhands|OpenHands]] CEO·공동창업자 — **자막에서 직접 자기소개**, 설명란과 일치) · 행사명 미발화(설명란 ai.engineer 링크 + #AIEngineer → AI Engineer 계열 추정) · 녹화일 미발화
date-published: 2026-10-16
ingested: 2026-10-17
created: 2026-10-17
updated: 2026-10-17
---

# Tech Bridge — 샌드박스는 선택이 아닙니다 (Robert Brennan · OpenHands)

[[tech-bridge|Tech Bridge]]가 재배포한 **13:51 단독 발표**다. 끝에 질문을 받겠다고 하지만 Q&A는 영상에 없다. 공식 챕터는 `meta.txt` 기준 12개다. 화자 [[robert-brennan|Robert Brennan]]이 직접 자기소개한다: *"my name is Robert Brennan. Uh, I'm the CEO at Open Hands."*(00:00~00:02) 측정 데이터는 없다. 발표는 **실행 환경 분류 + 비교 축 + 한계 + 마지막 50초의 자사 제품(OpenHands Agent Canvas) 소개**로 이루어진다. 테제는 다음과 같다.

> **2026년의 도약은 노트북에서 사람이 프롬프트하는 에이전트에서 클라우드에서 이벤트로 도는 에이전트로 가는 것이다. 클라우드에는 감독할 사람이 없을 수 있으니 에이전트가 허용된 것에만 접근하게 해야 한다. 로컬에서는 승인을 계속 누르거나 dangerously skip permissions로 사용자가 가진 모든 접근을 주는 것밖에 없다. 답은 최소 권한이다. 일에 필요한 것만 담은 샌드박스로 prompt injection과 혼란의 blast radius를 줄인다. 실행 방식은 로컬 Docker → GitHub Actions → 별도 VM·Mac mini → Kubernetes 세션당 pod 순으로 견고해진다. 그래도 샌드박스는 만병통치약이 아니다.**

> *"The leap that we're seeing organizations make over the course of 2026 is really to agents that run in the cloud. And this is really where sandboxing comes into play."* (02:14~02:21) · *"we limit the blast radius by limiting how much the agent has access to."* (05:23~05:27) · *"The fourth and and really like the most robust strategy here, I would say is to use Kubernetes"* (09:38~09:42) · *"sandboxing is not a panacea."* (12:15~12:18)

이 위키에 개념 하나가 생긴다. [[agent-sandboxing]](신규 제안)은 에이전트 실행 환경의 격리 스펙트럼과 다섯 비교 축, co-location 문제, 한계를 다룬다. "샌드박스"라는 말은 이미 70여 페이지에 나오지만 그것을 정면으로 다룬 페이지는 없었다. 나머지는 기존 페이지에 붙는 **새 증언**이다.
- [[cloud-agent-delegation]]: 3번 → 4번 도약, 감독할 사람이 없다는 근거
- [[least-privilege-connectors]]: 커넥터가 아니라 실행 환경 층의 최소 권한
- [[persistent-agent-teams]]·[[openclaw]]: 한 VM·Mac mini에 모은 에이전트의 co-location 문제
- [[pets-vs-cattle]]: VM 지속성 vs ephemeral pod
- [[scheduled-agent-automations]]: 트리거 축
- [[claude-mythos-preview]]: 샌드박스 탈출이라는 화자 주장(⚠️ 미확인)
- [[credential-injection-outside-sandbox]]: 비밀을 샌드박스에 마운트하는 쪽과 대비

ASR·ko 보정. ko는 **GitHub Actions의 한계 둘을 기능으로 뒤집는다.** *"you're not going to be able to really port this"* → **"이 파일을 쉽게 이전할 수 있습니다"**(07:54), *"You can't respond to like a Slack webhook"* → **"Slack 웹훅에 답장할 수 있습니다"**(07:59)이다. 둘 다 부정어가 앞 줄 "아니요"로 밀려 생긴 반전이다. 같은 방향의 반전이 더 있다.
- *"there's not necessarily going to be a human there to babysit them"* → **"거기에는 사람이 있을 겁니다"**(02:41)
- *"they're separated from your environment"* → **"여러분의 환경에 영향을 미칠 수 있지만"**(11:28)
- *"the most robust strategy"* → **"더 견고한 전략이 필요하다"**(09:40)

ko는 단위도 바꾼다(*you can run thousands* → **"수천 번"** 11:16). 용어 오역으로는 prompt injection → **"즉시 주사"**, agent → **"약물"**(05:20), trade-off → **"헌신"**(03:38), sandbox → **"모래놀이터"**(12:29), persistence → **"끈기"**(08:23, `en` *"You're persistent"* 공유)가 있다. en-orig는 Claude Code를 *"Quad Code"*·*"cloud code"*로 적는다. 전체 목록은 raw에 있다.

> ⚠️ **측정치가 없다.** 숫자는 연도와 예시다. *"the beginning of 2024"*(01:44), *"over the course of 2026"*(02:16~02:18), *"every Monday morning at 9:00 a.m."*(07:37~07:39), 노트북 *"ones of agents"* 대 Kubernetes *"thousands"*(11:12~11:17)가 그 예다. 어떤 조직이 어느 단계에 있는지, 어떤 전략이 얼마나 쓰이는지는 없다. 손들기 결과도 *"Fewer than I'd expect"*와 *"Somehow more hands than before"*(03:29~03:38)라는 인상뿐이다.
>
> ⚠️ **자사 제품 소개가 끝에 붙는다.** 12:54~13:44는 *"a quick plug for OpenHands Agent Canvas"*(12:54~12:58)다. 발화된 기능은 두 가지다. Claude Code·Codex·OpenHands 하네스 중 무엇으로든 돌릴 수 있고, 로컬 기본값에서 **토글 하나씩으로 Docker → 원격 VM → Kubernetes**로 옮긴다(13:07~13:20). 사용법·가격·고객·수치는 없다. 전략 1을 소개할 때도 *"the uh way we originally launched Open Hands"*(05:36~05:38)라는 자사 이력이 나온다.
>
> ⚠️ **Mythos 샌드박스 탈출은 화자 주장이다.** *"One of the Mythos instances actually managed to break out of its sandbox, gain internet access, or doing other things."*(12:28~12:33) 출처·시점은 발화되지 않는다. 이 위키는 이를 다른 소스로 확인하지 않았다([[claude-mythos-preview]]에 해당 기록이 없다). OpenAI 쪽 [[tech-bridge-openai-huggingface-incident-black-hat|Hugging Face 사건]]과는 다른 사건이다.
>
> ⚠️ **행사와 시점.** 행사명·도시·연도는 발화되지 않는다. 설명란의 `https://ai.engineer`·AI Engineer 링크·#AIEngineer로 **[[ai-engineer|AI Engineer]] 계열을 추정**할 뿐 확정하지 않는다. *"over the course of 2026"*(02:16~02:18)로 보아 2026년 발표다.

## 1. 화자와 OpenHands (00:00~00:43)

- *"I want to talk to you a little bit about today about, uh, sandboxing coding agents. Uh, why this is a really important pattern and, uh, different ways to actually get this done."*(00:01~00:12)
- *"co-founded it a little over two years ago, really with the vision of bringing, uh, coding agents to the community, right? Um, really giving software developers a say in the gigantic change that's happening to our jobs."*(00:18~00:29)
- *"we started Open Hands as an MIT-licensed coding agent. Uh, and I would say now we've we've evolved really to a a platform for running coding agents. Everything from the harness to the infrastructure to the control plane to actually like monitor these agents at scale."*(00:31~00:43)

→ [[openhands]](신규) · [[robert-brennan]](신규) · [[agent-platform-layers]](harness·infrastructure·control plane을 한 회사가 다 갖는다는 자기 규정)

## 2. AI 개발의 단계 — 3번에서 4번으로 (00:47~03:18)

화자가 슬라이드의 단계를 따라 말한다. 번호는 *"number three"*와 *"number four"*만 발화되고, 나머지는 발화 순서에 따른 추정이다.

| 단계 | 발화 |
|---|---|
| 챗봇 스니펫 | *"I remember the first time I typed in a ChatGPT like, 'Write a SQL query that does X.' And it just like one-shotted it"*(00:57~01:03). 복사·붙여넣기 루프는 *"kind of dumb"*(01:20)였다 |
| AI IDE | *"stuff like Cursor and GitHub Copilot, doing things like auto complete"*(01:25~01:29). 코드베이스의 맥락을 본다 |
| 에이전트 (3) | *"the big leap in like the beginning of 2024, uh, was this leap to agents. So, uh, AI that wasn't just writing code, but was actually running the code that it wrote"*(01:42~01:52). *"most developers today are still (…) running something like Quad Code[=Claude Code] or Open Hands uh or Codex on their laptop (…) as like kind of a pair programmer model, right? They're manually prompting this thing."*(02:01~02:13) |
| 클라우드 에이전트 (4) | ⭐ *"The leap that we're seeing organizations make over the course of 2026 is really to agents that run in the cloud."*(02:14~02:20) |
| 멀티에이전트 팀 | *"running uh you know, in response to events coming out of systems like GitHub and DataDog and Slack, rather than being manually prompted, you're going to get these interactions between agents where like one agent opens a PR, another's doing code review"*(02:48~03:00) |
| 끝 | *"I think the end game is really this full SDLC automation where, you know, humans aren't even looking at the source code anymore."*(03:03~03:08) |

클라우드에 샌드박스가 필요한 이유는 둘이다. 하나는 *"it needs a place to work in the cloud, right? You need to give this agent a terminal, a file system, etc."*(02:23~02:28)이다. 다른 하나는 ⭐ *"you need to make sure that they have access only to the things that they're they're allowed to access um cuz there's not necessarily going to be a human there to babysit them, right?"*(02:36~02:44)이다. 발표 범위는 *"how do we make this leap from from number three, where we're running agents on our machine, to number four, where we've got agents running in the cloud?"*(03:11~03:18)로 정한다.

→ [[cloud-agent-delegation]] · [[ai-native-sdlc]] · [[software-factory]](*"full SDLC automation"* — ⚠️ 화자의 전망일 뿐 근거는 없다) · [[persistent-agent-teams]]

## 3. 로컬의 trade-off — babysit 또는 dangerously skip permissions (03:20~04:39)

- 손들기: *"who here runs Quad Code[=Claude Code] on their laptop or Codex or Open Hands (…)? All right. Fewer than I'd expect. Uh keep your hand raised if you use dangerously skip permissions. (…) Somehow more hands than before."*(03:22~03:38)
- ⭐ *"This is the big trade-off when running agents locally, right? Is you can either sit there and hit like yes, yes, yes, you're allowed to do that over and over again and babysit the agent while it works, or you can go into dangerously dangerously skip permissions mode and just like trust that the agent isn't going to delete a file you really care about, or access your production database"*(03:39~03:57)
- skip permissions로 돌린 에이전트가 닿는 것: 로컬 파일 시스템 전체, 환경 변수의 비밀, 홈 디렉터리의 비밀, 연결된 프로덕션 DB와 Kubernetes 클러스터(04:10~04:26). *"It has access basically to everything that you have access to, right?"*(04:26~04:29)
- *"either sit there and baby sit it and watch what it's doing, or you find a way to cut off its access, and really only give it access to the things that it needs."*(04:32~04:39)

→ [[claude-code]](`--dangerously-skip-permissions`) · [[deny-and-continue]]·[[anthropic-claude-code-auto-mode]](같은 trade-off에 대한 Anthropic의 답은 분류기다. 이 발표의 답은 격리다) · [[privacy-auto-mode]]

## 4. 최소 권한과 blast radius (04:41~05:27)

- *"a paradigm that we actually know well from, you know, pre-agent security days, the principle of least privilege, right? The idea is that both agents and humans should only have access to the things that they need in order to do their job"*(04:41~04:53)
- 예: *"Should only have access to the GitHub repo that it's editing, and maybe a couple secrets that it needs to access a local database"*(05:00~05:04)
- ⭐ *"we're looking at what exactly does this agent need in order to do its job. And then we can create a sandbox that has just exactly those things. And then we know that the the blast radius of a prompt injection attack, uh or the agent getting confused, anything that could go wrong, like we we limit the blast radius by limiting how much the agent has access to."*(05:08~05:27)

→ [[least-privilege-connectors]](실행 환경 층) · [[prompt-injection]] · [[agentic-misbehavior]](injection과 *"getting confused"*를 한 blast radius로 묶는다) · [[lethal-trifecta]]

## 5. 전략 1 — 노트북의 Docker 컨테이너 (05:30~06:49)

- *"the first strategy that folks tend to experiment with is running inside of Docker containers on their laptop. This is actually the uh way we originally launched Open Hands was as an interface where every time you started a new conversation with the agent, we'd spin up a brand new Docker container."*(05:30~05:43)
- ephemeral: *"if it runs rm -rf / and deletes everything, uh you just kill the container and start again"*(05:52~05:57). *"the agent can can just kind of run wild."*(05:58~06:00)
- 선택적 마운트: Git 저장소, 포트(브라우저로 앱 확인), 특정 비밀·환경 변수, 로컬이나 컨테이너 안의 MCP 서버(06:05~06:23)
- 로컬 사본: *"the agent is still working with like your local copy of the code (…) instead of you editing it, the agent's editing it now and you're deciding when to get pushed"*(06:25~06:36)
- 한계: *"this doesn't really scale very well. Uh there's only so many Docker containers you can get running on a laptop. Uh your laptop can't like listen for events coming out of like Slack and DataDog, etc."*(06:36~06:46)

→ [[agent-sandboxing]] · [[action-reversibility]](ephemeral = 되돌림 비용 0) · [[model-context-protocol]] · [[credential-injection-outside-sandbox]](⚠️ 비밀을 샌드박스 *안에* 마운트하는 쪽이다. 아래 "갈리는 것" 참조)

## 6. 전략 2 — Claude Code + GitHub Actions (06:52~08:06)

- *"starting to like glue together Quad Code[=Claude Code] and GitHub Actions"*(06:52~06:57). 로컬 사본이 아니라 *"an ephemeral environment somewhere inside of GitHub Actions, cloning the repo, doing stuff, you know, uh and then like shipping it off and then everything everything goes away once that action spins down."*(07:10~07:18)
- 장점: *"you can run as many GitHub Actions as you're willing to pay for. Right? It has built-in support for things like a secrets registry."*(07:23~07:29) 스케줄도 된다. *"a GitHub Action that spins up an agent, you know, every Monday morning at 9:00 a.m. and updates your dependencies"*(07:36~07:40), *"anytime a PR gets opened is going to use an agent to do code review"*(07:41~07:44)
- ⭐ 한계: *"But you're locked into GitHub actions, right? This is a proprietary standard. Uh you're not going to be able to really port this. Um it's only able to respond to events coming out of GitHub, right? You can't respond to like a Slack webhook or a Datadog webhook."*(07:50~08:01)

→ [[scheduled-agent-automations]] · [[agent-sandboxing]](트리거 축) · [[tech-bridge-tailscale-aperture-ai-without-lock-in|Tailscale 편]](lock-in 논리. 그쪽은 샌드박스 층에서도 고를 수 있어야 한다고 한다)

## 7. 전략 3 — 별도 VM·Mac mini, 그리고 co-location 문제 (08:10~09:34)

- *"The next strategy we saw folks take was kind of in the open claw[=OpenClaw] craze where you actually get a separate computer, you know, a virtual machine in the cloud or maybe a Mac mini uh and just put all your agents on that, right?"*(08:10~08:20)
- 지속성은 양날이다: *"now you've got a long-lived environment. You've got persistence, right? Which is good and bad, right? You you your agents can modify the system and know it's going to be that way again when they run, you know, 2 days from now. Um but your machine could get into a bad state as well and you might have to go and debug"*(08:22~08:35)
- 트리거가 넓어진다: 스케줄과 webhook(*"Twilio if you want to listen for text messages from Slack. Uh you can listen for incidents coming out of Datadog, events coming out of GitHub"* 08:47~08:54). *"So, you get agents running automatically now."*(08:55~08:57)
- ⭐ *"But you still have this principle of least privilege problem, right? Where all of your agents are now like co-located in this virtual machine and they all have access to the same stuff."*(08:58~09:06) 예시는 코드 리뷰 에이전트와 Datadog 인시던트 분류 봇이 한 VM에 있는 경우다. *"the code review agent now for some reason has access to Datadog (…) The code review bot can even like uh you know, edit the the memory for the Datadog bot."*(09:12~09:23) *"way more opportunities for things to go wrong when all these agents are bumping into each other."*(09:31~09:34)

→ [[openclaw]] · [[persistent-agent-teams]](상시 봇 여럿이 한 기계에 있으면 생기는 문제) · [[pets-vs-cattle]](long-lived VM = pet) · [[agent-identity-separation]](에이전트마다 좁은 신원)

## 8. 전략 4 — Kubernetes, 세션당 pod (09:38~10:45)

- ⭐ *"The fourth and and really like the most robust strategy here, I would say is to use Kubernetes or some other like, you know, highly scalable environment that's ephemeral, right? Um and now you're getting, you know, with Kubernetes say, uh you get a pod for every agent session you want to run. It spins up, the agent runs, does its work (…) then it spins down and all that environment goes away. You know, the agent has opened up a pull request or something like that"*(09:38~10:03)
- *"you don't have to worry about like the long-term state of this thing the way you do with a VM. (…) every time an agent runs, you're you're basically killing the environment and starting fresh."*(10:04~10:15)
- *"you get like an infinite amount of scale, right? You're you have cloud scale at this point. Um you can run as many agents as you want as long as you're again willing to pay for the memory and CPU uh to run them."*(10:15~10:26)
- *"you can run things on a schedule using uh cron jobs. You can uh run things in response to HTTP events coming out of, you know, Slack and GitHub and Jira. Um you can basically run agents fully automatically."*(10:32~10:45)
- ⚠️ 단점은 발화되지 않는다. 비용(*"willing to pay"*)만 조건으로 붙는다. 세션 사이 상태를 어떻게 넘기는지는 비교 절의 *"saving files out or like writing to external systems"*(11:38~11:42)까지만 나온다.

→ [[pets-vs-cattle]] · [[brain-hands-decoupling]](sandbox를 cattle로) · [[cloud-agent-delegation]](Kimchi Teleport도 Kubernetes 컨테이너다)

## 9. 비교 — 다섯 축 (10:49~12:09)

화자가 꼽는 축은 *"the things that I look at when I'm comparing these different strategies"*(10:53~10:56)이다. 아래 표는 발화를 칸에 옮긴 것이다. 슬라이드에 표가 있었을 수 있지만 화면은 확인하지 않았다. 빈칸은 발화되지 않은 자리다.

| 축 | 로컬 (skip permissions) | ① 로컬 Docker | ② GitHub Actions | ③ VM·Mac mini | ④ Kubernetes |
|---|---|---|---|---|---|
| **local/remote** | 노트북, 내 사본 | 노트북, 내 사본(마운트) | 원격, repo를 clone | 원격 별도 컴퓨터 | 원격, pod 안 사본 |
| **scale** | *"ones of agents"*(11:12) | *"only so many Docker containers"*(06:40) | *"as many (…) as you're willing to pay for"*(07:23) | — | *"thousands"*(11:16), *"infinite amount of scale"*(10:17) |
| **isolation** | *"you've got nothing"*(11:22) | ephemeral, 선택적 마운트 | *"nice isolated environments"*(07:30) | *"separated from your environment, but they can still step on each other's toes"*(11:27~11:30) | *"every agent has its own workspace"*(11:31~11:33) |
| **persistence** | 기본 지속(11:42~11:48) | ephemeral | *"everything goes away"*(07:17) | long-lived, 좋기도 나쁘기도(08:22~08:35) | *"all that environment goes away"*(09:59~10:01) |
| **triggers** | 수동 프롬프트(11:53~11:56) | Slack·Datadog 이벤트 불가(06:43~06:46) | 스케줄 + GitHub 이벤트만(07:33~08:01) | 스케줄 + webhook(08:37~08:55) | cron + HTTP 이벤트(10:32~10:43) |

- local/remote: *"Is it on your on your laptop working with your copy of the code base or is it running somewhere else that has to like clone in the code itself or with its own copy? Those are two very different ways of working."*(10:58~11:07)
- persistence는 결정적이지 않다: *"you can you can always get some persistence by saving files out or like writing to external systems."*(11:38~11:42)
- 일화: *"If you've ever like been like biking home with your laptop open cuz you didn't want cloud code[=Claude Code] to shut down, this is a great reason to start moving your agents to the cloud."*(12:02~12:09)

→ [[agent-sandboxing]](이 표가 개념 페이지의 뼈대) · [[scheduled-agent-automations]] · [[cloud-agent-delegation]](Conductor의 *"they're not going to get shut down when you close your laptop lid"*와 같은 그림)

## 10. 한계 — "sandboxing is not a panacea" (12:12~12:50)

- ⭐ *"I did want to touch on the fact that sandboxing is not a panacea. There is evidence of agents escaping their sandboxes."*(12:12~12:22)
- *"You know, here we we saw during one when Anthropic was testing Mythos. One of the Mythos instances actually managed to break out of its sandbox, gain internet access, or doing other things."*(12:22~12:33) ⚠️ 출처 미제시, 이 위키에서 미확인이다.
- *"There are container escape attacks out there. Some of them are known if you're running an old version of Docker, say."*(12:33~12:40)
- *"So, it's not it's not perfect. You still have to be a little bit careful, but it is it is at least a good first pass at keeping agents limited to what they're what they should be doing."*(12:41~12:50)

→ [[claude-mythos-preview]] · [[agentic-misbehavior]] · [[tech-bridge-openai-huggingface-incident-black-hat]](그쪽 분석은 "샌드박스 탈출"이 아니라 허용된 의존성을 쓴 것이라고 정리했다. 이름이 같아도 기제는 확인해야 한다)

## 11. OpenHands Agent Canvas — 자사 제품 (12:54~13:47)

- *"Last, I'll give a quick plug for OpenHands Agent Canvas. This is a way you know, really to run with any type of sandbox. You can run it with cloud code[=Claude Code] or code X[=Codex] or the OpenHands harness."*(12:54~13:05)
- ⭐ *"by default if you saw it on your laptop, it's like running cloud code[=Claude Code] with dangerously skip permissions. But with one quick toggle, you can start running things in Docker containers. Another toggle, you can start running it in a remote VM. Another toggle, you can run it inside of Kubernetes."*(13:07~13:20) ⚠️ *"saw"*는 판독 보류다(start?).
- *"pick the right environment for the job"*(13:20~13:23): 로컬 사본으로 *"quick iterative development back and forth with an agent"*(13:28~13:30)를 할 때와 *"fire off events that, you know, let agents run autonomously in the background for a few hours"*(13:32~13:36)를 할 때를 가른다.

→ [[openhands]] · [[cloud-agent-delegation]](Rauch의 "양방향 토글"과 같은 방향) · [[embedded-agent-harness]](하네스를 바꿔 끼우는 쪽)

## 이 위키와의 연결

### 이어지는 것

- **[[cloud-agent-delegation]]: 보안이 근거로 앞에 선다.** 이 페이지의 기존 근거는 노트북을 닫아도 돈다는 것(Cursor·Conductor·Kimchi)과 규모·병렬이었다. Rauch(Vercel)가 보안을 근거 중 하나로 들었다. Brennan은 **감독할 사람이 없다는 사실**(02:41~02:44)을 샌드박스의 첫 근거로 놓는다. 그리고 클라우드 위임을 **하나의 범주가 아니라 네 단계의 격리 스펙트럼**으로 쪼갠다.
- **[[least-privilege-connectors]]: 층이 다른 새 서술이다.** 기존 서술(Zuckerberg·Google Cloud·Huang·Tailscale)은 커넥터·도구·신원 단위로 권한을 좁혔다. Brennan은 **실행 환경 단위**로 좁힌다. 무엇을 마운트하고 어떤 비밀을 넣을지를 정한다. 근거 어휘는 *blast radius*이고, *"both agents and humans"*(04:49~04:51)라며 사람에게도 같은 원칙을 건다.
- **[[persistent-agent-teams]]·[[openclaw]]: co-location 문제.** 상시 봇 여럿을 한 기계(VM·Mac mini)에 두는 패턴을 최소 권한 쪽에서 처음 비판한다. *"The code review bot can even (…) edit the the memory for the Datadog bot."*(09:19~09:23)
- **[[pets-vs-cattle]]**: VM의 *"long-lived environment"*는 좋기도 나쁘기도 하다(08:22~08:35). Kubernetes pod는 *"killing the environment and starting fresh"*(10:13~10:15)다. Anthropic Managed Agents가 sandbox를 cattle로 만든 이유와 같은 논리가 **에이전트 사용자 쪽**에서 나온다.
- **[[scheduled-agent-automations]]**: 트리거(수동 → 스케줄 → 이벤트)가 실행 환경의 함수라는 서술이다. GitHub Actions는 GitHub 이벤트에만 묶인다.
- **[[tech-bridge-tailscale-aperture-ai-without-lock-in|Tailscale 편]]**: 같은 날(10-17) ingest된 Guercio는 샌드박스를 내부 AI 배포의 네 층 가운데 하나로 두고 *"let a thousand flowers bloom phase"*(Tailscale 16:51~16:54)라고 했다. Brennan의 네 전략은 그 "천 송이"의 한 분류다. lock-in 비판(GitHub Actions *"proprietary standard"*)도 같은 방향이다.

### 갈리는 것

> ⚠️ **Contradiction(약): 샌드박스는 공급망 공격을 없애는가.** [[cloud-agent-delegation]]에 기록된 Rauch는 *"we could eradicate supply chain attacks (…) if we move more and more of this development life cycle to to sandboxes"*(Vercel 편 12:48~12:56, 스스로 *"bold statement"*)라고 했다. Brennan은 *"sandboxing is not a panacea. There is evidence of agents escaping their sandboxes."*(12:15~12:22)라고 한다. 위협 모델은 다르다. Rauch는 개발자 머신의 malware를 보고, Brennan은 샌드박스 안의 에이전트 자신과 컨테이너 탈출을 본다. 그래도 **"샌드박스로 옮기면 해결된다"는 강도**에서는 두 발언이 갈린다. 두 화자 모두 클라우드 실행 인프라를 판다.

> ⚠️ **긴장: 비밀은 샌드박스 안인가 밖인가.** Brennan의 처방은 필요한 비밀만 골라 넣는 것이다(*"You can mount specific secrets and environment variables for the agent"* 06:15~06:18, *"maybe a couple secrets"* 05:02). [[credential-injection-outside-sandbox]]는 **샌드박스에 자격증명을 두지 않고** 프록시 층에서 주입하는 쪽이다. [[least-privilege-connectors]]의 Muse도 *"에이전트는 그걸 알아서는 안 됩니다"*라고 한다. Brennan은 비밀의 *개수*를 줄이고, 다른 쪽은 비밀이 에이전트에 *보이지 않게* 한다. 발표는 이 차이를 다루지 않는다.

> **로컬은 출발점인가 남겨 둘 자리인가.** [[tech-bridge-lauren-tan-trusting-agents|Lauren Tan]]은 로컬에서 관찰하며 신뢰를 쌓은 뒤 클라우드로 가라고 했다(순서). Rauch는 로컬로 끌어내릴 선택지를 남기라고 했다(양방향). Brennan의 Agent Canvas 토글(13:07~13:20)과 *"Sometimes you really do want to be working with your local copy"*(13:23~13:26)는 **Rauch 쪽**이다. 다만 그는 로컬 기본값을 *"like running cloud code with dangerously skip permissions"*(13:08~13:12)라고 묘사한다. 관찰의 자리라기보다 격리가 없는 자리다.

## 해소하지 않고 표시만 한 것

- Mythos 샌드박스 탈출 주장의 출처·시점·세부(12:22~12:33). *"during one"*이 가리키는 것.
- 어떤 조직이 몇 번 단계에 있는지, 각 전략의 실제 사용 비율. 손들기 결과는 인상뿐이다.
- Kubernetes 전략의 단점(비용 외), 세션 간 상태 이전, 네트워크 egress 통제. *"gain internet access"*를 말하면서도 네트워크 격리는 처방에 없다.
- Agent Canvas의 실제 기능·인터페이스·가격, 토글 사이에서 무엇이 유지되는지. *"if you saw it on your laptop"*의 판독.
- *"Twilio if you want to listen for text messages from Slack"*(08:47~08:51)의 구조.
- 행사명·도시·녹화일. 슬라이드 내용(단계 번호, 비교 표, Mythos 자료).

## 등장 개체

- 인물: [[robert-brennan|Robert Brennan]](신규 제안 — 자막에서 자기소개, 설명란과 일치)
- 조직: [[openhands|OpenHands]](신규 제안 — Agent Canvas는 이 페이지에 섹션으로) · [[anthropic|Anthropic]](Mythos 테스트 일화) · [[ai-engineer|AI Engineer]](⚠️ 설명란 링크만, 추정)
- 모델·제품: [[claude-mythos-preview|Mythos]](⚠️ 화자 주장) · [[claude-code|Claude Code]](en-orig *"Quad Code"*·*"cloud code"*) · [[codex|Codex]] · [[cursor|Cursor]] · [[openclaw|OpenClaw]](en-orig *"open claw"*) · ChatGPT · GitHub Copilot · GitHub Actions · Docker · Kubernetes · Mac mini · Datadog · Slack · Twilio · Jira — 페이지 없음
- 개념: [[agent-sandboxing]](신규 제안) · [[cloud-agent-delegation]] · [[least-privilege-connectors]] · [[prompt-injection]] · [[agentic-misbehavior]] · [[lethal-trifecta]] · [[persistent-agent-teams]] · [[pets-vs-cattle]] · [[brain-hands-decoupling]] · [[scheduled-agent-automations]] · [[credential-injection-outside-sandbox]] · [[agent-identity-separation]] · [[action-reversibility]] · [[deny-and-continue]] · [[privacy-auto-mode]] · [[model-context-protocol]] · [[agent-platform-layers]] · [[embedded-agent-harness]] · [[ai-native-sdlc]] · [[software-factory]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=VOToAHcnhyA> (13:51, `upload_date` 2026-10-16)
- raw: `01.raw/articles/2026-10-16_샌드박스는 선택이 아닙니다 - 코딩 에이전트 격리 방법 4가지.md`
- 설명란 링크: <https://openhands.dev> · <https://github.com/OpenHands/OpenHands> · <https://x.com/rbren_dev> · <https://www.linkedin.com/in/robert-a-brennan> · <https://aie.codes> · <https://ai.engineer> (⚠️ 열어 보지 않았다)
- 클라우드 실행의 다른 서술: [[tech-bridge-vercel-rauch-agentic-workflow]] · [[tech-bridge-conductor-orchestras-not-factories]] · [[tech-bridge-kimchi-cost-per-task-harness]] · [[tech-bridge-cursor-legacy-refactoring]] · [[tech-bridge-lauren-tan-trusting-agents]]
- 같은 날 ingest, 샌드박스 층: [[tech-bridge-tailscale-aperture-ai-without-lock-in]]
- skip permissions의 다른 답: [[anthropic-claude-code-auto-mode]]
- "샌드박스 탈출"의 다른 사건: [[tech-bridge-openai-huggingface-incident-black-hat]]
- [[tech-bridge]] · [[openhands]] · [[robert-brennan]]
