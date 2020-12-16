N = int(input())

hh = 0
mm = 0
ss = 0

count = 0
while not(hh == N and mm == 59 and ss == 59):
    # tic toc
    ss += 1
    if ss == 60:
        ss = 0
        mm += 1
    if mm == 60:
        mm = 0
        hh += 1
    # print(f'{hh}:{mm}:{ss}')
    # count
    if '3' in str(hh):
        count += 1
        continue
    if '3' in str(mm):
        count += 1
        continue
    if '3' in str(ss):
        count += 1
        continue

print(count)

'''
<Lesson learned>
완전 탐색의 경우, 대부분 시간 복잡도가 좋지 않다.
따라서 전체 데이터의 개수가 100만 개 이하일때 사용해야 적절하다.

파이썬에서 시간 나타내는 것 저렇게 3중 for문으로 쉽다.

숫자 자리수마다 비교하는것. 파이썬에서는 str로 바꿔서 in 쓰면 쉽다.

<Answer>
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
'''