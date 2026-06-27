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
| `Self Encapsulate Field` | https://refactoring.guru/self-encapsulate-field | 클래스 내부에서도 필드에 직접 접근하지 말고 getter/setter를 통해서만 접근한다. |
| `Replace Data Value with Object` | https://refactoring.guru/replace-data-value-with-object | 고유한 동작·연관 데이터를 가진 데이터 필드를 별도 클래스(객체)로 승격한다. |
| `Change Value to Reference` | https://refactoring.guru/change-value-to-reference | 동일한 값 객체 인스턴스가 여러 개 존재할 때 단일 참조 객체로 통합한다. |
| `Change Reference to Value` | https://refactoring.guru/change-reference-to-value | 생명주기 관리 부담이 큰, 작고 잘 안 변하는 참조 객체를 값 객체로 바꾼다. |
| `Replace Array with Object` | https://refactoring.guru/replace-array-with-object | 서로 다른 의미의 요소가 섞인 배열을 요소별 필드를 가진 객체로 바꾼다. |
| `Duplicate Observed Data` | https://refactoring.guru/duplicate-observed-data | GUI 클래스에 든 도메인 데이터를 별도 도메인 클래스로 분리하고 양쪽을 동기화한다. |
| `Change Unidirectional Association to Bidirectional` | https://refactoring.guru/change-unidirectional-association-to-bidirectional | 서로의 기능이 필요하지만 단방향인 연관에 반대 방향 참조를 추가한다. |
| `Change Bidirectional Association to Unidirectional` | https://refactoring.guru/change-bidirectional-association-to-unidirectional | 한쪽이 더 이상 쓰지 않는 양방향 연관에서 불필요한 방향을 제거한다. |
| `Replace Magic Number with Symbolic Constant` | https://refactoring.guru/replace-magic-number-with-symbolic-constant | 특정 의미를 가진 숫자 리터럴을 의미를 드러내는 이름의 상수로 대체한다. |
| `Encapsulate Field` | https://refactoring.guru/encapsulate-field | public 필드를 private으로 바꾸고 접근 메서드를 통해서만 다루게 한다. |
| `Encapsulate Collection` | https://refactoring.guru/encapsulate-collection | 컬렉션 getter는 읽기 전용으로 반환하고 추가·삭제 전용 메서드를 따로 둔다. |
| `Replace Type Code with Class` | https://refactoring.guru/replace-type-code-with-class | 동작에 영향 없는 타입 코드를 전용 클래스로 만들어 타입 안전성을 높인다. |
| `Replace Type Code with Subclasses` | https://refactoring.guru/replace-type-code-with-subclasses | 동작을 분기시키는 타입 코드를 값마다 서브클래스로 만들어 다형성으로 대체할 길을 연다. |
| `Replace Type Code with State/Strategy` | https://refactoring.guru/replace-type-code-with-state-strategy | 서브클래스로 뺄 수 없는 동작 분기 타입 코드를 상태·전략 객체로 치환한다. |
| `Replace Subclass with Fields` | https://refactoring.guru/replace-subclass-with-fields | 상수만 다르게 반환하는 서브클래스들을 부모 클래스의 필드로 대체하고 서브클래스를 제거한다. |

## 적용 메모

- 한 번에 여러 technique를 섞기보다, 컴파일·테스트 가능한 작은 commit으로 나눈다.
- technique 이름은 구현 세부가 아니라 리뷰 커뮤니케이션 단위로 쓴다.
- smell이 사라졌는지보다 다음 변경이 쉬워졌는지를 검증한다.

## References

- [[refactoring-guru-refactoring]] — https://refactoring.guru/refactoring/techniques/organizing-data
