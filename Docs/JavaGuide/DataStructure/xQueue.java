package Docs.JavaGuide.DataStructure;

import java.util.Queue;

public class xQueue {
    /*
     * queue.add(val)
     * queue.poll()
     */
    static void ArrayDeque() {
        Queue<Integer> queue = new java.util.ArrayDeque<>();

        queue.add(1);
        queue.add(2);

        int v = queue.poll();
        System.out.println(v);

        queue.add(3);
        v = queue.poll();
        System.out.println(v);
    }
}

/*
 * 자바에서 큐를 간단하게 구현하는 방식은 2가지가 있다.
 * 1) Queue 인터페이스 활용
 * 2) 덱(ArrayDeque) 클래스 활용
 * 
 * 일반적인 코딩 테스트에서는 LinkedList 보다 ArrayDeque 를 더 많이 이용한다.
 * 찾아보니 내부적으로 Array 를 사용해서 성능이 더 좋은 편이다.
 * 
 * Queue 인터페이스는 add(), poll() 을 활용하는 편인데,
 * offer() 보다 add() 가 내부 메서드 호출 횟수가 1회 적어서, add() 가 더 선호된다.
 * 찾아보니, 성능 차이는 미미하고 offer 가 false 로 예외 처리하고, add 는 예외 발생시켜서 offer 가 선호되기도 한다더라.
 * 
 * ref:
 * https://goldenrabbit.co.kr/2024/03/06/%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%
 * ED%8A%B8-java-%ED%81%90-%E2%9D%B6/
 */