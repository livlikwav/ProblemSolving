'''
다익스트라 알고리즘 구현을 더 쉽게 했으면, 더 빨리 풀었을 문제였다.
익숙함의 문제. 다익스트라 구현 여러번 해서 몸에 익히기!

1)
distance(result) 배열과 heap 큐 모두,
시작점만 초기화해서 while q: 시작!
2)
이미 처리한 적 있는 노드는 < 이다. (<= 이 아닌)
if distance[x][y] < dist:
    continue
3)
min으로 갱신하는 것이 아닌,
if로 더 작은 경우에만 갱신하고 + 큐에 추가하기. (이렇게 안하면 무한 루프에 빠짐)
'''
import heapq

def dijkstra(n: int, data: list, start: tuple):

    dx = [0, 0, -1, +1]
    dy = [-1, +1, 0, 0]
    INF = int(1e9)

    q = [] # min heap

    # 0,0 에서 각 점 i,j 까지의 거리 배열 초기화
    result = [[INF] * n for _ in range(n)]
    
    # 시작점 초기화
    x, y = start
    result[x][y] = data[x][y]

    # 시작점과 연결된 edge만 초기화
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n: # in map
            result[nx][ny] = data[nx][ny] + data[x][y] # 0,0 비용도 포함되어야함
            heapq.heappush(q, (result[nx][ny], nx, ny))

    # greedy
    while q:
        cost, tx, ty = heapq.heappop(q)

        # 이미 체크된 cost의 경우 continue
        if result[tx][ty] < cost:
            continue

        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if 0 <= nx < n and 0 <= ny < n: # in map
                new = result[tx][ty] + data[nx][ny]

                if new < result[nx][ny]:
                    result[nx][ny] = new
                    heapq.heappush(q, (result[nx][ny], nx, ny))
    
    return result[n-1][n-1]
        
    

t = int(input())

for _ in range(t):
    n = int(input())

    data = []
    
    for _ in range(n):
        line = list(map(int, input().split()))
        data.append(line)

    print('answer', dijkstra(n, data, (0,0)))

'''
참고할 답안 코드 snippets

    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [[INF] * n for _ in range(n)]

    ...

    x, y = 0, 0 # 시작 위치는 (0, 0)
    # 시작 노드로 가기 위한 비용은 (0, 0) 위치의 값으로 설정하여, 큐에 삽입
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    ...

    while q:

        ...

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[x][y] < dist:
            continue

        ...
        

            cost = dist + graph[nx][ny]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧을 경우
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

'''
