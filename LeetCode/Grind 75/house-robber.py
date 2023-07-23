class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Voted #1 by all
        step 5 해결책인 iterative + 2 variables 가 좋아보인다. 점화식에서 i-1, i-2 까지만 저장이 필요한걸로 최적화
        bottom up 방식이므로 i-3 이하는 저장하지 않아도 되는것이다. 내 방식보다 SC 면에서 유리하다. O(1)
        아래 코드는 자바 코드를 파이썬으로 다시 짰다.
        """
        prev1, prev2 = 0, 0
        if len(nums) == 1:
            return nums[0]

        prev1 = nums[0]
        prev2 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            val = max(prev1 + nums[i], prev2)
            prev1 = prev2
            prev2 = val

        return prev2

        """
        MY SOLUTION about 10min elapsed
        botton up solution. guarantee that dp table item is optimal value

        파이썬에서 list indexing 에서 -1 쓰면 편하단거 기억하자!
        """
        d = [0] * len(nums)
        if len(nums) == 1:
            return nums[0]

        d[0] = nums[0]
        d[1] = max(d[0], nums[1])

        for i in range(2, len(nums)):
            d[i] = max(d[i - 1], d[i - 2] + nums[i])

        return d[len(nums) - 1]
