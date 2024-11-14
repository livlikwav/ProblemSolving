# Syntax overview

> gpt4o

## Hello World 출력

Java 프로그램의 기본 구조입니다. 모든 Java 코드는 클래스 내부에 작성되어야 하며, 프로그램 시작점은 `main` 메서드입니다.

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

## 변수 선언과 기본 자료형

Java에서 변수는 타입을 명시해야 합니다.

```java
int number = 10;       // 정수형
double decimal = 3.14; // 실수형
boolean isJavaFun = true; // 논리형
char letter = 'A';     // 문자형
String text = "Java";  // 문자열
```

## 조건문 (if-else 문)

Java의 조건문입니다.

```java
int age = 18;
if (age >= 18) {
    System.out.println("성인입니다.");
} else {
    System.out.println("미성년자입니다.");
}
```

## 반복문 (for, while)

Java에서 `for`와 `while` 반복문은 다음과 같습니다.

- **for 문**: 초기값, 조건식, 증감식을 포함하여 반복

```java
for (int i = 0; i < 5; i++) {
    System.out.println("i의 값: " + i);
}
```

- **while 문**: 조건이 참인 동안 반복

```java
int i = 0;
while (i < 5) {
    System.out.println("i의 값: " + i);
    i++;
}
```

- **향상된 for 문**: 배열이나 리스트 요소를 반복할 때 자주 사용됩니다.

```java
int[] numbers = {1, 2, 3, 4, 5};
for (int num : numbers) {
    System.out.println(num);
}
```

## 메서드 (Method) 선언과 호출

Java는 메서드를 사용해 코드를 모듈화합니다.

```java
public class Main {
    public static void main(String[] args) {
        sayHello();
        int result = add(3, 5);
        System.out.println("결과: " + result);
    }

    // 매개변수가 없는 메서드
    public static void sayHello() {
        System.out.println("Hello!");
    }

    // 매개변수가 있는 메서드
    public static int add(int a, int b) {
        return a + b;
    }
}
```

## 배열 (Array)

Java에서는 배열을 `[]`로 선언합니다.

```java
int[] numbers = {1, 2, 3, 4, 5};
System.out.println(numbers[0]); // 1 출력
```

## 클래스와 객체

Java는 객체 지향 언어이므로 클래스를 통해 객체를 생성합니다.

```java
class Car {
    String color;
    int speed;

    // 생성자
    public Car(String color, int speed) {
        this.color = color;
        this.speed = speed;
    }

    public void drive() {
        System.out.println(color + " 색상의 차가 " + speed + "km/h로 달립니다.");
    }
}

public class Main {
    public static void main(String[] args) {
        Car myCar = new Car("빨강", 120);
        myCar.drive();
    }
}
```
