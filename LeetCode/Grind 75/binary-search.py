class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return binary_search(nums, target, 0, len(nums)-1)


def binary_search(arr, target, start, end):
    """
    My solution solved in 18 minutes
    But there is more sugary codes
    """
    mid = (end + start) // 2
    # print(start, mid, end)

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        end = mid - 1
    else:
        start = mid + 1

    if end < start:  # end condition
        return -1

    return binary_search(arr, target, start, end)


def binary_search_stack(arr, target, start, end):
    """
    My solution by stack version, no recursion
    스택에서의 종료 조건은 그냥 넣지 않으면 된다.
    """
    stack = [(start, end)]

    while stack:
        x, y = stack.pop()
        mid = (end + start) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

        if end >= start:  # end condition == dont append stack
            stack.append((start, end))

    return -1


class SolutionVoted:
    """
    Most voted solution
    - 함수를 별도로 선언할 필요가 없다 (생각해보니 그러네 재귀도 아니네)
    - while 문으로 종료 조건 깔끔하게 할 수 있다.
    """

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
