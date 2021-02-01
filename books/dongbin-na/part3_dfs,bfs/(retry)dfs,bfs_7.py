'''
<반만 Success>
Pypy3로 성공하였으나, Python3에서는 시간 초과이다.

<답안과 차이점>
다 비슷하고,
내가 실수한 점이 딱 하나 다른 것이
data(graph)를 갱신할 때,
문제에서 주어진 것처럼 다 끝나고 다시 다 2중 for문 돌면서 갱신하지 않아도 된다.
visited 되었기 때문에, 어짜피 다음 연합 찾을때는 탐색하지 않기 때문

<답안 메모>
답안 풀이는 매우 간결했다.
나처럼 여러 경우에 대한 고려가 없이 문제에서 설명한대로 bfs 구현하였다.
'''
import sys
sys.setrecursionlimit(3000)

n, l, r = map(int, input().split())
data = []
for _ in range(n):
    line = list(map(int, input().split()))
    data.append(line)

# debug
# print(n, l, r)
# print(data)

dx = [0, 0, -1, +1]
dy = [-1, +1, 0, 0]

# global var
visited = [[False] * n for _ in range(n)]
union_list = []
union_mark = [[0] * n for _ in range(n)]
sum = 0

def dfs(x, y):
    global sum
    global visited
    global union_list

    # 이미 방문했을 경우 종료
    if visited[x][y]:
        return
    
    visited[x][y] = True
    union_list.append((x, y))
    sum += data[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 맵 밖이면 다음 loop 진행
        if not (0 <= nx < n and 0 <= ny < n):
            continue

        # 맵 안일 경우
        diff = abs(data[x][y] - data[nx][ny])
        # l이상 r이하 조건을 만족한다면
        if l <= diff <= r:
            dfs(nx, ny)

loop = True
result = 0 # 결과값 == 인구 이동 횟수

# 인구이동 1번 == 여러 연합을 찾고 값을 갱신
while loop:
    # 새로운 인구이동을 위한 변수 초기화
    moved = 0
    visited = [[False] * n for _ in range(n)]
    union_mark = [[-1] * n for _ in range(n)]

    # 연합 여러개 전체 탐색
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                # 새로운 연합을 위한 변수 초기화
                union_list = []
                sum = 0
                # 새로운 연합 찾기 진행
                dfs(i, j)

                # 새로운 연합 생겼는지 확인
                if len(union_list) > 1: # 맨 처음에 내가 넣어준애 혼자면 연합 없는거
                    moved += 1 # 소분류 인구이동 횟수 1 추가 == 연합 수

                    mean = sum // len(union_list) # 새로운 인구수 계산

                    for pos in union_list:
                        x, y = pos
                        union_mark[x][y] = mean

    # 연합이 하나도 없었다면 종료 조건
    if moved == 0:
        loop = False
        break
    # 하나라도 있었다면 인구이동 + 1
    else:
        # data 갱신
        for i in range(n):
            for j in range(n):
                if union_mark[i][j] != -1:
                    data[i][j] = union_mark[i][j]
                else:
                    pass
        # for val in unions:
        #     tmp_union, tmp_mean = val
        #     for pos in tmp_union:
        #         x, y = pos
        #         data[x][y] = tmp_mean

        # 총 인구 이동 수 갱신
        result += 1


        # debug
        # if result < 10:
        #     for line in data:
        #         print(line)
        #     print()

# 결과 출력
print(result)
'''
<Answer>
from collections import deque

# 땅의 크기(N), L, R값을 입력받기
n, l, r = map(int, input().split())

# 전체 나라의 정보(N x N)를 입력받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx~
dy~

result = 0

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def process(x, y, index):
    # (x, y) 의 위치와 연결된 나라(연합) 정보를 담는 리스트
    united = []
    united.append((x, y))
    # bfs를 위한 큐 자료구조 정의
    q = deque()
    q.append((x, y))
    union[x][y] = index # 현재 연합의 번호 할당
    summary = graph[x][y] # 현재 연합의 전체 인구 수
    count = 1 # 현재 연합의 국가 수
    # queue가 빌때까지 반복 (bfs)
    while q:
        x, y = q.popleft()
        # 4 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 바로 옆 나라 확인
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 옆에 있는 나라와 인구 차이가 L명 이상, R명 이하라면
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    # 연합에 추가
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    # 연합 국가끼리 인구를 분배
    for i, j in united:
        graph[i][j] = summary // count
    return count

total_count = 0

# 더 이상 인구이동 불가능할 때까지 반복
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 해당 나라가 아직 처리되지 않았다면
                process(i, j, index)
                index += 1
    # 모든 인구 이동이 끝난 경우
    if index == n * n:
        break
    total_count += 1

# 인구 이동 횟수 출력
print(total)
'''

'''
<개선 내역>
- 무한 루프
  - 종료 조건 len(union) > 1로 개선
- recursion error
  - sys.setrecursionlimit(3000)
- 시간 초과
  - visited list.in() O(N) --> visited[x][y] O(1)
  - Pypy3은 통과
- Python3 시간 초과
  - unions도 2d list로 변환해서 로직 수정
  - Python3는 여전히 시간 초과, Pypy3는 오히려 50 ms 정도 증가
'''

