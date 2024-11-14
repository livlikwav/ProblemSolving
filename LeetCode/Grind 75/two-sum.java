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