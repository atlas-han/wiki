---
title: Skill Self-Improvement
type: concept
category: pattern
tags: [agent-skills, feedback-loop, governance, claude-code]
related: [agent-skills, harness-pruning, self-harness, generator-evaluator-pattern, impeccable, adjective-verb-steering, query-to-skill-distillation, software-factory, agent-state-machine, trace-to-memory-loop, run-trace-skill-distillation, mcp-skill-distribution]
first-seen: tech-bridge-six-agent-skills
sources: [tech-bridge-six-agent-skills, tech-bridge-impeccable-design-steering, tech-bridge-lauren-tan-trusting-agents, tech-bridge-vercel-eve-filesystem-agent, tech-bridge-oracle-agent-memory-harness, tech-bridge-introspection-loop-is-the-product, tech-bridge-warp-factory-engineering, tech-bridge-pocock-pr-bottleneck, tech-bridge-rails-harness-engineering, tech-bridge-goodbye-slop-state-machines, tech-bridge-cooking-with-codex, tech-bridge-langchain-learning-agent-memory, tech-bridge-runlayer-self-improving-skills-mcp, tech-bridge-horthy-state-of-software-factory, tech-bridge-pocock-skills-implement-spec-pr-retro, tech-bridge-chieng-lee-ai-video-production, tech-bridge-harrison-chase-agent-improvement-loop, tech-bridge-dan-martell-grokbot-daily-automation]
created: 2026-09-05
updated: 2026-10-31
---

# Skill Self-Improvement

**실제 작업 중에 발생한 실패를 관찰해 [[agent-skills|스킬]] 자체의 개선안을 축적하되, 반영은 사람의 검토를 거치는 패턴.** [[tech-bridge-six-agent-skills]]의 `task-observer` 스킬이 이 위키에서의 first-seen이다.

## 문제 — 스킬은 만들기보다 유지가 어렵다

> **가장 큰 문제는 스킬을 만드는 것 자체가 아닙니다. 최신 상태로 유지하는 것입니다.**

핵심 논거는 예측 불가능성이다.

> **한 번 앉아서 에이전트가 저지를 모든 실수를 예측할 수는 없습니다.**

즉 스킬의 빈틈은 설계 시점이 아니라 **사용 시점**에만 드러난다. 그래서 개선의 원천을 회고가 아니라 **작업 중 관찰**에 둔다.

## 구조

| 요소 | 역할 |
|---|---|
| **관찰자** | 작업 중 상시 실행. `CLAUDE.md`에 지시를 넣어 유지한다 |
| **`log.md`** | 스킬별 섹션 아래 **제안된 변경 사항**이 쌓인다 |
| **전역 규칙 파일** | *"어떤 스킬도 실제 고객의 이름을 파일에 기록해서는 안 된다"* 처럼 **모든 스킬에 걸리는** 규칙 |
| **사람의 검토 게이트** | 로그의 교훈을 읽고 **영구 반영 여부를 결정** |

교훈은 두 종류로 나온다 — **금지**(이 도구를 여기 쓰지 마라)와 **대체**(올바른 출처는 이것이다). 금지만 쌓이면 스킬이 점점 방어적이 되므로 대체가 함께 기록되는 것이 중요하다.

## 핵심 설계 — 자동 반영하지 않는다

이 패턴의 값은 자동화가 아니라 **자동화를 멈춘 지점**에 있다.

> 로그에 기록된 내용은 (…) **검토한 후** 영구적으로 반영할지 결정할 수 있습니다. 이렇게 하면 **하나의 잘못된 결과가 에이전트가 영원히 따르는 규칙으로 자동 설정되는 것을 방지**할 수 있습니다.

즉 **관찰은 자동, 승격은 수동**이다. 한 번의 우연한 실패가 영구 규칙이 되면 스킬은 개선되는 게 아니라 오염된다.

## 스코프 선택

전역(`~/.claude`)과 프로젝트별 중에서 **프로젝트별을 권장**한다 — *"각 프로젝트의 교훈이 분리되어 관리하기가 더 쉬워집니다."* 교훈은 대개 그 코드베이스의 사정에 묶여 있기 때문이다.

## 사례 — Logo Hub

[[ai-labs|AI Labs]]의 영상 애니메이션 스킬에서 나온 실화다. 브랜드 로고 SVG를 얻으려고 에이전트가 Logo Hub의 CLI 도구를 썼는데 *"그 도구는 **다른 용도로 만들어진 것이라 실패**했습니다."* 기록된 교훈은 금지 하나와 대체 하나였고, 검토 후 반영되어 *"이제 애니메이션 에이전트는 브랜드 로고를 어디에서 가져와야 하는지 정확히 알고" 있다.*

## 위키에서의 좌표

| 패턴 | 무엇이 무엇을 고치는가 | 승격 게이트 |
|---|---|---|
| **skill-self-improvement** | 실패 관찰 → **스킬** | **사람** |
| [[self-harness]] | 하네스가 **자기 하네스** | 자동(논문 설정) |
| [[harness-pruning]] | 모델 향상 → 하네스 **축소** | 사람(팀 판단) |
| [[generator-evaluator-pattern]] | 채점기 → **산출물** | 루프 내 |

[[tech-bridge-ai-native-skills]]의 스킬 거버넌스가 *"스킬을 어떻게 승인·배포할 것인가"* 였다면, 이 패턴은 *"승인된 스킬이 어떻게 낡아가고 어떻게 갱신되는가"* 를 다룬다. 둘은 같은 수명주기의 앞뒤다.

## 승격 게이트가 커뮤니티일 때 (2026-09-12)

[[tech-bridge-impeccable-design-steering]]의 [[paul-bakaus]]가 [[impeccable]]의 명령을 이렇게 다듬는다 — *"가끔 확신 없는 명령을 만들어서 **커뮤니티로 테스트**하고, **정착하면** 더 많은 사람이 즐거움을 얻는구나 깨닫는다."* `overdrive`가 그 사례(반농담 → 열광).

위 표에 한 행이 더해진다:

| 패턴 | 무엇이 무엇을 고치는가 | 승격 게이트 |
|---|---|---|
| Impeccable 명령 | 제작자 실험 → **스킬의 어휘** | **커뮤니티 반응** |

이 페이지의 *승격은 사람이* 와 같은 원칙이되, 그 사람이 **제작자 한 명이 아니라 사용자들**이고 신호가 *실패 관찰* 이 아니라 *즐거움* 이다. ⚠️ 정착의 기준·기간은 없다.

## 거울상 — 성공한 질의에서, 게이트 없이 (2026-09-19)

[[tech-bridge-vercel-eve-filesystem-agent]]의 [[query-to-skill-distillation]]이 이 패턴의 **정확한 거울상**이다. [[vercel|Vercel]]은 하루 수천 건의 **실제 질의**를 주기적으로 모아 반복되는 형태를 스킬로 압축한다(현재 약 100개).

| | **skill-self-improvement** (09-05) | [[query-to-skill-distillation]] (09-19) |
|---|---|---|
| 원천 | **실패 관찰** | **성공한 실제 질의** |
| 방향 | 금지·대체 규칙을 **더한다** | 반복 형태를 **압축한다** |
| 승격 게이트 | **사람의 검토** | **없음 — 주기적 잡이 자동 증류** |
| 빈도 | 작업 중 상시 | 주기적 배치 |

두 패턴을 나란히 놓으면 **스킬의 수명주기에 입력이 둘**이라는 것이 보인다 — *무엇이 잘 되는가*(수요)와 *무엇이 안 되는가*(실패). Vercel 편은 앞쪽만 자동화했다.

> ⚠️ **이 페이지가 명시적으로 막으려 한 것이 그쪽에서는 열려 있다.** 여기서 *"하나의 잘못된 결과가 에이전트가 영원히 따르는 규칙으로 자동 설정되는 것을 방지"* 가 설계의 핵심이었는데, Vercel 편에는 그 게이트가 없고 **누가 증류된 스킬을 검토하는지 소스가 말하지 않는다.** 09-10 [[tech-bridge-agent-to-agent-as-search|Greze]]의 경고(*"한 번 오염되면 영원히 오염된다"*)가 그대로 적용되는 자리다.

## References

- [[tech-bridge-six-agent-skills]] — first-seen
- 관련: [[agent-skills]] · [[self-harness]] · [[harness-pruning]] · [[generator-evaluator-pattern]] · [[llm-coding-guidelines]]

## 세 번째 경로 — 성공한 긴 세션을 증류하고 옛 버전을 은퇴 (2026-09-24 · [[tech-bridge-oracle-agent-memory-harness]])

[[ignacio-martinez|Ignacio Martinez]]([[oracle|Oracle]])의 **스킬 승격(skill promotion)·워크플로 승격**:

> [승격한다면] 예를 들어, [스킬]이라면 (…) **증류를 통해 원본보다 더 나은 [skill.md]** (…) **이전 버전은 [은퇴시키고], 새 버전으로 업데이트** (36:47~37:04)

재료는 *"서너 시간 들여 하루 종일 성공시킨 워크플로"*(36:24~36:34), 결과는 **나의 어조·업무 방식·선호**가 들어간 스킬 — *"이 라이브러리가 마음에 든다, 이 DB 엔진이 버그가 적었다"*(37:04~37:29). 절차 기억의 예(프런트엔드 작업의 대화 전체 → 반복 가능한 워크플로, 24:33~24:54)도 같은 경로다.

| 패턴 | 무엇에서 | 무엇을 고치는가 | 승격 게이트 |
|---|---|---|---|
| task-observer (이 페이지) | **실패** 관찰 | 규칙·스킬 | **사람** |
| [[query-to-skill-distillation]] (Vercel) | **성공한 질의** 다수 | 새 스킬 추가 | 없음 |
| **스킬 승격 (Oracle)** | **성공한 긴 세션** 하나 | **기존 스킬을 새 버전으로 교체** | ⚠️ **말하지 않음** |

⭐ **버전 교체가 명시된 첫 사례** — 앞의 둘은 추가·수정이었고, 이것은 **옛 버전을 은퇴**시킨다. ⚠️ 그래서 이 페이지의 원칙(*한 번의 우연이 영구 규칙이 되면 오염*)이 가장 날카롭게 걸린다 — **세션 하나에서 증류한 스킬이 이전 버전을 덮어쓰는데, 회귀를 확인하는 [[skill-evals|eval]]이 없다.** ko는 *skill* 을 **"기술"**, *promote* 를 **"홍보"** 로 옮기고 **`skill.md` 라는 파일명을 지웠다**(36:49~36:56).

## 네 번째 경로 — 실패·반복·불만을 한 저장소의 세 칸으로 (2026-09-30 · [[tech-bridge-introspection-loop-is-the-product]])

[[roland-gavrilescu|Roland Gavrilescu]]([[introspection-dev|Introspection]]): *"Failure patterns should become judges and evals. Repeated behavior should become skills and prompts. User frustration, extensions and memories to your harness"*(06:09~06:17). 위 표의 경로들(실패 → 스킬 · 성공 질의 → 스킬 · 성공 세션 → 스킬 교체)이 **입력별로 다른 출력**을 갖는 한 표가 된다 — 실패는 스킬이 아니라 **judge·eval**로 간다는 점이 이 페이지(task-observer: 실패 → 스킬 개선)와 다르다. 승격 게이트는 **사람의 judge 보정 + 프로덕션 A/B**(14:45~15:48). ⚠️ 가상 예시·측정 없음. → [[agent-recipes]] · [[taste-encoded-evals]]

## 다섯 번째 경로 — 사람의 교정을 지켜보는 observer 에이전트 (2026-10-03 · [[tech-bridge-warp-factory-engineering]])

[[zach-lloyd|Zach Lloyd]]([[warp|Warp]])가 [[software-factory]]의 표준 루프로 든 **skill loop**: *"you're going to have your factory agents that are running skills, and then you'll have observer agents that are seeing how those skills are being applied, looking for issues and trying to improve the skills."*(14:06~14:17) 예 — 코드 리뷰 에이전트의 코멘트를 **시니어 엔지니어가 고치면**, *"you'd want an observer agent that would look at that and basically uh improve the code review agent for the next run."*(14:17~14:33)

구조는 이 페이지의 task-observer와 같지만 **신호가 다르다** — 에이전트 자신의 실패가 아니라 **사람이 결과물을 교정한 흔적**(diff)이 학습 재료다. 사람의 교정은 이미 일어난 리뷰의 부산물이라 **추가 라벨링 비용이 없다.** 공장에는 이것을 담을 **data plane**(*"lets agents remember what they've done, learn, um improve over time"* 13:01~13:11)이 있어야 한다고 한다. ⚠️ **승격 게이트를 말하지 않는다** — observer가 고친 스킬을 누가 검토하는지, 시니어 한 명의 취향이 영구 규칙이 되는 오염(이 페이지의 핵심 우려)을 어떻게 막는지 없다. 측정·사례도 없다.

## 여섯 번째 경로 — 사람의 리뷰를 회고하는 retro 스킬 (2026-10-09 · [[tech-bridge-pocock-pr-bottleneck]])

[[matt-pocock|Matt Pocock]]의 **retro**(retrospective) 스킬은 에이전트 세션 하나, PR + 세션, 또는 *"all of the PRs that we've done over the last week, all of the reviews"*(20:45~20:51)를 회고해 다음을 **제안**한다: 자동 검사 · coding standards 갱신(20:54~20:59) · **navigation pointers**(에이전트가 정보를 얼마나 쉽게 찾았나, AGENTS.md에 포인터를 둘 수 있나 21:21~21:29) · **tool economy**(더 토큰 효율적인 도구 21:31~21:38) · **bloat**(비대한 steering 파일·스킬 21:43~21:51).

| | 원천 | 반영 |
|---|---|---|
| task-observer (09-05) | 작업 중 실패 | 사람 검토 후 |
| observer 에이전트 (Warp, 10-03) | 사람의 교정 | — |
| **retro (이 소스)** | **사람의 코드 리뷰** | **제안** — 반영 절차는 발화되지 않음 |

목표는 복리 — *"by doing human review you're making the quality of the next human review higher"*(21:04~21:08). ⚠️ 화자 진술, *"It's amazing how many things this catches"*(21:38~21:40)에 측정 없음. retro가 v1.3에 포함되는지 미발화.

## 여섯 번째 경로의 두 번째 사례 — 세션 뒤 retro 스킬, 대상은 하네스 전체 (2026-10-09 · [[tech-bridge-rails-harness-engineering]])

[[joel-quenneville|Joël Quenneville]]의 **retro 스킬**은 긴 세션이 끝난 뒤 사람이 직접 돌린다 — *"it analyzes my history and suggests automations that I can do"*(29:22~29:29). 스킬이 묻는 질문은 사람의 회고 질문을 묶은 것이다: 어디서 개입했나 · 어떤 신호가 빠졌나 · 손으로 복사한 것 · AGENTS.md에서 결정론으로 옮길 것 · 대화가 열화했나, 나눌 수 있었나 · 반복되는 실수(28:47~29:09). 대상이 **스킬 자체**가 아니라 **하네스 전체**(훅·cop·제너레이터·스크립트)라는 점이 앞의 경로들(Pocock의 retro 포함 — Pocock 편은 standards·포인터·도구까지 넓히지만 출발점은 리뷰)과 다르다. 반영은 사람이 고른다(*"suggests"*). Matt Pocock도 *"I think last week"* 같은 이름(*Retro*)의 스킬을 냈다고 한다(29:41~29:49) — 통합 메모: 바로 위 [[tech-bridge-pocock-pr-bottleneck]] 섹션이 그 스킬이다(같은 회차에 들어옴). 트리거 질문은 *"how could this be the last time?"*(28:20~28:26).

## 일곱 번째 경로 — 개선 대상이 워크플로 그래프 (2026-10-09 · [[tech-bridge-goodbye-slop-state-machines]])

[[david-khourshid|David Khourshid]]: 상태 머신을 *"a durable artifact"* 로 삼아 트레이스(실제·시뮬레이션 사용자, 도그푸딩)와 단계별·전체 eval을 붙여 에이전트에게 *"Please propose some changes to this agent."*(12:44~13:15). 개선안을 내는 쪽은 *"Not the exact same agent, but a different agent"*(16:17~16:23), 검증은 같은 시나리오를 V1·V2에 돌려 비교(16:36~16:46). 앞의 경로들이 **스킬 텍스트**를 고친다면 이 경로는 **상태·전이 그래프**를 고친다 — diff가 *"화살표"* 단위로 읽힌다(*"you cannot draw arrows in paragraphs"* 11:39~11:42). ⚠️ V1→V2는 1회 시연·체감, Stately 내부 적용 결과 미공개. → [[agent-state-machine]]

## 여덟 번째 경로 — 실제 행동(ground truth)과 대조하는 두 번째 자동화 (2026-10-11 · [[tech-bridge-cooking-with-codex]])

[[gabriel-chua|Gabriel Chua]]([[openai|OpenAI]], 56:06~56:43): ① **매주 금요일** 대화 스레드를 훑어 *"are there skills that you could improve? Are there like things you could add to the agents markdown or are there skills you could just remove? maybe skills that you haven't been using."* ② 이메일 초안 자동화 옆에 *"a second automation that sort of cross validates against the eventual reply you send because that is the ground truth. Then it updates like a markdown file with the best practices"* → *"the email drafting automation can get better over time."*

- ②는 이 페이지의 기존 경로들(사람 교정 관찰·retro 스킬)과 달리 **사람이 실제로 보낸 결과물 자체를 정답으로 쓴다** — 교정 행위를 따로 기록할 필요가 없다.
- ①은 **삭제**까지 포함한다 → [[harness-pruning]].
- 같은 소스 Charlie(추정): 어려운 대화의 끝은 *"make this a skill or even better make this a plugin"*(12:41~12:48) → [[query-to-skill-distillation]]
- ⚠️ 사람 게이트 유무는 발화되지 않는다(마크다운 파일 자동 갱신으로 들린다).

## 아홉 번째 경로 — 트레이스 분석 엔진이 원격 스킬 파일을 고친다, 게이트는 메모리 종류로 (2026-10-12 · [[tech-bridge-langchain-learning-agent-memory]])

[[langsmith|LangSmith]]의 분석 엔진이 트레이스(실패한 도구 호출·사용자 정정·말투 이탈 플래그)에서 패턴을 찾아 *"identifies where different static skill markdown files that are based in Contexthub need to be changed or promoted and it'll make that change"*(12:04~12:13). 같은 발표의 교훈 3은 **procedural 메모리(지시·정책·말투 규칙) 변경은 커밋 전에 사람에게 보이고 eval로 보호**하라고 한다(14:23~14:55) — 이 페이지의 *자동 반영하지 않는다* 원칙을 **메모리 종류 기준**으로 다시 말한 것. ⚠️ 데모 구간(*"it'll make that change"*)과 교훈 3의 게이트가 어떻게 연결되는지는 발화되지 않는다. ⚠️ 벤더(LangChain) 당사자 진술. → [[trace-to-memory-loop]]

## 열 번째 경로 — 성공·실패 트레이스를 증류해 전사에 배포, 게이트는 자동 검사뿐 (2026-10-13 · [[tech-bridge-runlayer-self-improving-skills-mcp]])

[[rafal-wilinski|Rafal Wilinski]]([[runlayer|Runlayer]]): *"we just take that trace and we ask frontier LLM to simply distill a skill"*(11:32~11:41). 실패 실행도 재료로 쓴다 — *"every run or or pass or fail just feeds our distiller mechanism"*(12:07~12:14). 그리고 ⭐ *"it all happens completely autonomously asynchronously without human in loop"*(12:29~12:33). 조직 단위에서는 *"various series of checks like whether it's not containing some kind of prompt injection or maybe PII"*(15:18~15:27)를 거쳐 MCP gateway로 **회사의 모든 클라이언트·에이전트**에 배포한다 → [[run-trace-skill-distillation]] · [[mcp-skill-distribution]]

| | 원천 | 반영 | 반경 |
|---|---|---|---|
| task-observer (09-05) | 작업 중 실패 | 사람 검토 후 | 프로젝트 |
| LangChain (10-12) | 트레이스 | procedural은 사람·eval | 한 에이전트 |
| **Runlayer (이 소스)** | **성공 + 실패 트레이스** | **자동 검사만** | **전사** |

> ⚠️ **Contradiction:** 이 페이지의 원칙(*"하나의 잘못된 결과가 에이전트가 영원히 따르는 규칙으로 자동 설정되는 것을 방지"*)을 **명시적으로 버린** 첫 경로다. 앞의 경로들은 대부분 게이트에 대해 *말하지 않았을* 뿐인데, 이 소스는 게이트를 두지 않는다고 *말한다.* 회수·롤백·[[skill-evals|회귀 eval]]은 발화되지 않았다. 근거로 든 36% → 100%는 단일 태스크이고 실행 횟수가 발화되지 않았다. Voyager skill library를 계보로 명시한 첫 소스이기도 하다.

- (2026-10-15 · [[tech-bridge-horthy-state-of-software-factory]]) [[dex-horthy|Horthy]]의 "12 factor factories" 마지막 항목: *"compound over time, learn from past sessions, go read what your engineer go analyze the sessions of your team, figure out what they're struggling with, figure out how to get that into your skills or your memory or whatever it is."*(12:58~13:08) — 개인이 아니라 **팀 세션**이 재료. 그리고 그 세션을 보관할 *"system of record"*(13:53~14:01)가 도구 쪽 전제다 → [[agent-platform-layers]].

## /retro — 다음 작업의 환경을 고치되, 너무 자주 돌리지 않는다 (2026-10-25 · [[tech-bridge-pocock-skills-implement-spec-pr-retro]])

[[matt-pocock|Matt Pocock]]의 /retro를 소개한 편이다(발췌, 화자 추정 [[eric-tech|Eric Tech]]). 에이전트가 맞는 정보를 찾느라 오래 걸리면 *"a list of key files on exactly where they are and how to find them more quickly"* 를 담은 파일(*"AGMD"*, 판독 불가)을 만든다(04:08~04:17). 해설은 고칠 대상을 둘로 나눈다. 기계가 확인할 수 있는 실수는 자동 검사로, 판단이 필요한 기준은 사람이 읽는 규칙으로 보낸다.

> ⚠️ **빈도의 비용.** 해설: *"회고를 계속 자동으로 돌리면 기능보다 정리 작업만 늘어날 수 있어요."*(04:40~04:47) 이 페이지의 다른 사례들은 관찰을 상시화하고 반영만 사람이 거른다. 이 경고는 **실행 빈도 자체**를 비용으로 본다. 원음 근거는 없다(해설).

## 주간 작업 과정 점검 — 조회수 대신 새는 시간 (2026-10-26 · [[tech-bridge-chieng-lee-ai-video-production]])

코딩이 아니라 영상 제작 사례다. 해설: *"이번 주에 어디서 오래 걸렸는지, 매번 같은 수정을 한 곳은 어디인지 물어보는 거예요."*(06:40~06:46) 강연에서 찾은 문제는 *"보지 않는 곳으로 알림이 가거나 필요가 없어진 검사를 계속하던"* 것이었다. 원음([[cova-lee|Cova Lee]] 추정): *"we don't have a lot of time to kind of look back and go through all of our processes and understand inefficiencies."*(07:18~07:25) 전날 [[tech-bridge-pocock-skills-implement-spec-pr-retro|/retro]]가 *매 작업 뒤* 라면 이쪽은 **주 단위**다. 앞 절의 빈도 경고와 맞닿는다. 해설의 맺음은 *"결과를 고친 이유까지 남겨 두는"* 것이다(08:51~08:54).

## North Star로 남겨 둔 판본 — 에이전트가 eval 포인트를 스스로 만든다 (2026-10-30 · [[tech-bridge-harrison-chase-agent-improvement-loop]])

[[harrison-chase]](추정)는 *"the agent like notices that it made a mistake. The agent goes, creates an eval data point of its own, suggests its own changes"*(06:37~06:43)를 컨텍스트 · 하네스 코드 · 모델 가중치 모두에 대해 그리지만 *"very much a North Star vision"*(06:52~06:54)이라 못 박는다. 막는 것은 만능 정답 판정기의 부재다 → [[production-trace-eval-flywheel]].

## 사람이 실제로 보낸 것과의 diff — "review mode only" (2026-10-31 · [[tech-bridge-dan-martell-grokbot-daily-automation]])

[[dan-martell|Dan Martell]](⚠️ 추정)의 [[grokbot|Grok Bot]] inbox manager 팁. 처음 몇 주는 *"have it draft everything"*(02:22~02:24), 이후 *"Every Friday, compare the drafts you wrote to this week's of what I actually sent. Look at what I changed, like the words I cut, how long my replies are, and how I sign off, and update how you write emails for me, so next week's drafts need fewer edits."*(02:26~02:40) — *"I call this review mode only."*(02:40)

- 이 페이지의 다른 경로들은 실패 · 트레이스 · eval을 신호로 썼다. 여기서는 **사람이 고쳐서 실제로 보낸 결과물**이 정답이고, 초안과의 차이가 곧 피드백이다. 별도 평가 단계가 없다.
- 반영 대상은 스킬 파일이 아니라 봇의 *"how you write emails for me"* 다. 사람 승인 단계는 따로 없지만, 초안이 밖으로 나가지 않으므로 [[no-silent-write]]처럼 **보내는 행위는 늘 사람**에게 남는다.
- 같은 영상의 *"Do it once, save it as a skill"*(06:14~06:16)과 작업 녹화 → 스킬(06:16~06:24)은 스킬의 **생성** 경로다. 개선 루프는 아니다.

> ⚠️ 편집량이 실제로 줄었는지는 발화되지 않는다. 1인 사용 팁.
