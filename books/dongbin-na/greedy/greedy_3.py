import sys

def myinput():
    return sys.stdin.readline()

N, M = map(int, myinput().split())

count = 0
while(N != 1):
    if(N % M == 0):
        count += 1
        N = N // M
        # print(N)
    else: # != 0
        count += 1
        N -= 1
        # print(N)

print(count)

'''
<Lesson learned>
나는 구현 문제처럼 풀었다.. 문제 조건을 그대로 반복하듯 구현
그리디 문제처럼 푼다 == 무조건 많이 나누게 하는 것이 Greedy이고 답이다 라고 생각하고 구현함
그래서 코드도 나눌수 있나? 못나누면 빼고 일단 나눌 수 있는지 검사하듯 구현되어있다.

//= 연산자

target = (n // k) * k
result += (n - target)
이러한 과정을 통해서 1을 빼는 횟수를 한번에 빼는 테크닉
(N이 100억 이상일때도 빠르게 계산하기 위해서)

result += (n - 1)
n이 결국 1이 되어야하고, 1씩 빼면 되니까
n-1번 빼야할 것임. (음수는 아니고 무조건 2이상의 양수이기도 하고)

<Answer>
n, k = map(int, input().split())
result = 0

while True:
    # N == K로 나누어떨어지는 수가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
'''
