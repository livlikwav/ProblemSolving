N = int(input())
data = [input().split() for _ in range(N)]
new_data = [(val[0], int(val[1])) for val in data]

# debug
# print(N)
# print(data)
print(new_data)

def get_score(new_data: tuple):
    return new_data[1]

new_data.sort(key=get_score)

for val in new_data:
    print(val[0], end=' ')

'''
<Lesson learned>
나처럼 리스트를 두개 사용해서 인풋을 받는게 아닌,
일반 프로그래밍 언어처럼 할 수도 이이어ㅆ다.

lambda 함수 문법
함수 이름: 리턴값

<Answer>
n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')
'''
