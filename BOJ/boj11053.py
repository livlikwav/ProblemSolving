n = int(input())
data = list(map(int, input().split()))

# print(n, data)

dp = [0] * n
dp[0] = 1

for i in range(1, n):
    dp[i] = 1
    for j in range(0, i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))