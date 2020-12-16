'''
* 오름차순이 이므로 max를 체크할 필요가 없다.
'''
N = int(input())
data = list(map(int, input().split()))
data.sort()

# debug
print(N)
print(data)

result = 0
max = 0
count = 0

for num in data:
    if max == 0:
        max = num
    elif max < num:
        max = num

    count += 1

    if max == count:
        result += 1
        max = 0
        count = 0

print(result)
    
'''
5
2 3 1 2 2 

10  
1 2 3 4 3 2 1 2 5 7

20
1 1 1 2 2 2 3 3 3 3 4 4 4 4 4 4 5 5 5 6
'''

'''
<Answer>
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data:
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result) # 총 그룹의 수 출력 
'''