---
title: Exception Handling as the Job
type: concept
category: theory
tags: [automation, operations, edge-cases, scale, agents]
related: [self-serve-asset-generation, atomic-design, dynamic-workflows, agent-roi-measurement, architecture-as-remaining-art, action-reversibility]
first-seen: tech-bridge-one-designer-plus-ai
sources: [tech-bridge-one-designer-plus-ai]
created: 2026-09-15
updated: 2026-09-15
---

# Exception Handling as the Job

**자동화의 값은 정상 경로가 빨라지는 데 있지 않고, 정상 경로 밖이 생겼을 때 그것을 만드는 비용이 무너지는 데 있다.**

[[tech-bridge-one-designer-plus-ai]]의 한 문장:

> **그리고 진짜 일은 예외 처리입니다.** (14:45)

사례가 곧바로 따라온다. 일정표 생성기에 **편집 버튼이 없었다.** 어느 날 아침 일정이 바뀌었고 —

> **그냥 [[devin|Devin]]에게 "편집 버튼 하나 만들어 줄래?" 했고, 만들어 줬습니다.** 이제 전부 바꿔서 PNG로 내보내 화면에 다시 꽂을 수 있습니다. **그런 예외들은 예전에 손으로 해야 했을 때는 불가능했는데 이제는 훨씬 쉬워졌습니다.** (15:08~15:32)

## 왜 이것이 자동화 논의의 중심인가

자동화 도구를 평가할 때 대개 **정상 경로의 처리량**을 잰다. 그런데 실제 운영에서 시간을 먹는 것은 **한 번밖에 일어나지 않는 일들**이고, 그것들은 정의상 **미리 만들어 둘 수 없다.** 전통적으로 그 비용은 *"개발자에게 요청 → 우선순위 다툼 → 며칠"* 이었고, 그래서 **대개 수작업으로 우회**했다.

에이전트가 바꾸는 것은 **1회용 기능의 한계비용**이다. 그래서 *"이건 기능으로 만들 만큼 자주 일어나지 않아"* 라는 판단 자체가 흔들린다.

## 맺음말과의 연결

화자의 처방은 **작게 생각하기**다 — *"잘못될 수 있고 잘못될 모든 것을 생각해서 미리 풀어 두세요."* 겉보기에 *"예외는 미리 못 만든다"* 와 충돌하는 듯하지만 **층이 다르다**: **예상 가능한 예외는 미리 세고**, **예상 못한 예외는 즉석에서 만든다.** [[atomic-design]]이 방법론 층에서, 이 페이지가 운영 층에서 같은 형태를 반복한다.

> ⚠️ **즉석 기능에 대한 검토·롤백 이야기가 소스에 없다.** 아침에 급히 붙인 편집 버튼이 잘못 동작하면 무슨 일이 생기는지, 누가 확인하는지 다루지 않는다([[action-reversibility]]가 가리키는 자리).

## References

- [[tech-bridge-one-designer-plus-ai]] · [[vincent-wendy]] · [[devin]]
