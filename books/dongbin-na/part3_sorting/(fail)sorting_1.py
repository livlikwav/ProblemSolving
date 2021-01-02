'''
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
'''
N = int(input())
data = [input().split() for _ in range(N)]

# debug
print(N)
print(data)

def get_a1(array):
    result = []
    a1 = [[]*101]
    for i in range(len(array)):
        a1[array[i][1]].append(array[i])
    for i in range(101):
        if len(a1[i]) == 1:
            result.append(a1[i][0])
        elif len(a1[i]) >= 2:
            vals = get_a2(a1[i])
            for val in vals:
                result.append(val)
    return result

def get_a2(array):
    result = []
    a2 = [[]*101]
    for i in range(len(array)):
        a2[array[i][2]].append(array[i])
    for i in range(101):
        if len(a2[i]) == 1:
            result.append(a2[i][0])
        elif len(a2[i]) >= 2:
            vals = get_a3(a2[i])
            for val in vals:
                result.append(val)
    return result

def get_a3(array):
    result = []
    a3 = [[]*101]
    for i in range(len(array)):
        a3[array[i][3]].append(array[i])
    for i in range(101):
        if len(a3[i]) == 1:
            result.append(a3[i][0])
        elif len(a3[i]) >= 2:
            temp = []
            for x in a3[i]:
                temp.append(a3[i][0])
            temp.sort() # 사전 순이 증가하는 순서
            for val in temp:
                result.append(temp)
    return result

result = get_a1(data)
print(''.join(result))

'''
n = int(input())
students = []

# 모든 학생 정보를 입력받기
for _ in range(n):
    students.append(input().split())

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 정렬된 학생 정보에서 이름만 출력
for student in students:
    print(student[0])
'''