def insertion_sort(nums: list[int]) -> list[int]:
    """
    특정한 데이터를 적절한 위치에 삽입한다. 
    pivot 앞 까지의 데이터는 정렬되어 있다고 가정한다.
    TC O(N^2) Omega(N) 리스트가 정렬되어 있는것이 최선의 경우
    """
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
            else:  # Optimization: 자기보다 작은거 나오면 멈춤
                break

    return nums


nums = [3, 2, 4, 8, 1, 0, 5, 7, 6]

print(insertion_sort(nums))
