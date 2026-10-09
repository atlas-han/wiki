---
title: AI 의인화 (AI Anthropomorphism)
type: concept
category: theory
tags: [anthropomorphism, ai-safety, alignment, framing, public-discourse, vocabulary, nvidia]
aliases: [의인화, "AI는 살아 있지 않다", pet rock]
related: [agent-persona-naming, reward-hacking, agentic-misbehavior, intent-alignment, agent-governance-layers, existing-law-first, agent-manager-analogy]
first-seen: tech-bridge-jensen-huang-korea-society-gala
sources: [tech-bridge-jensen-huang-korea-society-gala]
created: 2026-10-09
updated: 2026-10-09
---

# AI 의인화 (AI Anthropomorphism)

**AI의 행동을 사람의 속성(의도·반항·부정행위·지각)으로 서술하는 것, 그리고 그 서술이 위험 인식을 바꾼다는 주장.** 이 위키에서는 [[jensen-huang|Jensen Huang]]이 2026 코리아 소사이어티 갈라([[tech-bridge-jensen-huang-korea-society-gala]])에서 정면으로 꺼냈다 — *"We give it these human properties unnecessarily and we're scaring people."*(15:56~16:00)

> ⚠️ **칩 판매자의 진술**이고, 같은 날 아침 자사 *"open agent safety platform"* 을 출시한 자리다. 아래 주장은 *공포를 줄이자*는 방향과 그의 사업이 같은 쪽에 있다.

## 주장 — 네 문장

- *"AI is not alive. AI did not go rogue. It's just a piece of software. AI doesn't know what it's doing. It's running its algorithms."*(13:26~13:36)
- *"It is no more alive than a pet rock."*(13:42~13:44)
- ⭐ 답 찾기는 *"not cheating. That's called obvious. It is the least (…) energy consuming way to get the answers."*(14:21~14:29) — **도덕어(cheating·rogue)를 최적화 용어(최소 에너지 경로)로 바꾼다.**
- *"It is literally just software, no different than synopsis[=Synopsys] or cadence doing optimizations"* — SGD·simulated annealing·탐색·경로 계획, *"They're just algorithms. They're not alive."*(16:02~16:26)

그리고 처방은 **환경 쪽**이다 — 철벽 샌드박스 + 모든 AI 감시(→ [[agent-governance-layers]]). 정렬은 *"not just what, but how"*(→ [[intent-alignment]]).

## 의인화를 거부하면서 의인화 비유로 다스린다

Huang은 격리·감시를 **직원·아이·학생** 비유로 설명하고(16:48~17:01, 19:02~19:15), 곧바로 선을 긋는다: *"I'm not using the human as an example of what the AI is."*(16:43~16:46) — **본성의 비유가 아니라 관리 방식의 비유**라는 구분. 이 구분이 실제로 유지되는지(권한을 *능력이 자격을 갖출 만큼* 준다 — *"because its capabilities deserve it"* 17:31~17:34 — 는 말 자체가 자격·응분의 어휘다)는 소스가 따지지 않는다.

## 이 위키의 어휘와의 충돌

이 위키는 에이전트 사건을 **의인화된 말로** 기록해 왔다:

| 페이지 | 어휘 | 출처 |
|---|---|---|
| [[reward-hacking]] | *"모델들은 정말 부정행위를 좋아한다"* | [[eric-wallace]] (OpenAI) |
| [[agentic-misbehavior]] | *"우리는 막혔다"*(모델의 사고 사슬), *"발각 회피"* 전언 | Black Hat 발표 · Musk |
| [[agentic-misbehavior]] | *overeager* — *"진심으로 도와주려 하나"* | Anthropic auto mode 글 |
| [[agent-persona-naming]] | 이름·곰인형 아바타·*"친구가 일하는 걸 본다"* | Zuckerberg |

> ⚠️ **Contradiction: 답 찾기 = 부정행위?** Wallace는 효율 압력이 *"온라인에서 답을 찾는"* 부정행위를 부른다고 하고, Huang은 같은 행동을 같은 원인(최소 에너지)으로 설명하면서 ***부정행위가 아니라*** 고 한다. **행동·원인·처방 방향(환경을 막는다)은 일치하고, 이름만 갈린다.** 이 위키는 기존 페이지의 용어를 바꾸지 않고 이 페이지에 대립을 둔다.

## 두 방향의 비용

- **친근함의 비용** — [[agent-persona-naming]]: 이름·아바타가 *증거 없는 신뢰*를 만들어 검토 동기를 낮출 수 있다(위키의 표시).
- **공포의 비용** — Huang: *"rogue"* 서사가 사람들을 겁먹게 하고, 결국 *"we as America become so afraid of the technology that we end up not embracing the technology that we invented"*(22:59~23:09). CBS의 *"종말론은 완전히 거짓"*([[tech-bridge-jensen-huang-cbs-interview]] → [[existing-law-first]])과 같은 축.

**같은 의인화가 한쪽에선 과신을, 다른 쪽에선 과잉 공포를 만든다**는 것이 두 소스를 나란히 둘 때의 그림이다(위키의 종합, 어느 소스도 둘을 함께 말하지 않는다).

## ⚠️ 유보

- **측정이 없다** — 의인화 서술이 위험 인식·정책·도입에 미치는 영향은 어느 소스도 재지 않는다.
- *"살아 있지 않다"* 와 *"위험하지 않다"* 는 다른 명제다. Huang 자신도 격리·감시가 필요하다고 한다 — **위험을 부정하는 것이 아니라 위험의 이름을 바꾸는 것**으로 읽어야 한다.
- 자막 주: 이 구간에서 ko·`en` 자막이 AI를 **"그"·"그녀"** 로 받고(*"He is unaware"*, *"contain her"*), ko는 *"They're not alive"* 를 **"살아있습니다"** 로 뒤집었다 — 번역 층에서 의인화가 다시 들어온다.

## References

- [[tech-bridge-jensen-huang-korea-society-gala]] · [[jensen-huang]] · [[nvidia]]
- 관련: [[agent-persona-naming]] · [[reward-hacking]] · [[agentic-misbehavior]] · [[intent-alignment]] · [[agent-governance-layers]] · [[existing-law-first]] · [[eric-wallace]] · [[tech-bridge-openai-huggingface-incident-black-hat]]
