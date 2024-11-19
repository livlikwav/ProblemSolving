# Java

## Lesson learned

- Java 는 매 statement 마다 ;(semicolon) 을 붙여야 함.
- Java 는 Go `:=` 처럼 암묵적 변수 타입 선언 불가능함. 변수 초기화 시에도 변수 타입 명시해야함.

## Overview

> gpt4o

### 1. 기본 자료형

- Java는 기본형 데이터 타입이 있고, 모두 소문자로 시작합니다.
  - `int`, `double`, `float`, `boolean`, `char`, `byte`, `short`, `long`
- 객체 타입과 다르게 기본형은 메모리 효율이 좋습니다.

### 2. 클래스와 객체

- Java는 객체 지향 프로그래밍 언어로, 모든 코드가 클래스 안에 있어야 합니다.
- 객체 생성은 `ClassName obj = new ClassName();` 형태로 하며, 생성자를 사용해 초기화합니다.

### 3. 조건문과 반복문

- 조건문: `if`, `else if`, `else`
- 반복문: `for`, `while`, `do-while`
- 향상된 for문: `for (Type item : collection) { ... }`

### 4. 컬렉션 프레임워크

- List, Set, Map 등의 인터페이스와 이를 구현하는 클래스들 (`ArrayList`, `HashSet`, `HashMap` 등)은 자주 사용됩니다.
- List는 순서가 있는 데이터, Set은 중복되지 않는 데이터, Map은 키-값 쌍의 데이터 관리에 사용됩니다.

### 5. 예외 처리

- Java는 `try-catch-finally`를 사용하여 예외를 처리하며, `throws`를 통해 예외를 호출자에게 전달할 수 있습니다.
- 자주 쓰이는 예외: `NullPointerException`, `ArrayIndexOutOfBoundsException`, `ClassCastException` 등

### 6. 입출력

- 코딩 테스트에서는 주로 `Scanner`나 `BufferedReader`를 사용해 입력을 받고, `System.out.println`으로 출력합니다.

     ```java
     Scanner sc = new Scanner(System.in);
     int x = sc.nextInt();
     ```

### 7. Java 특유의 문법과 주요 차이점

- String 불변성: `String` 객체는 불변(immutable)이며, 조작하려면 `StringBuilder`를 사용하는 것이 좋습니다.
- 메모리 관리: Java는 가비지 컬렉션을 자동으로 수행하며, `System.gc()`로 요청할 수 있지만, 수동으로는 할 수 없습니다.
- static 키워드: 클래스 변수와 클래스 메서드를 정의할 때 사용되며, 인스턴스화 없이도 접근할 수 있습니다.

### 8. Lambda 표현식 (Java 8 이상)

- 익명 함수 표현식으로, 주로 간결한 코드를 위해 사용합니다.

     ```java
     List<Integer> numbers = Arrays.asList(1, 2, 3, 4);
     numbers.forEach(n -> System.out.println(n));
     ```
