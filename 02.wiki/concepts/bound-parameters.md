---
title: 바운드 파라미터와 인증 파라미터 (Bound Parameters)
type: concept
category: technique
tags: [parameters, identity, pii, jwt, oidc, zero-trust, security, tool-design]
aliases: [bounded parameters, authenticated parameters, 바운드 파라미터, 인증된 파라미터]
related: [agent-identity-separation, secure-tool-evolution, credential-injection-outside-sandbox, confused-deputy-attack, lethal-trifecta, agent-governance-layers, multiplayer-agent-context]
first-seen: tech-bridge-build-time-vs-runtime-tools
sources: [tech-bridge-build-time-vs-runtime-tools]
created: 2026-09-11
updated: 2026-09-11
---

# 바운드 파라미터와 인증 파라미터

**사용자 신원 같은 민감한 파라미터를 에이전트가 채우게 두지 않고, 애플리케이션이 인증한 값(또는 검증된 토큰의 클레임)을 도구에 직접 묶는다. 에이전트는 그 값을 보지도 정하지도 못한다.** [[tech-bridge-build-time-vs-runtime-tools]]([[google-cloud|Google Cloud]], [[mcp-toolbox-for-databases|Toolbox]])의 [[secure-tool-evolution|진화]] 마지막 단계.

## 문제 — 사용자 ID는 PII다

커스텀 SQL 도구(항공편 조회)가 *사용자 ID와 날짜* 를 받는 상태에서:

> 하지만 **사용자 ID는 사실 아주 민감한 정보**입니다. **PII**죠. 그래서 그것도 **에이전트의 통제 능력에서 제거**해야 합니다.

에이전트가 사용자 ID를 채우면 두 가지가 생긴다 — 에이전트가 **다른 사용자 ID를 넣을 수 있고**([[confused-deputy-attack]]), 에이전트의 컨텍스트에 **PII가 흐른다**([[lethal-trifecta]]의 ①). 데모의 예고가 정확히 첫째 경우다 — *"제가 Prerna가 아니라 Avery라고 에이전트를 속여서 예약해 본다."*

## 두 방식

| | **바운드 파라미터** | **인증 파라미터** |
|---|---|---|
| 누가 신원을 확정 | **애플리케이션** — 먼저 사용자를 인증 | **도구** — OpenID 서명 **JWT** 를 받아 검증 |
| 무엇을 묶나 | 인증된 값을 도구에 **직접 바인딩** | 토큰에서 **클레임**(사용자 ID·이메일·발급자) 추출 후 바인딩 |
| 에이전트가 보는 것 | 없음 — *"그 사용자 신원을 실제로 전혀 보지 못한다"* | 없음 — *"사용자 신원을 에이전트의 통제 밖으로 꺼내 도구에 바인딩"* |
| 도구가 하는 검증 | (앱이 이미 함) | *"이 토큰이 진짜인가? 올바른가?"* |

> **바운드 파라미터.** 애플리케이션이 먼저 **사용자를 인증**하고, 그 파라미터를 **도구에 직접 바인딩**합니다. 그래서 에이전트의 통제가 제한되고 — **에이전트는 그 사용자 신원을 실제로 전혀 보지 못합니다.**

> **인증된 파라미터.** 도구에게 *"OpenID 서명된 JWT 신원 토큰을 받게 될 것"* 이라고 알려줍니다. 그 도구를 호출할 때 먼저 **토큰을 검증**하게 합니다 (…) 그다음 토큰에서 **사용자 클레임**을 추출합니다 — 보통 사용자 ID, 이메일, 발급자가 들어 있죠.

> ⚠️ ko 자막이 첫 인용의 주어를 *"시스템"* 으로 바꿔 요점을 뒤집었다(18:07). en-orig의 주어는 **에이전트**다 — 시스템은 신원을 알고, **에이전트만** 모른다.

## 결과 — 도구 시그니처에서 신원이 사라진다

> 항공편 조회 도구는 **날짜 같은 아주 쉬운 파라미터만** 받습니다. **PII나 사용자 신원 같은 민감한 정보를 다룰 필요가 없습니다.**

에이전트 입장에서 이 도구는 *"어느 날짜?"* 만 묻는 도구다. 누구의 항공편인지는 도구가 이미 안다. [[agent-identity-separation]]의 용어로 — 사용자 ID가 **에이전트 파라미터**에서 **애플리케이션 파라미터**로 옮겨갔다.

## 같은 벽, 다른 자리 — [[credential-injection-outside-sandbox]]

이 위키는 *에이전트가 사용자 권한으로 행동한다* 는 처방을 [[promptql]]에서 이미 봤다. 차이:

| | PromptQL ([[credential-injection-outside-sandbox]]) | Google Cloud (이 개념) |
|---|---|---|
| 벽의 자리 | **HTTP/SQL 프록시** — 요청 경로 | **도구 정의** — 파라미터 |
| 에이전트는 | 그 사람 *으로서* 행동 (자격증명 주입) | 그 사람의 *데이터만* 받음 (신원 바인딩) |
| 신원 전달 | 사용자 클레임 (읽기·쓰기 모두) | 앱 인증 / JWT 클레임 |
| 동기 | 멀티플레이어 권한 상승 | 혼동된 대리인 · PII |

둘 다 **에이전트 손에 신원을 두지 않는다.** [[anthropic-managed-agents]]의 *토큰을 샌드박스 밖에* 까지 합치면 같은 원칙이 **세 소스·세 자리**(vault+프록시 / 프록시 / 도구 파라미터)에서 나왔다. 세 소스는 서로를 모른다.

## ⚠️ 미해결

- **JWT 발급·수명** — 누가 발급하고 장기 실행 작업에서 어떻게 갱신하는지 없다.
- **위임** — 관리자가 다른 사용자를 대신해 조회하는 경우는 바인딩으로 표현되지 않는다.
- **데모 미실행** — *"속지 않는다"* 는 예고이지 시연 결과가 아니다.
- 당사자 진술 — 두 방식 모두 자사 제품 기능명이다.

## References

- [[tech-bridge-build-time-vs-runtime-tools]] (first-seen) · [[averi-kitsch]] · [[mcp-toolbox-for-databases]]
- 관련: [[agent-identity-separation]] · [[secure-tool-evolution]] · [[credential-injection-outside-sandbox]] · [[confused-deputy-attack]]
