---
title: "Tech Bridge — 코딩 에이전트를 전략 게임으로 만들었습니다 (Ido Salomon · AgentCraft): 우리가 병목이다, 게임에서 배운 감독 기술, 천장을 높이고 바닥을 낮춘다"
type: source
tags: [coding-agents, multi-agent, orchestration-ui, human-attention, game-design, visibility, review, collaboration, accessibility, agentcraft, vendor-demo, video]
source-url: https://www.youtube.com/watch?v=eTtZlAPA9H4
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 [[ido-salomon]] ([[agentcraft|AgentCraft]] 개발자 — 자막엔 이름 없음, 제목·설명란 표기) · 행사명·촬영일 미확정
date-published: 2026-10-07
ingested: 2026-10-09
created: 2026-10-09
updated: 2026-10-09
---

# Tech Bridge — 코딩 에이전트를 전략 게임으로 만들었습니다 (Ido Salomon · AgentCraft)

[[tech-bridge|Tech Bridge]]가 재배포한 **13:12 무대 발표 겸 라이브 데모**(Q&A 없음, 공식 챕터 18개 — 0초 무제 챕터 포함). 화자는 코딩 에이전트를 RTS 게임처럼 지도 위 유닛으로 다루는 오케스트레이터 [[agentcraft|AgentCraft]]의 개발자 [[ido-salomon|Ido Salomon]](이름은 제목·설명란에만). **측정 없는 당사자 데모**다 — 논지는 한 문장이고 나머지는 그 문장을 푸는 제품 기능 순회다. 이 위키의 [[verification-bottleneck]] 논의에 *리뷰* 가 아니라 **감독(supervision)·주의(attention)** 쪽 병목을 들였다 → [[agent-attention-management]] (신규).

> **에이전트는 대단한데 우리는 왜 무적이 아닌가 — 에이전트 하나하나를 조종·지시·리뷰해야 하고, 규모가 커지면 지친다. 병목은 우리다. 하지만 그 일에 필요한 기술은 이미 갖고 있다: 게임에서 유닛 여럿을 감독하던 기술. 가시성 → 할 일 생성(퀘스트) → 자율 실행 → 시각적 증거 리뷰 → 사람과 함께로 '천장'을 높이고, 단순판으로 '바닥'을 낮춰 나머지 사람들도 번아웃 없이 데려온다.**

> *"So, in reality, we are the bottleneck."* (01:01~01:02) · *"Like, if if you're playing Warcraft, for example, or Sims, and you have a bunch of different, uh, units running around and you need to understand what they're doing and supervise all of it, how different is that from from actually inspecting agents?"* (01:29~01:42) · *"So, we need to raise the ceiling, but we also need to uh lower the floor."* (10:54~10:59) · *"So, we are the bottleneck, but we don't have to be."* (13:02~13:04)

ASR·ko 보정: ⭐ ko가 **결론 문장을 뒤집었다** — *"we are the bottleneck, but we don't have to be"*(13:02~13:04)가 **"그것은 아닙니다. 우리에게는 그럴 만한 이유가 있다"**. 또 *without having them burn out*(사람이 지치지 않게)을 **"에이전트가 부족해지지 않는 미래"로**(11:07), *20 stuff going at the same time* 을 **"이제 저는 스무 살이에요"로**(05:57), 리뷰 키트의 *entire changes* 를 **"잔돈"으로**(07:16), 협업의 *hand off or fork* 를 **"송금 … 포크 하나"로**(09:14), *flunked out of college because he played StarCraft* 를 **"스타크래프트를 하기 위해 대학에 갔고"로**(10:39 — `en`의 *"dropped out … to play"* 경유 2단 변형) 옮겼다. *"They're just normal agents"* 는 `en`·ko 공유로 **"일반 경찰관"**(02:42). en-orig 자체는 제품을 처음 한 번 *"AtomCraft"*(01:46, 세 트랙 공유), Claude Code를 *"cloud code"* 로 들었다. 전체 목록은 raw. **인용은 en-orig에서만** 했다.

> ⚠️ **당사자 데모, 수치·측정 없음.** 발표의 약 80%(01:57~12:50)가 자사 제품 순회이고, 화면은 자막으로 확인할 수 없어 **기능은 화자의 서술로만** 기록했다. *"25 cloud code agents"*(00:31)·*"20 things"*(05:28)는 수사, *"probably around 90% of the people in the world"*(11:03~11:06)는 **근거 없는 추정**, 사용자 반응(아이들·StarCraft 중퇴자)은 **화자가 받은 피드백 일화**다.
>
> ⚠️ **화자·행사·시점.** 자막에 자기소개가 없고 **첫 줄이 문장 중간**(*"Uh, but we're here to talk about…"* 00:00)이다 — 앞부분이 잘렸다. 이름 *Ido Salomon* 과 링크(`x.com/idosal1`, `mcp-ui.dev`)는 설명란에만, 소속 회사는 발화되지 않는다. 설명란의 **#MCP·`mcp-ui.dev`에 대응하는 발화는 없다.** 행사명 미발화. 시점 단서는 *"Now it's called software factories, but at the time it was just doing stuff autonomously"*(06:13~06:18)와 *"loops, which everyone really likes right now"*(06:37~06:41)뿐 — **촬영일 미확정**, 업로드 2026-10-07.
>
> ⚠️ **`>>` 끼어든 소리** — *"At your command."*(02:39), *"Prompt prompt."*(02:54, 09:02), *"[music]"*(10:32). 음성 프롬프트 시연 직후라 **AgentCraft의 게임식 음성 효과로 읽었으나 위키의 추정**이다.

## 1. 문제 — 우리가 병목이다 (00:00~01:17)

- 에이전트는 *"from generating cat memes to B2B SaaS apps"*(00:12~00:15)까지 다 하는데 *"why aren't we all unstoppable? Why doesn't everyone have an army of agents"*(00:20~00:25).
- 모니터 몇 대에 에이전트 25개를 띄우면 될 것 같지만 *"it's just not that simple"*(00:36~00:38). 두 조건 — ① 에이전트를 정말 쓰고 싶어야 하고 ② *"each one of these agents require you to steer them, direct them, review them, and when it's at scale, especially, it's just exhausting"*(00:47~00:55).
- 필요한 것: *"the skills to allow us to do it without burning out"*(00:57~00:59). → *"we are the bottleneck"*(01:02).

→ [[verification-bottleneck]] — 다만 이 발표의 병목은 **리뷰만이 아니라 steer·direct·review 전부**, 즉 사람의 **주의와 기력**이다. → [[agent-attention-management]]

## 2. 기술은 이미 있다 — 게임 (01:05~02:05)

필요한 기술은 *"have been with us all along"*(01:15~01:18): Warcraft·Sims에서 유닛 여럿을 이해하고 감독하는 것과 에이전트를 살피는 것이 *"how different is that"*(01:29~01:42). 그래서 *"I took this concept, uh, too far"* — *"a game-inspired orchestrator, uh, that tries to bring all that good stuff together into work"*(01:42~01:53). 목표는 *"raise the ceiling of how humans and agents can collaborate"*(02:03~02:05).

→ [[agent-manager-analogy]]에 **네 번째 비유**(매니저·헤드셰프·뒷좌석 운전자 다음 — **RTS 지휘관**). [[orchestras-not-factories]]의 지휘자 비유와 같은 자리를 다른 은유로 채운다.

## 3. AgentCraft 기본 (02:08~03:19) → [[agentcraft]] (신규)

- **에이전트 = 지도 위 유닛.** *"an actual representation of uh cloud[=Claude] code or open claw, whatever agent"*(02:19~02:25) — 기기에서 **감지**하거나 AgentCraft에서 **생성**(02:27~02:32). Codex·OpenCode 등(02:34~02:36). *"They're just normal agents."*(02:43) → [[claude-code]] · [[openclaw]] · [[codex]]
- **사이드 패널 프롬프트 + 음성** — *"there's multimodality here"*(02:45~02:53).
- **건물 = 기능** — 플러그인·스킬 관리, 통합 터미널, 통합 Git. *"you can do in your all of your work from within this space"*(03:04~03:19). → [[agent-skills]]

## 4. 천장 높이기 ① 가시성 (03:19~05:16)

| 기능 | 화자 서술 | en-orig |
|---|---|---|
| 상태 사이드 패널 | 에이전트별 과제·마지막 행동·현재 행동 — *"who needs my attention and who doesn't"* | 03:32~03:44 |
| 파일 시스템 지도 | 파일 시스템을 지도에 투영, 파일은 **룬(rune)**, 어느 에이전트가 어느 디렉토리·파일에서 언제 무엇을 했는지 | 03:47~04:12 |
| 연결·히트맵 | *"because we are the orchestrator"* 이 정보를 엮어 **히트맵** | 04:12~04:25 |
| 주의 점프 | ⭐ RTS·Civilization처럼 **스페이스바** → *"the nearest thing that actually needed your attention"*, 질문 답하기·계획 승인 | 04:27~04:55 |

⭐ 가시성만으로는 부족하다 — *"It's pretty exhausting to keep looking at what the agents are doing in the granularity of what files are they using and what tools are they using at the moment."*(05:05~05:14) → 가시성이 오히려 **새 감독 부담**이 된다. → [[agent-attention-management]]

## 5. ② 머릿속 짐 덜기 — 퀘스트와 자율성 (05:16~06:56)

두 문제(05:18~06:04):

1. *"there's just too much to hold in our heads"*(05:22~05:24) — 다 보여도 20가지를 동시에 할 수 없고 다음 할 일조차 떠올리기 어렵다. → **퀘스트**: 에이전트에게 코드베이스를 훑어 다음 할 일을 만들게 하고, 사람은 *"I just click a button, I I accept the quest"*(05:46~05:50).
2. 그러면 이제 20개가 동시에 돌고 *"I have to babysit each and every one"*(05:58~06:04). → **자율성**: 대략의 의도를 주면 **오케스트레이터**가 쪼개 *"a local container"* 에서 격리 실행, *"I don't need to do any babysitting"*(06:20~06:36). ⭐ *"Now it's called software factories, but at the time it was just doing stuff autonomously."*(06:13~06:18) — 위에 **루프**: Twitter나 GitHub를 훑어 만들 만한 것을 찾아 백그라운드에서 기능을 만든다(06:37~06:54).

→ [[software-factory]] · [[loop-is-the-product]] · [[scheduled-agent-automations]] · [[proactive-idea-feed]]. ⚠️ 루프가 *"scan Twitter for cool stuff you want to build"* 하는 것의 품질 관리·검증은 말하지 않는다.

## 6. ③ 리뷰 키트 — 시각적 증거 (06:56~07:38)

*"what do I do when I have (…) even five things to review at the same time"*(07:00~07:09). → **review kit**(07:12~07:36):

- 전체 변경과 파일 목록 — *"if you want to go like file by file"*
- 또는 ⭐ *"just get visual evidence. So you can actually see videos of what changed or photos of what changed"*(07:22~07:28)
- 또는 여러 인스턴스를 병렬로 돌려 *"just pick the best implementation out of these"*(07:30~07:36)

→ [[agent-visual-qa]] · [[verification-bottleneck]] · [[minimizing-reader-load]]. ⚠️ 영상·사진 증거로 무엇을 **놓치는지**(UI에 드러나지 않는 변경 — [[mergeability-gap]]의 *"quietly broke other code"*)는 다루지 않는다.

## 7. ④ 협업 — 함께 쓰는 방 (07:38~10:01)

- 동기: 여전히 지치고 *"It's pretty lonely to just talk to agents all day"*(07:56~08:01), 팀이라면 *"I might not even be the right person to review what's going on"*(08:08~08:12).
- **방(room)** — *"war halls, war rooms, whatever"*, 완전 로컬 호스팅이지만 터널로 사람이 들어온다(08:21~08:34). 화자의 아내(프로덕트 디자이너)를 승인해 들인다(08:36~08:46).
- ⭐ 디자이너가 디자인하는 것을 엔지니어가 지도에서 보고, *"I can take that design, follow up on it, implement it while she keeps working"*(09:07~09:12). **hand off·fork**, 공유 워크스페이스 — *"I can use get[=Git], but I'm not really bound to something"*(09:14~09:23).
- 사람끼리만이 아니라 **사람·에이전트 공용 채팅**과 **게시판**(notice board) — *"They're all aware of each other"*(09:26~09:43). 모바일·Telegram에서도(09:53~09:59).

→ [[multiplayer-agent-context]] · [[design-handoff-friction]]. ⚠️ [[multiplayer-agent-context]]가 미해결로 둔 **권한 상승·동시 지시 충돌**은 다루지 않는다.

## 8. 바닥 낮추기 — Loopers(가칭) (10:01~12:50)

- 피드백에서 놀란 점: 파워 유저가 더 하게 된 것보다 *"people that had even nothing to do with agents or nothing to do with productivity"*(10:24~10:27)가 왔다 — 아이들, StarCraft 하다 대학을 중퇴한 사람(10:27~10:52). ⚠️ 일화.
- *"we need to raise the ceiling, but we also need to uh lower the floor"*(10:54~10:59) — *"probably around 90% of the people in the world"* 를 *"without having them burn out"*(11:03~11:09). ⚠️ 90%는 근거 없음.
- **단순판** — *"currently named TBD, um potentially loopers"*(11:15~11:21). Warcraft급 복잡함은 *"daunting"* 할 수 있으니 *"a lower denominator of what makes stuff accessible, especially now that agents are much more capable"*(11:37~11:42): 파일 단위 대신 *"more of a mobile game level"*, 돌아오고 싶은 프로젝트, 루프와 자율 에이전트에 기대 ⭐ *"I prompt, I get a result, I don't really care perhaps about the way, I can see it if I want to"*(12:00~12:09).
- 한계 인정: *"this is one visualization. It can really resonate with some people, but might not (…) with others"*(12:14~12:23) → 맞춤화 방향, *"a very very early draft"*(12:44~12:48).

→ [[agent-attention-management]] · [[capability-discovery-burden]] · [[steering-altitude]]

## 이 위키와의 연결

### 이어지는 것

- **[[verification-bottleneck]]** — 지금까지의 네 답(작업을 고른다 / 역량을 짓는다 / 일을 쪼갠다 / 리뷰를 시스템으로 재건한다)은 모두 **리뷰**의 병목이었다. Salomon은 같은 *"we are the bottleneck"* 을 **조종·지시·리뷰 전체의 주의 비용**으로 넓히고, 답을 **인터페이스**(무엇을 언제 보여 주느냐)에서 찾는다.
- **[[orchestras-not-factories]]** ([[conductor]]) — 둘 다 *여러 코딩 에이전트를 한 화면에서 다루는 앱* 의 제작자 발표이고, 둘 다 사람을 **지휘하는 자리**(지휘자 / RTS 지휘관)에 둔다. 둘 다 사람·에이전트 혼성 실시간 협업을 데모했다. 다만 Holtz는 *"software factory"* 라는 말을 거부하고, Salomon은 자기 자율 실행 기능을 *"Now it's called software factories"* 라며 **그 이름을 받아들인다**(06:13).
- **[[agent-manager-analogy]]** — 매니저·헤드셰프·뒷좌석 운전자에 이어 **RTS 지휘관 / 게임 플레이어**. 매니저 비유가 *위임과 신뢰* 를 말한다면 게임 비유는 **주의 배분과 인터페이스**를 말한다.
- **[[agent-visual-qa]]** — 리뷰 키트의 영상·사진 증거는 *에이전트가 시각 증거를 만들어 사람에게 넘긴다* 는 같은 방향의 제품화.
- **[[steering-altitude]]** — Warcraft급(파일·도구 단위)에서 모바일 게임급(*"I prompt, I get a result"*)으로 **같은 제품 계열 안에서 조향 고도를 둘로 나눈** 사례.

### 갈리는 것

> ⚠️ **Contradiction: 가시성은 짐을 줄이나 늘리나.** 이 발표는 가시성을 *천장 높이기의 첫 단계* 로 세웠다가 곧바로 *"pretty exhausting to keep looking at (…) the granularity of what files"*(05:05~05:14)라 하고, 단순판에서는 *"I don't really care perhaps about the way, I can see it if I want to"*(12:05~12:09)로 **과정 보기를 선택 사항으로 내린다.** [[verification-bottleneck]]·[[mergeability-gap]] 쪽 소스들(Voss — *"Please please read the code"* 인용)은 **과정(코드)을 덜 보는 것의 위험**을 말한다. Salomon은 이 긴장을 말하지 않는다 — 위키의 독해: 그의 답은 *덜 보기* 가 아니라 **볼 것을 고르게 하는 인터페이스**(주의 점프·시각 증거)이지만, 단순판의 *"don't care about the way"* 는 그 범위를 넘는다.

> ⚠️ **바닥 낮추기의 검증 공백.** 에이전트와 무관했던 사람(아이들 포함)을 *"I prompt, I get a result"* 로 데려온다는 방향은 [[capability-discovery-burden]](Brockman — 쓰다 그만둔 사람들)과 같은 문제의식이지만, **결과를 판정할 수 없는 사용자에게 검증을 누가 하는가**는 발표에 없다(위키의 표시).

## 해소하지 않고 표시만 한 것

- **화자 신원·소속** — 자막에 없음. `mcp-ui.dev`(설명란)와의 관계 미발화, 링크는 열어 보지 않았다.
- **행사·촬영일** — 미발화. 영상 첫머리가 잘렸다.
- **`>>` 소리들의 출처**, 08:52·09:04 *"that's her"* 가 가리키는 화면 요소.
- **"Loopers"** — *"currently named TBD"*, 가칭. 출시 여부·형태 미상.
- **OpenCode** — en-orig *"open code"*(02:34)의 제품 판독은 추정(`en`은 *open source*).
- 모든 수치(25·20·90%)와 사용자 일화.

## 등장 개체

- 인물: [[ido-salomon]] (신규) · 화자의 아내(프로덕트 디자이너, 이름 없음)
- 제품: [[agentcraft]] (신규) · Loopers(가칭, 페이지 없음) · [[claude-code]](*"cloud code"*) · [[openclaw]] · [[codex]] · OpenCode(페이지 없음) · Telegram · Git · 게임 — Warcraft · Sims · StarCraft · Civilization
- 개념: [[agent-attention-management]] (신규) · [[verification-bottleneck]] · [[agent-manager-analogy]] · [[orchestras-not-factories]] · [[software-factory]] · [[loop-is-the-product]] · [[agent-visual-qa]] · [[multiplayer-agent-context]] · [[design-handoff-friction]] · [[steering-altitude]] · [[capability-discovery-burden]] · [[mergeability-gap]] · [[minimizing-reader-load]] · [[scheduled-agent-automations]] · [[proactive-idea-feed]] · [[agent-skills]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=eTtZlAPA9H4> (13:12, `upload_date` 2026-10-07)
- raw: `01.raw/articles/2026-10-07_코딩 에이전트를 전략 게임으로 만들었습니다 — Ido Salomon, AgentCraft.md`
- 설명란 링크: <https://x.com/idosal1> · <https://www.linkedin.com/in/ido-salomon/> · <https://mcp-ui.dev> (⚠️ 열어 보지 않았다)
- 같은 주제: [[tech-bridge-conductor-orchestras-not-factories]] · [[tech-bridge-death-of-code-review]] · [[tech-bridge-lauren-tan-trusting-agents]] · [[tech-bridge-mousepower-measuring-agents]]
- [[tech-bridge]] · [[ido-salomon]] · [[agentcraft]]
