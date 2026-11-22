---
title: Comments
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-11-22
category: pattern
related: [code-smells, refactoring-techniques, technical-debt, codebase-gardening]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring, tech-bridge-lauren-tan-all-code-is-slop, tech-bridge-pocock-21k-lines-questions-before-code]
---

# Comments

메서드가 설명적 주석으로 가득 차, 주석이 직관적이지 않은 코드의 문제를 가리는 데오도란트(deodorant) 역할을 하는 상태. [[code-smells]] 중 **Dispensables(불필요한 것)** 계열이다.

## 신호와 증상
- 메서드 안이 "이 부분은 무엇을 한다"는 설명 주석으로 빽빽하다.
- 주석을 먼저 읽어야 코드가 이해되며, 주석을 지우면 의도를 알 수 없다.
- 주석이 복잡한 표현식·코드 블록의 의미를 대신 설명하고 있다.

## 원인
- 작성자가 코드가 직관적이지 않다고 느낄 때 주석을 덧붙인다.
- 주석은 개선이 필요한 나쁜 코드의 냄새를 덮는 향수처럼 쓰인다. 가장 좋은 주석은 메서드·클래스의 좋은 이름 그 자체다.

## 해결 방법 (Treatment)
- `Extract Variable` — 복잡한 표현식을 이해하기 쉬운 이름의 부분 표현식으로 쪼개 주석을 대체한다.
- `Extract Method` — 주석으로 구분하던 코드 블록을 별도 메서드로 추출하고, 주석 내용을 메서드 이름으로 옮긴다.
- `Rename Method` — 메서드가 하는 일을 설명하던 주석을 자명한 이름으로 흡수한다.
- `Introduce Assertion` — "여기서는 이 상태여야 한다"는 설명 주석을 코드로 강제되는 단언으로 바꾼다.

## 이득 (Payoff)
- 코드가 더 직관적이고 명확해진다.
- 이름과 구조가 의도를 드러내므로 주석을 따로 유지·동기화할 필요가 줄어든다.

## 무시해도 될 때
특정 구현을 왜 그렇게 했는지(WHY)를 설명하는 주석, 또는 다른 모든 단순화 시도가 실패한 복잡한 알고리즘을 설명하는 주석은 남겨두는 것이 좋다.

## References
- [[refactoring-guru-refactoring]] — Comments 원문: https://refactoring.guru/smells/comments
- [[code-smells]]

## 에이전트 시대의 판본 — 주석은 베껴도 된다는 허가 (2026-11-17 · [[tech-bridge-lauren-tan-all-code-is-slop]])

[[lauren-tan|Lauren Tan]]의 발표 해설에서 [[grokbot|GrokBot]] 팀은 주석의 99%를 금지했다(슬라이드 65,824 → 1,227, 팀 자체 집계). 계기는 Cursor의 *타이머 183개* 사건 — 임시방편 옆의 주석이 *이건 괜찮다* 고 설명해 주자 다음 에이전트들이 안심하고 베꼈다. 처방은 이 페이지의 Treatment와 같은 방향이되 대상이 다르다: *"주석이 말하던 제약이 진짜라면 주석이 아니라 타입이나 검사로 옮겨 적으라는 겁니다."*(05:49~05:53) 사람에게 주석은 낡는 설명이고 에이전트에게는 **관례로 읽히는 입력** 이다(위키의 정리). → [[codebase-gardening]] · [[hard-vs-soft-enforcement]]

⚠️ 한 팀의 사례다. 금지 뒤의 수치(되돌린 커밋 비율 0.98% → 0.47%)는 주석 금지만의 효과로 분리되지 않는다.

## 2026-11-22 — 에이전트가 쓴 2만 줄의 주석 감사: 2,053줄 중 940줄쯤 ([[tech-bridge-pocock-21k-lines-questions-before-code]])

[[matt-pocock|Matt Pocock]]이 에이전트가 쓴 21,349줄 PR을 리뷰하며 남긴 코멘트는 대부분 주석 이야기였다(한국어 해설 전달, 수치는 해설이 화면에서 읽은 값).

- 이유: *"주석은 에이전트가 함께 고쳐야 할 표면만 넓히고 코드가 이미 말하는 걸 되풀이한다는 겁니다."*(09:52~09:56)
- 비율: *"주석은 저장소 평균이 12%인데 새 기능 폴더는 18%였습니다."*(11:06~11:09)
- 감사 결과: *"새 기능 폴더의 주석 2053주 가운데 940줄쯤은 지금 지워도 되고 일곱 개는 이미 코드와 맞지 않는다는 결과였습니다."*(11:13~11:20)[=2,053줄]
- 남는 주석의 분류(더 공격적으로 보라고 한 뒤): *"22개는 그냥 지우면 되고 18개는 주석이 감싸던 우회 코드 자체를 고쳐야 하고 세 개는 ADR로 옮길 만하다고요."*(12:05~12:11) ⚠️ 세는 단위는 캡션에 없다.

11-17의 GrokBot 사례(99% 금지)와 견주면 방향은 같고 방법이 다르다 — 금지가 아니라 **감사와 분류** 다. *우회 코드를 감싸던 주석은 주석이 아니라 코드를 고친다* 는 항목은 이 페이지 본문의 *데오도란트* 정의 그대로이고, *ADR로 옮긴다* 는 항목은 지식이 사는 자리를 주석에서 결정 기록으로 옮기는 것이다. ⚠️ 에이전트는 *다 지우면 잃는 지식이 있다* 고 버텼다 — 무엇이 남았는지는 소스에 없다.
