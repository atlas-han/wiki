---
title: Anthropic
type: entity
category: org
tags: [ai-lab, frontier-lab, claude]
aliases: [앤트로픽]
sources: [anthropic-project-glasswing-update-2026-05, anthropic-claude-code-auto-mode, anthropic-harness-design-long-running-apps, anthropic-managed-agents, anthropic-dynamic-workflows]
links:
  - https://www.anthropic.com
created: 2026-05-25
updated: 2026-09-02
---

# Anthropic

미국 샌프란시스코 기반 AI 안전·연구 회사. [[claude-mythos-preview|Claude]] 모델 패밀리의 개발사. 본 위키에서 자주 등장하는 주요 frontier lab.

## 위키에서 알려진 사실

- Claude 모델 패밀리 운영: 현재 공개 플래그십은 [[claude-opus-4-7]], 비공개 차세대급으로 [[claude-mythos-preview]]. 세대: [[claude-opus-4-5]] / [[claude-opus-4-6]] / [[claude-opus-4-7]], 그리고 mid-tier [[claude-sonnet-4-5]] / [[claude-sonnet-4-6]].
- 보안 이니셔티브 [[project-glasswing]]을 ~50개 파트너와 운영 ([[anthropic-project-glasswing-update-2026-05]])
- **Agent 인프라 라인업**:
  - [[claude-code|Claude Code]] — 공식 coding agent CLI ([[anthropic-claude-code-auto-mode|auto mode]] + [[dynamic-workflows]] 신규)
  - [[claude-agent-sdk]] — 에이전트 빌딩 SDK
  - [[managed-agents]] — 장기 horizon 에이전트의 호스팅 메타-하네스
- Engineering Blog의 연작 모티프: *"harnesses encode assumptions about what Claude can't do"* — [[anthropic-harness-design-long-running-apps]], [[anthropic-managed-agents]], [[anthropic-claude-code-auto-mode]]
- 제품: Claude Security (엔터프라이즈 public beta), Claude for Open Source, External Researcher Access Program
- 정책 입장: dual-use 위험이 큰 모델(예: Mythos-class)은 안전장치가 충분해질 때까지 일반 공개 보류

## 알려진 협력·관계

- **Glasswing 파트너**: [[cloudflare]], [[mozilla]], Oracle, Microsoft, Palo Alto Networks, Cisco
- **평가·정부**: [[uk-aisi]], NIST, UK NCSC, OSSF Alpha-Omega, Linux Foundation
- 미국·동맹국 정부와의 보안 협력 확대 의지 표명

## Claude Platform 팀 (1차 진술, 2026-09-01)

[[tech-bridge-claude-platform-agent-era]]에서 [[angela-jiang]]·[[katelyn-lesse]]가 직접 밝힌 것들. 기존 항목이 대부분 블로그·문서 기반이었던 것과 달리 **팀 당사자의 진술**이다.

- **규모**: 플랫폼·제품 인프라를 포함해 팀 **200명**. 대담자는 *"1년 전에 이 정도 인원으로 이 일을 할 수 있을 거라고 누가 말했더라면 절대 불가능하다고 했을 것"*이라 표현.
- **퍼스트 파티 = 고객**: 자사 제품이 **외부 고객과 동일한 API·플랫폼** 위에 지어진다. *"퍼스트 파티 제품이 곧 저희 팀의 고객"*.
- **경계선**: 모델 실행·제공과 안전 분류기(Messages API 아래 계층)는 지키고, 그 위로는 *"아키텍처에 대해서는 확고한 의견을 갖고 있지만 **인프라에 대해서는 꼭 그렇지는 않다**"*. 샌드박스 자체 호스팅과 **MCP 터널**이 이미 열려 있다.
- **데이터 정책**: *"저희는 고객님의 데이터를 사용해서 학습하지 않습니다."*
- **조직 형태**: 새 모델 출시처럼 전 구간이 맞물려야 할 때 **타이거 팀**을 꾸린다. *"특별한 비결은 없고, 탄탄한 관계와 필요한 순간에 민첩하게 협력하는 능력"*.
- **새 병목**: 실행이 빨라지면서 **정렬(alignment)**이 병목이 됐다 — 예전에는 PM·TPM이 조율할 시간이 있었지만 *"이틀 만에 모든 게 끝났는데, 모두가 같은 생각을 갖도록 만드는 데 필요한 모든 작업을 할 시간이 부족"*하다.
- **제품 개발 방식**: 불확실성이 커서 집중된 베팅이 아니라 **포트폴리오**를 빠르게 구축한다 — *"어쩌면 투자와 조금 더 비슷하다"*.
- 관련 개념: [[token-roles]] · [[managed-agents]] · [[agent-distributed-systems]]

## 미해결 사항 (위키가 채워갈 부분)

- 창립·자금조달·인력 구조 등 회사 기본 프로필 (별도 소스 ingest 필요)
- 모델 release timeline 전체
- 안전·alignment 연구 출판물

## References

- [[anthropic-project-glasswing-update-2026-05]]
- [[anthropic-claude-code-auto-mode]]
- [[anthropic-harness-design-long-running-apps]]
- [[anthropic-managed-agents]]
- [[anthropic-dynamic-workflows]]
- [[tech-bridge-claude-platform-agent-era]]
