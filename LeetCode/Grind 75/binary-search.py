class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return binary_search(nums, target, 0, len(nums)-1)


def binary_search(arr, target, start, end):
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
