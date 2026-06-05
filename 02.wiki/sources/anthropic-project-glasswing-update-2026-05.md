---
title: "Anthropic — Project Glasswing: An Initial Update (2026-05-22)"
type: source
tags: [security, cybersecurity, vulnerability-discovery, dual-use, anthropic]
source-url: https://www.anthropic.com/research/glasswing-initial-update
source-type: article
author: Anthropic
date-published: 2026-05-22
ingested: 2026-05-25
created: 2026-05-25
updated: 2026-06-03
---

# Anthropic — Project Glasswing: An Initial Update (2026-05-22)

[[anthropic|Anthropic]]이 ~50개 파트너와 진행 중인 협업 사이버보안 이니셔티브 **[[project-glasswing]]** 의 첫 공개 업데이트. 비공개 모델 [[claude-mythos-preview]]를 활용해 critical SW에서 **10,000개 이상의 high/critical-severity 취약점** 발견. 사이버보안의 병목이 **발견 → 검증·공개·패치** 로 이동했음을 시사.

## 핵심 takeaways

1. **AI 취약점 발견의 산업화**: 단일 비공개 모델(Mythos Preview)이 50개 조직과 함께 1만 건 이상의 high/critical 취약점을 발견. [[claude-opus-4-6]] 대비 [[mozilla|Mozilla]] Firefox에서 10배 성능. [[cloudflare|Cloudflare]]는 버그 발견율 10배 증가 보고. → [[ai-vulnerability-discovery]] 패턴이 실증 단계 진입.

2. **병목의 이동**: "이제는 AI가 발견한 다수의 취약점을 얼마나 빨리 검증·공개·패치하느냐가 한계." 오픈소스 maintainer가 저품질 AI 생성 버그 리포트에 압도되는 부작용도 동시에 발생. → [[coordinated-vulnerability-disclosure]] 프로세스의 재설계 필요성.

3. **공개 모델과 비공개 모델의 분리**: Mythos Preview는 일반 공개 안 함 — "어떤 회사도 이런 모델의 오용을 막을 만큼 강한 안전장치를 만들지 못했다"는 입장. 대신 공개된 [[claude-opus-4-7]]을 활용한 cyberdefense 도구 제공.

4. **검증의 신뢰성**: 외부 firm이 1,752개 high/critical을 평가한 결과 **90.6%가 true positive**, 62.4%는 high/critical 등급 유지. Cloudflare는 false positive 비율이 인간 테스터보다 낮다고 보고.

5. **자가 시연된 dual-use**: 동일 capability가 방어(패치 가속)와 공격(악용 가속) 양쪽에 적용됨을 명시. Anthropic은 미국·동맹국 정부와의 협력 확대를 다음 단계로 제시.

6. **새 평가 인프라**: [[uk-aisi|UK AISI]] cyber range를 end-to-end로 해결한 첫 모델이 Mythos Preview. XBOW, ExploitBench, ExploitGym 등 정량 벤치마크 생태계 형성.

## 인용

> "Now it's limited by how quickly we can verify, disclose, and patch the large numbers of vulnerabilities found by AI."

> "Several have told us that their rate of bug-finding has increased by more than a factor of ten."

> "No company has developed safeguards strong enough to prevent such models from being misused."

## 주요 수치 요약

| 항목 | 수치 |
|---|---|
| 발견된 high/critical 취약점 (전체) | 10,000+ |
| Cloudflare 발견 (high/critical) | 2,000 (400) |
| Mozilla Firefox 150 취약점 | 271 (Opus 4.6 대비 10×) |
| 오픈소스 6,202 / 23,019 (high+crit / 전체) |
| 외부 검증 true positive 비율 | 90.6% |
| 패치 배포 / advisory | 75 / 65 |
| Opus 4.7가 3주간 패치한 엔터프라이즈 취약점 | 2,100+ |
| 차단된 사기 송금 (1건) | $1.5M |

## 등장 개체·개념

- **개체**: [[anthropic]], [[project-glasswing]], [[claude-mythos-preview]], [[claude-opus-4-6]], [[claude-opus-4-7]], [[cloudflare]], [[mozilla]], [[uk-aisi]]
- **개념**: [[ai-vulnerability-discovery]], [[coordinated-vulnerability-disclosure]]
- **이번 ingest에서는 stub 미생성**: Oracle, Microsoft, Palo Alto Networks, Cisco, wolfSSL, XBOW, OSSF Alpha-Omega, NIST, UK NCSC, ExploitBench, ExploitGym — 향후 관련 소스 ingest 시 페이지화 고려

## 미해결 질문 (위키 누적용)

- Mythos Preview의 architecture·학습 방식은? (이번 글에는 미공개)
- 정확한 "Mythos-class" 정의와 다른 lab(OpenAI, Google, xAI 등)의 동급 모델 존재 여부?
- 안전장치(safeguards)의 구체적 형태는 어디까지 공개되었나?
- AI-generated 버그 리포트가 오픈소스 maintainer에 끼치는 negative externality에 대한 정량 데이터?

## References

- [원문](https://www.anthropic.com/research/glasswing-initial-update)
- 로컬 캡처: `raw/articles/anthropic-project-glasswing-update-2026-05-22.md`
