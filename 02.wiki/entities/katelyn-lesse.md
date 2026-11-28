---
title: Katelyn Lesse
type: entity
category: person
tags: [anthropic, claude-platform, infrastructure, developer-platform]
links:
  - https://x.com/katelyn_lesse
  - https://www.linkedin.com/in/katelynlesse/
sources: [tech-bridge-claude-platform-agent-era, tech-bridge-tokens-should-have-jobs, tech-bridge-katelyn-lesse-anthropic-engineers-barely-read-code]
created: 2026-09-02
updated: 2026-11-28
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

## 두 번째 소스 — AI Engineer 발표 (2026-09-18 · [[tech-bridge-tokens-should-have-jobs]])

[[angela-jiang|Angela Jiang]]과 함께 [[ai-engineer|AI Engineer]] 무대에서 발표했다. 자기소개가 직함을 준다 — *"저는 케이틀린이고 앤트로픽에서 **플랫폼 엔지니어링을 담당**하고 있습니다"*(00:05~00:07). 설명란은 *"플랫폼 엔지니어링 리드"*. 09-01 대담의 *"Claude Platform 팀"* 이 **역할까지 확정**됐다.

이 발표에서 그의 몫으로 읽히는 부분(⚠️ 발언별 화자는 부분 판독 — Angela가 *"케이틀린이 언급했듯이"* 라고 두 번 가리키는 대목으로 역산):

- **재무 분석 벤치의 설계와 첫 두 실험**(04:09~06:22) — 실행만 하는 컨트롤, one-shot(15% · 39k), 그리고 **예산을 60만으로 고정**해 알파를 찾는 방법 → [[fixed-budget-alpha]]
- *"만약 테스트 타임 컴퓨트만이 중요한 요소라면 실행·조언·채점·회고가 같은 수준이어야 한다"* 는 **귀무가설**을 세운 쪽.
- 실행의 **진짜 비용 180만 토큰** 계산도 Angela가 *"케이틀린이 언급했듯이"* 로 돌린다(09:12) → [[true-cost-to-perfect-answer]]

09-01에서 *"이것은 분산 시스템 문제"* 라며 **인프라**를 말했던 화자가, 이번엔 **측정 방법**을 말한다. ⚠️ en-orig ASR은 *Caitlyn/Caitlin*, ko는 *케이틀린* — 설명란의 *Katelyn Lesse* 철자를 채택했다(09-01과 같은 처리).

## ⚠️ Contradiction (범위 차이, 2026-10-01)

[[tech-bridge-ai-data-exposure-hidden-risk]]의 [[jeff-crume|Jeff Crume]]은 공개 챗봇에 넣은 민감 데이터를 *"they can use that sensitive information to train their models, and then it's available to everyone"*(01:02~01:05)라고 일반화한다. 이 페이지의 *"고객 데이터로 학습하지 않는다"* 와 부딪히지만 **대상이 다를 수 있다**(소비자용 공개 챗봇 vs API 플랫폼) — Crume은 어떤 서비스·약관인지 말하지 않는다. 미해소. → [[ai-data-exposure]]

## 세 번째 소스 — The Pragmatic Engineer 인터뷰 해설 (2026-11-28 ingest · [[tech-bridge-katelyn-lesse-anthropic-engineers-barely-read-code]])

[[tech-bridge]]의 10:47 한국어 해설. 앞의 두 소스가 본인 발화의 번역 · 자막이었다면 **이 소스에는 본인 원음이 한 마디도 캡션에 없다** — 아래는 전부 내레이션이 옮긴 말이다. 직함은 내레이션 *플랫폼 엔지니어링 총괄*(00:22), 설명란 *Claude Platform 엔지니어링을 이끄는*. ⚠️ ASR은 *케이틀린 · 케이트린*, 더빙은 *Caitlin*.

- **맡은 것.** *"케이틀린의 팀은 클라우드의 모든 토큰이 지나가는 메시지 API를 맡고 있습니다."*(00:28~00:31)[=Claude의 · Messages API] 09-01 대담의 *퍼스트 파티 제품이 곧 저희 팀의 고객* 과 같은 말이 다시 나온다 — *"클라우드 앱도, 클라우드 코드도 전부 외부 고객과 같은 이 API 위에서 돌아갑니다."*(00:38~00:42)
- **Python → Rust 재작성.** *"파이썬으로 된 핵심 층을 러스트로 옮기는 데 걸린 시간은 다섯에서 여섯 달. 핵심 팀은 몇 명 뿐이었습니다."*(00:10~00:14) 계기는 CPU다 — *"케이틀린은 커리어 내내 CPU는 돈만 내면 얼마든지 늘릴 수 있는 자원이었다고 말합니다. 그런데 처음으로 클라우드의 CPU를 더 달라고 하는 일이 어려운 대화가 됐습니다."*(01:03~01:12) 팀에 Rust를 써 본 사람이 거의 없었는데도 골랐고, 본인의 Rust 이해는 *75대 25* 라고 했다 → [[rust]]
- **검증.** 실제 요청을 Rust 시스템에도 그림자처럼 흘려 결과를 견주었다 → [[shadow-traffic-verification]]. 해설의 요약으로는 *"클라우드의 모든 토큰이 지나가는 API를 통째로 새로 짰는데 에이전트가 올린 PR의 80%는 꼼꼼히 읽지 않았습니다."*(00:03~00:08)
- **팀.** *"팀 크기는 여전히 다섯에서 열 명쯤인데 더 시니어 쪽으로 기울었습니다."*(06:24~06:28) *"테크 리드가 설계하고 여러 명이 구현하던 구조 대신 누구나 설계와 조율을 고민하고 클라우드들에게 구현을 맡깁니다."*(06:30~06:35)
- **리뷰 · 온콜 · PM.** 변경마다 Claude 분류기가 사람 검토 여부를 정하고([[risk-proportional-human-review]]), 온콜 알림은 Claude가 먼저 받아 잡음을 거르며, PM이 직접 프로덕션에 올린다. 그래도 *"문제가 생기면 누가 책임질까요? 답은 예전과 같습니다. 그 시스템을 맡은 팀이 호출을 받습니다."*(08:22~08:26)
- **채용.** *"엔트로픽은 제품과 플랫폼 조직 전반에서 코딩 면접을 단계적으로 없앴습니다."*(08:34~08:39) ⚠️ 이유는 무캡션.
- **정체성 위기.** *"케이틀린은 지난 10월 블로그에 이렇게 썼습니다. 많은 소프트웨어 엔지니어가 정체성 위기를 겪고 있다고요."*(09:31~09:36) 설명란에 따르면 글은 *The new set of problems for engineers to solve*(2026.10.25, 위키 미열람). 내레이션이 옮긴 요지 — *"수천 개의 에이전트가 함께 일하는 시스템이 제대로 돌려면 사람이 먼저 풀어야 할 문제가 많다는 겁니다."*(10:12~10:16) *"케이트린의 표현으로는 야망의 수준을 올리라는 겁니다."*(10:36~10:38)

09-01의 *정렬이 새 병목* 은 이 편에서 *"엔지니어의 시간은 구현에서 다른 팀과의 조율로 옮겨갔습니다."*(10:30~10:32) 로 되풀이된다. ⚠️ 무캡션 다섯 곳(약 3분 57초)에 80% 대목의 본문 · 중간에 버리고 다시 한 것 · 면접 폐지의 이유가 들어 있어 이 페이지에도 적지 못했다.
