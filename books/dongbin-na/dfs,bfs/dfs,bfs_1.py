'''
4 5
00110
00011
11111
00000

15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''


N, M = map(int, input().split())
map = [input() for _ in range(N)]

visited = [[False] * M for _ in range(N)]
dn = [-1, +1, 0, 0] # 상하좌우
dm = [0, 0, -1, +1]


def dfs(map, n, m):
    global visited
    visited[n][m] = True
    # 상하좌우 체크
    for i in range(4):
        x = n + dn[i]
        y = m + dm[i]
        if x >= 0 and x < N and y >= 0 and y < M: # in map
            if map[x][y] == '0': # valid. 1 is invalid
                if not visited[x][y]:
                    dfs(map, x, y)

# Solution
count = 0
for n in range(N):
    for m in range(M):
        if map[n][m] == '0':
            if not visited[n][m]:
                count += 1
                dfs(map, n, m)
        

print(count)

'''
<Answer>
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    # check out of map
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # not visited
    if graph[x][y] == '0':
        # set visited
        graph[x][y] = 1
        # 상하좌우 재귀호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)
'''