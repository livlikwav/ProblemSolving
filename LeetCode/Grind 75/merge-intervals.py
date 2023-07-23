class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Voted #1
        """
        intervals = sorted(intervals, key=lambda x: x[0])
        ans = []

        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans
        """
        MY SOLUTION elapsed about 40min
        2 interval 사이에 정확히 6가지의 경우의 수만 있는걸 파악하는것이 첫번째이다.
        그리고 min, max 를 사용하여 if-else hell 이 아니라 간단히 구현하는 것이 중요하다.
        또한 sorting 을 해야하는 이유는, 왼쪽부터 차례로 해나가면, 딱 왼쪽 한개랑만 합치거나 안합치거나 하면 된다.
        증명은 i-2 랑도 합쳐야 하는 경우라면, 이미 i-1 가 합쳐진 애여야 하기 때문이다.

        하지만 답안을 보다보니, sorting 해서 체크하지 않아도 되는 경우가 있었다. d < a 한 경우는 없다. a < c < d 이므로.
        그리고 min(a,c) 도 체크하지 않아도 된다. 어짜피 sorted 이니까 무조건 a < c 이다.

        TC O(NlogN + N) = O(NlogN), SC O(N)
        """
        intervals.sort()  # sorted by first key
        result = []
        result.append(intervals[0])

        for i in range(1, len(intervals)):
            a, b = result.pop()
            c, d = intervals[i]

            if b < c:
                result.append([a, b])
                result.append([c, d])
            elif d < a:
                result.append([c, d])
                result.append([a, b])
            else:
                next = [min(a, c), max(b, d)]
                result.append(next)

        return result
