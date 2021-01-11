'''
다시 풀기!
현재 코드는 logN이라고 내가 증명하지 못하겠음.

이 문제를 bisect 사용하지 않고 풀기 위한 핵심 아이디어는,
binary search는 BST의 leaf node까지 탐색해도 O(logN)이므로,
만족하는 노드를 탐색할때까지 더 돌려도 된다는 것이다.

이것을 이용해, x가 등장하는 제일 왼쪽 노드까지 continue 시켜도
O(logN)을 보장한다.

따라서 답안 알고리즘은 O(2logN)으로 O(logN)이다.

7 2
1 1 2 2 2 2 3
>> 4

7 4
1 1 2 2 2 2 3
>> -1
'''

def binary_search(data, target):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid
        elif data[mid] > target: # go left
            end = mid - 1
        else: # go right
            start = mid + 1
    
    return -1

n, x = map(int, input().split())
data = list(map(int, input().split()))

def find_friends(data, target, target_idx):
    '''
    근데 이건 틀린 풀이일 수 밖에 없다.
    이게 최악의 경우 O(N)이기 때문이다.
    '''
    result = 1 # target

    left = target_idx - 1
    while 0 <= left:
        if data[left] == target:
            result += 1
        left -= 1

    length = len(data)
    right = target_idx + 1
    while right < length:
        if data[right] == target:
            result += 1
        right += 1
    
    return result

idx = binary_search(data, x)
if idx == -1:
    print(-1)
else:
    print(find_friends(data, data[idx], idx))



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

# 처음 위치를 찾는 이전 탐색 메서드
def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid
    # 중간점의 값 보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
    elif array[mid] >= target:
        return first(array, target, start, mid - 1)
    else:
        return first(array, target, mid + 1, end)

def last(array, target, start, end):
    ~
    # 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    ~
'''
