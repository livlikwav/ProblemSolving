'''
<Lesson Learned>
- 딱 붙어있는 int list 입력받는법
    - graph.append(list(map(int, input())))
- 변수 이름
    - graph, x, y, dx, dy, nx, ny
- 상하좌우
    - dx, dy, for i in range(4)
- bfs에서 최단거리 구하는 법
    - 노드마다 해당노드까지의 거리를 기록
    - 노드 첫 방문시, 전 노드 거리 + 1로 부여

<input>
5 6
101010
111111
000001
111111
111111
'''
from collections import deque

N, M = map(int, input().split())
data = [input() for _ in range(N)]
map = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        map[i][j] = int(data[i][j])

# debug
# print(N, M)
# for row in map:
#     print(row)
# def print_map(map: list):
#     for row in map:
#         print(row)
#     print()

distance = [[0] * M for _ in range(N)]
dn = [-1, +1, 0, 0]
dm = [0, 0, -1, +1]

def bfs(map, distance, start, N, M) -> int:
    queue = deque()
    queue.append(start) # tuple
    distance[start[0]][start[1]] = 1

    while queue: # not empty
        n, m = queue.popleft()
        map[n][m] = 0 # set visited
        # print_map(map)

        if n == N-1 and m == M-1:
            return distance[n][m]
        
        for i in range(4):
            x = n + dn[i]
            y = m + dm[i]
            if x >= 0 and x < N and y >= 0 and y < M:
                if map[x][y] == 1: # not visited
                    queue.append((x, y))
                    distance[x][y] = distance[n][m] + 1

print(bfs(map, distance, (0,0), N, M))

'''
<Answer>
from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]

print(bfs(0, 0))
'''