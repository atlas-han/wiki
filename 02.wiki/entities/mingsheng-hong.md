---
title: Mingsheng Hong
type: entity
category: person
tags: [ironclad, engineering-leadership, developer-productivity, token-economics]
aliases: [Mingshan Hong]
links:
  - https://www.linkedin.com/in/mingshenghong/
sources: [tech-bridge-trusted-throughput]
created: 2026-09-02
updated: 2026-09-02
---

# Mingsheng Hong

[[ironclad|Ironclad]]에서 AI를 담당하는 VP of Engineering. 본 위키 첫 등장은 [[tech-bridge]] 재배포 강연 [[tech-bridge-trusted-throughput]] (2026-09-01).

> ⚠️ **표기 불일치**: 영상 제목은 "Mingsheng Hong", 설명란 본문은 "Mingshan Hong", 자막 ASR은 "Minshan". 설명란이 링크한 LinkedIn 슬러그가 `mingshenghong`이라 이 위키는 제목 표기를 따르되 불일치를 해소하지 않고 기록한다.

## 위키에서 알려진 사실

- [[trusted-throughput]] 프레이밍의 제시자.
- 핵심 논증은 **토큰 = LOC 비유**: *"LOC는 중요한 지표이지만, 직접적으로 최적화해야 할 대상은 아닙니다. 토큰 사용량과 지출도 마찬가지입니다."*
- 토큰 대시보드를 **연기 감지기**로 규정하고, 조사할 신호는 많이 쓰는 쪽이 아니라 **거의 안 쓰는 국소적 집단**이라고 방향을 뒤집는다.
- 목표를 명시적으로 부정한다 — *"'긴축(austerity)'에 관한 것이 아니라"* ROI 향상에 관한 것.
- 지표 진화 경로를 실패 단계까지 공개: LOC → 열린 PR → 병합 PR → **복잡도 가중치가 적용된 병합 PR**. 복잡도는 LLM 1~2개에 프롬프트를 넣어 **티셔츠 사이즈**로 채점.
- 병목 이동을 **코드 리뷰와 CI**로 특정하고, flaky 테스트가 재시도를 유발해 **토큰 낭비의 원인이 CI 품질일 수 있다**는 연결을 제시.
- 안티패턴 경고: CI 과부하 때문에 **PR 분할을 중단**하는 것 — 사람 검토 부담이 커지고 주의력 분산으로 검토 품질이 떨어진다.
- build vs. buy 원칙: IDE·CI 인프라처럼 **차별화되지 않는 것은 구매**, 내부에서는 상황에 특화된 **프롬프트 플레이북**을 만든다.

## References

- [[tech-bridge-trusted-throughput]] — 22:21, 2026-09-01
