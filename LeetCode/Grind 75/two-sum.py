class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(N) by hash map
        d = {}
        for i, prev in enumerate(nums):
            next = target - prev
            if next in d:
                return [d[next], i] 
            
            d[prev] = i


        # O(N^2) time complexity
        # length = len(nums)
        # for i in range(length):
        #     for j in range(length):
        #         if i == j:
        #             continue

        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # return [0, 1] # impossible, because there is always a answer