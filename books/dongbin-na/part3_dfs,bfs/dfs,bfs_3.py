'''
개선 방안 :heap을 써서 삽입 삭제 logN이다
포인트: 그냥 맨처음에 순서 낮은 순서로 넣으면 순서 유지된다.

지난 시도 때 틀린 이유:
처음 Queue 초기화시 virus 체크 안하고 모두 큐에 넣어버림..

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
from collections import deque
import sys

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
    q = deque()
    # 초기 바이러스 위치로 큐 초기화
    tmp = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            if data[i][j] != 0: # is virus
                tmp.append((data[i][j], i, j)) # (virus, x,)
    tmp.sort() # asc order, NlogN
    for t in tmp:
        q.append(t) # 작은 virus# 순서로 넣음.
    
    # bfs
    while q:
        virus, x, y = q.popleft()

        if distance[x][y] == S: # S초뒤 결과가 나왔을 경우 break
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 1 <= nx <= n and 1 <= ny <= n: # in map
                if data[nx][ny] == 0: # empty
                    data[nx][ny] = virus
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((virus, nx, ny))
bfs(data)

# print(data)
print(data[X][Y])

'''
<Answer>
from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    # 보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            data.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기 (낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 바이러스가 퍼져나갈 수 있는 4가지 위치
dx = [-1, 0, +1, 0]
dy = [0, 1, 0, -1]

# BFS 진행
while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))

print(graph[target_x - 1][target_y - 1])
'''