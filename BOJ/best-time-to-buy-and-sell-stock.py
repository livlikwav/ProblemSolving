class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 3, success, greedy, elapsed 01:09:16, TC O(N), SC O(1)
        max_val = 0
        i, j = 0, 1
        while j < len(prices):
            if prices[i] >= prices[j]:
                i = j
                j = i+1
                continue

            max_val = max(max_val, prices[j]-prices[i])
            j += 1

        return max_val

        # 2, invalid, binary search
        length = len(prices)
        if length == 1:
            return 0
        if length == 2:
            return prices[1]-prices[0] if prices[1] > prices[0] else 0

        pivot = length // 2
        left = prices[:pivot]
        right = prices[pivot:]

        left_min = min(left)
        right_max = max(right)
        if left_min < right_max:
            if left_min <= min(right):
                return right_max - left_min
            else:
                return self.maxProfit(right)
        else:
            return self.maxProfit(left)

        # 1, time exceeded, brute forcing, O(N^2)
        length = len(prices)
        max_val = 0

        for right in range(1, length):
            for left in range(0, right):
                max_val = max(max_val, prices[right] - prices[left])

        return max_val
