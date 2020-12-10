import time, sys

# input
N, M, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()
arr.reverse()

count = 0
result = 0
for i in range(M):
    if(count < K):
        result += arr[0]
        count += 1
        # print(arr[0])
    else:
        result += arr[1]
        count = 0
        # print(arr[1])

# print('-----')
# print(N, M, K)
# print(arr)
print(result)

'''
<Lesson learned>

변수 네이밍 --> data

arr[0], arr[1] --> first, second
더 읽기 편하게 사용하기

Python에서의 나머지 구하기
int(A/B)
A // B

<Answer>

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

<Answer 2>

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(m / (k+1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)
'''