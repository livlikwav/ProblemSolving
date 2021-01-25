'''
5 3
0 0 1 0 0 
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2
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