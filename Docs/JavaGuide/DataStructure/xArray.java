package Docs.JavaGuide.DataStructure;

import java.util.Arrays;
import java.util.Collections;

public class xArray {
    /*
     * https://wikidocs.net/120876
     * arr.length;
     * Arrays.sort(arr);
     * Arrays.sort(arr, comparator);
     */
    static void Array() {
        // 선언과 대입을 같이 하는 경우 new 생략 가능
        int[] numbers = { 1, 2, 3, 4, 5 };
        int[] numbers2 = new int[] { 5, 4, 3, 2, 1 };
        System.out.println(numbers[0]);

        System.out.println(Arrays.toString(numbers));

        // 정렬 (오름차순)
        Arrays.sort(numbers2);

        String[] strings = { "a", "b", "c" };

        // 내림차순 정렬 (Reference)
        Arrays.sort(strings, Collections.reverseOrder());

        // 내림차순 정렬 (Primitive)
        // 내림차순 정렬 (Primitive - tip)
        // 그냥 for loop 에서 반대로 step 하면 됨

        // 내림차순 정렬 (Primitive - boxing)
        // https://changheesjunk.tistory.com/15#%C-%A-
        // 1) new Integer array
        Integer[] numbers3 = Arrays.stream(numbers).boxed().toArray(Integer[]::new);
        Arrays.sort(numbers3, Collections.reverseOrder());
        // 2) boxing from int to Integer -> Integer to int
        numbers = Arrays.stream(numbers).boxed().sorted(Collections.reverseOrder()).mapToInt(Integer::intValue)
                .toArray();

        // Arrays.fill
        boolean[] visited = new boolean[5];
        Arrays.fill(visited, false);
    }
}

/*
 * https://www.w3schools.com/java/ref_arrays_fill.asp
 * Arrays.fill(array, value)
 * 배열 일괄 초기화
 * 해당 배열의 모든 값을 지정한 값으로 초기화 한다. for 문의 syntax sugar 함수
 */

/*
 * https://80000coding.oopy.io/21cb57a3-681b-404d-a4ac-8ab0e7289bc0
 * 보통 2가지 메소드 사용해서 정렬한다
 * Arrays.sort();
 * Collections.sort();
 * 
 * Comparator 는 인터페이스이다.
 * Collections 에 이미 구현된 구현체 사용할 수 있다.
 */