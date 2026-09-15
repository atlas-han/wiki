---
title: 치명적 3요소 (Lethal Trifecta)
type: concept
category: theory
tags: [security, data-exfiltration, prompt-injection, agent-safety, llm-security, threat-model]
aliases: [lethal trifecta, 치명적 삼중주, 치명적 3요소]
related: [confused-deputy-attack, prompt-injection, agentic-misbehavior, agent-identity-separation, secure-tool-evolution, sweeper-agent, black-box-agent-approach]
first-seen: tech-bridge-build-time-vs-runtime-tools
sources: [tech-bridge-build-time-vs-runtime-tools, tech-bridge-one-designer-plus-ai]
created: 2026-09-11
updated: 2026-09-15
---

# 치명적 3요소

**에이전트가 ① 비공개 데이터, ② 신뢰할 수 없는 콘텐츠, ③ 그것을 외부로 노출할 능력에 동시에 접근하면 데이터 유출이 성립한다**는 판정 틀. Simon Willison이 명명했고, [[tech-bridge-build-time-vs-runtime-tools]]([[google-cloud|Google Cloud]])가 이 위키에 들여왔다.

> **Simon Willison**이 **치명적 3요소(the lethal trifecta)** 라는 표현을 만들었습니다. 에이전트가 세 가지에 **동시에** 접근할 때 데이터 유출이 일어납니다 — 첫째 **비공개 데이터**, 둘째 **신뢰할 수 없는 콘텐츠**, 셋째 **그 콘텐츠와 데이터를 외부 사용자에게 다시 노출할 수 있는 능력.**

> ⚠️ Willison의 원문은 이 위키에 없다. 이 페이지는 Google 발표자의 **전언**에 근거한다. 원문 ingest 전까지 정의의 정확한 표현은 소스 밖이다.

## 세 요소를 사례에 대입하면

[[confused-deputy-attack|트리아지 에이전트]] 사례:

| 요소 | 사례에서 |
|---|---|
| ① 비공개 데이터 | 급여 데이터베이스 (에이전트가 권한 보유) |
| ② 신뢰할 수 없는 콘텐츠 | 악의적 내부자가 **신뢰된 티켓 시스템**에 쓴 지시 |
| ③ 외부 노출 능력 | 결과를 **티켓에 다시 쓰기** — 요청자가 읽는다 |

셋 다 있다. 그래서 유출이 됐다. 이 틀의 힘은 **셋 중 하나만 빼도 유출이 성립하지 않는다**는 데 있다 — 처방을 셋 중 어디에 둘지 고를 수 있다.

## 이 위키의 [[prompt-injection]]과의 관계

[[prompt-injection]]은 지금까지 **벡터**를 넷 모았다 — 런타임 입력 · 스킬 파일 · 공유 사일로/위키 · (그리고 이 소스의) 신뢰된 내부 시스템. 전부 **②(신뢰할 수 없는 콘텐츠)가 어디로 들어오는가**의 목록이다. 이 틀은 처음으로 **나머지 두 요소**를 명시한다 — 콘텐츠가 들어와도 ①이 없으면 훔칠 게 없고 ③이 없으면 내보낼 길이 없다.

기존 방어를 이 틀로 다시 놓으면:

| 방어 | 빼는 요소 |
|---|---|
| [[anthropic-claude-code-auto-mode]]의 probe (입력 스캔) | ② 를 걸러내려 함 |
| [[anthropic-managed-agents]]·[[credential-injection-outside-sandbox]] (자격증명 격리) | ① 을 에이전트 손에서 뺌 |
| [[agentic-misbehavior]]의 *Sharing via external service* 차단 | ③ 을 막음 |
| [[secure-tool-evolution]] (읽기 전용·허용 데이터셋·출력 크기·고정 SQL) | ① 의 범위를 좁힘, ③ 의 양을 줄임 |
| [[bound-parameters]] (신원을 에이전트 밖에서 바인딩) | ①에 닿는 **주체**를 사용자로 고정 |

즉 이 위키가 따로따로 모아 온 방어들이 **세 요소 중 어디를 공략하는가**로 정렬된다.

## 이 위키의 다른 소스에 적용하면

- [[sweeper-agent]]([[tech-bridge-agent-to-agent-as-search]]) — 사일로의 비공개 데이터(①)를 읽고, 공유 공간(③, 모두가 읽는다)으로 옮기며, 사일로 안에 인젝션(②)이 들어올 수 있다고 화자가 인정했다. **셋 다 있다.** 그 소스의 *영구 오염·오공개* 우려가 이 틀로 설명된다.
- [[black-box-agent-approach]] — 읽기 전부 개방(①), 쓰기 직전 소유자 승인(③에 사람을 둠). 승인이 ③을 끊는 자리다.
- [[company-brain]] — 사용자 클레임으로만 읽기(①을 사용자 단위로), 자동 쓰기 금지(③에 사람). 두 요소를 동시에 다룬다.

## ⚠️ 미해결

- 소스는 ②의 **탐지**를 다루지 않는다. 처방은 ①(신원·데이터셋)과 ③(출력·고정 SQL)에 집중된다.
- ③의 정의 — *"외부 사용자"* 가 누구인가. 트리아지 사례의 내부자는 조직 내부인이지만 급여 DB 기준으로는 외부다. **경계는 데이터 단위**로 그어야 한다는 뜻이지만 소스가 명시하지 않는다.

## References

- [[tech-bridge-build-time-vs-runtime-tools]] (first-seen) · [[averi-kitsch]]
- 관련: [[confused-deputy-attack]] · [[prompt-injection]] · [[agentic-misbehavior]] · [[secure-tool-evolution]] · [[bound-parameters]]
