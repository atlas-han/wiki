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
| `Extract Method` | https://refactoring.guru/extract-method | 함께 묶이는 코드 조각을 별도 메서드로 추출하고 호출로 대체해 의도를 드러낸다. |
| `Inline Method` | https://refactoring.guru/inline-method | 메서드 본문이 이름보다 더 명확하면 호출부를 본문으로 바꾸고 메서드를 제거한다. |
| `Extract Variable` | https://refactoring.guru/extract-variable | 이해하기 어려운 표현식을 의미를 설명하는 변수에 담아 가독성을 높인다. |
| `Inline Temp` | https://refactoring.guru/inline-temp | 단순 표현식 결과만 담는 임시 변수를 그 표현식으로 직접 대체한다. |
| `Replace Temp with Query` | https://refactoring.guru/replace-temp-with-query | 표현식 결과를 담은 지역 변수를 별도 쿼리 메서드로 추출해 재사용과 추출을 쉽게 한다. |
| `Split Temporary Variable` | https://refactoring.guru/split-temporary-variable | 여러 중간값을 하나의 변수에 재사용하지 말고 값마다 별도 변수를 둔다. |
| `Remove Assignments to Parameters` | https://refactoring.guru/remove-assignments-to-parameters | 메서드 안에서 매개변수에 값을 대입하지 말고 별도 지역 변수를 사용한다. |
| `Replace Method with Method Object` | https://refactoring.guru/replace-method-with-method-object | 지역 변수가 얽혀 추출이 어려운 긴 메서드를 별도 클래스로 옮겨 분해 가능하게 만든다. |
| `Substitute Algorithm` | https://refactoring.guru/substitute-algorithm | 기존 알고리즘을 더 명확한 새 알고리즘으로 메서드 본문째 교체한다. |

## 적용 메모

- 한 번에 여러 technique를 섞기보다, 컴파일·테스트 가능한 작은 commit으로 나눈다.
- technique 이름은 구현 세부가 아니라 리뷰 커뮤니케이션 단위로 쓴다.
- smell이 사라졌는지보다 다음 변경이 쉬워졌는지를 검증한다.

## References

- [[refactoring-guru-refactoring]] — https://refactoring.guru/refactoring/techniques/composing-methods
