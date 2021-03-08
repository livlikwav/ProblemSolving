import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

# debug
# print(n, k)
# print(data)

# python recursion limit default: 1000
# k가 10000이고 data에 1이 포함되어 있으면 limit 초과 가능하므로
# stack을 사용한다
stack = []
answer = 0
    
def dfs(sum, idx):
    global answer

    if sum > k:
        return
    
    if sum == k:
        answer += 1
        return
    
    # 자기 자신부터 마지막 idx까지 한번씩 다 시도
    for next in range(idx, n):
        stack.append((sum + data[next], next))

# solution
stack.append((0, 0))

while stack:
    sum, idx = stack.pop()
    dfs(sum, idx)

print(answer)

