n = int(input())
data = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    dp[i] = 1
    for j in range(0, i):
        if data[i] < data[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))