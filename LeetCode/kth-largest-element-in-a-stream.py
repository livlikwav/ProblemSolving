import heapq

"""
MY SOLUTION
TC O(logN) = O(#add * logN)
SC O(K)
python 의 min heap 은 push, pop 둘 다 logN TC 를 보장한다.
"""


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)

        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]  # python min heap idx 0 이 최소 힙의 루트 노드이다.


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
