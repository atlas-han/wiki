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
| `Pull Up Field` | https://refactoring.guru/pull-up-field | 여러 서브클래스에 중복된 동일 필드를 상위 클래스로 끌어올린다. |
| `Pull Up Method` | https://refactoring.guru/pull-up-method | 서브클래스마다 같은 일을 하는 메서드를 동일하게 만든 뒤 상위 클래스로 끌어올린다. |
| `Pull Up Constructor Body` | https://refactoring.guru/pull-up-constructor-body | 서브클래스 생성자에 공통된 코드를 상위 클래스 생성자로 올려 호출하게 한다. |
| `Push Down Method` | https://refactoring.guru/push-down-method | 일부 서브클래스만 쓰는 상위 클래스의 동작을 해당 서브클래스로 내린다. |
| `Push Down Field` | https://refactoring.guru/push-down-field | 일부 서브클래스에서만 쓰이는 필드를 해당 서브클래스로 내린다. |
| `Extract Subclass` | https://refactoring.guru/extract-subclass | 특정 경우에만 쓰이는 기능을 새 서브클래스로 분리한다. |
| `Extract Superclass` | https://refactoring.guru/extract-superclass | 공통 필드·메서드를 가진 두 클래스의 공통부를 새 상위 클래스로 추출한다. |
| `Extract Interface` | https://refactoring.guru/extract-interface | 여러 클라이언트가 공유하는 인터페이스 부분을 별도 인터페이스로 분리한다. |
| `Collapse Hierarchy` | https://refactoring.guru/collapse-hierarchy | 상위·하위 클래스가 거의 같아졌으면 둘을 하나로 병합한다. |
| `Form Template Method` | https://refactoring.guru/form-template-method | 순서는 같고 일부 단계만 다른 서브클래스 알고리즘에서 공통 골격을 상위 클래스의 템플릿 메서드로 추출한다. |
| `Replace Inheritance with Delegation` | https://refactoring.guru/replace-inheritance-with-delegation | 상위 클래스 일부만 쓰는 상속을 필드 위임 관계로 바꿔 결합을 낮춘다. |
| `Replace Delegation with Inheritance` | https://refactoring.guru/replace-delegation-with-inheritance | 모든 메서드를 그대로 위임하는 단순 위임을 상속으로 바꿔 위임 보일러플레이트를 없앤다. |

## 적용 메모

- 한 번에 여러 technique를 섞기보다, 컴파일·테스트 가능한 작은 commit으로 나눈다.
- technique 이름은 구현 세부가 아니라 리뷰 커뮤니케이션 단위로 쓴다.
- smell이 사라졌는지보다 다음 변경이 쉬워졌는지를 검증한다.

## References

- [[refactoring-guru-refactoring]] — https://refactoring.guru/refactoring/techniques/dealing-with-generalization
