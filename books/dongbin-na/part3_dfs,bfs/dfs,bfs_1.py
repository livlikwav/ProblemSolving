'''
4 4 2 1
1 2
1 3
2 3
2 4

4 3 2 1
1 2
1 3
1 4

4 4 1 1
1 2
1 3
2 3
2 4
'''
from collections import deque

# map starts with 1,1
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    tmp = list(map(int, input().split()))
    graph[tmp[0]].append(tmp[1])

visited = [False] * (N + 1)
distance = [0] * (N + 1)

# debug
# print(N, M, K, X)
# for row in graph:
#     print(row)
# print(visited)
# print(distance)


def bfs(X: int, graph, visited, distance) -> None:
    queue = deque()
    queue.append(X)

    while queue:
        pos = queue.popleft()
        if not visited[pos]:
            visited[pos] = True

            for next in graph[pos]:
                if not visited[next]:
                    if distance[next] == 0:
                        distance[next] = distance[pos] + 1
                    queue.append(next)

bfs(X, graph, visited, distance)

result = [i for i in range(N + 1) if distance[i] == K]

if len(result) == 0:
    print(-1)
else:
    for val in result:
        print(val)

'''
<Lesson Learned>
* BFS할 때는 distance를 겹쳐서 체크하지 않나 잘 체크하기!
같은 노드를 여러 노드가 함께 가리킬 경우,
같은 레벨의 다른 노드가 먼저 해당 노드의 거리를 잘못된 값으로 덮어 씌울 수 있다.

* distance 배열에서도 visited를 겸용 체크함 -1로 초기화하여.
* 시작만 0으로 초기화

* map이 1,1에서 시작하는지 잘 보고, 그러면 N+1로 초기화해야함.

for _ in range(M):
    tmp = list(map(int, input().split()))
    graph[tmp[0]].append(tmp[1])
--> 더 나은 방법
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

<Answer>
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1]*(n+1) # -1로 초기화
distance[x] = 0 # 출발 도시만 0으로 설정

q = deque([x])
while q:
    now = q.popleft()

    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
'''