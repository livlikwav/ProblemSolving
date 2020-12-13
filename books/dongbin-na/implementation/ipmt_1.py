import sys

def myinput():
    return sys.stdin.readline()

N = int(myinput())
data = myinput().split()


dict = {
    'L' : [0, -1],
    'R' : [0, +1],
    'U' : [-1, 0],
    'D' : [+1, 0],
}

start = [1, 1]
for cmd in data:
    next = [start[i] + dict[cmd][i] for i in range(2)]
    # print(f'next is {next}')
    if next[0] >= 1 and next[1] >= 1:
        start = next
        # print(f'start is {start}')
    else: # out of map
        pass
        # print(f'start is {start}')

print(start)

'''
<Lesson learned>
list 길이 구하기 len(list)
size()나 length 같은거 아니다!

list 각 요소간의 합은 list comprehension 사용
list + list는 리스트 확장이다.

python의 비교 연산자는 &&이 아니라 and 이다

<Answer>
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
'''
