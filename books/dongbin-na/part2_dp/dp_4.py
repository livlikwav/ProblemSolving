'''
2 15
2
3

3 4
3
5
7

3 7
2
3
5
'''
n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))
data.sort()

d = [0] * (m+1)

d[0] = 0
for i in range(1, m+1): # 1 ~ m
    array = []
    for x in data: # 모든 화폐 단위에 대해서 검사
        if i - x >= 0: # 화폐 사용이 가능할때
            if d[i-x] >= 0: # -1이면 안넣음
                array.append(d[i-x])
    # 최소 1번은 가능한지 검사
    if len(array) == 0: # 다 -1이면 다음 행동 불가능
        d[i] = -1
        # print(f'{i}: -1, {array}')
    else:
        d[i] = min(array) + 1
        # print(f'{i}: {d[i]}, {array}')

print(d[m])

'''
n, m = map(int, input().split())
# N개의 화폐 단위 정보를 입력받기
array = []
for i in range(n):
    array.append(int(input()))
# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)
# DP bottom-up
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1 ):
        if d[j - array[i]] != 10001: # i-k원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)
# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else: 
    print(d[m])
'''