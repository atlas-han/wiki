---
title: Project Glasswing
type: entity
category: product
tags: [anthropic, cybersecurity, initiative, collaboration]
aliases: [Glasswing]
sources: [anthropic-project-glasswing-update-2026-05]
links:
  - https://www.anthropic.com/research/glasswing-initial-update
created: 2026-05-25
updated: 2026-05-25
---

# Project Glasswing

[[anthropic|Anthropic]]이 ~50개 기업·기관 파트너와 운영하는 협업 사이버보안 이니셔티브. 비공개 모델 [[claude-mythos-preview]]를 활용해 critical 소프트웨어의 보안 취약점을 대량으로 발견·검증·패치하는 프로그램. 첫 공개 업데이트는 2026-05-22.

> *category를 `product`로 분류했지만 정확히는 "initiative/program". 추후 entity 카테고리에 `initiative`를 추가하는 것을 고려.*

## 운영 구조

- 주관: [[anthropic]]
- 주요 파트너: [[cloudflare]], [[mozilla]], Oracle, Microsoft, Palo Alto Networks, Cisco, 다수의 엔터프라이즈·은행
- 외부 평가: [[uk-aisi]], XBOW, OSSF Alpha-Omega, Linux Foundation, NIST, UK NCSC

## 작동 방식

1. 파트너가 자사 코드베이스에 [[claude-mythos-preview]]를 적용
2. 모델이 취약점을 찾고 functional exploit을 직접 구성해 검증
3. 보안 firm 또는 Anthropic이 재현·심각도 재평가
4. [[coordinated-vulnerability-disclosure|90일(패치 조기 작성 시 45일) coordinated disclosure]]로 maintainer에 보고
5. 패치 배포 후 advisory 공개

## 첫 업데이트의 주요 결과 (2026-05-22)

| 항목 | 수치 |
|---|---|
| 발견된 high/critical 취약점 | 10,000+ |
| 외부 검증 true positive 비율 | 90.6% |
| Cloudflare 발견 (high/critical) | 2,000 (400) |
| Firefox 150 취약점 | 271 |
| 오픈소스 high/critical | 6,202 |
| [[claude-opus-4-7]] 가 패치한 엔터프라이즈 취약점 (3주) | 2,100+ |
| 차단된 사기 송금 (1건) | $1.5M |

## 함의

- [[ai-vulnerability-discovery]] 패턴의 산업 규모 실증
- 사이버보안 병목이 **발견 → 검증·패치**로 이동했음을 증명
- dual-use 정책: Mythos-class 모델 일반 공개 보류
- 향후: 미국·동맹국 정부와의 파트너 확대, ExploitBench/ExploitGym 같은 정량 벤치마크 생태계 구축

## References

- [[anthropic-project-glasswing-update-2026-05]]
