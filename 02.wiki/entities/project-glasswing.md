---
title: Project Glasswing
type: entity
category: product
tags: [anthropic, cybersecurity, initiative, collaboration]
aliases: [Glasswing]
sources: [anthropic-project-glasswing-update-2026-05, tech-bridge-anthropic-founders-secret-making-of-anthropic]
links:
  - https://www.anthropic.com/research/glasswing-initial-update
created: 2026-05-25
updated: 2026-11-24
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

## 2026-11-24 — 창업 서사의 끝자리에 놓인 Glasswing ([[tech-bridge-anthropic-founders-secret-making-of-anthropic]])

[[anthropic|Anthropic]] 창업사 해설이 이 프로그램을 *가장 강한 모델을 다르게 내놓은* 결정으로 놓는다. ⚠️ 해설 전달이다 — 바탕은 회사가 만든 다큐 *The making of Anthropic* 이고(위키 미열람) **창업자 원음은 캡션에 한 줄도 없다.** 인용은 전부 한국어 내레이션.

- 계기: *"클로드 미토스를 제한적으로 시험한다는 소식이 뉴스를 탔습니다."*(07:55~07:59)(해설은 4월이라 말한다) 문제는 *"소프트웨어 취약점을 찾아내는 능력"*(08:00)이었다. ⚠️ 그 능력에 대한 설명(08:04~08:43)은 무캡션.
- ⭐ 결정: *"미토스를 일반에 풀지 않고 방어하는 쪽에 먼저 줬습니다."*(08:44~08:47)
- 규모: *"Microsoft 같은 출시 파트너에 더해 40곳 넘는 조직이 접근권을"*(08:50~08:52) 받았다(앞에 아마존 · 애플 · Google을 든다). *"엔트로픽은 사용 크레딧 최대 1억 달러를 내걸었습니다."*(08:55~08:57)
- [[dario-amodei|Dario Amodei]]가 같은 날 쓴 글(해설의 번역): *"사이버는 최전선 AI 모델이 낳은 첫 번째 명백한 위험이지만 마지막은 아닐 것이다."*(09:22~09:27)

⚠️ **위 본문과의 차이.** 이 페이지는 2026-05 공식 업데이트를 따라 파트너를 약 50곳으로 적고 Amazon · Apple · Google을 주요 파트너로 들지 않는다. 해설은 출시 파트너 넷을 이름으로 들고 *40곳 넘는 조직* 을 따로 센다. 세는 방식이 다를 수 있고 해소하지 않았다. 사용 크레딧 1억 달러는 이 위키에 처음 나오는 수치다(공식 페이지 미열람).
