def quick_sort_classic(array: list[int], start: int, end: int) -> list[int]:
    """
    TC = 평균 O(NlogN) 최악 O(N^2)
    이미 데이터가 정렬되어 있는 경우 매우 느리게 동작한다.
    데이터가 무작위로 입력되는 경우 퀵 정렬은 빠르게 동작할 확률이 높다.
    언어 내부 라이브러리들은 이를 최적화 하기 위해 피벗값을 설정할 때 추가적인 로직을 더해준다.
    """
    if start >= end:
        return

    pivot = start  # hoare partition = 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # 피벗보다 작은 데이터를 찾을때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:  # 엇갈린다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
            array[left], array[right] = array[right], array[left]

        # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
        quick_sort_classic(array, start, right-1)
        quick_sort_classic(array, right+1, end)


array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

quick_sort_classic(array, 0, len(array) - 1)
print(array)


def quick_sort_pythonic(array):
    """
    전통 퀵 정렬의 분할 방식과는 조금 다른데, 피벗과 데이터를 비교하는 비교 연산 횟수가 증가하므로 
    시간 면에서는 조금 비효율적이다. 하지만 더 직관적이고 기억하기 쉽다는 장점이 있다.
    """
    # 리스트가 하나의 원소만 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]  # 피벗은 첫 번째 원소
    tail = array[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort_pythonic(left_side) + [pivot] + quick_sort_pythonic(right_side)


array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

quick_sort_pythonic(array)
print(array)
