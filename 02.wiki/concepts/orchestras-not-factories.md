---
title: 공장이 아니라 오케스트라 (Orchestras, Not Factories)
type: concept
category: framing
tags: [software-factory, human-in-the-loop, multi-agent, metaphor, developer-experience, coding-agents]
aliases: [orchestras not factories, 공장이 아닌 오케스트라, orchestra not factory, 지휘자 비유]
related: [software-factory, frontier-engineering, persistent-agent-teams, agent-swarm, slop-free-zone, multiplayer-agent-context, risk-proportional-human-review, goal-level-delegation]
first-seen: tech-bridge-conductor-orchestras-not-factories
sources: [tech-bridge-conductor-orchestras-not-factories]
created: 2026-10-02
updated: 2026-10-02
---

# 공장이 아니라 오케스트라 (Orchestras, Not Factories)

**에이전트로 소프트웨어를 만드는 일을 "공장"(자동화된 조립 라인, 사람은 라인 관리자)이 아니라 "오케스트라"(사람이 지휘자로 가운데 서고, 사람과 에이전트가 섞여 연주하며, 원할 때만 세부로 줌인)로 생각하자는 프레이밍.** [[conductor|Conductor]] 공동 창업자 [[charlie-holtz|Charlie Holtz]]가 [[tech-bridge-conductor-orchestras-not-factories]]의 제목이자 여섯 번째 원칙으로 제시했다. [[software-factory]]라는 말에 대한 **명시적 반론**이다.

> *"the title of this talk is orchestras not factories. The whole like talk track today is about software factories and I honestly kind of hate the term. I think it's the wrong way of thinking about these new tools that are emerging."* (14:18~14:34)

## 두 이미지

| | 공장 (거부) | 오케스트라 (제안) |
|---|---|---|
| 사람의 자리 | *"factory line managers like pushing buttons getting the agents to like pump out the next feature"* (15:20~15:24) | *"in front of an orchestra like waving my baton"* (14:57~15:02) |
| 에이전트 | *"managing swarms of agents"* (15:17~15:20) | *"this team of agents starts working and then this intermingling of humans and agents starts working"* (15:04~15:08) |
| 세부와의 거리 | (말하지 않음) | *"when I want to I can zoom in on the details but most of the time I can zoom out"* (15:10~15:14) |
| 결과물 | *"pump out the next feature"* | *"I want my software to feel human and crafted"* (15:30~15:35) |
| 극단 | *"my dark factory"* · *"a line manager"* (16:01~16:05) | *"Steve Jobs designing the Mac with a team of amazing humans and AI agents all in the same place"* (16:11~16:17) |

## 근거 — 역사, 경험, 책임

1. **역사**: *"we we we tried this like 10 years ago with the term feature uh feature factories and it just doesn't work"*(15:26~15:33). 지금의 software factory를 10년 전 **feature factory**의 재방송으로 본다. ⚠️ 무엇이 왜 실패했는지는 말하지 않는다.
2. **경험**: *"I want to feel like a human. I want to like be in the flow."*(14:55~14:57), *"I want to be having fun. I want to be crafting things."*(16:08~16:11)
3. **도구 제작자의 책임**: *"because we're all building these tools, we actually have a responsibility to make the tools um great for humans. I think it's really important to like use the words that make us feel excited and like feel uh feel capable"*(15:39~15:52).

**자동화 자체를 부정하지는 않는다** — *"there's a lot of amazing things about automation and like it makes our lives more efficient and we can like create more of everything. But the I don't want the future to be built around factories."*(14:42~14:52)

## 이 위키에서의 위치

- **[[software-factory]]** — 이 프레이밍이 반박하는 대상. 화자에 따르면 그 행사 트랙 전체가 software factory를 주제로 했다(14:23~14:30).
- **[[frontier-engineering]]** — Amazon의 frontier developer(사람은 루프 밖, 코드의 1~2%만)와 **태도가 갈린다.** 다만 화자도 *"most of the time I can zoom out"* 이라 하므로 **사람이 하는 일의 양**보다 **사람의 자리와 언어**가 쟁점이다.
- **[[persistent-agent-teams]] · [[agent-swarm]]** — 같은 "에이전트 여럿" 구성. 이 프레이밍은 구성을 거부하지 않고 **관리자 은유(swarm manager)를 지휘자 은유로 바꾼다.**
- **[[slop-free-zone]]** — 같은 발표에서 "지휘자가 언제 줌인하는가"에 대한 **유일한 운영상 답**: 엄격한 사람 검토 구역.
- **[[multiplayer-agent-context]]** — 오케스트라는 *"intermingling of humans and agents"* — 같은 발표의 실시간 협업 데모가 그 제품 형태다.

> ⚠️ **측정 주장이 아니라 언어·가치 주장이다.** 공장 모델이 덜 생산적이라는 증거는 없다. 근거는 10년 전 일화와 *"use the words that make us feel excited"*.
>
> ⚠️ **이해관계.** 화자의 회사 이름이 **Conductor(지휘자)** 다 — 결론의 은유가 제품명과 같다. 제품은 여러 에이전트를 한 화면에서 관리하는 도구로, 운영 형태만 보면 "에이전트 팀 관리"와 구분이 쉽지 않다.
>
> ⚠️ **ko 자막이 결론을 뒤집는다** — *"I don't want to be in my dark factory. I don't want to be a line manager"*(16:01~16:05)가 ko에서 **"어두운 내 공장에 있고 싶다 … 라인 관리자가 되고 싶습니다"**, *most of the time I can zoom out* 이 **"가끔씩 시간을 낼 수 있어"**, *feature factories* 가 **"함수"**. 한국어 자막만 본 독자에겐 반대 주장으로 읽힐 수 있다.

## References

- [[tech-bridge-conductor-orchestras-not-factories]] (first-seen) · [[charlie-holtz]] · [[conductor]]
- 관련: [[software-factory]] · [[frontier-engineering]] · [[persistent-agent-teams]] · [[agent-swarm]] · [[slop-free-zone]] · [[multiplayer-agent-context]]
