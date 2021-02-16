'''
마지막 n 번째 칸을 채우는 경우의 수는 2가지이다.
왜냐면 블록의 종류가 2가지 뿐이므로.

1x2 1개거나,
2x1 2개임

따라서
dp[n] = dp[n-2] + dp[n-1]
'''
n = int(input())
dp = [0] * 1000

dp[0] = 1
dp[1] = 2

for i in range(2, n):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n-1] % 10007)