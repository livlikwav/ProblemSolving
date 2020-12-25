'''
<틀린 이유 분석>
1. 아직 변수명이나, 함수구조가 이해하기 어렵다. C라던지 candidate라던지
그래서 늘 어려운 구현 문제 틀리는 듯 하다.

2. Python 전역변수 수정은 global 써야지 되는거 아니었나?
왜 동빈씨는 말안해주고 혼자서 temp를 만들어서 풀었을까?
나도 data 그대로가 아니라 temp 만들어서 하면 잘 돌아갈 것 같다.
--> 아니었다 ㅎㅎ
'''
from collections import deque
from itertools import combinations

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
temp = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# debug
# print(N, M)
# print(data)
# print(visited)

def find_empty(data) -> list:
    result = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 0:
                result.append((i, j))
    return result

# print(find_empty(data))

candidate = find_empty(data)
C = list(combinations(candidate, 3))

# print(C)

dx = [0, 0, -1, +1]
dy = [-1, +1, 0, 0]

def bfs(temp, visited) -> int:
    # find virus
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            if(temp[i][j] == 2): # if virus
                queue = deque([(i,j)])

                while queue:
                    x, y = queue.popleft()
                    if visited[x][y]:
                        continue
                    # not visited
                    visited[x][y] = True
                    temp[x][y] = 2 # Virus
                    # check NSEW
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]

                        if 0 <= nx < N and 0 <= ny < M:
                            if temp[nx][ny] == 0:
                                queue.append((nx, ny))
    # check count
    return(len(find_empty(temp)))

def check(data, points) -> int:
    # set temp
    for i in range(len(data)):
        for j in range(len(data[0])):
            temp[i][j] = data[i][j]
    # set wall
    for point in points:
        x, y = point
        temp[x][y] = 1 # set wall
    return bfs(temp, visited)


# Solution
result = 0
for points in C:
    result = max(result, check(data, points))

print(result)