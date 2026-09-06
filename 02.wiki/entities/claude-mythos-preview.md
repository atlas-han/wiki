---
title: Claude Mythos Preview
type: entity
category: model
tags: [anthropic, frontier-model, unreleased, cybersecurity]
aliases: [Mythos Preview, Mythos-class]
sources: [anthropic-project-glasswing-update-2026-05, tech-bridge-altman-frontier-rl-pause]
links: []
created: 2026-05-25
updated: 2026-09-06
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

## 외부 언급 (2026-09-06 · [[tech-bridge-altman-frontier-rl-pause]])

*Sources with Alex Heath* 진행자가 [[sam-altman|Sam Altman]]에게 종말론적 여론의 원인을 나열하며 *"Hugging Face 사건이나 **Mythos·Fable** 사태(what's happened with Mythos or Fable), 다른 연구소 책임자들이 이 문제에 대해 이야기하는 방식"* 이라고 말한다. ko 자막은 *"미소스, 페이블 사태"*.

> ⚠️ **무슨 일이 있었는지는 소스에 없다.** 진행자의 한 문장뿐이고 Altman은 그 부분을 받지 않는다. 이 위키는 이 모델이 [[project-glasswing]]에서 공개된 사이버 capability 외에 어떤 "사태"와 연결되는지 알지 못한다. *Fable* 이라는 이름도 이 언급이 위키 첫 등장이며 페이지를 만들지 않았다.

## 미해결 사항

- 아키텍처·학습 방법 공개되지 않음
- "Preview"가 의미하는 안정도·릴리스 시기 모호
- 다른 lab의 동급 모델(OpenAI, Google, xAI) 존재 여부 비교 데이터 없음

## References

- [[anthropic-project-glasswing-update-2026-05]]
