n, m = map(int, input().split())
data = [0] + list(map(int, input().split()))

INF = int(1e9)
dp = [[INF] * (m + 1) for _ in range(n + 1)] # 둘다 1 ~ n, 1 ~ m 개 사용한다

# 초기화
for i in range(1, n+1):
    dp[i][1] = sum(data[1:i+1])
# for line in dp:
#     print(line)

# dp
for i in range(1, n+1):
    for j in range(2, m+1): # 무조건 m개 까지만 확인하면 됨
        # j가 현재 i보다 클 경우 멈춤
        if j > i:
            break
        
        for step in range(0, i - j + 1):
            start = i - step
            new = sum(data[start:i+1])

            temp = max(new, dp[start-1][j - 1])

            if dp[i][j] > temp:
                dp[i][j] = temp

print(dp[n][m])

# for line in dp:
#     print(line)
