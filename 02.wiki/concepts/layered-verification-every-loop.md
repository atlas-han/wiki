---
title: "루프마다 다층 검증 (Zero-Trust Layered Verification)"
type: concept
category: pattern
tags: [verification, zero-trust, defense-in-depth, deterministic-checks, agentic-review, supply-chain-security, ci, software-factory]
aliases: [zero trust multi-layered verification, 다층 검증, 루프마다 검증, layered verification]
related: [swiss-cheese-defense-in-depth, automated-code-review, verification-bottleneck, software-factory, agent-verification-skill, three-level-agent-review, generator-evaluator-pattern, agent-plus-program-analysis]
first-seen: tech-bridge-anthropic-30k-merges-verification
sources: [tech-bridge-anthropic-30k-merges-verification, tech-bridge-anthropic-code-review-seven-layers]
created: 2026-10-31
updated: 2026-11-08
---

# 루프마다 다층 검증

**에이전트 산출물을 어느 한 검사도 믿지 않는다(zero trust)는 전제 아래, 결함 유형마다 맞춘 검증 층을 여러 겹 깔고, 그 묶음을 에이전트 루프 · CI 루프 · 유지보수 루프 모두에 둔다**는 패턴. [[manish-kapur]](추정)가 [[tech-bridge-anthropic-30k-merges-verification]]에서 말한 것이다.

> *"each company should adopt a zero trust multi-layered verification approach. And verification should be done in every loop. Whether you're operating inside the agentic loop or whether you're working inside the CI verification loop or whether you doing code maintenance."*(06:27~06:40)

## 세 층 — 각 층은 다른 결함을 잡는다

| 층 | 잡는 것 (en-orig) | 비고 |
|---|---|---|
| ① 결정론적 | *"bugs, security issues, things like sequel injection, buffer overflow bugs"*(06:59~07:03, ASR → SQL injection) | 정적 분석 · 린트류(위키의 독해) |
| ② 에이전트 리뷰 | *"logic and intent issues which the deterministic layer is not well suited to catch"*(07:15~07:20) | [[automated-code-review]] |
| ③ 소프트웨어 공급망 보안 | *"all the CVEs, all your malware detection happens, all your malicious package detection"*(07:30~07:36) | 의존성 · 패키지 |

> *"each layer is tuned and optimized to catch a certain type of issue."*(07:42~07:45)

설계 원리는 **분업**이다: 결정론 층이 못 잡는 의도 · 논리를 에이전트 층이, 둘 다 보지 않는 외부 코드 위험을 공급망 층이 맡는다. 같은 대담에서 [[addy-osmani]]가 말한 Anthropic의 *"end-to-end tasks, property tests, any visual verification tests"*(06:15~06:23)는 이 표의 ① · ②와 별개인 **동작 검증** 축이다 → [[agent-verification-skill]].

정리 발언(진행 쪽 추정): *"you need to put in independent automated verification inside each loop of your factory. Make sure that you can trust the output that the factory is producing."*(10:56~11:04) — "independent"가 핵심어다. 생성자와 다른 검증자라는 점에서 [[generator-evaluator-pattern]]과 같은 편이다.

## 이 위키의 다른 층 모델과의 관계

- [[swiss-cheese-defense-in-depth]]: 같은 *여러 겹* 발상의 AI 안전판. 그쪽은 모델 위험, 이쪽은 **코드 변경**의 결함을 겨냥한다.
- [[three-level-agent-review]]: *실패 유형마다 검토 하나* 라는 같은 원리를 에이전트 산출물 검토 안에서 쓴다. 이쪽은 결정론 도구와 공급망 스캐너까지 섞는다.
- [[agent-plus-program-analysis]]: ① + ②를 한 시스템으로 묶는 사례.
- [[software-factory]]: *"verification should be done in every loop"* 은 공장을 *"harnessing loops at scale"* 로 정의한 것과 짝을 이룬다 — 루프가 단위라면 검증도 루프 단위다.

## ⚠️ 유보

- 화자 귀속은 설명란 + 소거법 추정이고 소속 미상. *"So we look at it in terms of layers"*(06:50~06:51)의 "we"가 어느 회사 · 제품인지 발화되지 않는다.
- 층별 효과 · 오탐률 · 비용 수치가 없다. 세 층 목록은 *"could be"*(07:27)로 시작해 예시에 가깝다.
- 07:45~07:48에서 발언이 끊긴다(편집 컷 추정) — 뒤에 더 있었을 수 있다.

## 7겹 리뷰 — Swiss cheese로 읽기 (2026-11-08 · [[tech-bridge-anthropic-code-review-seven-layers]])

한국어 해설이 Claude Code 팀의 층을 일곱으로 센다: ① PR 전 자기 검증 + 새 맥락의 두 번째 에이전트 ② 모든 PR의 AI 리뷰(지적마다 다른 에이전트 그룹이 투표) ③ 보안 리뷰 ④ 필수 자동 검사 ⑤ 위험도별 사람 승인 ⑥ 머지 · 기능 플래그 ⑦ 빠른 감지 · 롤백.

- ⭐ *"각층이 일부 문제를 잡고 일부는 놓칩니다. 끝까지 뚫고 나가는 건 아주 적고 그건 롤백기[=롤백이] 처리하죠."*(04:01~04:06)
- 시점: 관문이 아니라 *맞춤법 검사처럼 코드를 쓰는 내내* 돈다.
- 속도: *천천히 가면 에러율이 낮아지지만 일을 덜하기 때문*이라는 동료의 말 → 더 빨리 발견하고 고치는 쪽.
- ⚠️ 해설 전달. 2층 효과 16% → 54%는 위키 첫 기록, 미대조.

## References

- [[tech-bridge-anthropic-30k-merges-verification]]
