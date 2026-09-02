---
title: Katelyn Lesse
type: entity
category: person
tags: [anthropic, claude-platform, infrastructure, developer-platform]
links:
  - https://x.com/katelyn_lesse
  - https://www.linkedin.com/in/katelynlesse/
sources: [tech-bridge-claude-platform-agent-era]
created: 2026-09-02
updated: 2026-09-02
---

# Katelyn Lesse

[[anthropic|Anthropic]] Claude Platform 팀. 본 위키 첫 등장은 [[tech-bridge]] 재배포 대담 [[tech-bridge-claude-platform-agent-era]] (2026-09-01).

## 위키에서 알려진 사실

- 경력: **Stripe**(Stripe Connect) → Anthropic. 대담 시점 기준 재직 약 1년. [[angela-jiang|Angela Jiang]]과 Stripe에서 함께 일했다.
- 지난 1년의 변화를 **"모델이 더 오랫동안 효율적으로 작동하게 된 것"**으로 요약하고, 그래서 **주변 인프라**가 중요해졌다고 말한다.
- 관리형 에이전트의 철학을 한 문장으로 제시 — *"플랫폼 위에 구축하는 입장에서 **차별화되는 일을 해야 하고, 차별화되지 않는 일은 할 필요가 없다**"*. 그리고 **차별화되지 않는 것 = 인프라**로 지목하며 *"이것은 **분산 시스템 문제**입니다"*라고 규정한다 ([[agent-distributed-systems]]).
- 이 대담의 핵심 아키텍처를 설명한 화자 — 샌드박스 기술이 대개 **일시적(ephemeral) 용도**로 설계되었기 때문에, **하네스는 내구성 서버에서 돌리고 작업 시점에만 샌드박스를 생성·삭제**한다. 그래야 샌드박스가 죽어도 **전체 에이전트가 다운되지 않는다**. 이것이 [[managed-agents]] session/harness/sandbox 분할의 이유.
- 지키는 것과 여는 것의 경계를 밝힌다 — 모델 실행·제공과 안전 분류기는 지키되, *"**아키텍처에 대해서는 확고한 의견을 갖고 있지만, 인프라에 대해서는 꼭 그렇지는 않습니다**"*. 샌드박스 자체 호스팅, MCP 터널이 이미 열려 있다.
- 폐쇄형 모델 논쟁에 대해 **"고객 데이터로 학습하지 않는다"**고 답한다.
- 팀 규모와 병목에 대한 관찰 — 플랫폼·제품 인프라 전체가 **200명**. 실행이 빨라지면서 **정렬(alignment)이 새 병목**이 됐다: *"이틀 만에 모든 게 끝났는데, 모두가 같은 생각을 갖도록 만드는 데 필요한 모든 작업을 할 시간이 부족했잖아요."*
- 팀 문화 표현: *"We have to be a team that's really ready to **get punched in the face**."* 얻어맞는 것의 정체는 안전·인프라·규모 문제.
- 개인 워크플로: **에이전트로 에이전트를 테스트**한다 — 고객 제품들을 대신 써보고 스크린샷을 보내는 에이전트를 Claude Managed Agents로 만든다.
- 플랫폼 팀의 위치 — 퍼스트 파티 제품이 **외부 고객과 동일한 API**를 쓰므로 *"퍼스트 파티 제품이 곧 저희 팀의 고객"*이다. 필요할 때 **타이거 팀**을 꾸린다.

## References

- [[tech-bridge-claude-platform-agent-era]] — 43:59, 2026-09-01
