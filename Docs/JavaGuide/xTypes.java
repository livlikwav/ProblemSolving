package Docs.JavaGuide;

public class xTypes {
    /*
     * Java는 기본형 데이터 타입이 있고, 모두 소문자로 시작
     * char 는 '', 2byte, uint
     * String 은 ""
     */
    static void Primitive() {
        int number = 10; // 정수형
        double decimal = 3.14; // 실수형
        boolean isJavaFun = true; // 논리형
        char letter = 'A'; // 문자형
        String text = "Java"; // 문자열
        // float
        // byte
        // short
        // long
    }
}

/*
 * https://inpa.tistory.com/entry/JAVA-%E2%98%95-wrapper-class-Boxing-UnBoxing
 * Boxing: Primitive -> Wrapper
 * Unboxing: Wrapper -> Primitive
 * 
 * Wrapper Class 는 산술 연산 불가
 * 모두 java.lang 에 포함되어 제공된다.
 * 
 * AutoBoxing, AutoUnBoxing = JDK 1.5 부터 지원
 * 불필요한 auto casting 은 성능 저하의 원인
 */