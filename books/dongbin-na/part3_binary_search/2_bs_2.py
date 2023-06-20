def Solution(nums: List[int], min: int) -> int:
    """
    떡볶이 떡 만들기, 소요시간 30분
    문제 입력값 조건에서 10억이라는 큰 수를 보면 당연스럽게 이진 탐색을 생각해야한다.

    전형적인 이진 탐색 문제이다.
    파라메트릭 서치 Parametric search = 최적화 문제를 결정 문제로 바꾸어 해결하는 방법이다
    주로 '원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제' 에 해당한다.
    결정 문제는 '예' 혹은 '아니오' 로 답하는 문제를 말한다.
    범위 내에서 조건을 만족하는 가장 큰 값을 찾으라는 최적화 문제이면 이진 탐색으로 결정 문제를 해결하면서 범위를 좁혀갈 수 있다.
    """
    heights = [0 for _ in range(0, 1000000000+1)]

    result = 0
    stack = [(1, 1000000000)]
    while stack:
        start, end = stack.pop()
        if start > end:
            return result

        mid = (start + end) // 2

        val = 0
        for i in range(len(nums)):
            v = nums[i] - heights[mid]
            if v > 0:
                val += v

        if val == min:
            return mid
        elif val < min:  # 떡을 더 잘라야함
            stack.append((start, mid-1))
        else:  # 떡을 덜 잘라야함
            result = mid
            stack.append((mid+1, end))

    return result
    """
    책 답안
    """
    start = 0
    # 이 부분이 최적화. 어짜피 제일 큰 떡 길이가 최대 높이니까. 내가 한건 10억이 최대로 잡고 했음. 사실 이진 탐색이라 상관은 없다.
    end = max(nums)

    result = 0
    while (start <= end):
        total = 0
        mid = (start + end) // 2

        for x in nums:
            # 잘랐을 때의 떡의 양 계산
            if x > mid:
                total += x - mid

        if total < m:  # 떡의 양이 부족할 경우 더 많이 자르기 = 왼쪽 부분 탐색
            end = mid - 1
        else:  # 떡의 양이 충분한 경우 덜 자르기 = 오른쪽 부분 탐색
            result = mid  # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result 에 기록
            start = mid + 1

    print(result)
