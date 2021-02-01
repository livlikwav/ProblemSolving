'''
<자주 실수하는 부분>
- for 문 종료 조건
- 중간결과, 최종결과 갱신 방식
--> 정교하게 설계한 뒤 코드로 옮기고,
--> 중간 채점 결과 틀리면 이 부분을 유심히 다시 살펴보기

<답안 팁>
나처럼 매번 tmp 맵 초기화하지 않고,
장애물 3개 뿐이니까
매번 설치하고, 다시 없애고 해도 되긴함!

<답안 메모>
정확히 3개 설치하는 모든 경우를 확인해서,
매 경우마다 모든 학생을 감시로부터 피하게 할 수 있는지 여부 출력

장애물 3개 설치하는 모든 경우 최악 36C_3이므로 10000 이하의 수이다
완전 탐색을 수행해도 시간 초과없이 문제를 해결할 수 있다.
따라서 모든 조합을 찾기위해서 dfs 사용해도되고,
from itertools import combinations 사용해도 된다.
'''
from itertools import combinations

n = int(input())

data = [[0] * n for _ in range(n)]
tmp = [[0] * n for _ in range(n)]

teachers = []
emptys = []

for i in range(n):
    line = input().split()
    for j in range(n):
        data[i][j] = line[j]

        if line[j] == 'X':
            emptys.append((i, j))
        elif line[j] == 'T':
            teachers.append((i, j))

# debug
# print(n)
# print(data)
# print(teachers)
# print(emptys)

candidates = list(combinations(emptys, 3))

def check_safe_direction(x, y, d):
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while True:
        nx = x + direction[d][0]
        ny = y + direction[d][1]
        if 0 <= nx < n and 0 <= ny < n: # 맵 안
            if tmp[nx][ny] == 'O':
                break # 장애물 만남
            elif tmp[nx][ny] == 'S':
                return False # 학생 발견함
        else:
            break # 맵 밖에 다다름
        
        x = nx
        y = ny
    
    return True # 학생 발견하지 못하고 종료

# 완전탐색 수행
result = True

for objects in candidates:
    # tmp 맵 다시 초기화
    for i in range(n):
        for j in range(n):
            tmp[i][j] = data[i][j]
    # object 추가
    for object in objects:
        tmp[object[0]][object[1]] = 'O'
    
    # 해당 tmp 맵에 대해서 선생님 별로 check 수행

    result = True  # 매 tmp 맵 결과에 대해초기화
        
    for teacher in teachers: # 모든 선생님별로, 
        for i in range(4): # 모든 방향에 대해 검사 수행
            if not check_safe_direction(teacher[0], teacher[1], i): # 한번이라도 안전하지 않을 경우
                result = False

    # 해당 tmp 맵 검사 결과가 모두 안전했다면, 결과 출력
    if result:
        print('YES')
        break

# 마지막 테스트 결과까지 False 인 경우 NO 출력
if not result:
    print('NO')
'''
<Answer>
from itertools import combinations

n = int(input()) # 복도의 크기
board = [] # 복도의 정보(N x N)
teachers = [] # 모든 선생님 위치 정보
spaces = [] # 모든 빈 공간 위치 정보

# 입력으로 각 배열 초기화
~~~
# 특정 방향으로 감시를 진행(학생 발견 : True, 미발견 : False)
def watch(x, y, direction):
~~~

# 장애물 서치 이후에, 한 명이라도 학생이 감지되는지 검사
def process():
    # 모든 선생님의 위치를 하나씩 확인
    for x, y in teachers:
        # 4 가지 방향으로 학생을 감지할 수 있는지 확인
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False # 학생이 한 명도 감지되지 않도록 설치할 수 있는지의 여부

# 빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(spaces, 3):
    # 장애물 설치해보기
    for x, y in data:
        board[x][y] = 'O'
    # 학생이 한 명도 감지되지 않는 경우
    if not process():
        # 원하는 경우를 발견한 것임
        find = True
        break
    # 설치된 장애물을 다시 없애기
    for x, y in data:
        data[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')
'''