def selection_sort(nums: list[int]) -> list[int]:
    """
    매번 가장 작은것을 '선택'한다. 
    TC O(N^2) = N * (N + 1) / 2 = N + N-1 + N-2 + ... + 2
    SC O(1)
    """
    for i in range(len(nums)):
        min_idx = i

        for j in range(i+1, len(nums)):
            if nums[min_idx] > nums[j]:
                min_idx = j

        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums


nums = [3, 2, 4, 8, 1, 0, 5, 7, 6]

print(selection_sort(nums))
