'''
정말 쉽게 풀었어야하는데, 또 구현과정에서 실수로 시간이 오래걸렸다.
dis, pos 위치를 바꿔서 그렇다.
차라리 주석으로 실수하지 않게 체크를 하자!

다익스트라로 최단 거리 테이블을 구한 이후에는 손쉽게 문제에서 요구하는 답을 구할 수 있는 문제였다.
문제에서의 거리가 1이기 때문에 BFS를 이용해서 최단거리를 계산할 수도 있다.

답안 코드와 거의 동일하게 풀었다.
'''

import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)] # 1번 ~ N번 사용

for _ in range(m):
    start, end = map(int, input().split())

    # undirected
    graph[start].append(end)
    graph[end].append(start)

INF = int(1e9)
result = [INF] * (n + 1)

# 시작점 초기화
result[1] = 0
q = []
heapq.heappush(q, (result[1], 1))

# dijkstra
while q:
    dis, pos = heapq.heappop(q)

    if result[pos] < dis:
        continue

    for next in graph[pos]:
        if dis + 1 < result[next]:
            result[next] = dis + 1
            heapq.heappush(q, (result[next], next))

# Solution
answer = []
max = -1
for pos in range(1, n + 1):
    dis = result[pos]

    if dis > max:
        max = dis
        answer = [pos]
    elif dis == max:
        answer.append(pos)
    else:
        pass

print(min(answer), max, len(answer))
        