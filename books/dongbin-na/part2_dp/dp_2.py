'''
DP 문제는 함수 호출되는 과정을 -> 그림으로 도식화하여 생각해보자

1)점화식을 만들고 2) 보텀업 방식으로 구현

또는 1) 일단 재귀로 풀고, 시간 복잡도 오버시 2) 탑바텀 방식으로 구현

내 답과 문제의 답은 좀 다르게 풀었다.
문제 답이 근본임. 점화식 세우고, 구현마저 바텀업으로 간단함!

점화식 세우는 연습을 많이 하자...!
a_n에 대해서, a_n을 구하기 위한 경우의 수를 정의하기.
이를 점화식으로 나타내기.

내 문제는 max()에 대한 존재를 잊었음.
a_n을 위해서 a_n-1 말고 a_n-2도 같이 생각해보면 되는 것이었다.
그래서 부분문제가 똑같이 반복될 수 있다는 것!
'''
N = int(input())
data = list(map(int, input().split()))

# debug
# print(N)
# print(data)

result = 0
d = dict() # dp table

def dfs(idx:int, sum:int):
    print(f'idx, sum: {idx}, {sum}')

    global result
    # break
    if idx >= N:
        result = max(result, sum)
        return

    # go
    if (idx+2, sum+data[idx]) in d:
        pass
    else:
        d[(idx+2, sum+data[idx])] = True
        dfs(idx+2, sum+data[idx])

    # pass
    if (idx+1, sum) in d:
        pass
    else:
        d[(idx+1, sum)] = True
        dfs(idx+1, sum)

# Solution
dfs(0, 0)
print(result)
'''
<Answer>
n = int(input())
array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])
'''