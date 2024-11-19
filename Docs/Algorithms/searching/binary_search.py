def binary_search(nums: List[int], target: int) -> int:
    """
    배열의 내부 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘
    TC O(logN): 확인하는 원소의 개수가 절반씩 줄어든다
    탐색 범위가 큰 상황에서의 탐색을 가정하는 문제가 많다.
    탐색 범위가 2000만을 넘어가면 이진 탐색을 고려해보자. (Python 에서 1초 내로 걸리려면 보통 2000만 번 이하, 2*10^7)
    """
    def bs_recursive(nums, start, end, target):
        if start > end:
            return -1
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return bs_recursive(nums, start, mid - 1, target)
        else:
            return bs_recursive(nums, mid + 1, end, target)

        return -1

    def bs_stack(nums, target):
        stack = []

        while stack:
            start, end = stack.pop()
            if start > end:
                continue

            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                stack.append((start, mid-1))
            else:
                stack.append((mid+1, end))

        return -1
