class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Top rated #1: Greedy(maybe)
        TC O(N), SC O(N)
        개선점: 보통 절대 if statement hell 은 요구하지 않음을 기억하자.
        이렇게 수수께기 같이 조건이 복잡한 문제는 Greedy 를 떠올리자.
        그리고 Greedy 가 정말 알고리즘의 정수같은 것이다. Divide & Conquer. 기본이다.
        Pythonic 한 방법도 아니었다. Go 로 구현했어도 단순히 result list 를 추가해주는거라서 쉬웠다.
        이런 문제를 잘 푸려면 PS 의 감을 유지할 필요가 있어보인다. 그리디 문제를 놓치지 않기 위해서.
        """
        result = []

        for interval in intervals:
            # the new interval is after the range of other interval, so we can leave the current interval because the new one does not overlap with it
            if interval[1] < newInterval[0]:
                result.append(interval)
            # the new interval's range is before the other, so we can add the new interval and update it to the current one
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval
            # the new interval is in the range of the other interval, we have an overlap, so we must choose the min for start and max for end of interval
            elif interval[1] >= newInterval[0] or interval[0] <= newInterval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        result.append(newInterval)
        return result
        """
        Top rated #2
        """
        START, END = 0, 1

        s, e = newInterval[START], newInterval[END]

        left, right = [], []

        for cur_interval in intervals:
            if cur_interval[END] < s:
                left += [cur_interval]
            elif cur_interval[START] > e:
                right += [cur_interval]
            else:
                s = min(s, cur_interval[START])
                e = max(e, cur_interval[END])

        return left + [[s, e]] + right
        """
        MY FAILED SOLUTION, 52min elapsed
        """
        left = len(intervals)
        right = len(intervals)

        for i in range(1, len(intervals)+1):
            if intervals[i-1][0] < newInterval[0]:
                continue
            else:
                left = i-1
                break

        for i in range(1, len(intervals)+1):
            if intervals[i-1][1] < newInterval[1]:
                continue
            else:
                right = i-1
                break

        print(left, right)

        if left == len(intervals):
            if right == len(intervals):
                return intervals + [newInterval]
            else:
                return intervals

        if left == right:
            if newInterval[1] < intervals[left][0]:
                return intervals[:left] + [newInterval] + intervals[left:]
            else:
                right_list = []
                if left + 1 < len(intervals):
                    right_list = intervals[left+1:]
                return intervals[:left] + [[newInterval[0], intervals[left][1]]] + right_list
        elif right < left:
            return intervals
        else:
            if newInterval[1] < intervals[right][0]:
                return intervals[:left] + [newInterval] + intervals[right:]
            else:
                right_list = []
                if right + 1 < len(intervals):
                    right_list = intervals[right+1:]
                return intervals[:left] + [[newInterval[0], intervals[right][1]]] + right_list
