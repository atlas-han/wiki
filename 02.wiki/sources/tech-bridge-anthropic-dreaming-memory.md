---
title: "Tech Bridge — 자는 동안 스스로 학습하는 AI (Anthropic · Lamis Mukta): 컨텍스트 엔지니어링 1년 회고와 아웃오브밴드 메모리 정리 'dreaming'"
type: source
tags: [context-engineering, agent-memory, dreaming, continual-learning, claude-md, agent-skills, file-system-memory, concurrency, versioning, permissions, managed-agents, anthropic, video]
source-url: https://www.youtube.com/watch?v=sINXtw4wmyM
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 [[lamis-mukta]] ([[anthropic|Anthropic]] 응용 AI 팀 — 자막엔 "Lamis"만, 성은 설명란) · AI DevCon(자막 00:04, 설명란 링크상 Tessl 행사로 보임 — 촬영일 미확정)
date-published: 2026-09-30
ingested: 2026-10-01
created: 2026-10-01
updated: 2026-10-01
---

# Tech Bridge — 자는 동안 스스로 학습하는 AI (Anthropic · Lamis Mukta)

[[tech-bridge|Tech Bridge]]가 재배포한 **31:27 발표 + Q&A**(공식 챕터 없음). 화자는 [[anthropic|Anthropic]] 응용 AI 팀(*"a team which sits between research, product and go to market"* 00:23~00:27)에서 스타트업·창업자를 맡는 [[lamis-mukta|Lamis Mukta]]. 이 위키에 **dreaming이 처음으로 구조째 들어왔다** — 지금까지는 [[token-roles]](09-01)·[[strategy-primitives]](09-18)에서 *역할 이름*과 *"Managed Agents에 기본 제공"* 이라는 말뿐이었다. → [[agent-dreaming]] (신규)

> **메모리를 파일 시스템으로 두고 에이전트에게 자율을 주는 것이 지금의 최선이다. 그러나 프로덕션에선 버전·동시성·권한·이식성이라는 가드레일이 필요하고, 세션 안에서 쓰는 메모리(인밴드)는 자원이 갈리고 세션을 넘어 보지 못한다. 그래서 세션 밖에서 배치로 트랜스크립트를 훑어 메모리 변경을 제안하는 두 번째 과정 — dreaming — 을 둔다.**

> *"the intelligence alone is not going to compound because they need this context"* (02:18~02:22) · *"we introduced this concept of dreaming which is like a second o second order process over memory"* (17:49~17:54) · *"we sort of are merging back into those practices, but that's because we have enough signal now to know that those things should just be done in a very deterministic way"* (31:06~31:13)

ASR·ko 보정: ko가 **라디안/도 예시의 정답·오답을 뒤집고**(20:17~20:21, *"라디안을 사용해야 할 때 다른 단위"*), **Memory & Dreaming API를 "메모리 및 스트리밍 API … 클라우드 관리형 에이전트"로**(28:17~28:19 — `en`도 같은 오류), *"more information that they need"* 를 **"필요 이상으로 많은 정보"로**(24:43 — `en`도 같은 오류), 커리큘럼에서 **주제가 빠졌다**는 말을 **"메모리 저장 공간이 부족"으로**(19:53), 비유 끝에 **없던 "연구 결과에 따르면"을**(17:28) 넣었다. 해시 동시성 절차(11:12~11:18)는 *"시간이 걸립니다 … 다시 시도하세요. 해시시"* 로 무너졌고, CLAUDE.md는 25:06에서 **"클로드 의학박사"**, em dash는 **"하이픈"**, directory는 **"예배 규칙서"**, Q&A 결론의 *harness* 는 **"시스템"** 이 됐다. 전체 목록은 raw. **인용은 en-orig에서만** 했다.

> ⚠️ **당사자 진술, 수치 없음.** 화자는 Anthropic 직원이다. 효과(정확도↑, 토큰·비용↓, 13:57~14:24)와 dreaming 비용이 상쇄된다는 주장(24:31~24:46)에 **숫자가 하나도 없다.** 슬라이드는 자막에 없다. 제품 언급은 청중 질문을 받고서다 — *"we're not allowed to make product call to actions but given that you asked"*(27:51~27:55).
>
> ⚠️ **행사·촬영일 미확정.** *"here at AI DevCon"*(00:04). 설명란 링크(tessl.co)로 보아 Tessl 행사로 보이나 자막에 Tessl은 없다. *"the newest model, we've just released one"*(02:32~02:35)은 모델명이 없다. 청중이 *"the cla code leak and the memory stuff. The dreaming stuff"*(28:38~28:41)를 언급한다 — 무엇이 언제 유출됐는지는 발화되지 않고, 이 위키에 해당 사건 페이지는 없다.

## 1. 왜 컨텍스트인가 (02:03~03:16)

*"the intelligence alone is not going to compound because they need this context that helps them perform the specific tasks"*(02:18~02:24). 그 컨텍스트는 *"often kind of orthogonal to the model intelligence"*(02:26~02:30) — 새 모델도 *"isn't going to out of the box know exactly what it takes to succeed in your organization"*(02:35~02:38). 그래서 컨텍스트 엔지니어링은 *"over time has the effect of multiplying the intelligence even as models get smarter"*(02:46~02:51). 증상: 코드베이스를 모름, 사용자 선호를 모름, 그리고 *"they might not learn from their mistakes"*(03:08~03:10) — *"you don't have this uh continual learning effect"*(03:13~03:15). → [[context-engineering]] · [[continual-learning]]

## 2. 1년 회고 — 네 정거장 (03:16~07:58)

*"at Anthropic, we like to say do the simple thing that works. And this is a timeline that's only really spanned the past year."*(03:25~03:31)

| 정거장 | 배운 것 | 한계 | en-orig |
|---|---|---|---|
| **CLAUDE.md** ([[claude-code]]와 출시) | *"kind of unreasonably effective"* — 세션 시작에 주입하는 마크다운, 사람이 읽고 사람·에이전트가 같이 쓴다 | 세션 시작 주입 → *"context bloat"*, 파일이 길어지면? | 03:31~04:37 |
| **memory tool** | 에이전트가 언제 읽고·쓰고·고칠지 스스로 정한다, **인밴드**(*"within the context of a session"*) — *"autonomy proved to work really well"* | (뒤에서 → §5) | 04:39~05:24 |
| **스킬** ([[agent-skills]]) | progressive disclosure — 프런트매터 몇 문장만 보고 로드, 본문은 원하는 만큼 깊게. **책장 비유**: 프랑스어로 말을 걸면 프랑스어 사전을 꺼낸다 | *"still kind of driven by humans and agents together"* — 무엇이 스킬이 될지 여전히 사람이 정한다 | 05:27~07:07 |
| **메모리 = 파일 시스템** (현재 최선) | 마크다운으로 채우고, *"agents are actually just very good at using normal file system tools like bash and gp[=grep]"* — 전용 메모리 도구 대신 검색. 검색이 progressive disclosure를 닮는다 | (→ §3) | 07:09~07:56 |

요점(07:58~08:17): **포맷은 마크다운, 메모리는 크게 자라게 두되 빨리 색인·검색할 도구를 주고, 쓰기에는 자율을.** → [[agent-memory]] · [[file-system-agent]]

> 위키의 정리: 이 회고는 **"전용 도구에 덜 opinionated하게"** 방향이다 — *"we've kind of developed that into systems where we're even less opinionated about what these tools need to look like"*(05:19~05:23). [[file-system-agent]](Vercel)·[[corpus-as-filesystem-workspace]]와 같은 결론에 **모델 공급자 쪽에서** 도달한 셈.

## 3. 프로덕션으로 키우면 (08:32~10:02)

*"many agents collaborating at the same time where they run over very long periods of time"*(08:50~08:54)에서 생기는 문제:

- 여러 에이전트가 **한 메모리 파일에 동시에 쓰기**(09:11~09:14)
- 한 에이전트가 **조직 전역 컨텍스트**에 잘못 쓰면 *"that would scale to all of your agents and be pretty disastrous"*(09:25~09:28)
- 사람과 에이전트가 **같은 메모리를 함께 편집**할 때 추적(09:30~09:37)
- **낡은 기억**, 잘못 쓰인 기억, *"even maliciously injected by someone trying to uh prompt inject your agents to write bad things to memory"*(09:47~09:55) → [[prompt-injection]]

## 4. 설계 원칙 넷 (10:06~13:44)

→ [[production-memory-guardrails]] (신규)

1. **버전 관리** — 롤백, *"what context was this update based on. So, which agent session, which transcript"*(10:37~10:42), 누가(에이전트·사람) 했는지(10:45~10:50)
2. **동시성** — ⭐ *"when an agent decides that it wants to write an update to a memory, it takes a hash. It then drafts its edit and then before it writes the update, it takes another hash. If those two things do not match, then the agent cannot write it"*(11:09~11:24), 그러면 메모리를 다시 읽고 초안을 다시 써 재시도(11:28~11:32). *"thousands of agents all working off the same memory system"*(10:58~11:00)을 위한 장치
3. **권한** — 조직 전역 지식부터 에이전트 개인 *"scratch pad"*(12:08~12:12)까지 층이 있고, 조직 전역은 *"you might want that as read only"*, 스크래치패드엔 쓰기(12:31~12:36)
4. **이식성** — 큐레이션한 메모리를 *"multiple product surfaces"* 에서 쓰도록 *"a clean API"*(13:16~13:24)

## 5. 효과 — 그리고 새 병목 (13:44~16:51)

효과(13:57~14:54, ⚠️ 수치 없음): 두 번째에 더 잘한다(정확도), 그 2차 효과로 *"spending fewer tokens. they can more easily oneshot these tasks"*(14:19~14:24), 개발자는 제품에 집중.

**인밴드 메모리의 한계**(15:04~16:49):

- **자원·주의의 분할** — *"how much capacity should an agent put into like helping future versions of itself versus doing the task that you actually asked it to do?"*(15:58~16:03), 지연도
- **가시성** — *"they just won't see patterns that happen across sessions"*(16:21~16:22). 같은 실수를 세션마다 되풀이해도 *"it has a new context window in each of those"*(16:29~16:31), 다른 환경의 다른 에이전트가 겪는 실패도 모른다
- (뒤늦게 덧붙임) **낡은 기억** — *"you need something some pass that checks that everything that's written there is still correct"*(17:40~17:45)

→ *"some outofband memory curation"*(16:45~16:47)

## 6. dreaming (16:51~24:50)

→ [[agent-dreaming]] (신규)

**학교 비유**(16:57~17:34): 과제를 내는 학생, 채점하는 교사, 전체를 보는 교장. *dedicated capacity* 와 *visibility over the whole fleet* 가 이 구조의 이유다.

**정의**: *"dreaming which is a process that runs in batch and asynchronously with its own allocated resources to ensure that those memories themselves are effective up to date"*(18:10~18:20).

**동작**(18:32~19:30): 기존 **메모리 스토어** + 일정 기간의 **세션 트랜스크립트** → 에이전트가 검토 → *"It then outputs a new memory store where there are proposed changes to the existing memory store"*(19:02~19:07).

**예시 셋**(19:32~21:16): ① 지리 답안이 전부 엉망 → 그 주제가 커리큘럼(메모리)에 **빠져 있다** → 추가 ② 수학 답안이 전부 **라디안**(정답은 도) → 계산기 설정 지시 = 트랜스크립트에서 **도구 설정 오류**를 찾는 것, *"we're also really scrutinizing like those tool calls and all of the other metadata"*(20:53~20:57) ③ 모두가 **em dash** 를 너무 많이 쓴다 → 조직 전역 공지.

**프로덕션 설계**(21:30~23:24): 메모리 = 디렉터리의 마크다운 파일, 트랜스크립트 + 도구·스킬 메타데이터 → **오케스트레이터가 서브에이전트 함대**를 띄워 분석(21:56~22:02) → 오케스트레이터가 *"prevalent enough patterns"*(22:43~22:46)만 골라 개별 변경 제안 → ⭐ *"the agent will additionally give you examples of transcripts where it's noticed this pattern has happened and also some stats on like how prevalent this issue is"*(22:57~23:05) → *"you as the individual can decide where you want to accept changes to the memory um where you want to reject them"*(23:13~23:21). 메모리 쓰기와 dreaming 모두 **조직 맞춤 지시로 steer** 가능(22:06~22:32).

**비용**(24:25~24:46): *"that sounds really expensive"* 에 대한 답은 **좋은 메모리가 원샷을 늘려 비용이 내려간다**는 것 — ⚠️ 수치 없음.

## 7. 요약과 맺음 (24:50~26:59)

① *"do the simple thing that works"* — CLAUDE.md·스킬·자율 메모리만으로도 멀리 간다 ② 다수 에이전트·장시간·복잡한 도메인이면 *"safe, verifiable, auditable"*(25:38~25:40) 가드레일 ③ 루프를 닫으려면 dreaming 같은 아웃오브밴드 과정으로 *"consolidate your memory and cut things that are no longer relevant, add things that agents are missing"*(26:17~26:23). 코딩 전용이 아니다 — 화자는 발표 자료 만들 때도 메모리를 쓴다(25:52~26:05). *"keep dreaming"*(26:53).

## 8. Q&A (27:01~31:23)

1. **구현 추천?** → 발표의 원칙은 *"the architecture that we used in our memory (…) infrastructure for our managed agent solutions"*(28:02~28:11), *"everything like versioning uh hashing etc that's all available within our memory in[=and] dreaming API through claude manage[=Managed] agents"*(28:13~28:21). → [[managed-agents]]
2. **수백 명·서로 다른 권한에서 dreaming이 가드레일을 지키나?** → *"when you set up a dreaming procedure you decide exactly which session transcripts to attach"*(29:20~29:25) — 같은 권한 집합의 트랜스크립트만 골라 메모리 스토어와 맞추면 된다(29:39~29:48). 기간 단위로 몽땅 넣는 설정도 가능.
3. ⭐ **"데이터베이스를 처음부터 재발명하는 것 아닌가?"** → 에이전트 자율과 *"things that are baked into the harness"*(30:34~30:36) 사이의 경계를 찾는 중이고, 잘 되는 프리미티브(해싱·버전 관리)를 하네스에 코드화하고 있다 — *"to to some extent like we sort of are merging back into those practices, but that's because we have enough signal now to know that those things should just be done in a very deterministic way and there's no need to reinvent the wheel"*(31:03~31:14). → [[files-vs-database-agent-memory]]

## 이 위키와의 연결

### 이어지는 것

- **[[token-roles]] · [[strategy-primitives]] · [[managed-agents]]** — 09-01·09-18에 이름만 있던 dreaming에 **입력(메모리 스토어 + 트랜스크립트)·구조(오케스트레이터 + 서브에이전트)·출력(제안 + 근거 + 빈도)·게이트(사람 수락/거부)** 가 붙었다. *"Managed Agents에 기본 제공"*(09-18)은 Q&A의 *memory and dreaming API*(28:19)와 일치.
- **[[nightly-memory-consolidation]]** (Muse, 09-17) — 같은 *"잘 때 정리"* 직관이지만 Muse는 **모델이 스스로 정하고 사용자 가시성이 없었다.** 이 소스는 **근거 트랜스크립트·빈도 통계·사람 승인**을 둔다 — 그 페이지의 미해결 항목(가시성·되돌리기·판정 검증)에 대한 한 설계 답.
- **[[agent-memory]]** — 오래된 빈자리(*틀린 기억의 정정, 무효화*)에 **낡은 기억을 점검하는 패스**(17:40~17:45)와 *cut things that are no longer relevant*(26:17~26:21)가 들어온다. 강등·삭제 경로가 처음으로 명시된 소스.
- **[[skill-self-improvement]]** — *사람 게이트*가 메모리 층에도 생겼다: dreaming 제안은 사람이 수락한다.
- **[[continual-learning]]** — Anthropic도 *continual learning*을 **컨텍스트 층**에서 말한다(*"you would have the feeling of continual learning"* 08:22~08:24 — 가중치 갱신 아님).

### 갈리는 것

> ⚠️ **Contradiction: 파일 메모리의 동시 쓰기 — DB로 갈 것인가, 하네스에 넣을 것인가.** [[files-vs-database-agent-memory]]([[ignacio-martinez|Oracle]], 09-24)는 *파일엔 트랜잭션이 없다 → 워크트리로 우회하거나 DB(DBFS)로 승격*. 이 소스는 **파일 시스템 메모리를 유지하고** 쓰기 전후 해시 비교·버전 관리를 **하네스/API 층**에 넣는다. Q&A에서 화자 스스로 *"merging back into those practices"* 라 인정한다 — 결론(DB의 원리는 필요하다)은 같고 **놓는 층**이 다르다. ⚠️ 어느 쪽이 나은지 측정은 양쪽 다 없다.

> ⚠️ **Contradiction: dreaming의 입력과 쓰기 권한.** [[tech-bridge-tokens-should-have-jobs]](09-18)에서 드리머는 *"발견한 내용을 메모리에 저장"* 하고, 회고에는 *채점을 통과한 것*을 보낸다(11:46~11:51). 이 소스의 dreaming은 **실패 패턴**(*"where agents are consistently failing"* 19:17~19:22)을 주로 찾고, 메모리에 직접 쓰는 대신 **변경을 제안해 사람이 수락**한다(23:13~23:21). 두 설명이 같은 제품의 다른 모드인지, 다른 층(전략 루프 vs 메모리 API)인지 **미확정.**

> ⚠️ **작성자 = 검증자는 절반만 풀렸다.** 근거 트랜스크립트·빈도 통계를 붙여 사람이 고르게 한 것은 [[skill-evals]]가 표시해 온 빈자리에 대한 답이다. 그러나 **사람이 수락한 변경이 실제로 다음 날 성능을 올렸는지 재는 단계**는 말하지 않는다 — [[production-trace-eval-flywheel]] 같은 eval 고리가 없다.

## 해소하지 않고 표시만 한 것

- **효과 수치 전부** — 정확도·토큰·비용·dreaming 비용 상쇄.
- **dreaming 주기** — *"next day"*(19:26~19:28, 20:05~20:06)만. "밤새"는 제목·설명란의 말.
- **수락/거부가 필수인지** — *"in our case, the way that we've designed this in production"*(22:54~22:56)이라 했을 뿐, 자동 적용 모드가 있는지 없음.
- **스킬도 dreaming의 출력인가** — 09-01은 *"메모리에 쓰고 스킬을 작성"*. 이 발표의 출력은 **메모리 스토어**만 말한다.
- **해시 충돌 시 재시도 한도·병합 규칙** — 없음. *"ripples the memory"*(11:28) 원래 단어 미확정.
- **"the cla code leak"** — 청중 발언. 무엇인지 미확정, 이 위키는 연결하지 않는다.
- **화자 성(Mukta)** — 설명란에만. 행사(Tessl AI DevCon로 보임)·촬영일 미확정.

## 등장 개체

- 인물: [[lamis-mukta]] (신규) · 사회자(이름 미발화) · 청중 질문자 3명
- 조직: [[anthropic]] · Tessl(설명란 링크만, 페이지 없음)
- 제품·도구: [[claude-code]] · CLAUDE.md · [[managed-agents|Claude Managed Agents]](memory and dreaming API) · [[agent-skills]] · bash · grep
- 개념: [[agent-dreaming]] (신규) · [[production-memory-guardrails]] (신규) · [[agent-memory]] · [[context-engineering]] · [[continual-learning]] · [[nightly-memory-consolidation]] · [[files-vs-database-agent-memory]] · [[token-roles]] · [[strategy-primitives]] · [[prompt-injection]] · [[file-system-agent]] · [[skill-self-improvement]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=sINXtw4wmyM> (31:27, `upload_date` 2026-09-30)
- raw: `01.raw/articles/2026-09-30_자는 동안 스스로 학습하는 AI — 단순 기억을 넘어 꿈으로 진화하는 에이전트의 비밀.md`
- 설명란 링크: <https://tessl.co/5re> · <https://tessl.co/6gq> (⚠️ 열어 보지 않았다)
- 같은 주제: [[tech-bridge-tokens-should-have-jobs]] · [[tech-bridge-claude-platform-agent-era]] · [[tech-bridge-oracle-agent-memory-harness]] · [[tech-bridge-zuckerberg-muse-in-daily-use]] · [[tech-bridge-agent-knowledge-four-ways]]
- [[tech-bridge]] · [[lamis-mukta]] · [[anthropic]] · [[managed-agents]]
