class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        """
        Voted #1 이것도 신기하네. 이건 겹친 부분 값을 저장해서 이걸 마지막에 빼준다
        아이디어 #1: 나처럼 last_right 를 저장하지 않고도, timeSeries[i+1] - timeSeries[i] 로 diff 를 계산해,
        diff < duration 이면 겹쳤다는걸 알아낼 수 있다.
        """
        repeat = 0
        for i in range(len(timeSeries) - 1):
            diff = timeSeries[i + 1] - timeSeries[i]
            if diff < duration:
                repeat += duration - diff
        return len(timeSeries) * duration - repeat
        """
        EDITORIAL TC O(N), SC O(1)
        IDEA #1: min(interval between i and i+1, duration)
        이거는 나와 다른 생각이다. 맨 오른쪽 애는 무조건 duration 만큼 할 수 있는거고,
        그 전 애들은 겹치면 겹치는 부분만 더해나간다.

        내 아이디어는, 마지막 right 값을 저장해서, 겹치지 않은 left 를 찾아 겹치지 않은 부분만 계속 더해나간다.
        editorial 아이디어를 차용해서, 내 해결책도 min 으로 수정해나갈 수 있어 보인다.
        """
        n = len(timeSeries)
        if n == 0:
            return 0
        total = 0
        for i in range(n - 1):
            total += min(timeSeries[i + 1] - timeSeries[i], duration)
        return total + duration
        """
        MY SOLUTION, keep last right pointer and sum not merged partition
        TC O(N) SC O(1)
        """
        result = 0
        last_right = -1

        for x in timeSeries:
            left = x
            right = left + duration - 1

            if last_right >= left:
                left = last_right + 1

            result += right - left + 1
            last_right = right
            # print(left, right, result, last_right)

        return result
