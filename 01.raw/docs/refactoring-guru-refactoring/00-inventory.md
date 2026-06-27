---
source_url: https://refactoring.guru/refactoring
ingested: 2026-06-27
sha256: 33dc61bc25206096e0b893fd6bb7ad65c099ccdb845b3b88b3de965c4bbc326f
---

# Refactoring.Guru Refactoring Inventory

저작권 보호 본문 전문을 복제하지 않고, 공개 URL inventory와 짧은 의도 요약만 보존한다.

## Source scope
- Root: https://refactoring.guru/refactoring
- Main sections: what/technical debt/when/how/catalog/code smells/refactorings
- Code smells: 23 items
- Refactoring technique groups: 6 groups, 66 techniques

## Code smells
### Bloaters
- Category URL: https://refactoring.guru/refactoring/smells/bloaters
- Summary: 코드 단위가 과도하게 커져 이해·변경 비용을 키우는 냄새
  - Long Method — https://refactoring.guru/smells/long-method — 한 메서드가 너무 길어 이름 붙일 수 있는 단계들이 한 몸에 섞인 상태.
  - Large Class — https://refactoring.guru/smells/large-class — 한 클래스가 필드·메서드·책임을 과도하게 많이 떠안은 상태.
  - Primitive Obsession — https://refactoring.guru/smells/primitive-obsession — 도메인 의미가 있는 값·범위·분류를 작은 객체 대신 primitive·상수로 표현하는 상태.
  - Long Parameter List — https://refactoring.guru/smells/long-parameter-list — 메서드 호출에 필요한 파라미터가 지나치게 많아 호출자와 구현이 강하게 결합된 상태.
  - Data Clumps — https://refactoring.guru/smells/data-clumps — 여러 위치에서 항상 함께 움직이는 변수 묶음이 반복되는 상태.

### Object-Orientation Abusers
- Category URL: https://refactoring.guru/refactoring/smells/oo-abusers
- Summary: 상속·조건분기·임시 상태 등 객체지향 구조를 어색하게 쓰는 냄새
  - Alternative Classes With Different Interfaces — https://refactoring.guru/smells/alternative-classes-with-different-interfaces — 같은 역할의 클래스들이 서로 다른 메서드 이름·인터페이스를 노출하는 상태.
  - Refused Bequest — https://refactoring.guru/smells/refused-bequest — 하위 클래스가 상위 클래스의 일부 상속만 실제로 필요로 하는 어긋난 상속 구조.
  - Switch Statements — https://refactoring.guru/smells/switch-statements — 타입·상태별 분기가 여러 곳에 반복되어 새 변형 추가가 여러 수정으로 번지는 상태.
  - Temporary Field — https://refactoring.guru/smells/temporary-field — 특정 상황에서만 값이 채워지는 필드가 객체의 정상 상태를 흐리는 상태.

### Change Preventers
- Category URL: https://refactoring.guru/refactoring/smells/change-preventers
- Summary: 하나의 변경이 여러 위치 수정으로 번지는 변경 저항 냄새
  - Divergent Change — https://refactoring.guru/smells/divergent-change — 한 클래스가 서로 다른 변경 이유들 때문에 계속 수정되는 상태.
  - Parallel Inheritance Hierarchies — https://refactoring.guru/smells/parallel-inheritance-hierarchies — 한 계층에 subclass를 추가할 때 다른 계층에도 대응 subclass를 추가해야 하는 상태.
  - Shotgun Surgery — https://refactoring.guru/smells/shotgun-surgery — 작은 기능 변경 하나가 여러 클래스의 작은 수정으로 흩어지는 상태.

### Dispensables
- Category URL: https://refactoring.guru/refactoring/smells/dispensables
- Summary: 없어도 되는 코드·주석·클래스가 유지보수 비용을 만드는 냄새
  - Comments — https://refactoring.guru/smells/comments — 코드 자체가 설명하지 못하는 의도·절차를 주석이 대신 떠받치는 상태.
  - Duplicate Code — https://refactoring.guru/smells/duplicate-code — 동일하거나 거의 동일한 코드 조각이 여러 위치에 존재하는 상태.
  - Data Class — https://refactoring.guru/smells/data-class — 데이터 필드와 단순 getter/setter만 있고 의미 있는 행동이 없는 클래스.
  - Dead Code — https://refactoring.guru/smells/dead-code — 더 이상 사용되지 않는 변수·필드·메서드·클래스가 남아 있는 상태.
  - Lazy Class — https://refactoring.guru/smells/lazy-class — 존재 비용에 비해 책임이 너무 적어 독립 클래스로 둘 이유가 약한 상태.
  - Speculative Generality — https://refactoring.guru/smells/speculative-generality — 미래에 필요할 것이라는 추측만으로 만들어진 추상화·파라미터·클래스.

### Couplers
- Category URL: https://refactoring.guru/refactoring/smells/couplers
- Summary: 객체·모듈이 서로 과도하게 의존해 독립 변경을 어렵게 하는 냄새
  - Feature Envy — https://refactoring.guru/smells/feature-envy — 메서드가 자기 객체보다 다른 객체의 데이터에 더 관심을 보이는 상태.
  - Inappropriate Intimacy — https://refactoring.guru/smells/inappropriate-intimacy — 한 클래스가 다른 클래스의 내부 세부사항에 과하게 접근·의존하는 상태.
  - Message Chains — https://refactoring.guru/smells/message-chains — 클라이언트가 객체 그래프를 따라 연쇄 호출하며 내부 구조를 알아야 하는 상태.
  - Middle Man — https://refactoring.guru/smells/middle-man — 클래스가 의미 있는 책임 없이 대부분의 호출을 다른 객체에 위임만 하는 상태.

### Other Smells
- Category URL: https://refactoring.guru/refactoring/smells/other
- Summary: 라이브러리 제약 등 위 범주에 깔끔히 들어가지 않는 냄새
  - Incomplete Library Class — https://refactoring.guru/smells/incomplete-library-class — 사용 중인 라이브러리가 필요한 기능을 제공하지 않지만 직접 수정하기 어려운 상태.

## Refactoring technique groups
### Composing Methods
- Category URL: https://refactoring.guru/refactoring/techniques/composing-methods
- Summary: 긴 메서드를 작은 의도 단위로 쪼개거나, 반대로 불필요한 간접층을 인라인해 메서드 내부 구성을 다듬는다.
  - Extract Method — https://refactoring.guru/extract-method — Problem: You have a code fragment that can be grouped together. Solution: Move this code to a separate new method (or function) and replace the old code with a call to the method.
  - Inline Method — https://refactoring.guru/inline-method — Problem: When a method body is more obvious than the method itself, use this technique. Solution: Replace calls to the method with the method’s content and delete the method itself.
  - Extract Variable — https://refactoring.guru/extract-variable — Problem: You have an expression that’s hard to understand. Solution: Place the result of the expression or its parts in separate variables that are self-explanatory.
  - Inline Temp — https://refactoring.guru/inline-temp — Problem: You have a temporary variable that’s assigned the result of a simple expression and nothing more. Solution: Replace the references to the variable with the expression itself.
  - Replace Temp with Query — https://refactoring.guru/replace-temp-with-query — Problem: You place the result of an expression in a local variable for later use in your code. Solution: Move the entire expression to a separate method and return the result from it. Query the method instead of using a 
  - Split Temporary Variable — https://refactoring.guru/split-temporary-variable — Problem: You have a local variable that’s used to store various intermediate values inside a method (except for cycle variables). Solution: Use different variables for different values. Each variable should be responsibl
  - Remove Assignments to Parameters — https://refactoring.guru/remove-assignments-to-parameters — Problem: Some value is assigned to a parameter inside method’s body. Solution: Use a local variable instead of a parameter.
  - Replace Method with Method Object — https://refactoring.guru/replace-method-with-method-object — Problem: You have a long method in which the local variables are so intertwined that you can’t apply Extract Method. Solution: Transform the method into a separate class so that the local variables become fields of the c
  - Substitute Algorithm — https://refactoring.guru/substitute-algorithm — Problem: So you want to replace an existing algorithm with a new one? Solution: Replace the body of the method that implements the algorithm with a new algorithm.

### Moving Features between Objects
- Category URL: https://refactoring.guru/refactoring/techniques/moving-features-between-objects
- Summary: 메서드·필드·책임이 더 자연스럽게 속해야 할 객체로 이동시켜 응집도를 높이고 결합도를 낮춘다.
  - Move Method — https://refactoring.guru/move-method — Problem: A method is used more in another class than in its own class. Solution: Create a new method in the class that uses the method the most, then move code from the old method to there. Turn the code of the original 
  - Move Field — https://refactoring.guru/move-field — Problem: A field is used more in another class than in its own class. Solution: Create a field in a new class and redirect all users of the old field to it.
  - Extract Class — https://refactoring.guru/extract-class — Problem: When one class does the work of two, awkwardness results. Solution: Instead, create a new class and place the fields and methods responsible for the relevant functionality in it.
  - Inline Class — https://refactoring.guru/inline-class — Problem: A class does almost nothing and isn’t responsible for anything, and no additional responsibilities are planned for it. Solution: Move all features from the class to another one.
  - Hide Delegate — https://refactoring.guru/hide-delegate — Problem: The client gets object B from a field or method of object А. Then the client calls a method of object B. Solution: Create a new method in class A that delegates the call to object B. Now the client doesn’t know 
  - Remove Middle Man — https://refactoring.guru/remove-middle-man — Problem: A class has too many methods that simply delegate to other objects. Solution: Delete these methods and force the client to call the end methods directly.
  - Introduce Foreign Method — https://refactoring.guru/introduce-foreign-method — Problem: A utility class doesn’t contain the method that you need and you can’t add the method to the class. Solution: Add the method to a client class and pass an object of the utility class to it as an argument.
  - Introduce Local Extension — https://refactoring.guru/introduce-local-extension — Problem: A utility class doesn’t contain some methods that you need. But you can’t add these methods to the class. Solution: Create a new class containing the methods and make it either the child or wrapper of the utilit

### Organizing Data
- Category URL: https://refactoring.guru/refactoring/techniques/organizing-data
- Summary: primitive, 배열, type code, association 등 데이터 표현을 도메인 의미와 변경 축에 맞게 재구성한다.
  - Self Encapsulate Field — https://refactoring.guru/self-encapsulate-field — Problem: You use direct access to private fields inside a class. Solution: Create a getter and setter for the field, and use only them for accessing the field.
  - Replace Data Value with Object — https://refactoring.guru/replace-data-value-with-object — Problem: A class (or group of classes) contains a data field. The field has its own behavior and associated data. Solution: Create a new class, place the old field and its behavior in the class, and store the object of t
  - Change Value to Reference — https://refactoring.guru/change-value-to-reference — Problem: So you have many identical instances of a single class that you need to replace with a single object. Solution: Convert the identical objects to a single reference object.
  - Change Reference to Value — https://refactoring.guru/change-reference-to-value — Problem: You have a reference object that’s too small and infrequently changed to justify managing its life cycle. Solution: Turn it into a value object.
  - Replace Array with Object — https://refactoring.guru/replace-array-with-object — Problem: You have an array that contains various types of data. Solution: Replace the array with an object that will have separate fields for each element.
  - Duplicate Observed Data — https://refactoring.guru/duplicate-observed-data — Problem: Is domain data stored in classes responsible for the GUI? Solution: Then it’s a good idea to separate the data into separate classes, ensuring connection and synchronization between the domain class and the GUI.
  - Change Unidirectional Association to Bidirectional — https://refactoring.guru/change-unidirectional-association-to-bidirectional — Problem: You have two classes that each need to use the features of the other, but the association between them is only unidirectional. Solution: Add the missing association to the class that needs it.
  - Change Bidirectional Association to Unidirectional — https://refactoring.guru/change-bidirectional-association-to-unidirectional — Problem: You have a bidirectional association between classes, but one of the classes doesn’t use the other’s features. Solution: Remove the unused association.
  - Replace Magic Number with Symbolic Constant — https://refactoring.guru/replace-magic-number-with-symbolic-constant — Problem: Your code uses a number that has a certain meaning to it. Solution: Replace this number with a constant that has a human-readable name explaining the meaning of the number.
  - Encapsulate Field — https://refactoring.guru/encapsulate-field — Problem: You have a public field. Solution: Make the field private and create access methods for it.
  - Encapsulate Collection — https://refactoring.guru/encapsulate-collection — Problem: A class contains a collection field and a simple getter and setter for working with the collection. Solution: Make the getter-returned value read-only and create methods for adding/deleting elements of the colle
  - Replace Type Code with Class — https://refactoring.guru/replace-type-code-with-class — Problem: A class has a field that contains type code. The values of this type aren’t used in operator conditions and don’t affect the behavior of the program. Solution: Create a new class and use its objects instead of t
  - Replace Type Code with Subclasses — https://refactoring.guru/replace-type-code-with-subclasses — Problem: You have a coded type that directly affects program behavior (values of this field trigger various code in conditionals). Solution: Create subclasses for each value of the coded type. Then extract the relevant b
  - Replace Type Code with State/Strategy — https://refactoring.guru/replace-type-code-with-state-strategy — Problem: You have a coded type that affects behavior but you can’t use subclasses to get rid of it. Solution: Replace type code with a state object. If it’s necessary to replace a field value with type code, another stat
  - Replace Subclass with Fields — https://refactoring.guru/replace-subclass-with-fields — Problem: You have subclasses differing only in their (constant-returning) methods. Solution: Replace the methods with fields in the parent class and delete the subclasses.

### Simplifying Conditional Expressions
- Category URL: https://refactoring.guru/refactoring/techniques/simplifying-conditional-expressions
- Summary: 복잡한 조건식을 명명·분해·다형성·guard clause 등으로 단순화한다.
  - Decompose Conditional — https://refactoring.guru/decompose-conditional — Problem: You have a complex conditional (if-then/else or switch). Solution: Decompose the complicated parts of the conditional into separate methods: the condition, then and else.
  - Consolidate Conditional Expression — https://refactoring.guru/consolidate-conditional-expression — Problem: You have multiple conditionals that lead to the same result or action. Solution: Consolidate all these conditionals in a single expression.
  - Consolidate Duplicate Conditional Fragments — https://refactoring.guru/consolidate-duplicate-conditional-fragments — Problem: Identical code can be found in all branches of a conditional. Solution: Move the code outside of the conditional.
  - Remove Control Flag — https://refactoring.guru/remove-control-flag — Problem: You have a boolean variable that acts as a control flag for multiple boolean expressions. Solution: Instead of the variable, use break, continue and return.
  - Replace Nested Conditional with Guard Clauses — https://refactoring.guru/replace-nested-conditional-with-guard-clauses — Problem: You have a group of nested conditionals and it’s hard to determine the normal flow of code execution. Solution: Isolate all special checks and edge cases into separate clauses and place them before the main chec
  - Replace Conditional with Polymorphism — https://refactoring.guru/replace-conditional-with-polymorphism — Problem: You have a conditional that performs various actions depending on object type or properties. Solution: Create subclasses matching the branches of the conditional. In them, create a shared method and move code fr
  - Introduce Null Object — https://refactoring.guru/introduce-null-object — Problem: Since some methods return null instead of real objects, you have many checks for null in your code. Solution: Instead of null, return a null object that exhibits the default behavior.
  - Introduce Assertion — https://refactoring.guru/introduce-assertion — Problem: For a portion of code to work correctly, certain conditions or values must be true. Solution: Replace these assumptions with specific assertion checks.

### Simplifying Method Calls
- Category URL: https://refactoring.guru/refactoring/techniques/simplifying-method-calls
- Summary: 메서드 이름·파라미터·예외·가시성을 다듬어 API 호출면을 명확하게 만든다.
  - Rename Method — https://refactoring.guru/rename-method — Problem: The name of a method doesn’t explain what the method does. Solution: Rename the method.
  - Add Parameter — https://refactoring.guru/add-parameter — Problem: A method doesn’t have enough data to perform certain actions. Solution: Create a new parameter to pass the necessary data.
  - Remove Parameter — https://refactoring.guru/remove-parameter — Problem: A parameter isn’t used in the body of a method. Solution: Remove the unused parameter.
  - Separate Query from Modifier — https://refactoring.guru/separate-query-from-modifier — Problem: Do you have a method that returns a value but also changes something inside an object? Solution: Split the method into two separate methods. As you would expect, one of them should return the value and the other
  - Parameterize Method — https://refactoring.guru/parameterize-method — Problem: Multiple methods perform similar actions that are different only in their internal values, numbers or operations. Solution: Combine these methods by using a parameter that will pass the necessary special value.
  - Replace Parameter with Explicit Methods — https://refactoring.guru/replace-parameter-with-explicit-methods — Problem: A method is split into parts, each of which is run depending on the value of a parameter. Solution: Extract the individual parts of the method into their own methods and call them instead of the original method.
  - Preserve Whole Object — https://refactoring.guru/preserve-whole-object — Problem: You get several values from an object and then pass them as parameters to a method. Solution: Instead, try passing the whole object.
  - Replace Parameter with Method Call — https://refactoring.guru/replace-parameter-with-method-call — Problem: Calling a query method and passing its results as the parameters of another method, while that method could call the query directly. Solution: Instead of passing the value through a parameter, try placing a quer
  - Introduce Parameter Object — https://refactoring.guru/introduce-parameter-object — Problem: Your methods contain a repeating group of parameters. Solution: Replace these parameters with an object.
  - Remove Setting Method — https://refactoring.guru/remove-setting-method — Problem: The value of a field should be set only when it’s created, and not change at any time after that. Solution: So remove methods that set the field’s value.
  - Hide Method — https://refactoring.guru/hide-method — Problem: A method isn’t used by other classes or is used only inside its own class hierarchy. Solution: Make the method private or protected.
  - Replace Constructor with Factory Method — https://refactoring.guru/replace-constructor-with-factory-method — Problem: You have a complex constructor that does something more than just setting parameter values in object fields. Solution: Create a factory method and use it to replace constructor calls.
  - Replace Error Code with Exception — https://refactoring.guru/replace-error-code-with-exception — Problem: A method returns a special value that indicates an error? Solution: Throw an exception instead.
  - Replace Exception with Test — https://refactoring.guru/replace-exception-with-test — Problem: You throw an exception in a place where a simple test would do the job? Solution: Replace the exception with a condition test.

### Dealing with Generalization
- Category URL: https://refactoring.guru/refactoring/techniques/dealing-with-generalization
- Summary: 상속·위임·공통화·계층 병합을 조정해 일반화 구조를 실제 변경 요구에 맞춘다.
  - Pull Up Field — https://refactoring.guru/pull-up-field — Problem: Two classes have the same field. Solution: Remove the field from subclasses and move it to the superclass.
  - Pull Up Method — https://refactoring.guru/pull-up-method — Problem: Your subclasses have methods that perform similar work. Solution: Make the methods identical and then move them to the relevant superclass.
  - Pull Up Constructor Body — https://refactoring.guru/pull-up-constructor-body — Problem: Your subclasses have constructors with code that’s mostly identical. Solution: Create a superclass constructor and move the code that’s the same in the subclasses to it. Call the superclass constructor in the su
  - Push Down Method — https://refactoring.guru/push-down-method — Problem: Is behavior implemented in a superclass used by only one (or a few) subclasses? Solution: Move this behavior to the subclasses.
  - Push Down Field — https://refactoring.guru/push-down-field — Problem: Is a field used only in a few subclasses? Solution: Move the field to these subclasses.
  - Extract Subclass — https://refactoring.guru/extract-subclass — Problem: A class has features that are used only in certain cases. Solution: Create a subclass and use it in these cases.
  - Extract Superclass — https://refactoring.guru/extract-superclass — Problem: You have two classes with common fields and methods. Solution: Create a shared superclass for them and move all the identical fields and methods to it.
  - Extract Interface — https://refactoring.guru/extract-interface — Problem: Multiple clients are using the same part of a class interface. Another case: part of the interface in two classes is the same. Solution: Move this identical portion to its own interface.
  - Collapse Hierarchy — https://refactoring.guru/collapse-hierarchy — Problem: You have a class hierarchy in which a subclass is practically the same as its superclass. Solution: Merge the subclass and superclass.
  - Form Template Method — https://refactoring.guru/form-template-method — Problem: Your subclasses implement algorithms that contain similar steps in the same order. Solution: Move the algorithm structure and identical steps to a superclass, and leave implementation of the different steps in t
  - Replace Inheritance with Delegation — https://refactoring.guru/replace-inheritance-with-delegation — Problem: You have a subclass that uses only a portion of the methods of its superclass (or it’s not possible to inherit superclass data). Solution: Create a field and put a superclass object in it, delegate methods to th
  - Replace Delegation with Inheritance — https://refactoring.guru/replace-delegation-with-inheritance — Problem: A class contains many simple methods that delegate to all methods of another class. Solution: Make the class a delegate inheritor, which makes the delegating methods unnecessary.
