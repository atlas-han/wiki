---
title: Simplifying Conditional Expressions
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [refactoring-techniques, refactoring, code-smells]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Simplifying Conditional Expressions

복잡한 조건식을 명명·분해·다형성·guard clause 등으로 단순화한다. 이 family는 [[refactoring-techniques]] 카탈로그의 일부이며, [[code-smells]] 중 특히 응집도·결합도·표현력 문제를 작은 변환으로 낮추는 데 쓰인다.

## Techniques

| Technique | URL | 요약 |
|---|---|---|
| `Decompose Conditional` | https://refactoring.guru/decompose-conditional | 복잡한 조건·then·else 부분을 의미가 드러나는 별도 메서드로 분해한다. |
| `Consolidate Conditional Expression` | https://refactoring.guru/consolidate-conditional-expression | 같은 결과로 이어지는 여러 조건을 하나의 표현식으로 합치고 메서드로 추출한다. |
| `Consolidate Duplicate Conditional Fragments` | https://refactoring.guru/consolidate-duplicate-conditional-fragments | 모든 분기에 중복된 코드를 조건문 밖으로 빼낸다. |
| `Remove Control Flag` | https://refactoring.guru/remove-control-flag | 흐름을 제어하는 불린 플래그 변수를 break·continue·return으로 대체한다. |
| `Replace Nested Conditional with Guard Clauses` | https://refactoring.guru/replace-nested-conditional-with-guard-clauses | 특수·예외 케이스를 guard clause로 먼저 처리해 중첩 조건을 평탄하게 만든다. |
| `Replace Conditional with Polymorphism` | https://refactoring.guru/replace-conditional-with-polymorphism | 타입·속성에 따라 분기하는 조건문을 서브클래스의 다형 메서드 호출로 대체한다. |
| `Introduce Null Object` | https://refactoring.guru/introduce-null-object | null 대신 기본 동작을 수행하는 null 객체를 반환해 곳곳의 null 체크를 없앤다. |
| `Introduce Assertion` | https://refactoring.guru/introduce-assertion | 코드가 암묵적으로 가정하는 전제 조건을 명시적인 assertion으로 드러낸다. |

## 적용 메모

- 한 번에 여러 technique를 섞기보다, 컴파일·테스트 가능한 작은 commit으로 나눈다.
- technique 이름은 구현 세부가 아니라 리뷰 커뮤니케이션 단위로 쓴다.
- smell이 사라졌는지보다 다음 변경이 쉬워졌는지를 검증한다.

## References

- [[refactoring-guru-refactoring]] — https://refactoring.guru/refactoring/techniques/simplifying-conditional-expressions
