'''
3 2 1
1 2 4
1 3 2
>> 2 4

[문제 잘 읽기 ... ㅜㅜ]
큰 실수할 뻔!
이 문제에서 총 소요시간은 sum이 아니라 max
왜냐면 신호는 각 도시로 브로드캐스트로 쏘기 때문에.
critical path의 소요시간인 max값
'''

import heapq
import sys
input = sys.stdin.readline

n, m, c = map(int, input().split())

INF = int(1e9)
distance = [INF for _ in range(n+1)]
# print(distance)

graph = [[] for _ in range(n+1)]
for _ in range(m):
    X, Y, Z = map(int, input().split()) # 출발 도시, 향하는 도시, 소요 시간
    graph[X].append((Z, Y)) # (소요시간, 향하는 도시 번호)

def dijkstra(start: int) -> None:
    '''
    :Param: 출발 도시 번호
    '''
    q = []
    # init start city
    distance[start] = 0
    heapq.heappush(q, (0, start))
    for i in graph[start]:
        distance[i[1]] = i[0] # (0, 1) = (소요시간, 향하는 도시 번호)
    # 출발 도시를 제외한 N-1 도시에 대해서 최단 거리 갱신
    while q:
        dist, now = heapq.heappop(q)
        # 갱신되었던 노드는 제외
        if distance[now] < dist:
            continue
        # 해당 노드의 간선들을 모두 확인
        for j in graph[now]:
            val, dest = j
            if distance[dest] > distance[now] + val:
                # 갱신
                distance[dest] = distance[now] + val
                heapq.heappush(q, (distance[dest], dest))

# Solution
dijkstra(c)

max_val = 0
count = 0
for k in range(n+1):
    if distance[k] != INF and distance[k] != 0: # 도달 불가능이거나, 출발 도시는 제외
        max_val = max(max_val, distance[k])
        count += 1
# answer
print(count, max_val)
'''
<Answer>
답은 거의 동일해서 적지 않았다.
'''