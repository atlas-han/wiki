---
title: 모델이 그리는 인터페이스 (Model-Rendered Interface)
type: concept
category: pattern
tags: [generative-ui, dynamic-interface, enterprise, code-generation, ux]
aliases: [동적 인터페이스, dynamic interface, generative UI, 생성형 UI]
related: [agentic-sites, adaptive-response-format, persistent-agent-teams, lethal-trifecta, prompt-injection]
first-seen: tech-bridge-altman-benioff-dreamforce
sources: [tech-bridge-altman-benioff-dreamforce]
created: 2026-09-23
updated: 2026-09-23
---

# 모델이 그리는 인터페이스

**미리 만든 애플리케이션 화면 대신, 모델이 사용자의 요청을 이해하고 필요한 데이터를 모은 뒤 그 자리에서 인터페이스 코드를 새로 써서 렌더링하는 방식.** [[tech-bridge-altman-benioff-dreamforce]]에서 [[marc-benioff|Marc Benioff]]가 [[salesforce|Salesforce]] 기조연설 데모로 제시하고 [[sam-altman|Sam Altman]]이 구조를 설명했다.

> **컴퓨터와 대화할 수 있고, 컴퓨터가 사용자의 요구를 이해할 수 있으며, 회사 내부 어디를 살펴봐야 하고 [어디를 살펴보도록 허용되는지] 판단하고 정보를 종합할 수 있다**는 사실이 중요합니다. 음, 그러면 **완전히 새로운 인터페이스를 보여줄 수 있습니다.** 이 시스템은 **1만 줄이든 그 이상이든 필요한 코드를 직접 작성하여** 모든 것을 통합하고, **의사 결정을 내리는 데 필요한 정보를 제공하거나, 다양한 시도를 계속하며 창의적인 과정을 이어갈 수 있도록** 도와줄 수 있습니다. — Altman (28:08~28:36)

⚠️ 대괄호는 ko *"어디를 살펴봐야 하는지, 어디를 살펴봐야 하는지"* 를 en-orig *"where it's allowed to look"* 로 보정한 것. **권한 개념이 ko에서 사라졌다.**

## 네 단계 (Altman의 서술 순서)

| 단계 | 내용 |
|---|---|
| ① 의도 이해 | *"사용자의 요구를 이해"* |
| ② 탐색 + **권한 판단** | 회사 안 **어디를 봐야 하고 어디를 볼 수 있는지** |
| ③ 종합 | 정보를 모아 엮는다 |
| ④ **렌더링** | 인터페이스 코드를 **1만 줄이든 필요한 만큼** 새로 써서 보여준다 → **결정** 또는 **창의적 루프** |

진행자 쪽의 관찰(데모를 본 경험):

> 그것은 제가 이전에 본 어떤 애플리케이션과도 근본적으로 달랐습니다. 왜냐하면 그것은 **실시간으로 역동적이고 지능적으로, 합성적인 방식으로, 마치 살아있는 것처럼 보이는 방식으로 스스로를 렌더링했기 때문**입니다. — Benioff (31:15~31:29)

인터페이스 계보에서의 위치 — *"DOS와 문자 모드, [GUI], 그리고 그 이후 휴대폰 (…) 이제는 모델에 의해 구동되는 이러한 동적 인터페이스"*(27:52~28:00, ⚠️ ko가 GUI 단계를 빠뜨렸다).

## 이 위키에서의 좌표 — 재조립 vs 재생성

| | [[agentic-sites]] (09-01, [[adobe\|Adobe]]) | **이 개념** (09-23) |
|---|---|---|
| 단위 | **블록**을 골라 붙인다 | 인터페이스 **코드를 새로 쓴다** |
| 전체 재생성 | **원하지 않는다** — 브랜드 가이드라인이 환각 예산을 정한다 | **장점**으로 제시 — *"1만 줄이든 그 이상이든"* |
| 그라운딩 | 자기 사이트 | **회사 내부 데이터 전체** |
| 지연 | 1~2초가 1급 지표 | **언급 없음** |
| 사용자 | 외부 방문자 | **사내 직원**(의사 결정자) |

**두 소스를 겹치면 설계 축이 하나 드러난다 — 생성 범위를 어디서 끊느냐.** [[adaptive-response-format]](09-04)은 그 사이 어딘가에서 *응답 형식* 만 모델에게 맡겼다. **세 소스가 같은 스펙트럼의 세 점**이다: 형식 선택 → 블록 재조립 → 전체 재생성.

그리고 같은 대담의 **"세 번째 단계"**(상시 실행 AI, 29:25~30:34)와 이어진다 — 코드를 *"렌더링해 주는"*(en-orig *"rendering new code for you"*) 것이 세 번째 단계의 구성 요소로 다시 나온다. → [[persistent-agent-teams]]

## ⚠️ 유보

- **데모다.** 판매자(Salesforce)의 기조연설이고, 무엇이 실제로 생성되고 무엇이 미리 짜였는지 알 수 없다.
- ⚠️ **보안이 한 단어뿐이다.** *allowed* 가 유일한 권한 언급이고 ko가 그것도 지웠다. **사내 데이터를 모아 1만 줄의 생성 코드로 렌더링하는 구조**는 [[lethal-trifecta]]의 세 요소(사적 데이터 접근 · 신뢰할 수 없는 콘텐츠 · 외부 통신)를 쉽게 갖춘다. [[prompt-injection]]·생성 코드의 검증·감사 로그가 **한 번도 나오지 않는다** — **같은 대담이 [[hugging-face|Hugging Face 사건]]을 20분 이야기한 뒤다.**
- **매번 새로 쓰면 재현성이 없다.** 같은 질문에 다른 화면이 나오는 것을 결정 도구로 쓸 때의 문제 — 소스는 다루지 않는다.
- **비용·지연** 없음.
- *"10배 더 빠르고 효율적"*(28:58~29:02) — Benioff의 체감, 측정 없음.

## References

- [[tech-bridge-altman-benioff-dreamforce]]
- [[marc-benioff]] · [[salesforce]] · [[sam-altman]]
- 관련: [[agentic-sites]] · [[adaptive-response-format]] · [[persistent-agent-teams]] · [[lethal-trifecta]] · [[prompt-injection]]
