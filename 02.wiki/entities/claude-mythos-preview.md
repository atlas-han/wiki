---
title: Claude Mythos Preview
type: entity
category: model
tags: [anthropic, frontier-model, unreleased, cybersecurity]
aliases: [Mythos Preview, Mythos-class]
sources: [anthropic-project-glasswing-update-2026-05]
links: []
created: 2026-05-25
updated: 2026-05-25
---

# Claude Mythos Preview

[[anthropic|Anthropic]]의 차세대급 비공개 모델. [[project-glasswing]]에서 처음 외부에 그 존재가 공개됨. 사이버보안·exploit 능력에서 이전 세대([[claude-opus-4-6]])를 큰 폭으로 상회하지만, dual-use 위험으로 인해 일반 공개는 보류 중. "Mythos-class"는 동급 capability를 가리키는 일반어로도 쓰임.

## 알려진 capability

- [[mozilla|Mozilla]] Firefox 150에서 271개 취약점 발견 — [[claude-opus-4-6]]의 Firefox 148 대비 **약 10배**
- [[uk-aisi|UK AI Security Institute]] 사이버 레인지 양쪽을 **end-to-end로 해결한 첫 모델**
- XBOW 평가: "기존 모든 모델 대비 significant step up over all existing models" (웹 exploit 벤치마크)
- ExploitBench, ExploitGym에서 최강 performer
- wolfSSL에서 인증서 위조 가능한 functional exploit를 직접 구성 (CVE-2026-5194 예시)

## 배포 상태

- **일반 공개 안 함**. Anthropic 공식 입장: "어떤 회사도 이런 모델의 오용을 막을 만큼 강한 안전장치를 만들지 못했다"
- [[project-glasswing]] 파트너 ~50개사 한정 접근
- 미국·동맹국 정부와의 협력 확대를 통한 점진적 확장 계획
- 안전장치 확보 후 일반 공개를 장기 비전으로 명시

## 위치 (다른 Claude 모델 대비)

- 공개된 플래그십: [[claude-opus-4-7]] (엔터프라이즈 패치 등에 활용)
- 직전 세대: [[claude-opus-4-6]]
- Mythos Preview: 비공개 frontier capability

## 미해결 사항

- 아키텍처·학습 방법 공개되지 않음
- "Preview"가 의미하는 안정도·릴리스 시기 모호
- 다른 lab의 동급 모델(OpenAI, Google, xAI) 존재 여부 비교 데이터 없음

## References

- [[anthropic-project-glasswing-update-2026-05]]
