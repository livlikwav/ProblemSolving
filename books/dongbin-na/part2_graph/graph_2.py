'''
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
>>> 8
'''

n, m = map(int, input().split())

parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i # 먼저 자기 자신으로 부모 테이블 초기화


def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

edges = []
costs = []

for x in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(a) != find_parent(b): # 사이클이 발생하지 않으면
        union_parent(a, b)
        costs.append(cost)        
    
# 제일 cost 큰 에지 삭제
costs = costs[:-1] # 맨 마지막 원소 제외한 리스트

# Solution
print(sum(costs))