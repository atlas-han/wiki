---
title: "사내 추론으로 지키는 데이터 경계 (In-House AI Data Boundary)"
type: concept
category: pattern
tags: [data-boundary, on-premise, local-ai, privacy, healthcare, sovereign-deployment]
aliases: [on-premise AI, 로컬 AI, 환자 정보는 병원 안에서, sovereign deployment]
related: [ai-data-exposure, confidential-vm, cloud-agent-delegation, software-marginal-cost, deterministic-agent-pipeline]
first-seen: tech-bridge-dental-clinic-ax-transformation
sources: [tech-bridge-dental-clinic-ax-transformation]
created: 2026-10-17
updated: 2026-10-17
---

# 사내 추론으로 지키는 데이터 경계 (In-House AI Data Boundary)

**민감 데이터가 조직 밖으로 나가지 않게 하려고, 모델 추론과 그 데이터를 쓰는 업무 프로그램을 모두 조직 안 하드웨어에 두는 배치다.** 데이터의 흐름을 감시하는 쪽([[ai-data-exposure]])이나 클라우드 안에서 격리하는 쪽([[confidential-vm]])과 달리, **경계 자체를 물리적으로 긋는다.** 이 위키에서는 [[gatsbydds]](치과 원장)의 사례를 다룬 [[tech-bridge-dental-clinic-ax-transformation]]에서 처음 나왔다.

> *"환자 정보는 병원 밖으로 보내지 않는다. 그래서 병원 안에 컴퓨터에서 AI를 직접 돌리기로 했다고 해요."* (해설, 01:36~01:43)

## 사례의 구성 (해설 전언)

- 하드웨어: DGX Spark 12대, Mac mini, 업무 서버, 정전 대비 전원 장치(01:43~01:51)
- *"AI가 돌아가는 곳과 직원들이 쓰는 프로그램을 병원 안에서 연결"*(01:54~01:56)
- 그 위의 업무: 통화 전사·요약, 보험 서류 대조, 경영 리포트. 모두 환자·재무 데이터를 다룬다.

## 비용과 한계 — 사례 스스로 단 단서

- *"장비 12대는 이분이 선택한 규모예요. 다른 치과도 이만큼 사야 한다는 이야기는 아니고요."*(02:03~02:09)
- 원장 본인도 *"취미에 빠진 과투자"*(01:59~02:03)라고 하고, 해설은 *"이 글만으로 전체 장비값을 언제 회수했는지 계산할 수는 없어요"*(07:25~07:30)라고 말한다. **경제성의 근거가 아니라 데이터 경계의 근거다.**
- 운영 부담(서버 관리, 실패한 시스템 재구축)이 원장 한 사람에게 몰린다(08:31~08:38).

## 위키의 다른 페이지와

- [[cloud-agent-delegation]]: 반대 방향이다. 에이전트를 원격 VM으로 보내는 흐름과 데이터를 안에 두는 흐름이 맞선다.
- [[tech-bridge-factory-bug-report-to-production|Factory 편]]이 3원칙의 하나로 든 *sovereign deployment* 는 같은 요구의 기업·벤더 판본이다.
- [[software-marginal-cost]]: 토큰 비용을 구독·API 대신 고정 하드웨어 비용으로 바꾼다. ⚠️ 이 사례에서는 회수 여부를 알 수 없다.
- [[deterministic-agent-pipeline]]: 같은 사례가 숫자 계산을 결정론적 프로그램에 맡긴다. 데이터 경계와는 별개의 원칙이다.

## ⚠️ 유보

- 단일 2차 소스(커뮤니티 글 → 해설)다. 사용 모델, 성능, 클라우드 모델 대비 품질 차이는 발화되지 않는다.
- 규제(의료 정보 관련 법)는 언급되지 않는다. 원칙은 원장 개인의 판단으로 제시된다.

## References

- [[tech-bridge-dental-clinic-ax-transformation]] · [[gatsbydds]]
