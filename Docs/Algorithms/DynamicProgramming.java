package Docs.Algorithms;

import java.util.Arrays;

public class DynamicProgramming {
    static void main() {
        System.out.println("Dynamic Programming");
    }
}

class MaxSubarraySum {
    static void main(String[] args) {
        int[] nums = { -2, 1, -3, 4, -1, 2, -5, 4 };
        System.out.println("최대 연속 합: " + maxSubArray(nums));
    }

    static int maxSubArray(int[] nums) {
        int maxSum = nums[0];
        int currentSum = nums[0];

        for (int i = 1; i < nums.length; i++) {
            currentSum = Math.max(nums[i], currentSum + nums[i]);
            maxSum = Math.max(maxSum, currentSum);
        }

        return maxSum;
    }
}

class MinCoinChange {
    static void main(String[] args) {
        int[] coins = { 1, 2, 5 };
        int amount = 11;
        System.out.println("최소 동전 개수:" + minCoins(coins, amount));
    }

    static int minCoins(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;

        for (int coin : coins) {
            for (int i = coin; i <= amount; i++) {
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }

        return dp[amount] > amount ? -1 : dp[amount];
    }
}
