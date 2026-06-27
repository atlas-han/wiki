---
title: Simplifying Method Calls
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [refactoring-techniques, refactoring, code-smells]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Simplifying Method Calls

메서드 이름·파라미터·예외·가시성을 다듬어 API 호출면을 명확하게 만든다. 이 family는 [[refactoring-techniques]] 카탈로그의 일부이며, [[code-smells]] 중 특히 응집도·결합도·표현력 문제를 작은 변환으로 낮추는 데 쓰인다.

## Techniques

| Technique | URL | 요약 |
|---|---|---|
| `Rename Method` | https://refactoring.guru/rename-method | Problem: The name of a method doesn’t explain what the method does. Solution: Rename the method. |
| `Add Parameter` | https://refactoring.guru/add-parameter | Problem: A method doesn’t have enough data to perform certain actions. Solution: Create a new parameter to pass the necessary data. |
| `Remove Parameter` | https://refactoring.guru/remove-parameter | Problem: A parameter isn’t used in the body of a method. Solution: Remove the unused parameter. |
| `Separate Query from Modifier` | https://refactoring.guru/separate-query-from-modifier | Problem: Do you have a method that returns a value but also changes something inside an object? Solution: Split the method into two separate methods. As you would expect, one of th |
| `Parameterize Method` | https://refactoring.guru/parameterize-method | Problem: Multiple methods perform similar actions that are different only in their internal values, numbers or operations. Solution: Combine these methods by using a parameter that |
| `Replace Parameter with Explicit Methods` | https://refactoring.guru/replace-parameter-with-explicit-methods | Problem: A method is split into parts, each of which is run depending on the value of a parameter. Solution: Extract the individual parts of the method into their own methods and c |
| `Preserve Whole Object` | https://refactoring.guru/preserve-whole-object | Problem: You get several values from an object and then pass them as parameters to a method. Solution: Instead, try passing the whole object. |
| `Replace Parameter with Method Call` | https://refactoring.guru/replace-parameter-with-method-call | Problem: Calling a query method and passing its results as the parameters of another method, while that method could call the query directly. Solution: Instead of passing the value |
| `Introduce Parameter Object` | https://refactoring.guru/introduce-parameter-object | Problem: Your methods contain a repeating group of parameters. Solution: Replace these parameters with an object. |
| `Remove Setting Method` | https://refactoring.guru/remove-setting-method | Problem: The value of a field should be set only when it’s created, and not change at any time after that. Solution: So remove methods that set the field’s value. |
| `Hide Method` | https://refactoring.guru/hide-method | Problem: A method isn’t used by other classes or is used only inside its own class hierarchy. Solution: Make the method private or protected. |
| `Replace Constructor with Factory Method` | https://refactoring.guru/replace-constructor-with-factory-method | Problem: You have a complex constructor that does something more than just setting parameter values in object fields. Solution: Create a factory method and use it to replace constr |
| `Replace Error Code with Exception` | https://refactoring.guru/replace-error-code-with-exception | Problem: A method returns a special value that indicates an error? Solution: Throw an exception instead. |
| `Replace Exception with Test` | https://refactoring.guru/replace-exception-with-test | Problem: You throw an exception in a place where a simple test would do the job? Solution: Replace the exception with a condition test. |

## 적용 메모

- 한 번에 여러 technique를 섞기보다, 컴파일·테스트 가능한 작은 commit으로 나눈다.
- technique 이름은 구현 세부가 아니라 리뷰 커뮤니케이션 단위로 쓴다.
- smell이 사라졌는지보다 다음 변경이 쉬워졌는지를 검증한다.

## References

- [[refactoring-guru-refactoring]] — https://refactoring.guru/refactoring/techniques/simplifying-method-calls
