"""
무방향 그래프에서 사이클 판별 알고리즘 = union-find 사용함
방향 그래프에서 사이클 판별 알고리즘 = dfs 사용함

간선의 개수가 E 개일 때 모든 간선을 하나씩 확인하여, 매 간선에 대해 union 및 find 함수를 호출하는 방식으로 동작한다.
간선에 방향성이 없는 무향 그래프에서만 적용 가능하다.

경로 압축 방법을 적용했을 때,
노드의 개수가 V 개, 최대 V-1개의 union 연산과 M 개의 find 연산이 가능할 때,
TC O(V + M(1 + log_(2-M/V)V))
"""
"""
서로소 집합 disjoint sets = 공통 원소가 없는 두 집합
서로소 집합 자료구조는 tree 로 표현한다.
두 노드가 tree 내에서 루트 노드가 같으면, 같은 tree 에 위치하고, 같은 집합으로 간주한다.

서로소 집합 자료구조는 union-find 자료구조라고 불리기도 한다. 합집합과 찾기 연산으로 구성된다.
union = 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
find = 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산
"""


# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])  # 최적화 경로 압축 적용함
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선(union 연산) 의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

cycle = False  # 사이클 발생 여부

for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 합집합(union) 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클 발생")
else:
    print("사이클 발생 X")
"""
비 효율적인 find 연산 구현 (루트 노드 테이블 선형 탐색)
"""


def find_parent_slow(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])  # parent[x] 를 업데이트, 즉 경로 압축을 해주지 않고 있다.
    return x
