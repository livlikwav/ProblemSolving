'''
경로 압축 알고리즘이면 
union에서 그냥 Parent 찾아도 될 거 같긴한데,
그래도 root를 찾는 함수를 쓰도록 하자! (헷갈리지 않게)

7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
>>
NO
NO
YES
'''
N, M = map(int, input().split())
data = []
for _ in range(M):
    data.append(list(map(int, input().split())))

# debug
# print(N, M)
# print(data)

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return a 

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b
    
# parent 초기화
parent = [0] * (N + 1)
for i in range(1, N+1):
    parent[i] = i # 자기 자신으로 초기화

# data 처리
for line in data:
    if line[0] == 0: # Union
        union_parent(parent, line[1], line[2])
    elif line[0] == 1: # Find
        root_a = find_parent(parent, line[1])
        root_b = find_parent(parent, line[2])
        if root_a == root_b:
            print('YES')
        else:
            print('NO')

'''
<Answer>
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속합 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(0, n+1):
    parent[i] = i

# 각 연산을 하나씩 확인
for i in range(m):
    oper, a, b = map(int, input().split())
    # 합집합 union 연산일 경우
    if oper == 0:
        union_parent(parent, a, b)
    # 찾기 연산일 경우
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')
'''