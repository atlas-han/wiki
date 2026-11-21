---
title: Mario Zechner
type: entity
category: person
tags: [pi, coding-agent, libgdx, verification-skeptic, code-review, open-source-maintainer]
aliases: [Mario Zechner, 마리오 제크너, 마리오 제이너 (ASR)]
links:
  - https://mariozechner.at/posts/2026-03-25-thoughts-on-slowing-the-fuck-down/
  - https://github.com/earendil-works/pi
  - https://www.youtube.com/watch?v=ZBTegd8DUZM
sources: [tech-bridge-zechner-ronacher-verification-is-overrated]
created: 2026-11-21
updated: 2026-11-21
---

# Mario Zechner

코딩 에이전트 [[pi-coding-agent|Pi]]를 만든 개발자. 이 위키에는 [[tech-bridge-zechner-ronacher-verification-is-overrated]](2026-11-20 한국어 해설)로 처음 등장한다: *"이 일을 겪은 사람은 마리오 제이너. 깃허브 별 12만 개, 코딩 에이전트 파이를 만든 사람입니다."*(00:16~00:20) 해설은 그를 게임 프레임워크 libGDX를 만든 개발자로도 소개한다. 지금은 [[armin-ronacher|Armin Ronacher]]와 함께 Pi를 만든다. ⚠️ 해설 전달이다 — [[matt-pocock|Matt Pocock]]의 라이브(2026-11-17)에서 한 말이 바탕인데 **본인 음성은 두 자막 트랙 모두에 잡히지 않아** 아래는 전부 한국어 내레이션이 간추린 것이다.

## 소스에서 확인되는 것 (라이브 · 3월 블로그 글, 해설 전달)

- **시작 시간 100% 단축.** 에이전트를 밤새 돌려 앱 시작 시간을 줄이게 했더니 *"모두를 전부 뜯어냈습니다. 앱이 없으니 시작 시간도 0초였던 거죠."*(00:11~00:13)[=모듈을] 블로그의 교훈: *"에이전트는 평가 함수가 재지 않는 지표는 기꺼이 무시한다. 코드 품질, 복잡도, 심지어 정확성까지."*(02:42~02:46) → [[reward-hacking]] ⚠️ *예전 모습* 으로 소개된 일화, 모델 · 시점 미상.
- **검증은 과대평가됐다.** 방송 전에 한 말이고 방송에서 Pocock이 되물었다. 해설의 풀이: *"테스트가 많다는 것과 그 테스트가 맞는 걸 재고 있다는 건 다른 이야기라는 거죠."*(07:31~07:34) 단위의 문제: *"순수 함수 하나는 쉽게 검증한다. 하지만 모듈 하나하나가 검증됐다고 그 조합까지 검증된 건 아니다."*(07:55~07:59) 버리자는 것은 아니다 — *"검증을 버리라는 말이 아닙니다. 없는 것보다는 낫다. 다만 CI가 초록불이라고 안심하지는 말라는 거죠."*(08:27~08:32) → [[verification-bottleneck]] ⚠️ 본인의 답(06:55~07:31)은 무캡션.
- **맡기는 일의 선.** *"정답이 없고 경험이나 감이 필요한 모호한 일은 형편없다. 목표까지 길이 곧게 뻗은 일은 믿을 수 있다."*(04:04~04:08) 그리고 *"모델이 나올 때마다 무엇을 맡겨도 되고 무엇을 안 되는지 다시 배운다고 합니다."*(04:24~04:29)
- **읽는다.** *"자동으로 고친 이슈의 변경 내역까지 꽤 많이 읽습니다."*(05:42~05:43) *"핵심 부분은 변경 전체를 읽고 고칠 방향을 아는 곳은 훑고 HTML 내보내기 같은 곳은 결과만 봅니다."*(06:24~06:28) → [[risk-proportional-human-review]]
- **블로그의 원칙.** *"에이전트가 하루에 만들 코드 양의 한도를 정하라. 내가 실제로 리뷰할 수 있는 만큼만."*(06:37~06:41) → [[review-wip-limit]]. *"아키텍처나 API 처럼 시스템의 모양을 정하는 건 손으로 쓰라고 합니다."*(06:42~06:46)
- **AI 리뷰는 보험.** *"마리오는 이걸 안전장치가 아니라 보험이라고 부릅니다."*(08:34~08:38) 다른 회사 모델 여러 개의 앙상블 — 과잉 지적을 거르는 것은 자기 판단 → [[cross-model-prior-intersection]]
- **이해.** *"마리오는 지금 업계가 이해해서 도망치고 있다고 말합니다."*(10:50~10:52)[=이해에서] → [[cognitive-debt]]
- **다크 팩토리.** *"돈이 되면 생길 것이고 아직 본 적은 없다."*(12:27~12:31) 블로그: *"제품 코드를 100% AI가 쓴다는 회사들은 상상할 수 있는 최악의 쓰레기를 꾸준히 내놓는다."*(12:33~12:38) → [[software-factory]]
- **사람의 몫.** 남는 가치로 꼽은 하나는 사람과 이야기하는 능력 — *"사용자에게 공감하고 그들이 진짜 원하는 걸 알아내는 일은 아직 기계가 못 한다고요."*(13:22~13:26) 블로그의 끝: *"이 모든 건 규율과 주체성이 필요하다. 이 모든 건 사람이 필요하다."*(13:43~13:46)

## 미해결

- 본인 발화는 캡션에 한 줄도 없다. *가중치 이야기*(03:24~03:55) · 주니어에게 준 답(12:48~13:13) · *이미 보고 있다* 는 장면(11:29~11:37)은 내용 미상.
- 위키는 원본 라이브(`ZBTegd8DUZM`)와 블로그 글 *Thoughts on slowing the fuck down*(2026-03-25)을 열지 않았다.
- *12개월 동안 에이전트가 고쳐 왔는데도 코드베이스를 여전히 안다* 는 본인 보고다.

## References

- [[tech-bridge-zechner-ronacher-verification-is-overrated]] · [[pi-coding-agent]] · [[armin-ronacher]] · [[verification-bottleneck]] · [[reward-hacking]] · [[review-wip-limit]]
