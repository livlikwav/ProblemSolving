import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a 번 노드에서 b 번 노드로 가는 비용이 c 라는 의미
    graph[a].append((b, c))


"""
개선된 다익스트라 알고리즘 TC O(ElogV) E 는 edge, V 는 Vertex(Node)
Heap 자료구조를 사용한다. heap 은 삽입 logN, 삭제 logN 이다. python 의 heapq 는 min heap 이다.
대부분의 프로그래밍 언어에서는 PriorityQueue 라이브러리에 데이터 묶음을 넣으면, 첫 번째 원소를 기준으로 우선순위를 설정한다.

다익스트라 알고리즘은 Greedy 알고리즘의 일부로 볼 수 있다.
목표: 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘
조건: '음의 간선' 이 없을 때 정상적으로 동작한다. (음의 간선이 있으면, visited 최단 거리가 최소라는 논리가 깨진다.)

'각 노드에 대한 현재까지의 최단 거리' 정보를 항상 1차원 리스트에 저장하여 리스트를 계속 갱신한다는 특징이 있다.

코드 상의 테크닉
1) 리스트 N+1 개로 선언하여, 노드 번호 그대로 사용
2) INF=int(1e9) 로 연결되지 않은 간선을 무한 값으로 표현
"""


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0 으로 설정하며, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if (
            distance[now] < dist
        ):  ##### 이게 dijkstra 가 greedy 라서 가능한 논리이다. visited 노드의 최단 거리는 이미 결정된거기 때문에 바뀌지 않는다.
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])

"""
heap 을 사용하지 않고, 리스트 선형 탐색을 통해 다음 최단 거리 노드를 찾는 로직도 있는데,
이는 TC O(V^2) 이다. 그래서 굳이 알 필요는 없을 것 같다.
"""
