import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        // O(n^2), backtracking
        /*
         * for i in range (0, len(n))
         * for j in range(i, len(n))
         * res := nums[i] + num[j]
         * if res == target
         * return i, j
         */
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                int sum = nums[i] + nums[j];
                if (sum == target) {
                    int[] result = new int[] { i, j };
                    return result;
                }
            }
        }

        return null;
    }
}

class Solution2 {
    public int[] twoSum(int[] nums, int target) {
        // O(n) solution
        // 시간 복잡도를 줄이려면 탐색을 줄여야 하고, 그러려면 이진 탐색 같은 log N 이나 Hash 같은 1 짜리가 필요함을 기억하자.
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];

            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i };
            }

            map.put(nums[i], i);
        }

        throw new IllegalArgumentException("No two sum solution found");
    }
}