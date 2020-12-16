dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8
}

move_types = [
    [-2, -1],
    [-2, +1],
    [-1, +2],
    [+1, +2],
    [+2, +1],
    [+2, -1],
    [+1, -2],
    [-1, -2]
]

data = input()
x = dict[data[0]]
y = int(data[1])
pos = [x, y]
# print(pos)

count = 0
for move in move_types:
    next = [pos[i] + move[i] for i in range(2)]
    if(next[0] >= 1 and next[1] >= 1 and next[0] <= 8 and next[1] <= 8):
        count += 1
        print(next)
print(count)

'''
<Lesson learned>
답안 제출 전에 테스트를 엄격하게 잘 수행하기. 특히 경곗값 테스트
이번 문제 틀릴뻔함. <= 8 조건을 검사하지 않아서.
다행히 내기 전에 입력값 넣어보다가 발견함.

ord(char) 유니코드 정수 반환
chr(int) 유니코드 문자 반환

<Answer>
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
'''
