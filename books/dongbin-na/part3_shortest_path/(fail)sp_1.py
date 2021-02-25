# boj11404

n = int(input())
m = int(input())

INF = int(1e9)
data = [[INF] * (n + 1) for _ in range(n+1)] # 나중에 출력시에는 1,1 부터 출력하기

for _ in range(m):
    start, end, cost = map(int, input().split())
    data[start][end] = min(data[start][end], cost)

# debug
# print(n, m)
# for i in range(1, n+1):
#     print(data[i][1:])

# d_ab = min(d_ab, d_ak + d_kb)
for a in range(1, n+1):
    for b in range(1, n+1):
        for k in range(1, n+1):
            if a != b:
                data[a][b] = min(data[a][b], data[a][k] + data[k][b])

# INF 값 0으로 변환
for i in range(1, n+1):
    for j in range(1, n+1):
        if data[i][j] == INF:
            data[i][j] = 0

# 결과 출력
for i in range(1, n+1):
    print(' '.join(list(map(str, data[i][1:]))))
    # print(data[i][1:])