// HASH
package Programmers;

import java.util.HashMap;

class Solution {
    public int solution(int[] nums) {
        HashMap<Integer, Integer> uniques = new HashMap<>();
        int cnt = nums.length / 2;

        for (int num : nums) {
            uniques.put(num, uniques.getOrDefault(num, 0) + 1);
        }

        return Math.min(cnt, uniques.size());
    }
}

/*
 * nums = N
 * count = N / 2
 * hash? set, dictionary like DS needed
 * result = max unique value
 * nums 는 항상 짝수 (even)
 * 종류 번호 몹시 다양 2*10^5 개
 * 
 * nums 는 곧 len(array)
 * 모든 경우의 수를 하려면 for loop 가 c 만큼 있어야 함.
 * 그러면 10만개라고 하면 10만 * 10만-1 * 10만-2.... 10만은 10^5
 * Operation num = N P C(N/2)
 * 2*10^7 이 제한이잖어
 * 그럼 for 는 안된다는 소리임
 * HASH 는 O(1) 이다.
 * 근데 우리가 찾는건 array idx 마다 검사해서
 * unique val 최대값을 찾는거다.
 * 012 013 014 015 016
 * 123 124 125 이렇게 하나하나 하는게 아니라
 * 처음부터 arr 를 쭉 한번 읽어서 uniq 한 애들을 골라
 * 333333 3 한개야
 * 그럼 1개고
 * 123456789
 * C 가 9 야
 * uniq len 이 C 보다 작으면 그냥 그거 답으로 하고
 * 음 근데 커도 C 만큼이 답이겠네!
 * 123456 이면 C 가 3 이니까
 * max (C, len(uniqArr)) 이게 답이네
 */
