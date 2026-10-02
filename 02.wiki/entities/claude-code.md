---
title: Claude Code
type: entity
category: product
tags: [anthropic, agent, cli, coding-agent]
aliases: [클로드 코드]
sources: [anthropic-claude-code-auto-mode, anthropic-managed-agents, multica-karpathy-skills-claude-md, anthropic-dynamic-workflows, lum1104-understand-anything, charlychoi-claude-code-best-practices, tech-bridge-impeccable-design-steering, tech-bridge-graft-code-knowledge-graph, tech-bridge-vercel-eve-filesystem-agent, tech-bridge-rlhf-assistance-vs-automation, tech-bridge-lopopolo-agent-harness, tech-bridge-jensen-huang-cbs-interview, tech-bridge-sdd-full-course, tech-bridge-agents-vs-humans-optimizer-speedrun, tech-bridge-skill-engineering-dark-arts, tech-bridge-anthropic-dreaming-memory, tech-bridge-sdd-enterprise-lessons, tech-bridge-conductor-orchestras-not-factories]
links:
  - https://code.claude.com/docs
created: 2026-05-25
updated: 2026-10-02
---

# Claude Code

[[anthropic|Anthropic]]의 공식 coding agent CLI. 본 위키 운영 환경 자체. 터미널·VS Code·JetBrains·웹 등에서 동작하고, 파일 편집·shell·subagent를 다룬다.

## 위키에서 알려진 사실

- **Permission modes** ([[anthropic-claude-code-auto-mode]]):
  - 기본: 매 action마다 사용자 승인. 실측 93% 승인.
  - Sandbox 모드 — 안전하지만 high-maintenance
  - `--dangerously-skip-permissions` — zero-maintenance, 무방비
  - **Auto mode** (2026 신규) — model-based classifier로 위험 행동만 차단 ([[transcript-classifier]])
- Auto mode는 [[claude-sonnet-4-6|Sonnet 4.6]] 기반 classifier + 서버측 prompt-injection probe로 구성
- Auto mode 진입 시 blanket shell / 인터프리터 / 패키지 매니저 run 룰은 drop (broad escape 방지)
- [[anthropic-managed-agents|Managed Agents]]는 Claude Code 같은 범용 harness를 한 형태로 수용하는 "메타-하네스"
- [[anthropic-harness-design-long-running-apps|harness design 연구]]는 Claude Code의 다중 에이전트 후속 형태로 볼 수 있음
- **System prompt 가이드라인** ([[llm-coding-guidelines]]): CLAUDE.md 헤더로 over-engineering·scope creep·weak success criteria 같은 *선의의 과잉 행동*을 줄임. [[anthropic-claude-code-auto-mode|auto mode]]가 *권한 게이트*로 위험 행동을 차단한다면, 본 가이드라인은 *프롬프트*로 작업의 질을 잡는 보완 layer. 사례: [[multica-karpathy-skills-claude-md]] (4원칙)
- **[[dynamic-workflows|Dynamic workflows]]** (2026 신규, research preview): Claude가 오케스트레이션 스크립트를 동적으로 작성해 한 세션에서 10s~100s parallel subagent를 돌리고 검증 후 수렴. 진입은 직접 요청 또는 **[[ultracode]]** 세팅(effort=xhigh + workflow 자동 판단). 토큰 소모 大, 최초 1회 확인. 사례: [[bun|Bun]] Zig→Rust 포팅 ([[jarred-sumner|Jarred Sumner]], [[anthropic-dynamic-workflows]])
- **플러그인 생태계**: 마켓플레이스로 서드파티 플러그인 설치 (`/plugin marketplace add <repo>` → `/plugin install`). 사례: [[understand-anything|Understand-Anything]] ([[lum1104-understand-anything]]) — 코드베이스를 [[code-knowledge-graph|지식 그래프]]로 만드는 멀티 에이전트 플러그인. Claude Code는 이런 도구들의 네이티브 호스트.

## 실무 운영 계약

[[charlychoi-claude-code-best-practices]]는 공식 best practices를 **목표 + 맥락 + verifier + permission + review**의 task contract로 재구성한다.

1. 복잡한 작업은 Explore → Plan → Implement → Verify → Review로 분리한다.
2. 완료는 설명이 아니라 test·build·typecheck·screenshot 같은 executable evidence로 판정한다 ([[verifiable-goals]]).
3. 항상 필요한 짧은 project rule은 `CLAUDE.md`, 특정 업무는 Skills, 강제 규칙은 Hooks, 외부 연결은 CLI/MCP에 둔다 ([[harness-engineering]]).
4. unrelated task는 `/clear`, 조사·review는 subagent, 대량 변경은 소수 pilot 후 fan-out해 context와 blast radius를 관리한다.

## Internal incident log 예시 (Anthropic 공개)

- 원격 git 브랜치 삭제 (오해된 지시)
- GitHub auth 토큰을 내부 컴퓨트 클러스터에 업로드 시도
- 프로덕션 DB 마이그레이션 시도

이런 사례들이 [[agentic-misbehavior]] 분류와 auto mode 설계 motivation의 근거.

## 만드는 팀의 사용기 (2026-09-05 ingest · [[tech-bridge-claude-code-team-workflow]])

Claude Code 팀 엔지니어 3인이 자기 도구를 어떻게 쓰는지 증언했다.

- **[[claude-tag|Claude Tag]]** — Slack 네이티브 에이전트. 팀 업무의 **70~80%** 가 여기서 일어난다. Slack을 고른 이유는 UI가 아니라 **맥락**이다 — 팀이 제품에 대해 내린 *"모든 결정들"* 이 이미 거기 있다.
- **routine** — 클라우드 컨테이너에서 도는 정기 작업. 예: *"매일 우리가 받는 **모든 피드백을 살펴보고 중요도에 따라 분류**한 다음, 실제로 해결할 가능성이 높은 문제부터 해결."*
- **workflows** — 에이전트가 서브에이전트 오케스트레이션 코드를 직접 쓴다. 신뢰의 근거가 고전적이다 — *"이 항목들을 순회하는 **for 루프**를 작성할 때 (…) '아, 맞다. **for 루프는 항목 중 하나라도 건너뛰지 않겠구나**'."*
- **기능은 지워진다** — todo 리스트는 Sonnet 3.5의 장기 시야 부족을 메우려 만들었고 1년 뒤 *"마치 사라진 것처럼"* 됐다. AskUserQuestion은 HTML 아티팩트에 밀렸다. → [[harness-pruning]]
- 지난 1년의 추가분을 팀이 이렇게 요약한다 — *"Claude Code로 시작해서 **자동 모드, 메모리, workflow** 같은 기본적인 기능들을 추가해 나간 것."*
- ⚠️ 자막에 미해소 토큰 **"2E"** 가 나온다(*"open up the 2E or the desktop app"*). Claude Tag 바깥의 직접 조작 표면을 가리키지만 확장형은 확정하지 않는다.

## 계층적 CLAUDE.md 상속 (2026-09-05 · [[tech-bridge-six-agent-skills]])

> Claude Code는 프로젝트 내의 `CLAUDE.md`와 **그 상위 폴더에 있는 모든 `CLAUDE.md`를 읽습니다.**

[[ai-labs]]가 이 성질로 **중간 스코프**를 만든다 — 모든 프로젝트를 담는 "개발자 폴더" 하나에 `CLAUDE.md`를 두어 공통 규칙을 상속시키되, *"컴퓨터의 **다른 부분에서 실행되는 관련 없는 세션에는 적용되지 않도록**"* 한다. 전역(`~/.claude`)과 프로젝트별 사이의 빈자리를 디렉터리 계층으로 메운 것이다. → [[llm-coding-guidelines]]

## 디자인 스킬의 호스트, 그리고 "Claude 베이지" (2026-09-12 · [[tech-bridge-impeccable-design-steering]])

- [[impeccable|Impeccable]](디자인 스킬)이 *"모든 하네스에서 동작"* 하는 목록의 첫 자리 — Claude Code, GitHub Copilot, [[cursor]], [[codex]]. ASR은 *"cloud code"* 였으나 하네스 목록 문맥이라 **Claude Code로 확정**(09-11 Google Cloud 편의 *"Cloud Code"* 판정 불가와 다른 처리).
- [[paul-bakaus]]가 지금의 [[ai-slop|슬롭]]을 **"Claude 베이지"**(Instrument Serif·이탤릭)라 부른다 — *"꼭 나쁜 디자인은 아니다, 그냥 전부 그렇게 생겼을 뿐."* 그리고 섹션 번호를 *"GPT가 아주 좋아하고 Claude도 좋아하는"* 흔적으로 든다. ⚠️ 이 관찰의 대상은 *"Claw Design"*(Claude Design 추정)의 기본 출력이며 Claude Code 자체의 평가는 아니다.

## 외부 증언 — 파일 시스템 에이전트의 원형으로 (2026-09-19 · [[tech-bridge-vercel-eve-filesystem-agent]])

[[vercel|Vercel]]의 [[andrew-qu|Andrew Qu]]가 **자사 에이전트를 세 번 실패한 뒤** Claude Code를 보고 무엇을 바꿨는지 공개했다. **이 위키가 받은 Claude Code에 대한 가장 구체적인 제3자 증언**이다 — 그동안의 서술은 대부분 [[anthropic|Anthropic]] 자신의 것이었다.

> 우리는 옆에서 **"와, [Claude Code]와 [[claude-opus-4-5|Opus 4.5]]는 우리가 이전에 가지고 있던 것과 비교하면 거의 인공 일반 지능(AGI)이나 다름없네."** 라고 생각했습니다. 우리가 직접 개발한 에이전트와는 달리, **이 에이전트는 거의 모든 질문에 막힘없이 답해줬습니다.** (07:38~07:53)

그가 **무엇이 달랐는지** 로 지목한 것:

> **핵심은 바로 파일 시스템이었다** … **최소한의 도구 세트, 즉 파일 목록 보기, 파일 읽기, bash 실행 정도만** … 하지만 가장 중요한 것은 **에이전트가 잘 훈련된 도구를 활용할 수 있었고 필요한 곳에 스스로 탐색하고 작업을 작성할 수 있었다**는 점입니다. **[Claude Code]에 매우 구체적인 도구 세트를 제공하지 않았습니다.** 마치 **자유롭게 탐색하고 새로운 행동(emergent behavior)을 발견하도록 내버려 둔 것**과 같았습니다. (07:53~08:28)

→ [[file-system-agent]]

그리고 **도약을 두 단계로 센다** — 단일 에이전트 → **[[claude-agent-sdk|Claude Code SDK]]** → 자기 용례에 맞춰 바닥을 다시 깐 파일 시스템 에이전트(09:04~09:09). 즉 SDK를 그대로 쓰는 것과 **원리를 가져와 자기 바닥을 까는 것**을 구분한다. 결과는 *"eval 점수 두 배"*(⚠️ 실체 없음).

Claude Code는 이 소스에서 **비교 기준점으로도** 쓰인다 — 베타 고객 Aura가 *"기성품 Claude 코드를 쓰는 것과 달리"* [[eve-framework|Eve]]로 처음부터 구축했다는 대목(14:15~14:26, ⚠️ 수치 없음).

⚠️ en-orig가 *Claude Code* 를 **"Cod code"** 로 반복 오인식했고 ko가 일부 자리에서 *Claude* 를 떨어뜨렸다 — raw 헤더 참조.

## 2026-10-02 — 엔터프라이즈 SDD 데모의 실행기, 거의 빈 CLAUDE.md ([[tech-bridge-sdd-enterprise-lessons]])

[[simon-martinelli|Simon Martinelli]]가 Spring PetClinic 역설계 스펙에 *implement* 한 마디로 의사 목록 화면을 만든다(약 1분 30초, ⚠️ 화자 진술 22:09~22:12). 도구명은 en-orig ASR *"flow code"*(15:47) — 설명란 해시태그 *#ClaudeCode* 로 판독. *"I don't run it here inside the ID[=IDE]. That's just for for demo purposes"*(15:52~15:56). CLAUDE.md는 *"has not much inside"*, 아키텍처·패키지 구조·도구 가이드라인을 **참조**만 하고 *"most of the things are in the skills"*(16:06~16:34). 근거로 ETH Zurich 연구를 들며 *"it's maybe even better to have none of those files than a big one"*(23:20~23:23) — ⚠️ 연구명·수치 미발화. 스킬 공유의 문제로 *"not everybody in the organization is maybe using the same agent"*(15:42~15:47). → [[ai-unified-process]] · ⚠️ ko는 CLAUDE.md를 **"DMD 흐름"**(16:07)으로 옮겼다.

## References

- [[anthropic-claude-code-auto-mode]]
- [[anthropic-managed-agents]]
- [[anthropic-harness-design-long-running-apps]]
- [[anthropic-dynamic-workflows]]
- [[multica-karpathy-skills-claude-md]]
- [[lum1104-understand-anything]]
- [[charlychoi-claude-code-best-practices]]
- [[tech-bridge-claude-code-team-workflow]]
- [[tech-bridge-six-agent-skills]]
- [[tech-bridge-ai-native-sdlc]]

## 학습 패러다임으로 분류된 첫 비판 (2026-09-20 · [[tech-bridge-rlhf-assistance-vs-automation]])

이 페이지의 평가는 지금까지 전부 **도구로서의 평가**였다 — 09-19 [[tech-bridge-vercel-eve-filesystem-agent|Vercel 편]]은 *"우리 것에 비하면 거의 AGI"* 라며 **모범**으로 삼았다. [[diogo-almeida|Diogo Almeida]](GPT-4·ChatGPT·InstructGPT 공동 저자)는 **품질이 아니라 시대 구분으로** 비판한다.

발표의 힌트가 제목부터다:

> **[이것이] 클로드 코드[Claude Code] 시대는 아니라는 것**입니다. … **저는 실제로 그들이 같은 시대의 것이라고 생각합니다.** (00:26~00:46)

근거:

> **[Claude Code]는 여전히 보조의 시대에 속하기 때문에 답이 아닙니다. [Claude Code]는 여전히 [[rlhf|RLHF]]이고, 만약 순수하게 RLVR이었다면 지금과는 매우 다른 모습이었을 것입니다.** (08:54~09:10)

> **[Claude Code] 같은 것의 일은 단순히 코드를 작동시키는 것만이 아닙니다.** 대화 방식이 완전히 다를 거예요. **목표는 그 안에 있는 사람을 만족시키는 것입니다.** (04:25~04:43)

그리고 **실사용자가 관찰해 온 현상에 설명을 붙인다**:

> **어떤 때는 에이전트 작업은 정말 잘 해내지만, 정작 사용자가 원하는 바를 따라가지 못하는 경우가 있죠.** 이것은 **끊임없이 춤을 추는 최적화 공간에서의 절충안**과 같습니다. **하지만 이 두 가지 절충 관계 어느 쪽도 자동화 요소에는 아무런 도움이 되지 않습니다.** (09:10~09:24)

→ [[assistance-vs-automation]] · [[post-training-northstars]]

**이 위키가 이 도구에 대해 받은 가장 이론적인 비판**이고, 주장의 형태가 특이하다 — **제품을 더 잘 만들어도 이 천장은 남는다**는 것이다.

> ⚠️ **화자는 같은 발표에서 *"솔직히 말해서 저는 Claude Code를 좋아합니다. ChatGPT도 좋아하고 계속 쓸 겁니다"*(11:14~11:16)라고 말한다.** 이 비판은 **제품 평가가 아니다.**
>
> ⚠️ **화자는 "제3의 길"을 파는 스텔스 회사 소속**이고, RLVR이었다면 어떻게 달랐을지에 대한 근거는 제시되지 않는다.
>
> ⚠️ **ko 자막이 제품명을 "클로드 코드"와 "클라우드 코드" 두 갈래로 옮긴다**(en-orig가 *cloud code* 로 오인식). 09-19 Vercel 편에서 기록한 **같은 유형이 하루 만에 재발**했다.

→ [[tech-bridge-rlhf-assistance-vs-automation]] · [[diogo-almeida]] · [[rlhf]] · [[assistance-vs-automation]]

## Google 에피소드가 부른 "가장 인기 있는 하네스" (2026-09-23 · [[tech-bridge-lopopolo-agent-harness]])

빌리가 *"현재 가장 인기 있는 에이전트 하네스는 Google [Antigravity], [Claude Code], Cursor"*(24:24~24:28)라 하고, *"매끄러운 느낌을 주는 이유는 모델 자체 때문이 아닙니다 (…) 모델들을 둘러싼 하네스 엔지니어링"*(24:56~25:03)이라 한다. [[google-skills|Google Skills]]도 호환 하네스로 Claude Code를 든다(29:39~29:48). ⚠️ **이름이 양 트랙에서 또 깨졌다** — en-orig *cloud code* → ko **"Cloud Code"·"클라우드 코드"**(24:28·29:43). 09-20·09-21에 이어 **세 번째**. 영상 **제목에는 Claude Code가 옳게** 있다.

## 하드웨어 공급자의 사내 사용 목록 (2026-09-25 · [[tech-bridge-jensen-huang-cbs-interview]])

[[jensen-huang|Jensen Huang]](NVIDIA CEO)이 CBS 인터뷰 첫 답변에서 사내 사용 도구를 나열한다 — *"OpenAI의 최신 Astra (…) 어디에서나 사용하고 있습니다. **우리는 [Claude Code]를 사용합니다.** 우리는 [Cursor]를 사용합니다 (…) 우리는 [Cognition]을 사용합니다."*(01:09~01:21). 09-06 G20의 *"Anthropic, OpenAI, Cursor 같은 기성 AI"* 가 **제품명**으로 갱신됐다. ⚠️ 규모·용도는 없다. ⚠️ **이름이 양 트랙에서 또 깨졌다** — en-orig ASR부터 *"cloud code"*, ko **"클라우드 코드"**(01:16). 09-20·09-21·09-23에 이어 **네 번째**.

## SDD 강좌의 시연 에이전트 (2026-09-27 · [[tech-bridge-sdd-full-course]])

[[jetbrains|JetBrains]] 협업 스펙 주도 개발 강좌가 **WebStorm + Claude Code**로 전 과정을 시연한다(13:28~13:36). 강좌가 짚은 기능:

- **AskUserQuestion 도구** — 헌법·기능 스펙 인터뷰에서 프롬프트로 직접 부른다. *"This tool is totally optional, but we just like the way it looks in the interface."*(17:32~17:35)
- **권한 확인** — 명령마다 확인을 묻는다, *"unless you start Claude Code in an unsafe mode"*(14:17~14:25). *"The ultimate responsibility for the code is yours."*(14:30~14:32) 세션 단위 일괄 승인은 보안 트레이드오프를 감수할 때만(18:42~18:49).
- **`/clear`** — 구현 전·기능 사이마다 컨텍스트를 비운다(23:37~23:41, 36:52~36:55).
- **skill creator와 global skills** — changelog 스킬을 만들자 **global skills area**에 두었고 곧바로 그 스킬로 changelog를 생성했다(34:57~35:09).
- **plugins** — *"a collection of agent extensions that can be installed and updated"*(54:16~54:23), ⚠️ 아직 에이전트 간 표준이 아니고 코드를 실행하므로 신뢰를 확인하라(54:31~54:42).
- 강좌는 Claude Code를 **여럿 중 하나**로 둔다 — 같은 스킬을 [[codex|Codex]]로 옮겨 돌리고(57:45~57:53), ACP registry로 OpenCode를 붙인다.

## 장시간 자율 연구 에이전트로 — 9~10시간마다 멈춘 쪽 (2026-09-28 · [[tech-bridge-agents-vs-humans-optimizer-speedrun]])

[[prime-intellect|Prime Intellect]]가 Claude Code(Opus — ⚠️ 버전은 en-orig *1.8*, en·ko *4.8* 로 미확정)를 optimizer speedrun에 풀었다. 화자가 *"honestly very painful to work with"*(07:34~07:36)라 부른 행동:

> *"Claude Claude code keeps stopping every 9 or 10 hours and basically said, "Yeah, I cannot improve the record. It's too hard for me. There is no way to to go beyond it.""* (07:36~07:46)

*"계속해, 새 방향을 탐색해"* 라고 하면 다시 10시간 — 결과적으로 **시간의 약 1/3을 놀았다**(08:00~08:04, 화자가 모니터링할 수단이 없었으므로). 그 밖의 관측:

- scratchpad는 적게, **이모지와 함께 새 기록에 흥분**(09:01~09:07). 서브에이전트·compaction은 Codex보다 훨씬 적다(compaction은 전체 실행에 ~1회, 09:55~10:01).
- **그런데 성적은 최고** — 당시 최고 기록 2,990 step을 **50~60 step 앞섰고**(11:05~11:15), 초반이 특히 빨랐다(10:34~10:39). 재시작 때 **인간의 새 기록을 가져와 개선**했다(10:50~10:56).
- 6일 실험에서도 *"once again very good"*(12:57~12:59), **점진적** 개선. 단 **max mode에선 토큰을 훨씬 많이** 쓴다(13:39~13:41).
- **논문 검색이 가장 활발했고, 다른 모델이 못 찾은 논문으로 최고 결과**(14:04~14:17).

> ⚠️ **포기가 모델 성향인지 하네스(goal.md 방식)·설정 탓인지는 소스가 가리지 않는다.** 단일 실험이다. 이 위키의 [[reward-hacking]] 사례(막히자 답을 찾아 나간 평가 에이전트)와 **막혔을 때의 반응이 정반대**라는 점만 기록한다. ⚠️ en-orig ASR은 또 *"Cloud Code"*(05:32·05:41) — 제목·설명란은 옳다. → [[automated-ai-research]]

## 2026-09-28 — 스킬 배포자가 본 Claude Code의 하네스 동작 ([[tech-bridge-skill-engineering-dark-arts]])

[[paul-bakaus]]([[impeccable|Impeccable]])가 여러 하네스용으로 스킬을 컴파일하며 관찰한 것(화자 진술, 시점 미확정) → [[cross-harness-skill-compilation]]:

- **서브에이전트를 스킬이 프로그래밍적으로 쉽게 띄운다**(41:08~41:13) — Codex는 사용자 요청 필요.
- **AskUserQuestion** — *"one of the coolest tools"*(41:33~41:41).
- **백그라운드 작업이 끝나면 모델이 자동으로 깨어난다**(42:52~43:00) — Impeccable 라이브 모드가 이것에 기댄다.
- **스킬 디렉터리를 가리키는 환경 변수**가 있다 — *"no other harness supports this right now I believe"*(22:52~23:04).
- **자기 작업을 자기가 리뷰하면 높게 매긴다**(Codex와 공통, 08:02~08:08).
- ⚠️ **마켓플레이스** — *"the claude code one for sure doesn't work particularly well"* — 업데이트가 안 되고 캐싱 문제(1:02:38~1:02:50). *"Anthropic[] has still not adopted agents.md"*(40:51~40:54).

## 2026-10-01 — CLAUDE.md가 컨텍스트 엔지니어링 1년의 출발점으로 ([[tech-bridge-anthropic-dreaming-memory]])

[[anthropic|Anthropic]] 응용 AI 팀의 [[lamis-mukta|Lamis Mukta]]가 지난 1년의 타임라인을 *"these Claude MD files that we launched with Claude code"*(03:34~03:36)에서 시작한다 — *"kind of unreasonably effective"*(03:39~03:40), 그러나 세션 시작에 주입하니 길어질수록 *"context bloat"*(04:14~04:16). 이어 memory tool → 스킬 → 파일 시스템 메모리로 간다(→ [[context-engineering]]). 인밴드 메모리의 예로도 Claude Code를 든다 — 새 세션은 *"largely like focusing on that specific context"*(15:18~15:24). → [[agent-dreaming]]. 청중이 *"the cla code leak and the memory stuff. The dreaming stuff"*(28:38~28:41)를 언급하지만 무엇인지는 발화되지 않는다 — ⚠️ 이 위키는 연결하지 않는다. ⚠️ ko는 25:06에서 CLAUDE.md를 **"클로드 의학박사"** 로 옮겼다.

## 2026-10-02 — Conductor를 낳은 도구, 그리고 "매일 인턴 귀에 속삭이는 말" ([[tech-bridge-conductor-orchestras-not-factories]])

- **제품 기원**: [[conductor|Conductor]] 팀은 *"we were such power users of cloud[=Claude] code back in February of last year that we uh started building our whole workflow around cloud code and we started cloning our repo five times and then we discovered work trees"*(02:14~02:26) — Claude Code 여러 개를 병렬로 돌리던 사용 패턴이 멀티 에이전트 관리 앱이 됐다.
- **CLAUDE.md = 슬롭 없는 구역**: *"if you had a a new intern (…) you had the opportunity to like whisper something in their ear every time they started working (…) And this is what the cloud MD or agents uh MD is."*(06:28~06:49) 최고 빌더들은 *"put an unusual amount of time into the CloudMD or their skill files"*(06:17~06:23). → [[slop-free-zone]]

⚠️ en-orig는 Claude Code·CLAUDE.md를 일관되게 *"cloud code"*·*"cloud MD"* 로 들었고 ko는 *"클라우드 코드"*·*"클라우드 MD"*.
