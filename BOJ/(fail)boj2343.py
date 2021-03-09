n, m = map(int, input().split())
data = list(map(int, input().split()))

INF = int(1e9)
dp = [[INF] * m for _ in range(n)]

# print(n, m)
# print(data)
# print(dp)

dp[m-1][m] = 1
for x in range(m, n): # n은 index m-1 부터 n-1까지
    for y in range(1, m+1): # m은 1개부터 m개 까지
        for step in range(0, x-y):
            start = x - step
            new = sum(data[start:])

            if start - 1 < m - 2:
                continue
            if m - 1 < 1:
                continue

            new_dp = max(new, dp[start - 1][y - 1])
            dp[x][y] = min(dp[x][y], new_dp)
