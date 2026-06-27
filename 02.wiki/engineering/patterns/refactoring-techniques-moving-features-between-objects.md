---
title: Moving Features between Objects
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [refactoring-techniques, refactoring, code-smells]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Moving Features between Objects

메서드·필드·책임이 더 자연스럽게 속해야 할 객체로 이동시켜 응집도를 높이고 결합도를 낮춘다. 이 family는 [[refactoring-techniques]] 카탈로그의 일부이며, [[code-smells]] 중 특히 응집도·결합도·표현력 문제를 작은 변환으로 낮추는 데 쓰인다.

## Techniques

| Technique | URL | 요약 |
|---|---|---|
| `Move Method` | https://refactoring.guru/move-method | Problem: A method is used more in another class than in its own class. Solution: Create a new method in the class that uses the method the most, then move code from the old method  |
| `Move Field` | https://refactoring.guru/move-field | Problem: A field is used more in another class than in its own class. Solution: Create a field in a new class and redirect all users of the old field to it. |
| `Extract Class` | https://refactoring.guru/extract-class | Problem: When one class does the work of two, awkwardness results. Solution: Instead, create a new class and place the fields and methods responsible for the relevant functionality |
| `Inline Class` | https://refactoring.guru/inline-class | Problem: A class does almost nothing and isn’t responsible for anything, and no additional responsibilities are planned for it. Solution: Move all features from the class to anothe |
| `Hide Delegate` | https://refactoring.guru/hide-delegate | Problem: The client gets object B from a field or method of object А. Then the client calls a method of object B. Solution: Create a new method in class A that delegates the call t |
| `Remove Middle Man` | https://refactoring.guru/remove-middle-man | Problem: A class has too many methods that simply delegate to other objects. Solution: Delete these methods and force the client to call the end methods directly. |
| `Introduce Foreign Method` | https://refactoring.guru/introduce-foreign-method | Problem: A utility class doesn’t contain the method that you need and you can’t add the method to the class. Solution: Add the method to a client class and pass an object of the ut |
| `Introduce Local Extension` | https://refactoring.guru/introduce-local-extension | Problem: A utility class doesn’t contain some methods that you need. But you can’t add these methods to the class. Solution: Create a new class containing the methods and make it e |

## 적용 메모

- 한 번에 여러 technique를 섞기보다, 컴파일·테스트 가능한 작은 commit으로 나눈다.
- technique 이름은 구현 세부가 아니라 리뷰 커뮤니케이션 단위로 쓴다.
- smell이 사라졌는지보다 다음 변경이 쉬워졌는지를 검증한다.

## References

- [[refactoring-guru-refactoring]] — https://refactoring.guru/refactoring/techniques/moving-features-between-objects
