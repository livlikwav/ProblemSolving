class Solution:
    # TODO 이 또한 답이긴 하지만, Discussion 에 이진 탐색을 활용하는 방법이 있었다... 이것도 공부해서 이해하자
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        SUCCESS SOLUTION, but no good at performance
        TC O(NlogN), heap sort 할 때 시간 복잡도를 가장 많이 필요로 한다.
        SC O(N) = O(N + k)
        """
        # arr is ordered in ascending order

        dis_arr = []
        for i in range(len(arr)):
            node = (abs(arr[i] - x), i)
            heapq.heappush(dis_arr, node)

        result = []
        for _ in range(k):
            val, idx = heapq.heappop(dis_arr)
            result.append(arr[idx])

        result.sort()
        return result

    def findClosestElements1(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        MY #1 FAILED SOLUTION
        """
        abs_arr = []
        min_val = int(1e9)
        min_idx = -1
        for i in range(len(arr)):
            val = abs(arr[i] - x)
            abs_arr.append(val)

            if val < min_val:
                min_val = val
                min_idx = i

        print(arr, abs_arr)

        left, right = min_idx, min_idx
        cnt = 0

        while cnt < k and left - 1 >= 0 and right + 1 < len(abs_arr):
            if abs_arr[left - 1] > abs_arr[right + 1]:
                cnt += 1
                right += 1
            else:
                cnt += 1
                left -= 1
        print(left, right, cnt)

        if cnt != k:
            if left == 0:
                right = right + k - cnt - 1
            elif right == 0:
                left = left - (k - cnt - 1)
        print(left, right)

        return arr[left : right + 1]
