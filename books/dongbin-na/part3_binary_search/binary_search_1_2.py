'''
:Point: 이진탐색을 수정할때, 수정한 조건에서 제대로 분기하는지 확인해보기!
이 문제의 경우에는, 가장 왼쪽이나 오른쪽 값이 아니라면
각각 왼쪽으로, 또는 오른쪽으로 이동해야한다.

위 분기를 제대로 작성하지 않아 틀릴뻔!

1) O(logN)을 유지하는 선에서 커스텀
2) 커스텀된 분기가 제대로 작동하는지 체크

7 2
1 1 2 2 2 2 3
>> 4

7 4
1 1 2 2 2 2 3
>> -1

7 1
1 1 2 2 2 2 3
>> 2
'''
def bs_first(data, target):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2

        # if (mid == 0 or data[mid - 1] < target) and data[mid] == target:
        #     return mid
        if data[mid] == target:
            if mid == 0 or data[mid - 1] < target:
                return mid
            else: # go left
                end = mid - 1
        elif data[mid] < target: # go right
            start = mid + 1
        else: # go left
            end = mid - 1

def bs_last(data, target):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        # if (mid == len(data) - 1 or data[mid + 1] > target) and data[mid] == target:
        #     return mid
        if data[mid] == target:
            if (mid == len(data) - 1 or data[mid + 1] > target):
                return mid
            else: # go right
                start = mid + 1
        elif data[mid] < target: # go right
            start = mid + 1
        else: # go left
            end = mid - 1

n, x = map(int, input().split())
data = list(map(int, input().split()))

first = bs_first(data, x)
last = bs_last(data, x)

# print(first)
# print(last)
if first == None:
    print(-1)
else:
    print(last - first + 1)

'''
<Answer>
def count_by_value(array, x):
    # 데이터의 개수
    n = len(array)

    # x가 처음 등장하는 인덱스 계산
    a = first(array, x, 0, n-1)

    # 수열에 x가 존재하지 않는 경우
    if a == None:
        return 0 # 값이 x인 원소의 개수는 0개이므로 0 반환

    # x가 마지막으로 등장한 인덱스 계산
    b = last(array, x, 0, n-1)

    # 개수를 반환
    return b - a + 1

def first(array, target, start, end):
    ~
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid
    elif array[mid] >= target:
    ~

def last(array, target, start, end):
    ~
    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    elif array[mid] > target:
    ~

count = count_by_value(array, x)
if count == 0:
    print(-1)
else:
    print(count)
'''