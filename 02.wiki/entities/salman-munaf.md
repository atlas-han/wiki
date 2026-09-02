---
title: Salman Munaf
type: entity
category: person
tags: [tiktok, distributed-systems, agent-reliability]
links:
  - https://www.linkedin.com/in/salman96/
sources: [tech-bridge-agents-as-distributed-systems]
created: 2026-09-02
updated: 2026-09-02
---

# Salman Munaf

[[tiktok|TikTok]] 소속 엔지니어. 본 위키 첫 등장은 [[tech-bridge]] 재배포 강연 [[tech-bridge-agents-as-distributed-systems]] (2026-09-02).

## 위키에서 알려진 사실

- 이 위키에 [[agent-distributed-systems]] 관점을 들여온 소스의 발표자. 테제는 **"에이전트가 부작용을 낼 수 있게 된 순간 그것은 분산 시스템 문제"**.
- 가장 이식성 높은 한 줄: *"타임아웃이 발생했다고 해서 실제로 오류가 발생한 것은 아닙니다. 이는 **알 수 없음**을 의미"* — 요청 ID·멱등성 키·상태 조회를 요구하는 근거.
- 에이전트를 **확률적 코디네이터**로 규정하고, 기존 조율 서비스가 결정론적이었다는 점을 대비시킨다. 처방은 **결정론적 통제 장치**로 행동 집합을 미리 자르는 것.
- **컨텍스트 = 상태** 논증: *"그러한 맥락이 행동에 영향을 미칠 수 있다면 그것은 상태"* → 메모리를 **무효화 가능하고 출처가 붙는 캐시**로 다뤄야 한다.
- 승인 설계 원칙: 승인은 **동작·타임스탬프·행위자·만료 시간**에 묶여야 하며, 30달러 환불 승인이 300달러 환불로 재사용되면 안 된다.
- 모델 개선의 한계를 명시 — 좋은 모델은 오류를 줄이지만 **네트워크 오류·stale 데이터·악의적 입력은 제거하지 못한다.**

> 강연은 Replit 프로덕션 DB 삭제, Air Canada 챗봇 오환불을 예시로 들지만 이는 **공개 보도 사례에 대한 발표자의 사후 해석**이고 독립 조사가 아니다.

## References

- [[tech-bridge-agents-as-distributed-systems]] — 19:19, 2026-09-02
