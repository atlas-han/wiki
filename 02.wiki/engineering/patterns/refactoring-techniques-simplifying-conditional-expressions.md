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
| `Decompose Conditional` | https://refactoring.guru/decompose-conditional | Problem: You have a complex conditional (if-then/else or switch). Solution: Decompose the complicated parts of the conditional into separate methods: the condition, then and else. |
| `Consolidate Conditional Expression` | https://refactoring.guru/consolidate-conditional-expression | Problem: You have multiple conditionals that lead to the same result or action. Solution: Consolidate all these conditionals in a single expression. |
| `Consolidate Duplicate Conditional Fragments` | https://refactoring.guru/consolidate-duplicate-conditional-fragments | Problem: Identical code can be found in all branches of a conditional. Solution: Move the code outside of the conditional. |
| `Remove Control Flag` | https://refactoring.guru/remove-control-flag | Problem: You have a boolean variable that acts as a control flag for multiple boolean expressions. Solution: Instead of the variable, use break, continue and return. |
| `Replace Nested Conditional with Guard Clauses` | https://refactoring.guru/replace-nested-conditional-with-guard-clauses | Problem: You have a group of nested conditionals and it’s hard to determine the normal flow of code execution. Solution: Isolate all special checks and edge cases into separate cla |
| `Replace Conditional with Polymorphism` | https://refactoring.guru/replace-conditional-with-polymorphism | Problem: You have a conditional that performs various actions depending on object type or properties. Solution: Create subclasses matching the branches of the conditional. In them, |
| `Introduce Null Object` | https://refactoring.guru/introduce-null-object | Problem: Since some methods return null instead of real objects, you have many checks for null in your code. Solution: Instead of null, return a null object that exhibits the defau |
| `Introduce Assertion` | https://refactoring.guru/introduce-assertion | Problem: For a portion of code to work correctly, certain conditions or values must be true. Solution: Replace these assumptions with specific assertion checks. |

## 적용 메모

- 한 번에 여러 technique를 섞기보다, 컴파일·테스트 가능한 작은 commit으로 나눈다.
- technique 이름은 구현 세부가 아니라 리뷰 커뮤니케이션 단위로 쓴다.
- smell이 사라졌는지보다 다음 변경이 쉬워졌는지를 검증한다.

## References

- [[refactoring-guru-refactoring]] — https://refactoring.guru/refactoring/techniques/simplifying-conditional-expressions
