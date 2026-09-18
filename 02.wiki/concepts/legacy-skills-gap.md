---
title: 레거시 숙련 격차 (Legacy Skills Gap)
type: concept
category: framing
tags: [legacy, workforce, cobol, mainframe, modernization, productivity]
aliases: [개발자를 늘려도 현대화는 빨라지지 않는다, COBOL 세대의 은퇴]
related: [legacy-code-modernization, technical-debt, ai-engineer-vs-ml-researcher, three-tier-ai-skill-stack, read-fluency-for-agent-output]
first-seen: tech-bridge-legacy-code-modernization-ai
sources: [tech-bridge-legacy-code-modernization-ai]
created: 2026-09-18
updated: 2026-09-18
---

# 레거시 숙련 격차

**개발자 수를 늘려도 현대화가 빨라지지 않는다 — 옛 시스템을 아는 사람은 은퇴하고, 새로 들어오는 사람은 다른 스택을 배웠기 때문이다.** [[anna-gutowska|Anna Gutowska]]([[ibm|IBM]])가 [[tech-bridge-legacy-code-modernization-ai]]에서 레거시 문제를 악화시키는 첫 번째 추세로 꼽았다.

> 첫째, **개발자 수가 많다고 해서 현대화 속도가 빨라지는 것은 아닙니다.** COBOL, 메인프레임 아키텍처, 레거시 프레임워크와 같은 오래된 시스템을 깊이 이해하는 개발자들이 **은퇴하고 있습니다.** 신입 졸업생들은 파이썬, 자바스크립트, 클라우드 네이티브 아키텍처 등에 대한 교육을 받습니다. **숙련 격차가 점점 커지고 있습니다.** (02:11~02:49)

## 왜 인원이 답이 아닌가

병목이 **인원**이 아니라 **특정 숙련의 분포**에 있다. 레거시의 정의([[legacy-code-modernization]])가 *아무도 완전히 이해하지 못하는 도메인 로직* 이므로, 그 로직을 아는 마지막 사람들이 떠나면 **인원을 아무리 붙여도 이해가 복원되지 않는다.** 옛 플레이북(*"몇 달씩 코드를 읽는다"*)이 그래서 몇 달인 것이다 — 읽어서 복원하는 것 말고 방법이 없었다.

## AI가 겨냥하는 자리

이 소스에서 AI의 첫 역할(**발견** — 코드베이스를 읽고 모듈 기능·데이터 흐름·도메인 로직 위치를 요약)은 정확히 이 격차를 겨냥한다 — **떠난 사람의 이해를 코드에서 다시 끌어낸다.** ⚠️ 다만 소스는 *"몇 달 → 몇 주"* 라고만 하고 근거를 주지 않으며, 같은 영상의 한계 절이 *"매우 복잡하게 얽힌 도메인별 논리"* 에 AI가 약하다고 말한다 — **격차가 가장 큰 바로 그 자리에서 AI가 가장 약하다**는 긴장을 화자는 다루지 않는다.

## 이 위키의 다른 페이지와의 자리

- [[ai-engineer-vs-ml-researcher]] · [[three-tier-ai-skill-stack]](09-16, 같은 [[ibm]]) — 그쪽은 **새로 필요한 숙련**(AI 엔지니어)을 말하고, 이쪽은 **사라지는 숙련**(COBOL·메인프레임)을 말한다. 같은 벤더의 교육 콘텐츠가 숙련의 **양 끝**을 하루 간격으로 다뤘다.
- [[read-fluency-for-agent-output]] — *쓰기는 오프로드하고 읽기는 남긴다* 가 여기서는 **옛 코드 읽기**에 적용된다: AI가 요약해도 그 요약이 맞는지는 읽을 줄 아는 사람이 봐야 한다. 소스는 이 연결을 하지 않는다.
- [[technical-debt]] — 부채를 갚을 사람이 없어지는 것도 이자의 한 형태다.

## 표시해 둔 것

> ⚠️ **은퇴 규모·시점·산업별 수치가 없다.** *"기술 격차"* 라는 ko 표기는 technology/skill이 겹쳐 뜻이 흐리다(raw 헤더 참조). **신입 교육 과정에 대한 서술도 일반론**이다.

## References

- [[tech-bridge-legacy-code-modernization-ai]] · [[anna-gutowska]] · [[ibm]]
- 관련: [[legacy-code-modernization]] · [[technical-debt]] · [[ai-engineer-vs-ml-researcher]] · [[three-tier-ai-skill-stack]] · [[read-fluency-for-agent-output]]
