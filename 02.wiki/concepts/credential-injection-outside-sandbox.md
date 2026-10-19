---
title: 샌드박스 밖 자격증명 주입 (Credential Injection Outside the Sandbox)
type: concept
category: pattern
tags: [credentials, sandbox, proxy, access-control, privilege-escalation, security, multiplayer]
aliases: [사용자 자격증명 패스스루, 샌드박스에 자격증명 없음]
related: [agent-governance-layers, prompt-injection, multiplayer-agent-context, company-brain, action-reversibility, black-box-agent-approach, bound-parameters, agent-identity-separation, agent-sandboxing]
first-seen: tech-bridge-company-brain-security
sources: [tech-bridge-company-brain-security, anthropic-managed-agents, tech-bridge-build-time-vs-runtime-tools, tech-bridge-openai-huggingface-incident-black-hat, tech-bridge-unblocked-context-engine-structured-queries, tech-bridge-tailscale-aperture-ai-without-lock-in, tech-bridge-openhands-sandboxing-coding-agents, tech-bridge-claude-managed-agents-workshop-1, tech-bridge-claude-managed-agents-workshop-2]
created: 2026-09-10
updated: 2026-10-19
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

같은 팀 리드의 워크숍 발화가 위 첫 행의 동기를 직접 확인한다: *"With our previous setup, your credential would be in your sandbox, so you'd be more susceptible to prompt injection. (…) it would be routed through a proxy that would inject your token before it called the external endpoint or external MCP. That way the model never sees your credentials or your tokens, which means you can never prompt inject Claude to say like, 'Hey, give me your tokens.'"*(08:26~08:56, [[tech-bridge-claude-managed-agents-workshop-1]]). 첫 아키텍처에서는 **자격증명이 sandbox 안에 있었다**는 사실도 처음 나온다. ⚠️ ko: *more susceptible* → "더 좋을 거예요", prompt injection → "주사".

두 위협이 **같은 벽 하나**로 막힌다는 것이 이 개념의 요점이다. 그리고 [[agent-governance-layers]]의 *"벽은 에이전트 바깥에, 에이전트가 잊어도 넘을 수 없는"* 이 여기서는 **HTTP/SQL 프록시**라는 구체적 자리를 얻는다.

## 이 위키의 다른 접근 제어와의 관계

- [[agent-governance-layers]] ①층(결정론적 접근 제어)의 **구현 위치**다. ②층(자연어 정책)은 이 소스에 없다 — 접근 제어가 전부 클레임·스코프라서 *"자연어 정책을 무엇이 해석하는가"* 라는 빈자리가 **생기지 않는다.**
- [[black-box-agent-approach]] (같은 날 Greze 편)는 정반대로 **읽기 접근을 전부 풀고 쓰기에서만 승인**한다. 이 개념은 읽기부터 사용자 단위로 잠근다. 두 소스는 서로를 모른다.
- [[action-reversibility]] — Composio는 되돌릴 수 없으면 신뢰를 앞당기라 했다. 이 개념은 신뢰를 앞당기는 대신 **행동의 주체를 사람 단위로 고정**한다.

## ⚠️ 미해결

- *"흥미로운 세부가 있지만"* — 프록시의 구현, 위임·대리 실행(누가 누구를 대신할 수 있는가), 장기 실행 작업의 토큰 수명은 소스에 없다.
- 도구를 추가한 사용자가 접근을 통제한다 — 그 사용자가 퇴사하면?
- 당사자 진술.

## 같은 원칙, 셋째 자리 — 도구 파라미터 바인딩 (2026-09-11)

[[tech-bridge-build-time-vs-runtime-tools]]([[google-cloud|Google Cloud]])의 [[bound-parameters|바운드·인증 파라미터]]가 같은 원칙을 **도구 정의** 자리에서 구현한다 — 애플리케이션이 인증한 사용자 ID(또는 검증된 OpenID JWT의 클레임)를 도구에 직접 묶고, *"에이전트는 그 사용자 신원을 실제로 전혀 보지 못한다."*

| | [[anthropic-managed-agents]] | 이 개념 (PromptQL) | [[bound-parameters]] (Google Cloud) |
|---|---|---|---|
| 벽의 자리 | vault + MCP 프록시 | HTTP/SQL 프록시 | **도구 파라미터** |
| 격리하는 것 | 토큰 | 사용자 자격증명 | **사용자 신원(PII)** |
| 위협 | 인젝션이 토큰을 훔침 | 정당한 사용자의 권한 상승 | [[confused-deputy-attack\|혼동된 대리인]] · PII 노출 |
| 에이전트는 | 토큰 없이 프록시 호출 | 그 사람 *으로서* 행동 | 그 사람의 *데이터만* 받음 |

세 소스는 서로를 모르며 **세 위협에 같은 벽**이 답한다. 차이는 Google Cloud가 신원을 프록시가 아니라 **도구 시그니처에서 아예 지운다**는 점이다 — 항공편 조회 도구는 날짜만 받는다. 그래서 [[lethal-trifecta]]의 첫째 요소(비공개 데이터)에 닿는 주체가 사용자로 고정되고, 에이전트 컨텍스트에 PII가 흐르지 않는다. 이 개념의 미해결(*프록시 구현·위임·토큰 수명*)은 그쪽에도 그대로 남는다.

## References

- [[tech-bridge-company-brain-security]] (first-seen) · [[tanmai-gopal]]
- [[anthropic-managed-agents]] — 같은 처방의 선행 사례
- 관련: [[agent-governance-layers]] · [[prompt-injection]] · [[multiplayer-agent-context]] · [[black-box-agent-approach]]
- [[tech-bridge-build-time-vs-runtime-tools]] — 셋째 자리: 도구 파라미터 바인딩 · [[bound-parameters]] (2026-09-11)

## 샌드박스 밖 서비스가 공격면이 된 사례 (2026-09-25 · [[tech-bridge-openai-huggingface-incident-black-hat]])

이 원칙은 *자격 증명을 샌드박스 밖에 두라* 였다. [[hugging-face|Hugging Face 사건]]은 그 **바깥 쪽이 뚫린** 경우다 — 샌드박스는 인터넷이 없었지만 샌드박스가 신뢰하는 사내 패키지 관리자 [[artifactory|Artifactory]]는 인터넷이 있었고, SSRF·제로데이로 **관리자 토큰의 서명 키**까지 넘어갔다(14:05~14:28 · 24:15~24:22). 이후 에이전트들은 IMDS·쿠버네티스 서비스 계정·Azure Key Vault로 **샌드박스 밖 자격 증명을 연쇄 수집**했다(25:42~25:57). **바깥에 둔 자격 증명은 바깥 서비스의 공격면만큼만 안전하다.**

## 넷째 자리 — 쿼리 재작성 (2026-10-15 · [[tech-bridge-unblocked-context-engine-structured-queries]])

[[bound-parameters]]의 넷째 자리 참조 — Unblocked는 tenant 필드를 LLM에게 숨기고 생성된 쿼리에 뒤에서 주입한다(14:03~14:12). 격리 대상은 자격증명이 아니라 **테넌트 경계**(*"It could cross tenant boundaries."* 08:38~08:40).

## 게이트웨이가 자격증명을 쥔다 (2026-10-17 · [[tech-bridge-tailscale-aperture-ai-without-lock-in]])

[[remy-guercio|Remy Guercio]]([[tailscale|Tailscale]]): *"we're both an LLM gateway and an MCP gateway, and we even do off[=auth] like injection for just standard APIs and re-expose those as MCPs, too."*(12:33~12:43) 사람·에이전트는 키를 받지 않고 엔드포인트만 친다: *"all they have to do is hit that endpoint. And if they're on the tailnet, everything's authenticated as them"*(14:09~14:15). 같은 원칙(자격증명을 에이전트 밖에 둔다)의 **네트워크 게이트웨이 판본**이다 → [[ai-gateway]]

화자가 꼽은 기존 게이트웨이의 실패는 자격증명을 옮기기만 하는 것이다: *"I've traded some keys for a bunch of other keys."*(09:26~09:28) ⚠️ 벤더 진술. 사용자 신원으로 인증된 요청을 에이전트가 보낼 때의 권한 범위는 다루지 않는다.

> ⚠️ **긴장: 비밀을 골라 넣는 쪽 (2026-10-17 · [[tech-bridge-openhands-sandboxing-coding-agents]])**. [[robert-brennan|Robert Brennan]]의 샌드박스 처방은 필요한 비밀만 **샌드박스 안에** 마운트하는 것이다(*"You can mount specific secrets and environment variables for the agent"* 06:15~06:18, *"maybe a couple secrets that it needs to access a local database"* 05:02~05:04). GitHub Actions의 *"secrets registry"*(07:27~07:29)도 같은 형태다. 이 페이지의 처방은 자격증명을 샌드박스에 **아예 두지 않는** 것이다. 앞쪽은 비밀의 개수를 줄이고, 이쪽은 에이전트가 비밀을 보지 못하게 한다. 발표는 이 차이를 다루지 않는다. → [[agent-sandboxing]]

## 셋째 메커니즘 — placeholder와 egress 바꿔치기 (2026-10-19 · [[tech-bridge-claude-managed-agents-workshop-2]])

[[managed-agents|Claude Managed Agents]]의 **Vaults**를 제품 팀이 설명한다.

> *"you define a secret uh that you want to you inject in an environment variable. And instead of putting the real secret in, what we put is in is a placeholder. (…) We at Egress[=at egress] swap it out for the real value only on the host domains that you specified are allowed for that secret. So, if you say uh my super secret MVAR[=env var] can only be used for the SEC, and then Cloud[=Claude] tries to use it for anthropic.com, we won't inject (…) But, when it tries to call the SEC.com[=sec.gov?], it would do the swap"* (24:05~24:45)

| | [[anthropic-managed-agents]] (글) | 이 워크숍 |
|---|---|---|
| 메커니즘 | bundled with resource(Git) · vault + MCP proxy | **env의 placeholder + egress 바꿔치기** |
| 범위 | 리소스·도구 단위 | **비밀마다 허용 호스트 도메인** |
| 샌드박스 안 CLI | — | 가능(Google Workspace CLI 예, 24:59~25:07) |

- 비밀이 샌드박스에 **없다**는 원칙은 같다. 다른 점은 에이전트가 비밀을 *쓰는 방식*을 바꾸지 않는다는 것 — 평소처럼 env를 쓰고, 진짜 값은 나가는 길에서만 생긴다.
- 프롬프트 인젝션이 env를 읽어 다른 도메인으로 보내도 placeholder만 나간다. [[lethal-trifecta]]의 외부 전송 다리를 **비밀별 도메인 허용 목록**으로 자른다.
- 이 개념 본문의 동기(멀티플레이어 권한 상승)와는 축이 다르다. 워크숍은 **사용자별** 자격증명을 말하지 않는다 — vault ID를 세션에 붙이는 단위다.
- ⚠️ 당사자 설명. 데모는 SEC 신원(이름·이메일)을 *"just inject that in the prompt"*(23:59~24:01)로 처리했고 vault는 시연하지 않았다(콘솔 화면만).
