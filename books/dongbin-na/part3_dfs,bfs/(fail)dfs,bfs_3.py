'''
BOJ 18405에서 시간 초과남...
--> 해결함: 어이없는 실수함.. 
처음 q 초기화시 0도 큐에 넣어버림. if문 안써서..

3 3
1 0 2
0 0 0
3 0 0
2 3 2
>>> 3

3 3
1 0 2
0 0 0
3 0 0
1 2 2
>>> 0
'''
import heapq, sys

input = sys.stdin.readline

n, k = map(int, input().split())

data = []
# map index 1부터 N이므로 편의상 N+1 * N+1로 초기화
data.append([0] * (n+1)) # empty row #0
for i in range(1, n+1):
    new_row = [0] + list(map(int, input().split()))
    data.append(new_row)

S, X, Y = map(int, input().split())
distance = [[0] * (n+1) for _ in range(n+1)] # 시간 S는 0으로 초기화

dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]

# print(n, k)
# print(data)
# print(S, X, Y)
# print(distance)

def bfs(data: list) -> None:
    q = []
    # 초기 바이러스 위치로 큐 초기화
    for i in range(1, n+1):
        for j in range(1, n+1):
            if data[i][j] != 0: # is virus
                heapq.heappush(q, (0, data[i][j], i, j)) # dist, virus, x, y
    # bfs
    while q:
        dist, virus, x, y = heapq.heappop(q)

        if dist == S: # S초뒤 결과가 나왔을 경우 break
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 1 <= nx <= n and 1 <= ny <= n: # in map
                if data[nx][ny] == 0: # empty
                    data[nx][ny] = virus
                    distance[nx][ny] = dist + 1
                    heapq.heappush(q, (dist + 1, virus, nx, ny))
bfs(data)

# print(data)
print(data[X][Y])
