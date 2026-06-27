---
title: Dealing with Generalization
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [refactoring-techniques, refactoring, code-smells]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Dealing with Generalization

상속·위임·공통화·계층 병합을 조정해 일반화 구조를 실제 변경 요구에 맞춘다. 이 family는 [[refactoring-techniques]] 카탈로그의 일부이며, [[code-smells]] 중 특히 응집도·결합도·표현력 문제를 작은 변환으로 낮추는 데 쓰인다.

## Techniques

| Technique | URL | 요약 |
|---|---|---|
| `Pull Up Field` | https://refactoring.guru/pull-up-field | Problem: Two classes have the same field. Solution: Remove the field from subclasses and move it to the superclass. |
| `Pull Up Method` | https://refactoring.guru/pull-up-method | Problem: Your subclasses have methods that perform similar work. Solution: Make the methods identical and then move them to the relevant superclass. |
| `Pull Up Constructor Body` | https://refactoring.guru/pull-up-constructor-body | Problem: Your subclasses have constructors with code that’s mostly identical. Solution: Create a superclass constructor and move the code that’s the same in the subclasses to it. C |
| `Push Down Method` | https://refactoring.guru/push-down-method | Problem: Is behavior implemented in a superclass used by only one (or a few) subclasses? Solution: Move this behavior to the subclasses. |
| `Push Down Field` | https://refactoring.guru/push-down-field | Problem: Is a field used only in a few subclasses? Solution: Move the field to these subclasses. |
| `Extract Subclass` | https://refactoring.guru/extract-subclass | Problem: A class has features that are used only in certain cases. Solution: Create a subclass and use it in these cases. |
| `Extract Superclass` | https://refactoring.guru/extract-superclass | Problem: You have two classes with common fields and methods. Solution: Create a shared superclass for them and move all the identical fields and methods to it. |
| `Extract Interface` | https://refactoring.guru/extract-interface | Problem: Multiple clients are using the same part of a class interface. Another case: part of the interface in two classes is the same. Solution: Move this identical portion to its |
| `Collapse Hierarchy` | https://refactoring.guru/collapse-hierarchy | Problem: You have a class hierarchy in which a subclass is practically the same as its superclass. Solution: Merge the subclass and superclass. |
| `Form Template Method` | https://refactoring.guru/form-template-method | Problem: Your subclasses implement algorithms that contain similar steps in the same order. Solution: Move the algorithm structure and identical steps to a superclass, and leave im |
| `Replace Inheritance with Delegation` | https://refactoring.guru/replace-inheritance-with-delegation | Problem: You have a subclass that uses only a portion of the methods of its superclass (or it’s not possible to inherit superclass data). Solution: Create a field and put a supercl |
| `Replace Delegation with Inheritance` | https://refactoring.guru/replace-delegation-with-inheritance | Problem: A class contains many simple methods that delegate to all methods of another class. Solution: Make the class a delegate inheritor, which makes the delegating methods unnec |

## 적용 메모

- 한 번에 여러 technique를 섞기보다, 컴파일·테스트 가능한 작은 commit으로 나눈다.
- technique 이름은 구현 세부가 아니라 리뷰 커뮤니케이션 단위로 쓴다.
- smell이 사라졌는지보다 다음 변경이 쉬워졌는지를 검증한다.

## References

- [[refactoring-guru-refactoring]] — https://refactoring.guru/refactoring/techniques/dealing-with-generalization
