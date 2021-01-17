'''
40분 제한시간 문제였지만 1시간 만에 품 : 틀림!

pseudo code 35m
impt 14m
debugging 10m

의사코드 작성 시간을 줄이자.
그러기 위해서는 적다말고 헷갈리는 경우가 없도록,
먼저 이해를 잘 하고 넘어가기!

손으로 그림 그려서 과정을 생각해보자.
단, 상세하게 바로바로 코드를 작성하는 생각을 하면서,
빼먹는 로직이 없도록!

백준 3190번 문제
'''
from collections import deque
n = int(input())

# 0 empty, 1 snake, 2 apple
data = [[0] * (n + 1) for _ in range(n + 1)]
data[1][1] = 1 # snake init
direction = 0 # (direction +- 1) % 4
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    data[x][y] = 2 # apple

l = int(input())
rotate_dict = {}
for _ in range(l):
    a, b = input().split()
    # print(a, b) # debug
    rotate_dict[int(a)] = b # a초에 b방향으로 회전

# 뱀의 행동 정의
queue = deque()
queue.append((1, 1)) # head

# 초는 0으로 초기화
second = 0

# def pretty_print(data):
#     for line in data:
#         print(line)
#     print()

def move_snake(queue) -> bool:
    global second
    global direction
    # 1초 카운트
    second += 1
    # 머리부터 다음칸으로 늘려본다
    x, y = queue.pop() # 가장 최근꺼 빼서 보고
    queue.append((x, y)) # 다시 넣어놓고
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 맵 밖에 나가면 게임끝이니 체크
    if not (1 <= nx <= n and 1 <= ny <= n):
        return False
    # snake 1 밟으면 게임 끝
    if data[nx][ny] == 1:
        return False
    # 머리 칸에 사과 있나 체크
    if data[nx][ny] != 2: # Apple이 아닌 칸이면
        tail_x, tail_y = queue.popleft()
        data[tail_x][tail_y] = 0 # tail 칸은 비우기
    data[nx][ny] = 1 # snake 머리로 채움
    queue.append((nx, ny))

    # 회전할 시간인지 체크해서 회전
    if second in rotate_dict:
        tmp = rotate_dict[second]
        if tmp == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
    
    # 끝까지 잘 왔으면 True 반환
    return True

# 문제 해결 과정
isValid = True
while isValid:
    isValid = move_snake(queue)
    # pretty_print(data)
print(second)

'''
<Answer>
n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)] # 맵 정보
info = [] # 방향회전 정보

# 맵 정보(사과 있는 곳은 1로 표시)
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 처음에는 오른쪽을 보고 있으므로(동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 # 처음에는 동쪽을 보고 있음
    time = 0 # 시작한 뒤에 지난 '초' 사간
    index = 0 # 다음에 회전할 정보
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 뱀의 몸통과 부딪혔다면
        else:
            time += 1
            break
        x, y = nx, ny # 다음 위치로 머리를 이동
        time += 1
        if index < 1 and time == info[index][0]: # 회전할 시간인 경우 회전
            direction = turn(directio, info[index][1])
            index += 1
    return time

print(simulate())
'''