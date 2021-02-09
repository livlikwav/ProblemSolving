'''
경계값 테스트를 잘하자.
n == 0, 1, 2에 대해서 했어야했다.
boj에서 채점 100프로쯤 오류뜨는거랑, IndexError인거 안떴으면 더 헤맬뻔 했다...
'''
n = int(input())
data = [0] * (n + 1)
for i in range(1, n+1):
    data[i] = int(input())
# print(n)
# print(data)

dp = [0] * (n + 1)

if n == 1:
    print(data[1])
elif n == 2:
    print(data[1] + data[2])
else:
    dp[1] = data[1]
    dp[2] = data[1] + data[2]

    # dp[i] = i를 밟았을때 max 결과값 

    for i in range(3, n+1):
        dp[i] = max((dp[i-2] + data[i]), (dp[i-3] + data[i] + data[i-1]))

    # print(dp)

    print(dp[n])