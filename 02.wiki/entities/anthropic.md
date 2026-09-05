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

## Claude Code 팀의 일하는 방식 (2026-09-05 ingest · [[tech-bridge-claude-code-team-workflow]])

같은 회사의 다른 팀에 대한 1인칭 증언이 들어왔다. 위 [[tech-bridge-claude-platform-agent-era]]가 플랫폼 설계 관점이었다면 이쪽은 **자기 하네스를 직접 쓰는 사용자 관점**이다.

- 업무의 **70~80%가 [[claude-tag|Claude Tag]]**(Slack 네이티브 에이전트)에서 일어난다. → [[goal-level-delegation]]
- **하네스 기능을 지운다.** *"이러한 기능들을 하네스에 내장하는 것은 **현재 모델이 가지고 있는 오류 모드를 보완하기 위한 것**"* 이므로, 모델이 좋아지면 없앤다. todo 리스트와 AskUserQuestion이 사례다. → [[harness-pruning]]
- 기반 기술이 **2개월마다** 근본적으로 바뀌고 *"시간이 흐를수록 그 변화가 압축"* 된다. 그래서 *"권한 시스템을 재작성하고 결과물을 만드는 작업을 **동시에 진행할 수 있는 소규모 팀**"* 을 둔다.
- **workflows의 기원은 코드 리뷰**다 — fan-out으로 버그를 찾고, 각 버그를 **3관점 적대적 검토**로 거른 뒤 합친다. *"이것이 바로 우리가 **test-time compute**라고 부르는 것."* → [[dynamic-workflows]]
- fan-out의 병목은 map이 아니라 **reduce**라고 짚는다 — *"**마치 map-reduce 문제와 같아요.** (…) 전체 출력값을 다 읽어버리면 미쳐버릴 것 같거든요."*
- *"**Claude는 자기만의 하네스를 만드는 데 정말 능숙**하죠"* — 토폴로지와 배선을 스스로 정한다. → [[self-harness]]
- 화자: [[thariq-shihipar]] · [[sid-bidasaria]] · [[robert-boyce]] (⚠️ 발언별 화자 특정 불가)

## AI-Native SDLC Playbook (2026-09-05 · 제3자 해설로만 유입)

Anthropic이 *AI-Native SDLC Playbook*을 공개했고, 이 위키는 [[tech-bridge-ai-native-sdlc]]의 **해설을 통해서만** 그 내용을 안다. 핵심은 [[intent-md|intent.md]] → `spec.md` → `plan.md`로 이어지는 **아티팩트 체인**과, 유지보수에서 Claude가 스스로 intent를 만들어 **루프를 닫는** 구조다. → [[ai-native-sdlc]]

> ⚠️ **원문서(<https://claude.com/blog/the-ai-native-sdlc-playbook>)는 아직 직접 ingest하지 않았다.** 해설에 나온 *"우리는 두 배 더 빠릅니다"* 같은 수치는 근거가 확인되지 않았다.

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
- [[tech-bridge-claude-code-team-workflow]]
- [[tech-bridge-ai-native-sdlc]]
