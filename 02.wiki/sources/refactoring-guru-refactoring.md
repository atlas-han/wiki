---
title: Refactoring.Guru Refactoring
type: source
tags: [source, engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
source-url: https://refactoring.guru/refactoring
source-type: docs
date-published: unknown
ingested: 2026-06-27
---

# Refactoring.Guru Refactoring

Refactoring.Guru의 refactoring 섹션은 리팩터링을 “새 기능 추가 없이 코드 내부 구조를 개선하는 통제 가능한 과정”으로 설명하고, [[code-smells]] → [[refactoring-techniques]] → [[refactoring]] workflow로 연결한다. 본 위키에는 저작권 보호 본문 전문을 복제하지 않고, URL inventory와 실무 의사결정에 필요한 요약만 보존한다.

## 핵심 takeaway

1. **리팩터링은 기능 개발과 분리된 품질 투자**다. 외부 동작은 유지하면서 내부 구조를 바꾸므로, 자동화 테스트와 작은 step이 전제다.
2. **[[code-smells]]는 진단 언어**다. 냄새는 버그가 아니라 변경 비용·이해 비용이 커졌다는 신호이며, 어떤 [[refactoring-techniques]]를 적용할지 고르는 출발점이다.
3. **[[technical-debt]]는 품질 문제가 아니라 이자 비용 문제**다. 빠른 delivery를 위해 미룬 구조 개선이 이후 변경마다 비용을 키운다.
4. **카탈로그는 recipe가 아니라 vocabulary**다. `Extract Method`, `Move Method`, `Replace Conditional with Polymorphism` 같은 이름은 리뷰·설계 토론에서 변경 의도를 압축하는 용어로 유용하다.

## 보존 범위

- 원문 inventory: `01.raw/docs/refactoring-guru-refactoring/00-inventory.md`
- 신규 engineering hub: [[refactoring]], [[technical-debt]], [[code-smells]], [[refactoring-techniques]]
- 신규 code smell 개별 페이지: 23개
- 신규 refactoring technique family 페이지: 6개

## References

- Refactoring.Guru Refactoring: https://refactoring.guru/refactoring
- Catalog: https://refactoring.guru/refactoring/catalog
- Code Smells: https://refactoring.guru/refactoring/smells
- Refactorings: https://refactoring.guru/refactoring/techniques
