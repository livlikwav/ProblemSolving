class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Proof of greedy method
        when ai < aj, if we move j to the left:
        1. the length on x-axis will definitly decrease
        2. if a(j-1) > ai, the area will be ai * length on x-axis which is smaller than original area
        3. if a(j-1) < ai, the area will be a(j-1) * length on x-axis which is also smaller than original area
        so moving j to the left won't give us a larger area, we can only move i to the right to get a possible larger area.

        어짜피 h[j] > h[i] > h[j-1] 이 되므로, 무조건 넓이가 더 작아지므로 저쪽 방향으로 찾을 필요가 없다.
        """
        """
        Voted #1, greedy two pointers
        이렇게 한번 해볼까? 해서 그리디하게 푸는건 이해했다. 하지만 그리디하게 풀어서 답이 되는 과정 증명하는건 역시 아직 감이 잘 안온다.
        TC O(N) SC O(1)
        """
        l, r, area = 0, len(height) - 1, 0
        while l < r:
            area = max(area, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area
        """
        After giving up, check only summary of solutions and try again.
        IDEA #1: greedy + 2 pointer (do not need even 1 sorting)
        """
        i, j = 0, len(height) - 1
        result = -1

        while i < j:
            area = (j - i) * min(height[i], height[j])
            result = max(result, area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return result
