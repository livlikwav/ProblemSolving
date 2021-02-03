'''
<풀이 메모>
탐색, O(logN), 오름차순 정렬이라 이분 탐색 문제인 것은 명확했다.

case study, 그림 그려서 어떻게 이분 탐색해야할지,
if 문 분기 3가지에 대해서 파악했다.

bisect로는 어떻게 풀어야할지 감이 안와서, 반복문으로 직접 구현했다.


'''
n = int(input())
data = list(map(int, input().split()))
length = len(data)
# debug
# print(n)
# print(data)

result = -1
# bisect
start = 0
end = length - 1
while start <= end:
    mid = (start + end) // 2
    
    # print(start, mid, end)

    if data[mid] == mid:
        result = mid
        break
    elif data[mid] < mid:
        start = mid + 1 # go right
    else:
        end = mid - 1 # go left


print(result)
'''
<Answer>
# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 고정점을 찾은 경우 인덱스 반환
    if array[mid] == mid:
        return mid
    # 중간점이 가리키는 위치의 값보다 중간점이 작은 경우 왼쪽 확인
    elif array[mid] > mid:
        return binary_search(array, mid + 1, end)

n = int(input())
array = list(map(int, input().split()))

# 이진 탐색(Binary Search) 수행
index = binary_search(array, 0, n - 1)

# 고정점이 없는 경우 -1 출력
if index == None:
    print(-1)
# 고정점이 있는 경우 해당 인덱스 출력
else:
    print(index)
'''