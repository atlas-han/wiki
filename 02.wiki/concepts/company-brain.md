---
title: 회사 두뇌 (Company Brain)
type: concept
category: pattern
tags: [company-brain, wiki, shared-context, access-control, knowledge-base, coding-agent]
aliases: [company brain, 사내 두뇌, 사내 AI 지식 베이스]
related: [llm-wiki-pattern, agent-memory, agent-knowledge-sourcing, no-silent-write, named-human-accountability, credential-injection-outside-sandbox, multiplayer-agent-context, knowledge-work-agent-gap, sweeper-agent]
first-seen: tech-bridge-company-brain-security
sources: [tech-bridge-company-brain-security, tech-bridge-agent-to-agent-as-search, tech-bridge-vercel-eve-filesystem-agent]
created: 2026-09-10
updated: 2026-09-19
---

# 회사 두뇌

**조직의 공유 컨텍스트를 서로 링크하는 마크다운 파일로 두고, 데이터·도구 접근 제어 규칙과 함께 코딩 에이전트에게 주는 것.** [[tanmai-gopal]]([[promptql]])의 정의이며, 이 위키의 [[llm-wiki-pattern]]을 **조직 규모로 옮긴 형태**다.

> 회사 두뇌란 — **마크다운 파일 묶음에 넣을 공유 컨텍스트**, 그리고 **접근하려는 여러 데이터와 도구에 대한 접근 제어 규칙**을 **코딩 에이전트에게 준 것**입니다. — [[tech-bridge-company-brain-security]]

## 정의에서 배제된 것

정의만큼 **아닌 것**이 명시된다.

| 아니다 | 이다 |
|---|---|
| LLM에 끌어다 넣어 도구 호출을 하게 하는 지식 | 코딩 에이전트가 읽을 **파일** |
| 범용 AI | *"당신이 던지는 어떤 문제든 푸는 **코딩 에이전트**"* |
| 회사를 위한 거대한 지식 그래프를 만들고 나서 보호하는 것 — *"작동한 적 없고 앞으로도 안 된다"* | 각 사람이 **자기 몫을 키우는** 것 |

근거는 제품 관찰이다 — *"Claude Code가 모든 것에 쓰인다. Claude Cowork도, Codex 앱도 같은 아키텍처."* 즉 [[tech-bridge-knowledge-work-agent-infrastructure|Composio 편]]이 *코딩 에이전트는 인프라 덕에 된다* 고 진단한 자리에서, 이 개념은 **그 에이전트를 그대로 쓰고 회사 지식을 그것의 입력 형식(마크다운)에 맞추자**는 처방이다.

## 키우는 것이지 만드는 것이 아니다

> 100년 된 조직의 회사 두뇌는 만들 수 없어요. **자기 가족 것도 겨우 만들까 말까**인데. (…) **회사에서 일의 일부를 하는 각 사람이 회사 두뇌의 자기 몫을 소유하고 만드는** 것입니다.

→ 이것이 [[agent-org-adoption]]의 *"에이전트 우선 재설계는 가장 흔한 실수"* 와 같은 결의 진술이다 — 2년짜리 프로젝트가 아니라 **셀프 서비스 누적**.

## 건강의 지표 — 일일 업데이트 수

이 위키가 본 **지식 베이스 건강의 첫 정량 지표** 제안이다.

> 잘 작동하는 회사 두뇌의 **일일 업데이트 수**를 그래프로 그리면 — 하강할까요, 안정적일까요, 꾸준히 증가할까요? **공유 스킬 저장소의 커밋 히스토리**가 어떤 모양일지 생각해 보세요.

발표자의 자사 2개월 데이터는 **완만한 상승**이었고, 해석은 *"작동하기 시작하는 시스템이 있으면 사람들이 훨씬 더 많이 가르친다"* + *"어떤 학습도 완벽하지 않으니 각각의 일정한 비율이 더해진다"*. 하강은 *첫날 열정 뒤 방치*, 안정은 *자동 학습이 열정에 따라 오르내림*.

⚠️ 자사·2개월·수치 없음·화자 유보. 그리고 **업데이트 수는 품질을 재지 않는다** — 같은 날 [[tech-bridge-agent-to-agent-as-search|Greze 편]]이 말한 *영구 오염* 은 이 지표에 잡히지 않는다.

## 세 구성 요소

[[tech-bridge-company-brain-security]]가 채택한 셋째 선택지의 요소:

1. **서로 링크하는 마크다운** — 폴더에 사일로화하지 않는다.
2. **파일별 읽기/쓰기 스코프** — 재무·개인 등. 에이전트는 **그 사용자의 클레임으로** 읽는다 → [[credential-injection-outside-sandbox]].
3. **자동 추가 금지** — 에이전트는 스코프와 함께 **제안**만, 사람이 **이름을 걸고** 수락/거부 → [[no-silent-write]] · [[named-human-accountability]].

그리고 두 사용 사례 — **개인**(남의 지식이 내 에이전트로) / **멀티플레이어**(여러 사람이 공유 컨텍스트로, 서로 다른 권한으로) → [[multiplayer-agent-context]].

## [[llm-wiki-pattern]]과의 차이

| | [[karpathy-llm-wiki-gist|Karpathy LLM Wiki]] | 회사 두뇌 |
|---|---|---|
| 규모 | 개인 | 조직(자사 5,000페이지) |
| 쓰는 주체 | LLM이 위키를 전담 관리, 사람은 큐레이션 | **사람이 승인**, 에이전트는 제안 |
| 접근 제어 | 없음 | **파일별 스코프**, 사용자 클레임으로 읽기 |
| 저자 표기 | 없음 | **모든 변경에 사람 이름** |
| 건강 지표 | lint(모순·고아) | **일일 업데이트 수** |

즉 개인 위키에서 조직 위키로 갈 때 더해지는 것은 **누가 볼 수 있는가**와 **누가 책임지는가**다.

## 같은 날의 이웃 개념

[[tech-bridge-agent-to-agent-as-search|Greze 편]]의 **공유 사일로**(전략 3)가 같은 물건을 다른 이름으로 부른다 — *"회사 안에 데이터가 쌓이는 새 장소, 모든 에이전트가 접근"*. 그리고 그것을 채우는 방식으로 [[sweeper-agent]]를 제안한다 — 회사 두뇌의 **입력 파이프라인** 후보다. 두 소스는 서로를 모른다.

## ⚠️ 미해결

- 스코프의 정의·충돌·운영 주체.
- 5,000페이지에서의 **검색·lint** — 언급 없음. (SRE 사례의 *"페이지 이름 접두사가 조회 문제를 일으킨다"* 가 유일한 운영 힌트다.)
- **틀린 항목의 정정** — 사람이 승인한 사실이 나중에 틀리면? Greze 편의 Apex/Ivy가 그 실패 형태다.
- 당사자 진술 — 발표자는 이것을 파는 회사의 창업자다.

## 같은 방향, 다른 형식 — 에이전트가 grep하는 회사 지식 (2026-09-19)

[[tech-bridge-vercel-eve-filesystem-agent]]가 이 페이지와 **서로를 모른 채 같은 결론**에 닿는다 — 조직에서 에이전트를 쓸모 있게 만드는 것은 모델이 아니라 **조직이 쌓은 맥락**이다. [[vercel|Vercel]]은 기성 수직 에이전트 스타트업들을 테스트한 뒤 이렇게 결론짓는다:

> **우리 에이전트를 진정으로 돋보이게 하는 것은 매우 구체적인 회사 지식을 활용하는 것**이라는 사실을 알게 되었습니다. … **어떤 데이터를 언제 쿼리해야 하는지, 어떤 요소들이 서로 어떻게 연결되는지** … (15:02~15:37)

→ [[company-knowledge-moat]]

**형식이 다르다:**

| | **company-brain** ([[promptql\|PromptQL]], 09-10) | [[company-knowledge-moat]] ([[vercel\|Vercel]], 09-19) |
|---|---|---|
| 지식의 형태 | **사람이 읽는 위키** (5,000페이지) | **에이전트가 grep하는 시맨틱 레이어** |
| 갱신 | 에이전트 제안 → **사람 승인**([[named-human-accountability]]) | 질의 증류([[query-to-skill-distillation]]) |
| 접근 제어 | 파일별 스코프 | ⚠️ **없음 — 소스가 다루지 않는다** |
| 목적 | 조직의 기억 | 에이전트의 성능 |

세 번째 행이 이 대조의 핵심이다. 이 페이지가 개인 위키에서 조직 위키로 갈 때 더해지는 것으로 꼽은 두 가지(*누가 볼 수 있는가* · *누가 책임지는가*)가 **Vercel 편에는 둘 다 없다** — 시맨틱 레이어 전체를 샌드박스에 붓고 [[no-silent-write]]에 해당하는 게이트도 두지 않는다.

## References

- [[tech-bridge-company-brain-security]] (first-seen) · [[tanmai-gopal]] · [[promptql]]
- [[tech-bridge-agent-to-agent-as-search]] — 공유 사일로·청소부 AI
- 관련: [[llm-wiki-pattern]] · [[agent-memory]] · [[agent-knowledge-sourcing]] · [[knowledge-work-agent-gap]]
