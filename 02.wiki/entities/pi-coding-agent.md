---
title: Pi (코딩 에이전트)
type: entity
category: product
tags: [coding-agent, open-source, earendil, issue-triage, auto-fix, mario-zechner, armin-ronacher]
aliases: [Pi, 파이, pi coding agent, Aider (더빙 ASR 오인식), Pie (더빙 ASR 오인식)]
links:
  - https://github.com/earendil-works/pi
sources: [tech-bridge-zechner-ronacher-verification-is-overrated]
created: 2026-11-21
updated: 2026-11-21
---

# Pi (코딩 에이전트)

[[mario-zechner|Mario Zechner]]가 만든 코딩 에이전트. 이 위키에는 [[tech-bridge-zechner-ronacher-verification-is-overrated]](2026-11-20 한국어 해설)로 처음 등장한다: *"이 일을 겪은 사람은 마리오 제이너. 깃허브 별 12만 개, 코딩 에이전트 파이를 만든 사람입니다."*(00:16~00:20) 2026년 4월 [[armin-ronacher|Armin Ronacher]]의 회사 Earendil이 인수했고(*"아르민이 세운 회사 엘엔딜이 올해 4월 파이를 인수했고 지금은 둘이 함께 파이를 만듭니다."*(00:44~00:48)[=Earendil]) 저장소는 설명란 기준 `earendil-works/pi` 다. ⚠️ 해설 전달 — 위키는 저장소를 열지 않았고, 이 페이지는 **제품의 기능이 아니라 유지보수 방식** 만 담는다(소스가 그것만 말한다). 영어 더빙 ASR은 이 이름을 *Aider* · *Pie* 로 잘못 적는다 — Aider는 다른 도구다.

## 소스에서 확인되는 것 (해설 전달)

- **규모.** GitHub 별 12만 개. *"파이에 하루 40에서 50개씩 새 이슈가 들어옵니다."*(04:30~04:32)(Zechner의 말로)
- **이슈 분류 봇.** *"그래서 동료 데이비드가 분류 봇을 만들었습니다."*(04:34~04:35) *"봇은 버그가 진짜인지 살피고 재현해 본 뒤 고칠 방법과 우선순위를 붙입니다."*(04:37~04:41) 해설이 저장소에서 확인했다는 예: *"실제 저장소에는 이런 이슈에 가장 급하다는 P0 라벨이 붙습니다. 읽기를 취소하면 파이가 그대로 꺼지는 버그였죠."*(04:43~04:49)
- ⭐ **자동 수정의 조건.** *"조건은 셋입니다. 라벨, 지금 코드에서 실패하는 테스트, 그리고 고친 뒤에 통과. 기능 작업은 예외고요."*(05:31~05:37) ⚠️ 원음 설명(04:52~05:28)은 무캡션 — 병합까지 자동인지는 캡션으로 알 수 없다.
- **그래도 사람이 읽는다.** *"자동으로 고친 이슈의 변경 내역까지 꽤 많이 읽습니다."*(05:42~05:43) *"그 덕에 12개월 동안 에이전트가 고쳐왔는데도 파이의 코드베이스를 여전히 안다는 겁니다."*(06:30~06:34) → [[review-wip-limit]] · [[risk-proportional-human-review]]
- **Lean으로 일부를 증명해 봤다**(Ronacher) — 결론은 회의적 → [[ai-formal-verification]]

## 위키의 다른 페이지와

- [[software-factory]] — 이슈 → 분류 → 조건부 자동 수정은 공장의 한 구간이지만 만든 사람들은 다크 팩토리를 *아직 본 적 없다* 고 한다.
- [[verification-bottleneck]] — 자동 수정 조건 셋이 전부 검증 장치인데 만든 사람은 *검증은 과대평가됐다* 고 말한다. 두 말은 *초록불을 믿되 안심하지 않는다* 로 이어진다.

## 미해결

- Pi가 어떤 모델 · 하네스 구조를 쓰는지, 다른 코딩 에이전트와 무엇이 다른지는 소스에 없다.
- 분류 봇을 만든 *데이비드* 의 성, P0 이슈의 번호는 캡션에 없다.

## References

- [[tech-bridge-zechner-ronacher-verification-is-overrated]] · [[mario-zechner]] · [[armin-ronacher]]
