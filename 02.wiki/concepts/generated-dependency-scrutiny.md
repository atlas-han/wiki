---
title: 생성된 의존성 검토 (Generated Dependency Scrutiny)
type: concept
category: pattern
tags: [security, supply-chain, dependencies, licensing, ai-assisted-development]
aliases: [생성된 의존성, 소프트웨어 공급망, dependency validation]
related: [shift-left-security, continuous-security-validation, secure-tool-evolution, credential-injection-outside-sandbox, behavior-validated-trust, ai-vulnerability-discovery]
first-seen: tech-bridge-shift-left-security-ai-code
sources: [tech-bridge-shift-left-security-ai-code]
created: 2026-09-17
updated: 2026-09-17
---

# 생성된 의존성 검토

**AI는 코드만 쓰는 것이 아니라 의존성을 들여오고, 들여온 의존성은 생성된 코드와 같은 수준의 검토를 받아야 한다는 원칙.** [[tech-bridge-shift-left-security-ai-code]]의 세 번째 원칙.

> **AI는 단순히 코드만 생성하는 것이 아니라 의존성(dependencies)도 들여옵니다.** 새로운 패키지, 새로운 라이브러리, 새로운 서비스, 새로운 통합.

## 비대칭 — 능력과 위험이 같이 온다

> **모든 의존성은 능력을 더하고 — 좋은 일이죠 — 모든 의존성은 위험도 더합니다 — 그다지 좋지 않죠.**

리뷰의 시선이 어긋나는 지점이 명확하다:

> 개발자들은 **생성된 소스 코드를 검토하는 데 집중하면서 그 코드가 무엇에 의존하는지는 간과하는 경우가 많습니다.** 이 모든 일이 **AI의 기적 덕분에 눈에 보이지 않는 곳에서** 일어나고 있습니다. **눈에서 멀어지면 마음에서도 멀어지는** 거죠.

**리뷰 대상이 diff이기 때문이다** — 사람이 보는 것은 추가된 코드이고, `import` 한 줄 뒤에 딸려 오는 트리는 보지 않는다.

> **보안 사고는 애플리케이션 로직 자체보다 소프트웨어 공급망(software supply chain)에서 비롯됩니다.**

## 검토 항목 다섯

| 항목 | 묻는 것 |
|---|---|
| **패키지 평판** | 누가 만들고 유지하는가 |
| **취약점** | 알려진 CVE가 있는가 |
| **라이선스** | 이 프로젝트가 쓸 수 있는가 |
| **출처 무결성(source integrity)** | 받은 것이 그 저장소의 것이 맞는가 |
| **조직 표준** | 우리 쪽에서 허용하는 것인가 |

> **AI 지원 개발에서 의존성 검증은 선택 사항이 아닙니다. 그것은 안전한 코드 생성의 일부입니다.**

마지막 문장이 핵심이다 — 의존성 검증을 **별도 단계가 아니라 생성의 일부**로 놓는다. [[shift-left-security]]의 ②와 같은 배치다.

## 이 위키에서의 자리 — 공급망이 처음 들어온다

이 위키의 보안 페이지들은 지금까지 **런타임**을 봤다.

| 기존 페이지 | 보는 것 |
|---|---|
| [[prompt-injection]] · [[lethal-trifecta]] | 실행 중 들어오는 입력 |
| [[confused-deputy-attack]] · [[agent-identity-separation]] | 실행 중 쓰이는 권한 |
| [[credential-injection-outside-sandbox]] | 자격증명이 놓인 위치 |
| [[secure-tool-evolution]] | 도구가 바뀌는 것 |
| **이 페이지** | **빌드 재료의 출처** |

가장 가까운 기존 개념은 [[secure-tool-evolution]]이다 — 둘 다 *내가 쓰기로 한 것이 나중에 다른 것이 되어 있을 수 있다*를 다룬다. 다르게는, [[ai-vulnerability-discovery]]가 보여 준 *발견의 자동화*가 여기서는 **수입(import)의 자동화**로 뒤집혀 나타난다.

## 미해결 사항

- **도구가 없다** — SBOM·SCA·서명 검증 같은 구체적 수단을 소스가 하나도 말하지 않는다.
- **모델이 만든 의존성과 사람이 고른 의존성을 다르게 다뤄야 하는지** 소스가 구분하지 않는다.
- **환각된 패키지명**(존재하지 않는 패키지를 제안해 그 이름이 선점되는 문제)을 언급하지 않는다 — 이 위키에도 아직 소스가 없다.
- **전이 의존성(transitive)** 의 깊이를 어디까지 볼지 없다.

## References

- [[tech-bridge-shift-left-security-ai-code]] · [[jeff-crume]] · [[ibm]]
- 같은 묶음: [[shift-left-security]] · [[continuous-security-validation]]
- 관련: [[secure-tool-evolution]] · [[credential-injection-outside-sandbox]] · [[ai-vulnerability-discovery]] · [[behavior-validated-trust]]
