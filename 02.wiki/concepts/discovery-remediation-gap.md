---
title: "찾기와 고치기의 속도 차 (Discovery–Remediation Gap)"
type: concept
category: theory
tags: [security, vulnerability-discovery, patching, coordinated-disclosure, asymmetry, machine-speed]
aliases: [찾는 속도와 고치는 속도, find-fix gap, 버그 하나에 두 달, discovery-remediation gap]
related: [ai-vulnerability-discovery, coordinated-vulnerability-disclosure, defense-factory, defenders-window, verification-cost-asymmetry, verification-bottleneck]
first-seen: tech-bridge-openai-gpt-6-cyber-keynote
sources: [tech-bridge-openai-gpt-6-cyber-keynote]
created: 2026-11-14
updated: 2026-11-14
---

# 찾기와 고치기의 속도 차 (Discovery–Remediation Gap)

모델이 취약점을 **찾는** 속도는 기계 속도로 올라가는데, 그것을 **고쳐서 세상에 내보내는** 과정(패치 작성 · 조율 · 릴리스 · 배포)은 여전히 사람과 조직의 속도에 묶여 있다는 비대칭. 그 차이만큼 *알려졌지만 고쳐지지 않은* 구간이 생기고, 그 구간이 공격자의 시간이 된다.

> *"찾는 속도를 고치는 속도가 따라가지 못하면 그 사이에 무슨 일이 생길까요?"*(00:45~00:48, [[tech-bridge-openai-gpt-6-cyber-keynote]])

## 첫 사례 — PHP2Shell (2026-11-13 · [[tech-bridge-openai-gpt-6-cyber-keynote]])

- **찾기**: 14년 묵은 PHP 버그를 8월에 AI 모델로 서버 장악까지 증명, Calif · Wiz · OpenAI **세 팀이 두 달 사이에 각자** 찾았다(Wiz는 Google Gemini의 기여를 적었다).
- **고치기**: 신고(8-11) → 패치 목표일(10-22) → 실제 패치(10-21)까지 **두 달**. 그 사이 조율은 목표일 이틀 전에 무너졌고(번호 유출 · 시연 영상 실수 게시), Amazon은 **패치 나흘 전** 첫 공격 시도를 관측했다. PHP 재단은 2024년부터 알려진 문제의 수정이 멈췄다 섰다 한 것을 *구조적 실패* 라고 적었다.
- **규모**: 같은 시기 자율 파이프라인 1회로 리눅스 권한 상승 948개(OpenAI 자체 발표). *"버그 하나에 두 달이 걸리던 방식으로 1,000개를 감당할 수는 없습니다."*(08:52~08:53)
- **점수**: 공격 코드를 만드는 벤치마크는 +24점, 고치는 벤치마크는 +5.6점(서로 다른 시험, 슬라이드 기준).
- Greg Brockman 본인의 평가: *꽤 느리고 수작업이었고 에이전트 시대에는 통하지 않을 방식*.

## 제시된 대응 (벤더 진술)

- **고치는 쪽도 에이전트로** — Daybreak Defense Factory: 결과를 모아 중복을 합치고 담당자를 배정하고, 클라우드 개발 환경에서 실제로 돌려 확인한 뒤에야 PR을 올린다 → [[defense-factory]] · [[openai-daybreak]]
- **같은 코드를 새 모델로 다시 훑기** — *어제 통과한 코드도 다시 봐야 한다*(Firefox 81개) → [[ai-vulnerability-discovery]]
- **권한을 받은 방어자의 원격 패치**(Brockman 10월 제안, 극단적인 경우) — 조율 단계를 건너뛰는 방향.
- 해설의 유보: *"고치는 일까지 에이전트에게 맡기는 게 답인지는 이제부터 확인될 겁니다."* 그리고 *찾는 모델을 만드는 회사가 막는 제품도 파는 구도* 는 감안해야 한다.

## 위키의 다른 비대칭과의 관계

- [[verification-cost-asymmetry]] · [[verification-bottleneck]] — 코드 생성은 싸고 검증 · 리뷰가 병목이라는 개발 쪽 판. 여기서는 *발견은 싸고 수정 · 배포가 병목* 이다.
- [[coordinated-vulnerability-disclosure]] — 조율 공개는 *사람 속도의 수정* 을 전제로 설계된 절차다. 발견이 대량이 되면 그 전제가 흔들린다.
- [[defenders-window]] — 창은 *모델 간 간격* 이고, 이 개념은 *같은 버그의 발견과 수정 사이 간격* 이다. 창이 열려 있어도 수정이 느리면 방어자의 이점이 줄어든다(위키의 읽기).

## References

- [[tech-bridge-openai-gpt-6-cyber-keynote]]
