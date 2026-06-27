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
| `Move Method` | https://refactoring.guru/move-method | 자기 클래스보다 다른 클래스에서 더 많이 쓰이는 메서드를 그 클래스로 옮기고 호출을 위임·대체한다. |
| `Move Field` | https://refactoring.guru/move-field | 자기 클래스보다 다른 클래스에서 더 많이 쓰이는 필드를 그 클래스로 옮기고 사용처를 그쪽으로 돌린다. |
| `Extract Class` | https://refactoring.guru/extract-class | 한 클래스가 두 역할을 맡고 있으면 관련 필드·메서드를 새 클래스로 분리한다. |
| `Inline Class` | https://refactoring.guru/inline-class | 책임이 거의 없는 클래스의 기능을 다른 클래스로 합치고 그 클래스를 제거한다. |
| `Hide Delegate` | https://refactoring.guru/hide-delegate | 클라이언트가 위임 객체를 직접 거치지 않도록 위임 메서드를 만들어 의존을 감춘다. |
| `Remove Middle Man` | https://refactoring.guru/remove-middle-man | 단순 위임만 하는 메서드가 너무 많으면 제거하고 클라이언트가 실제 객체를 직접 호출하게 한다. |
| `Introduce Foreign Method` | https://refactoring.guru/introduce-foreign-method | 수정할 수 없는 유틸리티 클래스에 필요한 메서드를, 그 객체를 인수로 받는 클라이언트 측 메서드로 추가한다. |
| `Introduce Local Extension` | https://refactoring.guru/introduce-local-extension | 수정할 수 없는 유틸리티 클래스에 여러 메서드가 필요하면 서브클래스나 래퍼로 확장 클래스를 만든다. |

## 적용 메모

- 한 번에 여러 technique를 섞기보다, 컴파일·테스트 가능한 작은 commit으로 나눈다.
- technique 이름은 구현 세부가 아니라 리뷰 커뮤니케이션 단위로 쓴다.
- smell이 사라졌는지보다 다음 변경이 쉬워졌는지를 검증한다.

## References

- [[refactoring-guru-refactoring]] — https://refactoring.guru/refactoring/techniques/moving-features-between-objects
