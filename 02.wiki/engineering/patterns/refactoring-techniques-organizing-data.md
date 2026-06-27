---
title: Organizing Data
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [refactoring-techniques, refactoring, code-smells]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Organizing Data

primitive, 배열, type code, association 등 데이터 표현을 도메인 의미와 변경 축에 맞게 재구성한다. 이 family는 [[refactoring-techniques]] 카탈로그의 일부이며, [[code-smells]] 중 특히 응집도·결합도·표현력 문제를 작은 변환으로 낮추는 데 쓰인다.

## Techniques

| Technique | URL | 요약 |
|---|---|---|
| `Self Encapsulate Field` | https://refactoring.guru/self-encapsulate-field | Problem: You use direct access to private fields inside a class. Solution: Create a getter and setter for the field, and use only them for accessing the field. |
| `Replace Data Value with Object` | https://refactoring.guru/replace-data-value-with-object | Problem: A class (or group of classes) contains a data field. The field has its own behavior and associated data. Solution: Create a new class, place the old field and its behavior |
| `Change Value to Reference` | https://refactoring.guru/change-value-to-reference | Problem: So you have many identical instances of a single class that you need to replace with a single object. Solution: Convert the identical objects to a single reference object. |
| `Change Reference to Value` | https://refactoring.guru/change-reference-to-value | Problem: You have a reference object that’s too small and infrequently changed to justify managing its life cycle. Solution: Turn it into a value object. |
| `Replace Array with Object` | https://refactoring.guru/replace-array-with-object | Problem: You have an array that contains various types of data. Solution: Replace the array with an object that will have separate fields for each element. |
| `Duplicate Observed Data` | https://refactoring.guru/duplicate-observed-data | Problem: Is domain data stored in classes responsible for the GUI? Solution: Then it’s a good idea to separate the data into separate classes, ensuring connection and synchronizati |
| `Change Unidirectional Association to Bidirectional` | https://refactoring.guru/change-unidirectional-association-to-bidirectional | Problem: You have two classes that each need to use the features of the other, but the association between them is only unidirectional. Solution: Add the missing association to the |
| `Change Bidirectional Association to Unidirectional` | https://refactoring.guru/change-bidirectional-association-to-unidirectional | Problem: You have a bidirectional association between classes, but one of the classes doesn’t use the other’s features. Solution: Remove the unused association. |
| `Replace Magic Number with Symbolic Constant` | https://refactoring.guru/replace-magic-number-with-symbolic-constant | Problem: Your code uses a number that has a certain meaning to it. Solution: Replace this number with a constant that has a human-readable name explaining the meaning of the number |
| `Encapsulate Field` | https://refactoring.guru/encapsulate-field | Problem: You have a public field. Solution: Make the field private and create access methods for it. |
| `Encapsulate Collection` | https://refactoring.guru/encapsulate-collection | Problem: A class contains a collection field and a simple getter and setter for working with the collection. Solution: Make the getter-returned value read-only and create methods f |
| `Replace Type Code with Class` | https://refactoring.guru/replace-type-code-with-class | Problem: A class has a field that contains type code. The values of this type aren’t used in operator conditions and don’t affect the behavior of the program. Solution: Create a ne |
| `Replace Type Code with Subclasses` | https://refactoring.guru/replace-type-code-with-subclasses | Problem: You have a coded type that directly affects program behavior (values of this field trigger various code in conditionals). Solution: Create subclasses for each value of the |
| `Replace Type Code with State/Strategy` | https://refactoring.guru/replace-type-code-with-state-strategy | Problem: You have a coded type that affects behavior but you can’t use subclasses to get rid of it. Solution: Replace type code with a state object. If it’s necessary to replace a  |
| `Replace Subclass with Fields` | https://refactoring.guru/replace-subclass-with-fields | Problem: You have subclasses differing only in their (constant-returning) methods. Solution: Replace the methods with fields in the parent class and delete the subclasses. |

## 적용 메모

- 한 번에 여러 technique를 섞기보다, 컴파일·테스트 가능한 작은 commit으로 나눈다.
- technique 이름은 구현 세부가 아니라 리뷰 커뮤니케이션 단위로 쓴다.
- smell이 사라졌는지보다 다음 변경이 쉬워졌는지를 검증한다.

## References

- [[refactoring-guru-refactoring]] — https://refactoring.guru/refactoring/techniques/organizing-data
