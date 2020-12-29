'''
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1 
0 1 0 0 0 0 0
0 1 0 0 0 0 0
'''
import copy

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

temp = [[0] * M for _ in range(N)]
result = 0
dx = [0, 0, -1, +1]
dy = [-1, +1, 0, 0]

# debug
# print(N, M)
# print(data)
# print(temp)
# print(result)

def set_walls(map:list, pos:tuple, count:int) -> None:
    global result
    x, y = pos

    for i in range(len(map)):
        temp[i] = copy.deepcopy(map[i])

    if count == 3:
        result = max(result, spread_virus(temp))
        return

    if y + 1 < M: # go right
        set_walls(temp, (x, y+1), count)
        temp[x][y+1] = 1
        set_walls(temp, (x, y+1), count + 1)
    elif x + 1 < N: # new line
        set_walls(temp, (x+1, 0), count)
        temp[x+1][0] = 1
        set_walls(temp, (x+1, 0), count + 1)
    else: # (N-1, M-1)
        return

def spread_virus(map: int) -> int:
    for i in range(len(map)):
        temp[i] = copy.deepcopy(map[i])
    
    visited = [[False] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                if temp[i][j] == 2:
                    visited[i][j] = True
                    dfs(temp, visited, (i, j))
    
    # count safe area
    count = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                count += 1
    return count

def dfs(temp, visited, pos):
    x, y = pos
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny]:
                if temp[nx][ny] == 0:
                    visited[nx][ny] = True
                    temp[nx][ny] = 2
                    dfs(temp, visited, (nx, ny))

set_walls(data, (0,0), 0)

print(result)
'''
<Answer>
n, m = map(int, input().split())
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))

# 4가지 이동방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# DFS를 통해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상 하 좌 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# DFS를 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최댓값 계산
        result = max(result, get_score())
        return
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)
'''