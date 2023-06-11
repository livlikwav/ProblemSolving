class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Kadane's Algorithm = Dynamic Programming = an optimization of plain recursion (= memoization)
        문제를 부분합의 합으로 보고, 이미 푼 문제를 다시 풀지 않는다.
        """
        # Hot solution #1
        n = len(nums)
        maximumSum, currSumSubarray = float('-inf'), 0
        for i in range(n):
            currSumSubarray += nums[i]
            maximumSum = max(maximumSum, currSumSubarray)
            currSumSubarray = max(currSumSubarray, 0)
        return maximumSum

        # First accepted answer
        length = len(nums)

        left, right = 0, 0
        val = 0
        max_val = nums[0]

        while right < length:
            if left == right:
                val = nums[left]
            else:
                val += nums[right]

            if val > max_val:
                max_val = val

            # print(left, right, val, max_val)
            right += 1
            if val < 0:
                left = right

        if left == right:
            return max_val

        while left < right:
            val -= nums[left]
            left += 1
            if val > max_val:
                max_val = val
            # print(left, right, max_val)

        return max_val
