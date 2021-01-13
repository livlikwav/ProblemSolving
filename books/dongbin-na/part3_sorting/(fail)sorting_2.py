'''
첫번째 시도 : 시간 초과
두번째 시도 : 중간값이 최소가 된다는 것이 확실하지 않다가 문제 풀이 시간 초과

4
5 1 7 9
>> 5
'''
n = int(input())
data = list(map(int, input().split()))

data.sort()

INF = int(1e9)
min_val = INF
min_house = INF


for x in data:
    tmp_val = 0
    for i in data:
        if i == x:
            continue
        tmp_val += abs(i - x)

    if min_val > tmp_val:
        min_val = tmp_val
        min_house = x

print(min_house)
'''
실제로 종이에 그려가며 생각해보면,
항상 성립한다는 점을 떠올릴 수 있을 것이다 ...
--> 20분 내에 못풀었지만, 이거를 잘 생각해보기.

<Answer>
n = int(input())
data = list(map(int, input().split()))
data.sort()

# 중간값 (medium)을 출력
print(data[(n - 1) // 2])
'''