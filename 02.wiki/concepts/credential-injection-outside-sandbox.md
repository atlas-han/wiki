---
title: 샌드박스 밖 자격증명 주입 (Credential Injection Outside the Sandbox)
type: concept
category: pattern
tags: [credentials, sandbox, proxy, access-control, privilege-escalation, security, multiplayer]
aliases: [사용자 자격증명 패스스루, 샌드박스에 자격증명 없음]
related: [agent-governance-layers, prompt-injection, multiplayer-agent-context, company-brain, action-reversibility, black-box-agent-approach]
first-seen: tech-bridge-company-brain-security
sources: [tech-bridge-company-brain-security, anthropic-managed-agents]
created: 2026-09-10
updated: 2026-09-10
---

# 샌드박스 밖 자격증명 주입

**에이전트가 도는 샌드박스에는 자격증명을 두지 않고, HTTP·SQL 계층(프록시)에서 그 상호작용의 사용자 자격증명을 주입해 에이전트가 그 사람으로서 읽고 행동하게 한다.** [[tech-bridge-company-brain-security]]의 둘째 아키텍처.

> **샌드박스에 자격증명을 절대 저장하지 마세요.** 대신 **HTTP 계층에서, SQL 계층에서 사용자의 자격증명을 주입**해 **AI가 그 상호작용에서 그 사람으로서 행동하게** 합니다.

## 읽기와 쓰기 양쪽

| | 무엇을 | 어떻게 |
|---|---|---|
| **읽기** (컨텍스트) | 위키의 올바른 부분 | 에이전트가 **그 사용자의 클레임**으로 읽는다 — *"재무 문제를 풀려고 읽는다면 재무 클레임으로 나로서. 매번."* |
| **쓰기** (도구 실행) | 로그 조회·PR·배포·알림 | 코드가 도구를 실행할 때도 **사용자 자격증명** — 프록시가 주입 |

요약된 네 원칙 중 셋·넷이 이것이다 — *"클라우드 샌드박스에 자격증명을 저장하지 마라"*, *"실제 데이터와의 모든 상호작용을 가상화(프록시)하고, 도구를 추가한 사용자가 접근을 통제하게 하라."* 발표자는 *"거기서 역산하면 말이 되는 아키텍처는 하나뿐"* 이라 한다.

## 왜 — 멀티플레이어의 권한 상승

동기는 [[multiplayer-agent-context]]다. 여러 사람이 **하나의 에이전트**를 공유 컨텍스트로 쓸 때:

> 엔지니어는 PR 작업이 허용됐는데 **이제 내가 같은 에이전트로 프로덕션에 배포할 수 있으니까요.** 너무 무섭습니다. (…) 은행이라면 디버그·스테이징·알림·배포하는 사람이 **같은 사람이 아닙니다.** 하지만 **같은 자리에 있는 것에 큰 가치가 있죠 — 거기에 모든 지식이 있으니까.**

에이전트가 **자기 자격증명**을 가지면 그 에이전트에 말을 거는 모든 사람이 그 권한을 얻는다. 에이전트가 **말하는 사람의 자격증명**으로 행동하면 권한 경계가 사람의 경계와 일치한다.

## 같은 처방, 다른 이유 — [[anthropic-managed-agents]]

이 위키는 이미 *자격증명을 샌드박스에 두지 않는다* 는 설계를 알고 있었다 — [[anthropic-managed-agents]]의 vault + MCP proxy. 그런데 동기가 다르다.

| | 이유 | 위협 |
|---|---|---|
| [[anthropic-managed-agents]] | [[prompt-injection]] 피해 축소 — *"인젝션이 환경변수를 grep하게 만들어도 잡을 게 없다"* | 외부 콘텐츠가 에이전트를 속임 |
| 이 소스 | **권한 상승** 방지 — 공유 에이전트가 사용자 권한을 넘지 못하게 | **정당한 사용자**가 남의 권한을 얻음 |

두 위협이 **같은 벽 하나**로 막힌다는 것이 이 개념의 요점이다. 그리고 [[agent-governance-layers]]의 *"벽은 에이전트 바깥에, 에이전트가 잊어도 넘을 수 없는"* 이 여기서는 **HTTP/SQL 프록시**라는 구체적 자리를 얻는다.

## 이 위키의 다른 접근 제어와의 관계

- [[agent-governance-layers]] ①층(결정론적 접근 제어)의 **구현 위치**다. ②층(자연어 정책)은 이 소스에 없다 — 접근 제어가 전부 클레임·스코프라서 *"자연어 정책을 무엇이 해석하는가"* 라는 빈자리가 **생기지 않는다.**
- [[black-box-agent-approach]] (같은 날 Greze 편)는 정반대로 **읽기 접근을 전부 풀고 쓰기에서만 승인**한다. 이 개념은 읽기부터 사용자 단위로 잠근다. 두 소스는 서로를 모른다.
- [[action-reversibility]] — Composio는 되돌릴 수 없으면 신뢰를 앞당기라 했다. 이 개념은 신뢰를 앞당기는 대신 **행동의 주체를 사람 단위로 고정**한다.

## ⚠️ 미해결

- *"흥미로운 세부가 있지만"* — 프록시의 구현, 위임·대리 실행(누가 누구를 대신할 수 있는가), 장기 실행 작업의 토큰 수명은 소스에 없다.
- 도구를 추가한 사용자가 접근을 통제한다 — 그 사용자가 퇴사하면?
- 당사자 진술.

## References

- [[tech-bridge-company-brain-security]] (first-seen) · [[tanmai-gopal]]
- [[anthropic-managed-agents]] — 같은 처방의 선행 사례
- 관련: [[agent-governance-layers]] · [[prompt-injection]] · [[multiplayer-agent-context]] · [[black-box-agent-approach]]
