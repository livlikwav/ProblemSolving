'''
i->i 인 경우를 INF에서 0으로 변경하도록 초기화한다면,
a->b에서 a와 b가 같은 경우도 정상 동작한다.

또는 INF로 그대로 진행한다면, 내 답안과 같이 a == b인 경우는 배제해야한다.

python에서 줄바꿈없이 프린트하려면, print()에 end='<특정문자>' argument를 주면된다. (default='\n')
'''
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)
data = [[INF] * (n + 1) for _ in range(n+1)] 

for _ in range(m):
    start, end, cost = map(int, input().split())

    # 새로운 노선 비용이 더 작을 경우 비용 갱신
    if cost < data[start][end]:
        data[start][end] = cost

# 플로이더 워셜 -> dp 0, 1, 1~2, 1~3 ... 0~N 거치는 경우 중 최단거리
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b:
                continue

            data[a][b] = min(data[a][b], data[a][k] + data[k][b])

for line in data[1:]:
    for val in line[1:]:
        if val == INF:
            print('0', end=' ')
        else:
            print(val, end=' ')
    print() # new line
'''
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end=' ')
        else:
            print(graph[a][b], end =' ')
    print()

이렇게 구현하는 것이 더 속도가 빨랐을 것 같다.
나는 List slicing하는 비용이 소비됨.
'''