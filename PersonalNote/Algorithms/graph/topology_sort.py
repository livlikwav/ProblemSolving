"""
위상 정렬
이 코드는 그래프에 사이클이 없음을 가정한다.
진입 차수 0 인 노드부터 큐에 넣고, 하나씩 빼면서 새로 진입차수 0 이 되는 애들을 큐에 넣는다.
사이클이 있는 경우에 진입차수가 0 이 되는 것이 불가능하다. = 서로 가리키고 있기 때문에 먼저 0 이 되는 애가 없기 때문이다.

TC O(V+E), 모든 노드를 차례차례 확인하며, 각 노드에서 모든 간선을 하나씩 확인해야한다.
"""
from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v + 1)
graph = [[] for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    result = []
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

        while q:
            now = q.popleft()
            result.append(now)

            for i in graph[now]:
                indegree[i] -= 1

                if indegree[i] == 0:
                    q.append(i)

    for i in result:
        print(i, end=" ")


topology_sort()
