'''
풀다가 시간이 넘기도 했고,
도저히 모르겠어서 포기...
포기하지말고 알고리즘 꾸준히 풀어보자.. 언젠간 늘겠지 화이팅.

<개선 방안>
1. LIS 를 이해하고 체화하기
2. LIS 자체를 외우고, 증가하는(또는 감소하는) 부분 수열 찾는 문제에 적용하기

<답안 메모>
이 문제의 기본 아이디어
가장 긴 증가하는 부분 수열
LIS, Longest Increasing Subsequence

하나의 수열이 주어졌을 때 값들이 증가하는 형태의 가장 긴 부분 수열을 찾는 문제이다.

D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
DP 테이블의 값은 모두 1으로 초기화한다
가장 긴 증가하는 부분 수열을 계산하는 점화식은 다음과 같다
모든 0 <= j < i에 대하여
D[i] = max(D[i], D[j] + 1) if array[j] < array[i]

주어진 배열을 뒤집은 뒤에, 위 점화식을 그대로 사용하면 해결할 수 있다.
'''
n = int(input())
data = list(map(int, input().split()))

# print(n)
# print(data)

dp = []

def test(arr, target):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] <= target:
            arr.remove(arr[i])
        else:
            arr.append(target)
            break
    return arr

dp[0] = 1
max_val = 1
for i in range(1, n):
    if data[i-1] > data[i]:
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = max(max_val, test(data[:i], data[i]))

print(dp)
print(dp[n-1])
'''
n = int(input())
array = list(map(int, input().split()))
# 순서를 뒤집어 '가장 긴 증가하는 부분 수열'문제로 변환
array.reverse()

# 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
dp = [1] * n

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 열외시켜야 하는 병사의 최소 수를 출력
print(n - max(dp))
'''