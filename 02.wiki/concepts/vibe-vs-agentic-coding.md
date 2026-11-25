---
title: "바이브 코딩 vs 에이전틱 코딩 (Vibe Coding vs Agentic Coding) — 짧은 고리와 긴 고리, 작업을 가르는 질문 넷"
type: concept
category: framing
tags: [vibe-coding, agentic-coding, coding-agents, human-review, context-engineering, subagents, guardrails, disposable-software, ibm, andrej-karpathy]
aliases: [vibe coding, 바이브 코딩, agentic coding, 에이전틱 코딩, vibe vs agentic, 두 개의 루프, 짧은 고리와 긴 고리, accept all]
related: [disposable-vs-durable-software, risk-proportional-human-review, action-reversibility, agent-governance-layers, context-engineering, cognitive-offloading, agentic-coding-maturity-curve, tactical-vs-strategic-programming]
first-seen: tech-bridge-grace-ableidinger-vibe-vs-agentic-coding
sources: [tech-bridge-grace-ableidinger-vibe-vs-agentic-coding]
created: 2026-11-25
updated: 2026-11-25
---

# 바이브 코딩 vs 에이전틱 코딩 (Vibe Coding vs Agentic Coding)

**AI로 코드를 짜는 두 방식을 고리(loop)의 길이로 가르는 틀 — 바이브 코딩은 *프롬프트 → 생성 → 반복* 의 짧은 고리, 에이전틱 코딩은 *이해 → 계획 → 실행 → 테스트 → 검증* 의 긴 고리다.** [[grace-ableidinger|Grace Ableidinger]](Red Hat)가 [[ibm|IBM Technology]] 영상에서 라이트보드에 그린 그림이고, 위키에는 [[tech-bridge-grace-ableidinger-vibe-vs-agentic-coding]](2026-11-24 한국어 해설)로 들어왔다. ⚠️ 해설 전달이다 — 화자의 원음은 전부 무캡션이고, 아래 인용은 한국어 내레이션이 화자의 판서 · [[andrej-karpathy|Andrej Karpathy]]의 X 글 · IBM Think 글을 옮긴 것이다. 측정은 없다.

위키의 여러 페이지가 *바이브 코딩* 을 낱말로만 써 왔다. 이 페이지는 그 말의 뜻과 짝이 되는 방식을 한 소스의 정의로 적어 둔다.

## 두 정의

| | 바이브 코딩 | 에이전틱 코딩 |
|---|---|---|
| 정의 | *"주로 프롬프트와 에이아이가 생성한 코드로 소프트웨어를 만드는 방식입니다. 핵심은 속도입니다."*(01:17~01:22) | *"에이전틱 코딩은 AI가 개발자와 함께 일하는 방식입니다. 코드를 만들어 주는 데서 끝나지 않습니다."*(02:53~02:57) |
| 고리 | *"프롬프트를 쓰고 AI가 만들고 다시 고쳐달라고 합니다."*(04:10~04:12) | *"먼저 코드를 이해하고 계획을 세우고 실행하고 테스트하고 마지막에 검증합니다."*(04:18~04:24) |
| 맞는 일 | *"빠른 버그 수정, 새 디자인 시험, 변수 이름 바꾸기 같은 일"*(07:41~07:43) | 새 기능을 프로덕션에 올릴 때 · 데이터베이스나 결제 시스템을 건드릴 때 · 큰 리팩토링(07:47~07:55) |

해설이 짚은 차이: *"결국 두 루프의 차이는 단계수가 아니라 사람이 생각을 보태는 자리가 있느냐입니다."*(04:48~04:51)

## 말의 출처 — Karpathy의 글 (내레이션이 옮김)

*"바이브코딩이라는 말을 만든 사람은 코드를 읽지 않는다고 썼습니다."*(00:00~00:02) AI가 고친 코드는 늘 전부 수락하고 바뀐 부분은 읽지 않으며, 에러가 나면 에러 메시지를 그대로 붙여 넣는다는 것이다. 단서도 그 글에 있다: *"다만 그도 이 방식은 버려도 되는 주말 프로젝트에나 괜찮다고 선을 그었습니다."*(00:13~00:16) 말은 2025년 초에 생겼고 *"뜻은 처음부터 좀 흐릿했다고 합니다."*(00:41~00:43) ⚠️ 위키는 원 글(2025.02.02)을 열지 않았다.

## 스펙트럼 (IBM Think 글, 내레이션이 옮김)

둘은 대립이 아니라 한 줄 위에 있다: *"한쪽 끝은 속도와 탐색이 먼저인 바이브 코딩, 그다음이 역할과 제약을 정해 에이전트를 지휘하는 에이전틱 코딩."*(03:48~03:55) 팀은 보통 바이브 코딩으로 시작해 걸린 것이 커지고 위험해질수록 구조가 갖춰진 쪽으로 옮겨 간다고 한다(03:56~04:01).

## 작업을 가르는 질문 넷

*"이 일의 배경 정보가 얼마나 필요한지, 미리 계획을 세워야 하는지, 결과를 얼마나 꼼꼼히 확인해야 하는지, 그리고 AI에게 얼마나 알아서 하게 둘 건지."*(07:30~07:39) ⚠️ 화자가 낸 원 표현은 무캡션(07:12~07:30)이고 이것은 내레이션이 풀어 옮긴 것이다.

## 긴 고리에 딸린 것 둘

- **걸러 낸 컨텍스트.** *"그래서 목표는 많은 컨텍스트가 아니라 걸러낸 컨텍스트입니다."*(05:33~05:35) 방법은 사람이 확인하는 단계를 더 넣는 것과 서브에이전트 — 서브에이전트가 깊이 파고든 뒤 짧은 요약만 들고 돌아와 *"메인 에이전트는 수많은 파일에 묻히지 않고 계획과 지위에만 집중합니다."*(05:50~05:54)[=지휘] → [[context-engineering]]
- **준 힘만큼의 안전 장치.** 테스트 · 거버넌스 · 관찰 가능성 · 롤백 · 가드레일 다섯 → [[agent-governance-layers]]. *"그리고 에이전트에게 준 힘만큼 안전 장치를."*(08:15~08:17)

## 위키에서의 좌표

- [[disposable-vs-durable-software]] — *버려도 되는 코드 / 남길 코드* 는 같은 가름이다. 그쪽은 네 기준(피해 · 교체 비용 · 의존 · 유지 비용)으로 위치를 정하고, 이쪽은 위치가 정해진 뒤 **어떤 고리로 일할지** 를 말한다(짝짓기는 위키의 읽기).
- [[risk-proportional-human-review]] · [[action-reversibility]] — *되돌릴 수 없거나 비용이 큰 결정에는 사람이 서명* 과 겹친다.
- [[agentic-coding-maturity-curve]] — 그쪽은 조직의 단계, 이쪽은 작업 한 건의 선택이다.
- [[cognitive-offloading]] — 실력 걱정에 대한 IBM 글의 답(*이해를 자동화로 대신하지 말라*).

## ⚠️ 유보

- 한 입문 영상의 틀이다. 측정 · 사례 · 수치가 없고, 고리의 단계 이름은 판서를 내레이션이 옮긴 것이다.
- 컨텍스트가 많으면 왜 나빠지는지(05:08~05:33), 보안 문제의 내용(06:11~06:33), 화자의 마지막 조언(08:34~08:44)은 무캡션이라 이 페이지에 없다.
- *에이전틱 코딩* 의 경계(어디부터가 에이전틱인가)는 소스에 없다 — 스펙트럼이라고만 한다.

## References

- [[tech-bridge-grace-ableidinger-vibe-vs-agentic-coding]] · [[grace-ableidinger]] · [[ibm]] · [[andrej-karpathy]] · [[disposable-vs-durable-software]]
