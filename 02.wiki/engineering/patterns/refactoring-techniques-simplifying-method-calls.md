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
| `Rename Method` | https://refactoring.guru/rename-method | 동작을 제대로 설명하지 못하는 메서드 이름을 의미가 드러나게 바꾼다. |
| `Add Parameter` | https://refactoring.guru/add-parameter | 메서드에 필요한 데이터가 부족하면 이를 전달할 매개변수를 추가한다. |
| `Remove Parameter` | https://refactoring.guru/remove-parameter | 본문에서 더 이상 쓰이지 않는 매개변수를 제거한다. |
| `Separate Query from Modifier` | https://refactoring.guru/separate-query-from-modifier | 값 반환과 상태 변경을 함께 하는 메서드를 조회용과 변경용 두 개로 분리한다. |
| `Parameterize Method` | https://refactoring.guru/parameterize-method | 내부 값만 다른 유사 메서드들을 그 값을 받는 하나의 매개변수화된 메서드로 합친다. |
| `Replace Parameter with Explicit Methods` | https://refactoring.guru/replace-parameter-with-explicit-methods | 매개변수 값에 따라 동작이 갈리는 메서드를 값마다 별도의 명시적 메서드로 나눈다. |
| `Preserve Whole Object` | https://refactoring.guru/preserve-whole-object | 객체에서 여러 값을 꺼내 넘기는 대신 객체 자체를 통째로 전달한다. |
| `Replace Parameter with Method Call` | https://refactoring.guru/replace-parameter-with-method-call | 쿼리 결과를 인수로 넘기는 대신 메서드가 직접 그 쿼리를 호출하게 한다. |
| `Introduce Parameter Object` | https://refactoring.guru/introduce-parameter-object | 여러 메서드에 반복되는 매개변수 묶음을 하나의 매개변수 객체로 대체한다. |
| `Remove Setting Method` | https://refactoring.guru/remove-setting-method | 생성 시에만 설정되고 이후 바뀌면 안 되는 필드의 setter를 제거한다. |
| `Hide Method` | https://refactoring.guru/hide-method | 외부에서 쓰이지 않는 메서드를 private·protected로 낮춰 공개 API를 줄인다. |
| `Replace Constructor with Factory Method` | https://refactoring.guru/replace-constructor-with-factory-method | 단순 필드 설정 이상을 하는 복잡한 생성자를 팩토리 메서드로 대체한다. |
| `Replace Error Code with Exception` | https://refactoring.guru/replace-error-code-with-exception | 오류를 나타내는 특수 반환값 대신 예외를 던진다. |
| `Replace Exception with Test` | https://refactoring.guru/replace-exception-with-test | 사전 조건 검사로 충분한 곳에서는 예외 대신 조건 테스트를 쓴다. |

## 적용 메모

- 한 번에 여러 technique를 섞기보다, 컴파일·테스트 가능한 작은 commit으로 나눈다.
- technique 이름은 구현 세부가 아니라 리뷰 커뮤니케이션 단위로 쓴다.
- smell이 사라졌는지보다 다음 변경이 쉬워졌는지를 검증한다.

## References

- [[refactoring-guru-refactoring]] — https://refactoring.guru/refactoring/techniques/simplifying-method-calls
