---
source_url: https://refactoring.guru/ko/design-patterns
ingested: 2026-06-27
sha256: 6415d06c73c88f83f0cbcb37814a2c3dd475ffacab1f36319d98041d67495a61
---

# Refactoring.Guru 한국어 Design Patterns URL Inventory

이 raw 파일은 저작권 보호 본문을 전문 보존하지 않고, 공개 URL 목록과 각 페이지의 “의도” 요약만 보존한다. 상세 본문은 원 URL을 기준으로 재확인한다.

## 생성 패턴

- 팩토리 메서드 (Factory Method) — https://refactoring.guru/ko/design-patterns/factory-method
  - source-intent: 팩토리 메서드 는 부모 클래스에서 객체들을 생성할 수 있는 인터페이스를 제공하지만, 자식 클래스들이 생성될 객체들의 유형을 변경할 수 있도록 하는 생성 패턴입니다.
- 추상 팩토리 (Abstract Factory) — https://refactoring.guru/ko/design-patterns/abstract-factory
  - source-intent: 추상 팩토리 는 관련 객체들의 구상 클래스들을 지정하지 않고도 관련 객체들의 모음을 생성할 수 있도록 하는 생성패턴입니다.
- 빌더 (Builder) — https://refactoring.guru/ko/design-patterns/builder
  - source-intent: 빌더 는 복잡한 객체들을 단계별로 생성할 수 있도록 하는 생성 디자인 패턴입니다. 이 패턴을 사용하면 같은 제작 코드를 사용하여 객체의 다양한 유형들과 표현을 제작할 수 있습니다.
- 프로토타입 (Prototype) — https://refactoring.guru/ko/design-patterns/prototype
  - source-intent: 프로토타입 은 코드를 그들의 클래스들에 의존시키지 않고 기존 객체들을 복사할 수 있도록 하는 생성 디자인 패턴입니다.
- 싱글턴 (Singleton) — https://refactoring.guru/ko/design-patterns/singleton
  - source-intent: 싱글턴 은 클래스에 인스턴스가 하나만 있도록 하면서 이 인스턴스에 대한 전역 접근​(액세스) 지점을 제공하는 생성 디자인 패턴입니다.

## 구조 패턴

- 어댑터 (Adapter) — https://refactoring.guru/ko/design-patterns/adapter
  - source-intent: 어댑터 는 호환되지 않는 인터페이스를 가진 객체들이 협업할 수 있도록 하는 구조적 디자인 패턴입니다.
- 브리지 (Bridge) — https://refactoring.guru/ko/design-patterns/bridge
  - source-intent: 브리지 는 큰 클래스 또는 밀접하게 관련된 클래스들의 집합을 두 개의 개별 계층구조​(추상화 및 구현)​로 나눈 후 각각 독립적으로 개발할 수 있도록 하는 구조 디자인 패턴입니다.
- 복합체 (Composite) — https://refactoring.guru/ko/design-patterns/composite
  - source-intent: 복합체 패턴은 객체들을 트리 구조들로 구성한 후, 이러한 구조들과 개별 객체들처럼 작업할 수 있도록 하는 구조 패턴입니다.
- 데코레이터 (Decorator) — https://refactoring.guru/ko/design-patterns/decorator
  - source-intent: 데코레이터 는 객체들을 새로운 행동들을 포함한 특수 래퍼 객체들 내에 넣어서 위 행동들을 해당 객체들에 연결시키는 구조적 디자인 패턴입니다.
- 퍼사드 (Facade) — https://refactoring.guru/ko/design-patterns/facade
  - source-intent: 퍼사드 패턴은 라이브러리에 대한, 프레임워크에 대한 또는 다른 클래스들의 복잡한 집합에 대한 단순화된 인터페이스를 제공하는 구조적 디자인 패턴입니다.
- 플라이웨이트 (Flyweight) — https://refactoring.guru/ko/design-patterns/flyweight
  - source-intent: 플라이웨이트 는 각 객체에 모든 데이터를 유지하는 대신 여러 객체들 간에 상태의 공통 부분들을 공유하여 사용할 수 있는 RAM에 더 많은 객체들을 포함할 수 있도록 하는 구조 디자인 패턴입니다.
- 프록시 (Proxy) — https://refactoring.guru/ko/design-patterns/proxy
  - source-intent: 프록시 는 다른 객체에 대한 대체 또는 자리표시자를 제공할 수 있는 구조 디자인 패턴입니다. 프록시는 원래 객체에 대한 접근을 제어하므로, 당신의 요청이 원래 객체에 전달되기 전 또는 후에 무언가를 수행할 수 있도록 합니다.

## 행동 패턴

- 책임 연쇄 (Chain of Responsibility) — https://refactoring.guru/ko/design-patterns/chain-of-responsibility
  - source-intent: 책임 연쇄 패턴은 핸들러들의 체인​(사슬)​을 따라 요청을 전달할 수 있게 해주는 행동 디자인 패턴입니다. 각 핸들러는 요청을 받으면 요청을 처리할지 아니면 체인의 다음 핸들러로 전달할지를 결정합니다.
- 커맨드 (Command) — https://refactoring.guru/ko/design-patterns/command
  - source-intent: 커맨드 는 요청을 요청에 대한 모든 정보가 포함된 독립실행형 객체로 변환하는 행동 디자인 패턴입니다. 이 변환은 다양한 요청들이 있는 메서드들을 인수화 할 수 있도록 하며, 요청의 실행을 지연 또는 대기열에 넣을 수 있도록 하고, 또 실행 취소할 수 있는 작업을 지원할 수 있도록 합니다.
- 반복자 (Iterator) — https://refactoring.guru/ko/design-patterns/iterator
  - source-intent: 반복자 는 컬렉션의 요소들의 기본 표현​(리스트, 스택, 트리 등)​을 노출하지 않고 그들을 하나씩 순회할 수 있도록 하는 행동 디자인 패턴입니다.
- 중재자 (Mediator) — https://refactoring.guru/ko/design-patterns/mediator
  - source-intent: 중재자 는 객체 간의 혼란스러운 의존 관계들을 줄일 수 있는 행동 디자인 패턴입니다. 이 패턴은 객체 간의 직접 통신을 제한하고 중재자 객체를 통해서만 협력하도록 합니다.
- 메멘토 (Memento) — https://refactoring.guru/ko/design-patterns/memento
  - source-intent: 메멘토 는 객체의 구현 세부 사항을 공개하지 않으면서 해당 객체의 이전 상태를 저장하고 복원할 수 있게 해주는 행동 디자인 패턴입니다.
- 옵서버 (Observer) — https://refactoring.guru/ko/design-patterns/observer
  - source-intent: 옵서버 패턴은 당신이 여러 객체에 자신이 관찰 중인 객체에 발생하는 모든 이벤트에 대하여 알리는 구독 메커니즘을 정의할 수 있도록 하는 행동 디자인 패턴입니다.
- 상태 (State) — https://refactoring.guru/ko/design-patterns/state
  - source-intent: 상태 패턴은 객체의 내부 상태가 변경될 때 해당 객체가 그의 행동을 변경할 수 있도록 하는 행동 디자인 패턴입니다. 객체가 행동을 변경할 때 객체가 클래스를 변경한 것처럼 보일 수 있습니다.
- 전략 (Strategy) — https://refactoring.guru/ko/design-patterns/strategy
  - source-intent: 전략 패턴은 알고리즘들의 패밀리를 정의하고, 각 패밀리를 별도의 클래스에 넣은 후 그들의 객체들을 상호교환할 수 있도록 하는 행동 디자인 패턴입니다.
- 템플릿 메서드 (Template Method) — https://refactoring.guru/ko/design-patterns/template-method
  - source-intent: 템플릿 메서드 는 부모 클래스에서 알고리즘의 골격을 정의하지만, 해당 알고리즘의 구조를 변경하지 않고 자식 클래스들이 알고리즘의 특정 단계들을 오버라이드​(재정의)​할 수 있도록 하는 행동 디자인 패턴입니다.
- 비지터 (Visitor) — https://refactoring.guru/ko/design-patterns/visitor
  - source-intent: 비지터 (방문자) 패턴은 알고리즘들을 그들이 작동하는 객체들로부터 분리할 수 있도록 하는 행동 디자인 패턴입니다.
