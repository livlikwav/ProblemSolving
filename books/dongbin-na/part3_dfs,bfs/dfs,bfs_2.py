'''
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1   
0 1 0 0 0 0 0
0 1 0 0 0 0 0
>>27

4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
>>9

8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
>>3
'''

import time

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
temp = [[0] * m for _ in range(n)]

# debug
# print(n, m)
# print(data)
# print(temp)

# 4-d
dx = [0, 0, -1, +1]
dy = [-1, +1, 0, 0]
result = 0

def virus(pos: tuple) -> None: # recursive
    x, y = pos
    # move 4-d
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus((nx, ny))

def get_score() -> int: # from temp
    sum = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                sum += 1
    return sum

def dfs(pos: tuple, count: int) -> None: # 벽 3개 세우는 경우 완전 탐색
    global result
    if count == 3:
        # temp 복사
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # virus 전파
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus((i, j))
        result = max(result, get_score())
        return
    # 벽 3개 세우는 경우 완전 탐색
    x, y = pos
    isValid = False
    for i in range(n):
        for j in range(m):
            if i == x and j == y:
                isValid = True
            if isValid:
                if data[i][j] == 0:
                    data[i][j] = 1
                    count += 1
                    dfs((i,j), count)
                    data[i][j] = 0
                    count -= 1

start_time = time.time()

dfs((0,0), 0)

end_time = time.time()

print(result, ' time:', end_time-start_time)
'''
아무리 봐도 시간이 넘 오래 걸리는데... 
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1   
0 1 0 0 0 0 0
0 1 0 0 0 0 0
27  time: 4.092300891876221

8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
3  time: 24.35809874534607

---> 공식 답지에도 그냥 PyPy3로 제출하라 되어있다 ㅋㅋㅋㅋ;
내생각에는... dfs 돌릴때 계속 앞에 있는거 다시 건드릴거 같은데..
visited를 설정하면 되지 않을까?
>> visited는 왠지 틀렸어..

쉽게 start pos를 넣으면 어떨까?
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1   
0 1 0 0 0 0 0
0 1 0 0 0 0 0
27  time: 0.6597177982330322

8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
3  time: 4.366018056869507

---> 그래도 4초를 넘는거 보면 힘든가부다 ㅋㅋ
'''