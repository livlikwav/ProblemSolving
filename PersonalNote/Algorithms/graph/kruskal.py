# kruskal is greedy algorithm for find MST(Minumum Spanning Tree)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0

for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# edge 를 min cost 부터 오름차순으로 정렬함
edges.sort()

for edge in edges:
    cost, a, b = edge

    # 부모 노드가 같다 = 같은 그룹에 있다 = Cycle 이 생긴다
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
