'''
시뮬레이션(구현)으로 풀기위한 판단 과정, 근거 정리

기본적으로 입력으로 들어오는 치킨집의 개수 범위 생각.
치킨집의 개수 범위는 M <= 치킨집 개수 <= 13
13C_M의 값은 100,000 을 넘지 않는다.
집의 개수 또한 최대 100개 이기 때문에,
각 집에 대해서 모든 조합을 검사해서 최소값을 구해도
시간초과(1초, 2e7)없이 문제를 해결할 수 있다.

Python 조합 라이브러리 기억하기
하지만, 나는 dfs로 다행히 잘 풀었다.
dfs 코드도 까먹지 말기
일단 추가후 한 실행흐름 돌리고,
뺀다음에 한 실행흐름 돌리고 하면 됨.

from itertools import combinations

candidates = list(combinations(chicken, m))
'''
n, m = map(int, input().split())

houses = []
chickens = []
candidates = []

# input값 받아옴
for i in range(1, n+1):
    line = list(map(int, input().split()))
    for j in range(1, n+1):
        if line[j-1] == 1: # ㅈㅣㅂ
            houses.append((i, j))
        elif line[j-1] == 2: # 치킨집
            chickens.append((i, j))

# print(n, m)
# print(houses)
# print(chickens)

# candidates 초기화

def dfs(data, m, idx):
    tmp = []
    for x in data:
        tmp.append(x)
    
    if len(tmp) == m:
        candidates.append(tmp)
        return
    else:
        if idx <= len(chickens) - 1:
            # 일단 추가해서 넣고
            tmp.append(chickens[idx])
            dfs(tmp, m, idx + 1)

            # 빼고 넣고
            tmp.remove(chickens[idx])
            dfs(tmp, m, idx + 1)

dfs([], m, 0)

# print(candidates)

result = int(1e9)

for tmp in candidates:
    sum = 0

    for house in houses:
        min_val = int(1e9)

        for chichi in tmp:
            min_val = min(min_val, abs(house[0]-chichi[0]) + abs(house[1]-chichi[1]))

        sum += min_val
    
    result = min(result, sum)

print(result)
'''
from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c)) # 일반 집
        elif data[c] == 2:
            chicken.append((r, c)) # 치킨 집

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))

# 치킨 거리의 합을 계산하는 함수
def get_sum(candidtate):
    result = 0
    # 모든 집에 대하여
    for hx, hy in house:
        # 가장 가까운 치킨집을 찾기
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx -cx) + abs(hy - cy))
        # 가장 가까운 치킨집까지의 거리를 더하기
        result += temp
    # 치킨 거리의 합 반환
    return result

# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)
'''