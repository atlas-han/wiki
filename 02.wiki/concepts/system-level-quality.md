---
title: 시스템 단위 품질 평가 (System-Level Quality)
type: concept
category: practice
tags: [code-review, distributed-systems, ripple-effect, architecture]
aliases: [시스템 단위 평가, 파일 단위 리뷰]
related: [decision-quality, behavior-validated-trust, agent-distributed-systems, surgical-edits, code-knowledge-graph]
first-seen: tech-bridge-ai-era-code-quality
sources: [tech-bridge-ai-era-code-quality, tech-bridge-lauren-tan-trusting-agents]
created: 2026-09-09
updated: 2026-09-13
---

# 시스템 단위 품질 평가

**리뷰 단위가 파일에서 시스템으로 옮겨가야 한다**는 주장.

> 수년간 우리는 소프트웨어를 **파일별로 하나씩** 검토해 왔습니다. 누군가 PR을 열고, 변경된 파일을 검토하고, 댓글을 남기고, 승인하고, 병합합니다. **하지만 현대 소프트웨어는 더 이상 개별 파일 안에 존재하지 않습니다.** — [[tech-bridge-ai-era-code-quality]]

## 한 변경이 닿는 표면

**API · 인프라 · 이벤트 스트림 · 데이터 계약 · 클라우드 리소스 · 모니터링 · 보안 · 정책 · 수십 개의 다운스트림 서비스.**

> 어느 하나의 아주 작은 수정도 **분산 시스템 전체로 파급될 가능성이 큽니다.**

## 질문이 바뀐다

| 이전 | 이후 |
|---|---|
| **이 함수가 올바른가?** | **이 변경이 플랫폼 전체에 걸쳐 어떤 영향을 미칠 것인가?** |

> AI는 코드를 생성할 수 있지만, **시스템을 이해해야 하는 것은 여전히 엔지니어입니다.**

## 이 위키에서의 자리

[[tech-bridge-agents-as-distributed-systems|TikTok 편]]이 *에이전트를 분산 시스템으로 보는* 관점을 놓았다면, 이 페이지는 **에이전트가 만지는 코드를 분산 시스템으로 보는** 관점이다. 둘은 같은 렌즈를 서로 다른 대상에 댄다.

그리고 [[surgical-edits]]가 말한 *작은 변경의 미덕* 에 단서를 붙인다 — **변경이 작다는 것이 파급이 작다는 뜻은 아니다.** [[code-knowledge-graph]]가 다룬 *코드베이스 전체 구조를 에이전트가 갖는 것* 이 이 요구에 대한 한 가지 대응이다.

## ⚠️ 미해결

- **파급 범위를 무엇이 계산하는가에 답이 없다.** 시스템 단위로 평가해야 한다는 당위만 있고 도구·방법이 제시되지 않는다.
- **리뷰 비용의 증가**가 다뤄지지 않는다 — 모든 PR을 시스템 단위로 평가하면 무엇이 느려지는가.

## References

- [[tech-bridge-ai-era-code-quality]] · [[ibm]] · [[decision-quality]]
