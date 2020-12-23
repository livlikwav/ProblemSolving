'''
4 6
19 15 10 17
'''
N, M = map(int, input().split())
data = list(map(int, input().split()))

# debug
# print(N, M)
# print(data)

def binary_search(data, M, start, end):
    result = 0

    while start <= end:
        mid = (start + end) // 2

        sum = 0
        for i in data:
            if i > mid:
                sum += (i - mid)
        
        if sum == M:
            result = mid
            break
        elif sum > M: # go right
            result = mid # save last one
            start = mid + 1
        else: # go left
            end = mid - 1

    return result

# Solution
start = 0
end = max(data)
result = binary_search(data, M, start, end)
print(result)

'''
전형적인 이진 탐색 문제

Parametric Search
파라메트릭 서치는
최적화 문제를 결정 문제로 바꾸어 해결하는 기법

원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제

최적화 문제를 이진 탐색으로 결정 문제를 해결하면서 범위를 좁혀간다.

결정 문제는 예 혹은 아니오로 답하는 문제를 말한다.
<Answer>
n, m ~
array ~ 

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
'''