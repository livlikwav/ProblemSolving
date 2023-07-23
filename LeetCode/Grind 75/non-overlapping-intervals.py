class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Voted #1 나랑 약간 다르게 풀었다.
        핵심 아이디어: 회의룸 시간 최대한 많이 잡기라고 생각하고, end_time 순으로 정렬해서 왼쪽부터 채워나가는 거다.
        이 사람은 남은 interval 갯수를 세서 마지막에 빼주는 방식으로 구현해서 헷갈렸는데 크게 어려운 아이디어는 아니었다.
        SC O(1)
        좋은 점은 SC 가 나보다 효율적이다. result list 를 저장할 필요 없이 마지막 lnterval 의 index 만 저장한다.

        문제 유형은 Merge intervals 변형이라고 볼 수 있고, 적용된 알고리즘은 greedy + sort 인것 같다.
        """
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)

        prev = 0
        count = 1

        for i in range(1, n):
            if intervals[i][0] >= intervals[prev][1]:
                prev = i
                count += 1

        return n - count
        """
        MY SOLUTION elapsed about 25min
        문제를 제대로 이해하고 풀어야 했다 ㅠ 이 문제는 merge 하는게 아니라, 그냥 overlapping 인 애를 삭제한다.

        삭제하는 순간 merging 이랑 다른 문제이므로 다르게 접근해야한다.
        이 경우 minimum number of intervals 임에 집중한다. 어떻게 삭제해야 min 을 보장할까?
        
        최대한 intervals 를 잘게 유지해야 많이 들어가고, 덜 삭제한다.
        divide and conquer 로 deleting one 하는 부분 함수에 집중했고, 이 경우에, y 값이 더 작은 애를 남기도록 했다.
        TC O(NlogN) SC O(N)
        sorting 은 안할 수 없었다. 그러면 계속 result 를 재귀적으로 더 delete 해야하는지 체크해야하기 떄문이다.
        """
        intervals.sort()
        result = []
        cnt = 0
        for i in range(len(intervals)):
            if not result or result[-1][1] <= intervals[i][0]:
                result.append(intervals[i])
            else:
                cnt += 1
                # remain item that has smallar y
                if result[-1][1] > intervals[i][1]:
                    result.pop()
                    result.append(intervals[i])

        return cnt
