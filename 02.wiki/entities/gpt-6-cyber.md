---
title: GPT-6 Cyber
type: entity
category: model
tags: [openai, cybersecurity, vulnerability-discovery, frontier-model, dual-use]
aliases: [GPT-6 Cyber, GPT 6 사이버, GPT-6 사이버]
links:
  - https://deploymentsafety.openai.com/gpt-6-cyber
sources: [tech-bridge-openai-gpt-6-cyber-keynote]
created: 2026-11-14
updated: 2026-11-14
---

# GPT-6 Cyber

[[openai|OpenAI]]의 사이버 보안 특화 모델. 키노트 *"Cyber at the Frontier"* 에서 [[openai-daybreak|Daybreak]] Red Team · Defense Factory와 함께 소개됐고, [[tech-bridge|Tech Bridge]]의 기록 대조 해설([[tech-bridge-openai-gpt-6-cyber-keynote]])로 위키에 들어왔다. 일반 GPT-6 계열(위키의 [[tech-bridge-gpt-6-1-terra-first-look|GPT-6.1 Terra]] 등)과의 관계는 소스에 없다.

> ⚠️ **모든 수치는 OpenAI 자체 발표 · 자체 평가다**(설명란 · 해설 반복). 위키는 키노트 원본과 배포 안전성 문서를 열지 않았다.

## 위키에서 알려진 것 (2026-11-13 · [[tech-bridge-openai-gpt-6-cyber-keynote]])

| 항목 | 값 | 출처(해설 전달) |
|---|---|---|
| 리눅스 권한 상승 취약점 | 자율 파이프라인 1회, **948개 검증 + 패치**, API 비용 120만 달러 | Clint Gibler 게시물(11-04) |
| 이전 모델 대비 | 약 석 달 전 모델이 찾은 것의 **5.7배**, 새 공격 기법 최소 10가지(*"우리가 아는 한"*) | 슬라이드 · 글 |
| Firefox 재검사 | 이미 다른 연구소 최신 모델로 검사된 코드에서 심각도 높음 **81개** — MFSA 2026-118 신고자 칸 OpenAI는 41개(해설자 집계), 81건 목록 미확인 | Gibler · Mozilla |
| ExploitBench(판독 추정) | 슬라이드 **52.6%**(다음 모델 77%) vs 배포 안전성 문서 **48.45%**, 방어 장치(ASLR 추정) 켠 판 **36.94%** | 슬라이드 · 문서 |
| PatchBench(표기 추정) | **73.5%**(다음 모델 79.1%) | 슬라이드 |
| 허니팟 범위 시험 | **0.07%**, 배포용 안전 지침을 주면 0% — 이전 모델 49.5% | 자체 평가 |

- 비교: Anthropic Mythos 5.2는 ExploitBench(추정) 331/869 = 38%(Anthropic 시스템 카드) — *같은 조건에서 잰 숫자인지는 알 수 없다*. → [[claude-mythos-preview]]
- 같은 모델로 [[defenders-window|방어자의 창]] 논리 — 검증된 방어자가 먼저 쓰게 한다(Daybreak 프로그램).

## 위키의 읽기

- **공격 코드 점수는 크게, 고치는 점수는 작게 올랐다**(슬라이드 기준 +24 vs +5.6, 서로 다른 시험) → [[discovery-remediation-gap]].
- **같은 모델의 점수가 슬라이드와 문서에서 다르다** — 위키가 벤더 벤치마크를 기록할 때 *조건 · 문서* 를 같이 적어야 하는 이유의 사례.

## References

- [[tech-bridge-openai-gpt-6-cyber-keynote]]
