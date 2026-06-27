---
title: Composing Methods
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [refactoring-techniques, refactoring, code-smells]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Composing Methods

긴 메서드를 작은 의도 단위로 쪼개거나, 반대로 불필요한 간접층을 인라인해 메서드 내부 구성을 다듬는다. 이 family는 [[refactoring-techniques]] 카탈로그의 일부이며, [[code-smells]] 중 특히 응집도·결합도·표현력 문제를 작은 변환으로 낮추는 데 쓰인다.

## Techniques

| Technique | URL | 요약 |
|---|---|---|
| `Extract Method` | https://refactoring.guru/extract-method | Problem: You have a code fragment that can be grouped together. Solution: Move this code to a separate new method (or function) and replace the old code with a call to the method. |
| `Inline Method` | https://refactoring.guru/inline-method | Problem: When a method body is more obvious than the method itself, use this technique. Solution: Replace calls to the method with the method’s content and delete the method itself |
| `Extract Variable` | https://refactoring.guru/extract-variable | Problem: You have an expression that’s hard to understand. Solution: Place the result of the expression or its parts in separate variables that are self-explanatory. |
| `Inline Temp` | https://refactoring.guru/inline-temp | Problem: You have a temporary variable that’s assigned the result of a simple expression and nothing more. Solution: Replace the references to the variable with the expression itse |
| `Replace Temp with Query` | https://refactoring.guru/replace-temp-with-query | Problem: You place the result of an expression in a local variable for later use in your code. Solution: Move the entire expression to a separate method and return the result from  |
| `Split Temporary Variable` | https://refactoring.guru/split-temporary-variable | Problem: You have a local variable that’s used to store various intermediate values inside a method (except for cycle variables). Solution: Use different variables for different va |
| `Remove Assignments to Parameters` | https://refactoring.guru/remove-assignments-to-parameters | Problem: Some value is assigned to a parameter inside method’s body. Solution: Use a local variable instead of a parameter. |
| `Replace Method with Method Object` | https://refactoring.guru/replace-method-with-method-object | Problem: You have a long method in which the local variables are so intertwined that you can’t apply Extract Method. Solution: Transform the method into a separate class so that th |
| `Substitute Algorithm` | https://refactoring.guru/substitute-algorithm | Problem: So you want to replace an existing algorithm with a new one? Solution: Replace the body of the method that implements the algorithm with a new algorithm. |

## 적용 메모

- 한 번에 여러 technique를 섞기보다, 컴파일·테스트 가능한 작은 commit으로 나눈다.
- technique 이름은 구현 세부가 아니라 리뷰 커뮤니케이션 단위로 쓴다.
- smell이 사라졌는지보다 다음 변경이 쉬워졌는지를 검증한다.

## References

- [[refactoring-guru-refactoring]] — https://refactoring.guru/refactoring/techniques/composing-methods
