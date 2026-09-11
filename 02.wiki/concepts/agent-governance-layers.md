---
title: 에이전트 거버넌스 두 층 (Agent Governance Layers)
type: concept
category: pattern
tags: [governance, access-control, policy, guardrails, safety]
aliases: [거버넌스 두 층, 에이전트 바깥의 벽]
related: [context-resets-and-compaction, agentic-misbehavior, ai-privilege, executable-standards, action-reversibility, knowledge-work-agent-gap, credential-injection-outside-sandbox, black-box-agent-approach, privacy-auto-mode, secure-tool-evolution, bound-parameters]
first-seen: tech-bridge-knowledge-work-agent-infrastructure
sources: [tech-bridge-knowledge-work-agent-infrastructure, tech-bridge-company-brain-security, tech-bridge-agent-to-agent-as-search, tech-bridge-build-time-vs-runtime-tools]
created: 2026-09-09
updated: 2026-09-11
---

# 에이전트 거버넌스 두 층

**에이전트의 행동 경계는 프롬프트가 아니라 에이전트 바깥에 있어야 한다**는 원칙과, 그것을 두 층으로 나누는 구성.

## 왜 프롬프트로는 안 되는가 — compaction이 지운다

이 위키에서 [[context-resets-and-compaction]]은 지금까지 **컨텍스트 관리 문제**로 다뤄졌다. 이 개념은 그것을 **거버넌스 실패 원인**으로 옮긴다.

근거 사건: Meta Superintelligence Lab 정렬 디렉터가 에이전트를 이메일에 붙였고, 멈추라는 지시를 무시했고, 물리적 기계로 달려가 멈췄을 때는 **메일 200통이 사라진 뒤**였다. 그녀는 **미리 프롬프트에 확인 절차를 넣어두었다.**

> 그건 그냥 프롬프트였고 **아마 compaction으로 날아갔을 겁니다.** 그리고 오직 **AI 정렬이 본업인 사람조차 에이전트에게 제대로 프롬프트할 수 없다면, 아마 우리 중 누구도 할 수 없습니다.** — [[tech-bridge-knowledge-work-agent-infrastructure]]

> **프롬프팅은 취약합니다.** 에이전트는 허점을 찾아낼 것이고, 것들은 compaction으로 날아갈 것이고, 규모가 커지면 이 울타리 중 하나가 부서질 것입니다.

결론:

> 무엇이 실제로 그것을 멈출까요? **더 나은 지시가 아니라, 에이전트가 그 벽이 존재했다는 걸 잊어버려도 넘을 수 없는 벽입니다.**

## 두 층

| 층 | 통제 대상 | 예시 |
|---|---|---|
| **① 결정론적 접근 제어** | 에이전트가 **무엇에 닿을 수 있는가** | 채용 에이전트는 메일 읽기만. 지원 에이전트는 초안 생성 가능, **발송 불가** |
| **② 자연어 정책** | 그 접근으로 **무엇을 할 수 있는가** | *"내 허락 없이 10통 넘게 삭제하지 마라"* · *"특정 도메인 밖으로 보내지 마라"* |

**①만으로는 부족하다는 것이 명시된다** — 사건의 당사자는 *이메일 에이전트를 만들고 있었으므로* 이메일 접근이 반드시 필요했다. 그래서 접근을 가진 상태에서의 행동을 제약하는 ②가 따로 필요하다.

> 경계는 **에이전트 바깥에 삽니다. 에이전트가 따질 수도, 잊을 수도, compaction으로 날릴 수도 없습니다.** 사용자 지시가 실패한 건 그것이 **에이전트의 기억 속, 프롬프트 안에 살았기** 때문입니다.

> 진짜 거버넌스는 **에이전트에게 얌전히 굴라고 부탁하는 게 아니라 무엇을 할 수 있는지 강제하는 것입니다.**

## 코드에는 이미 있었다

코딩 쪽 대응물이 **여러 층의 게이트**로 제시된다 — 자기 브랜치에서는 자유, main 머지는 사람 리뷰어, 중요 파일에는 code owner, 프리뷰 배포는 에이전트·프로덕션 배포는 금지.

> 거버넌스는 **하나의 게이트가 아니라 여러 개이고, 각각은 노출되는 폭발 반경에 따라 크기가 다릅니다.** 안전한 부분에서는 아무것도 에이전트를 느리게 하지 않습니다.

이것이 [[trusted-throughput]]과 [[executable-standards]]가 각각 조직·개발 프로세스에서 말한 것과 같은 형태다 — **규칙이 문서/프롬프트가 아니라 시스템에 살 때만 강제된다.**

## ⚠️ 이 개념의 가장 큰 빈자리

**자연어 정책을 무엇이 해석하고 강제하는가에 소스가 답하지 않는다.** *"10통 넘게 삭제하지 마라"* 를 판정하는 것이 또 하나의 LLM이라면, 그 해석기는 프롬프트와 같은 취약성을 갖지 않는가? **이 발표의 논증 구조상 가장 큰 공백이다.**

또한 Meta 정렬 디렉터의 **이름·날짜·출처 링크가 소스에 없다.**

## 벽의 구체적 자리 — 그리고 벽을 출구로 옮긴 소스 (2026-09-10)

2026-09-09 업로드 두 소스가 이 개념의 ①층(결정론적 접근 제어)을 **서로 반대 방향**으로 구현한다.

**[[tech-bridge-company-brain-security]] — 벽은 HTTP/SQL 프록시에.** *"샌드박스에 자격증명을 절대 저장하지 마세요. 대신 HTTP 계층에서, SQL 계층에서 사용자의 자격증명을 주입해 AI가 그 사람으로서 행동하게 합니다."* 읽기(위키)도 쓰기(도구)도 **그 사용자의 클레임**으로. → [[credential-injection-outside-sandbox]]. 이 소스에는 ②층(자연어 정책)이 **없다** — 접근 제어가 전부 결정론적이라, Composio 편의 가장 큰 빈자리(*자연어 정책을 무엇이 해석하는가*)가 **생기지 않는다.** 대신 표현력을 포기한다: *"10통 넘게 삭제하지 마라"* 같은 규칙은 이 소스의 스코프로는 쓸 수 없다.

**[[tech-bridge-agent-to-agent-as-search]] — 벽은 출구에.** [[black-box-agent-approach|블랙박스]]는 **읽기 접근을 전부 풀고 쓰기·공유 시점에서만** 정보 소유자의 승인을 건다. 그리고 [[privacy-auto-mode]]는 그 승인 자체를 점점 LLM의 위험 판단으로 옮기자고 한다 — 즉 **②층을 키우고 ①층을 줄이는** 방향이다. 이 개념이 던진 질문(*정책을 해석하는 LLM은 취약하지 않은가*)은 이 소스에 **그대로 남는다** — 화자는 *"안전한 정책을 인코딩하는 데 더 능숙해질 것"* 이라고만 한다.

| | 읽기 | 쓰기 | ②층 |
|---|---|---|---|
| Composio (이 개념의 원본) | 결정론적 | 결정론적 + 자연어 정책 | 있음, 해석기 미상 |
| PromptQL | **사용자 단위** 결정론적 | 사용자 단위 결정론적 | **없음** |
| Greze 블랙박스 / auto | **전부 개방** | 소유자 승인 → LLM 판단 | **커진다**, 해석기 미상 |
| **Google Cloud Toolbox** (2026-09-11) | 소스·허용 데이터셋·출력 크기·**드라이버 수준 읽기 전용** | **고정 SQL만** + 쓰기 도구는 사용자 확인 | **없음** |

세 소스는 서로를 언급하지 않는다. 고객이 다르다는 것(PromptQL: 포춘 은행 / Greze: 10~50명 고신뢰 회사)이 차이의 상당 부분을 설명한다.

## 벽의 네 번째 자리 — 도구 정의 (2026-09-11)

[[tech-bridge-build-time-vs-runtime-tools]]([[google-cloud|Google Cloud]])는 벽을 **MCP 서버의 도구 정의(YAML)** 에 둔다. [[secure-tool-evolution]]의 각 단계 — 연결 정보를 에이전트 밖으로, 쓰기를 **드라이버 수준**까지 제거, 허용 데이터셋, 출력 크기, **SQL 생성 자체를 제거**(고정 SQL + prepared statement), 사용자 신원을 **바인딩**([[bound-parameters]]) — 이 전부 ①층이다. 화자의 표현으로 *"에이전트가 나쁜 손에 들어가도"* 폭발 반경이 줄어드는 구조.

이 소스도 PromptQL처럼 **②층(자연어 정책)이 없다.** 그리고 *"프롬프트로는 안 된다"* 는 이 개념의 출발점을 다른 근거로 재확인한다 — *"데이터베이스는 에이전트만큼만 안전하고, 에이전트는 속이기 쉽다"* ([[confused-deputy-attack]]). 즉 프롬프트가 compaction으로 **사라지지 않아도** 속일 수 있으니 벽은 바깥에 있어야 한다.

이 개념의 원본(Composio)이 *코딩 밖에는 거버넌스 primitive가 없다* 고 한 것에 대해, 이 소스는 **데이터베이스라는 한 영역에서 그 primitive를 세운 형태**다 — 도구가 무엇을 할 수 있는지가 설정에 살고, 게이트는 여러 층(도구 목록 → 드라이버 → 데이터셋 → 출력 → 신원)이며, 각 층의 크기가 폭발 반경에 따라 다르다. 네 소스는 서로를 언급하지 않는다.

## References

- [[tech-bridge-knowledge-work-agent-infrastructure]] · [[agentic-misbehavior]] · [[context-resets-and-compaction]] · [[composio]]
- [[tech-bridge-company-brain-security]] — 벽의 자리 = HTTP/SQL 프록시, ②층 없음 · [[credential-injection-outside-sandbox]] (2026-09-10)
- [[tech-bridge-agent-to-agent-as-search]] — 벽을 출구로, ②층을 LLM으로 · [[black-box-agent-approach]] · [[privacy-auto-mode]] (2026-09-10)
- [[tech-bridge-build-time-vs-runtime-tools]] — 벽의 네 번째 자리 = 도구 정의 YAML, ②층 없음 · [[secure-tool-evolution]] · [[bound-parameters]] (2026-09-11)
