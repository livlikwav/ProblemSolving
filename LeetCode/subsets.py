class Solution:
    """
    FAIL-23-06-12
    Backtracking - dfs/bfs
    Solution: https://youtu.be/REOH22Xwdkk (in NeetCode Roadmap)
    핵심 아이디어는 각 item 을 포함/미포함으로 생각하고, decision tree 를 그려 이 트리를 탐색하는데에 dfs 를 사용하는 것이다.
    TC: O(2^n), SC: O(N)
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # include i-th item
            subset.append(nums[i])
            dfs(i+1)

            # exclude i-th item
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res
