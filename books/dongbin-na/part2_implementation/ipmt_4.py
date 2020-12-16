N, M = map(int, input().split())
A, B, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]

# debug input
# print(N, M)
# print(A, B, d)
# def debug(map: list, pos: list, d: int) -> None:
#     for row in map:
#         print(row)
#     print(f'pos: {pos}, d: {d}')


def rotate(d: int) -> int:
    return (d-1)%4 # 3, 2, 1, 0, 3, 2 ...

def move(pos: list, d: int) -> list:
    move_type = {
        3: [0, -1], # West
        2: [+1, 0], # South
        1: [0, +1], # East
        0: [-1, 0], # North
    }
    return [pos[i] + move_type[d][i] for i in range(2)]

def check(map: list, pos: list, d: int) -> bool:
    new_pos = move(pos, d)
    new_map_val = map[new_pos[0]][new_pos[1]]
    if new_map_val == 0:
        return True
    else: # 1, 2
        return False

def check_sea(map: list, pos: list, d: int) -> bool:
    new_pos = move(pos, d)
    new_map_val = map[new_pos[0]][new_pos[1]]
    if new_map_val == 1: # sea
        return True
    elif new_map_val == 2: # visited
        return False
    else: # 0 == ground
        raise Exception('ground not checked')

def set_visited_and_count(map: list, pos: list, count: int) -> int:
    map[pos[0]][pos[1]] = 2 # 0, 1, 2 == ground, sea, visited
    return count + 1
    
# solution
count = 0
pos = [A, B]
count = set_visited_and_count(map, pos, count) # first pos
stopped = False
while not stopped:
    for i in range(5):
        if(i == 4):
            back_direction = rotate(rotate(d)) # rotate twice
            stopped = check_sea(map, pos, back_direction)
            if stopped: # sea
                break
            else: # visited
                pos = move(pos, back_direction)
                # debug(map, pos, d)
        else: # 0, 1, 2, 3
            d = rotate(d)
            valid = check(map, pos, d)
            if valid: # move
                pos = move(pos, d)
                count = set_visited_and_count(map, pos, count)
                # debug(map, pos, d)
                break
            else: # sea or visited
                pass

# debug(map, pos, d)
# result
print(count)

'''
<Lesson learned>
if-else나 break 잘못해서 오류가 많이 난다.
그냥 확실하게 if-else하도록 하자.
이번에도 다 실패했을때 뒤로갈때 빼먹어서 잘못 동작했다.

복잡한 구현 문제일수록 함수 사용해서 푸는 것이 나은 것 같다.

* 단일 책임 원칙이란 ?
Single Responsibility Principle 의 약어
객체지향 5대 원리 SOLID 중, 가장 첫번째 S 
각각의 함수, 클래스 및 컴포넌트는 한가지의 기능만 수행하도록 개발하는 것

* 단일 책임 원칙이 왜 필요할까 ?
하나의 함수 혹은 클래스가 단 한가지 기능만 수행하도록 개발되어 있다면 사람이 코드를 봤을 때 이해하기 쉽다는 점이 있음 (가독성이 좋음)
만약 함수의 기능에 문제가 발생하여 해당 함수를 수정 할 일이 발생하였을 경우, 한가지 기능만 하기 때문에 유지보수 하기가 쉽다. 

* 단일 책임 원칙에 위배 된다면 어떤 문제가 발생할 수 있을까 ?
함수 또는 클래스가 두 가지 이상의 기능을 가지고 있다면 함수 로직을 파악하는데 그만큼 시간이 걸리게 된다. (가독성이 떨어짐)
한가지 기능만 수행했을 경우에 비해 상대적으로 버그가 발생할 확률이 높아진다. (유지보수가 힘듦)
출처: https://2dubbing.tistory.com/30 [비실이의 개발 성장기]
<Answer>
# N, M 입력
n, m = map(int, input().split())
# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북 동 남 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 엇는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤로 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)
'''
