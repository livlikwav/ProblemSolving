from collections import deque
n, m, v = map(int, input().split())

data = [[] for _ in range(n + 1)] # 정점의 갯수 + 1만큼 초기화, 정점번호 1~N
for i in range(m):
    start, end = map(int, input().split())

    # 두 정점 사이에 간선 여러개일 수 있지만 일단 다 받는다
    # 양 방향 간선임에 주의
    data[start].append(end)
    data[end].append(start)

# 정점 번호 작은것부터 방문하도록 정렬
for list in data:
    list.sort()

def dfs(x):
    # 방문처리
    visited[x] = True
    result.append(str(x))

    # 깊이 우선 탐색
    for vertex in data[x]:
        if not visited[vertex]:
            dfs(vertex) # recursive

def bfs(x):
    # 시작 번호로 큐 초기화
    queue = deque([x])
    visited[x] = True
    result.append(str(x))

    # 너비 우선 탐색
    while queue:
        now = queue.popleft()
        
        for next in data[now]:
            if not visited[next]:
                queue.append(next)

                # 방문처리
                visited[next] = True
                result.append(str(next))
        
    
# 문제 해결
visited = [False] * (n + 1) # 정점 갯수만큼 초기화
result = []
dfs(v)
print(' '.join(result))

visited = [False] * (n + 1) # 정점 갯수만큼 초기화
result = []
bfs(v)
print(' '.join(result))

