'''
<풀이 메모>
다행히 ㅎㅎ 답안과 정확히 동일한 접근법으로 문제 해결함.

1) 학생들의 성적을 비교한 결과를 방향 그래프 형태로 표현가능
2) A에서 B로, 또는 B에서 A로 도달이 가능하면 성적비교가 가능한 것이다.
3) 자기 자신을 뺀 다른 모든 노드와 도달이 가능하면 정확한 순위를 알 수 있다.
'''
n, m = map(int, input().split())
INF = int(1e9)

data = [[INF] * (n+1) for _ in range(n+1)] # index 1,1 start
for _ in range(m):
    start, end = map(int, input().split())
    data[start][end] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                data[i][j] = min(data[i][j], data[i][k] + data[k][j])

# 순위 계산할 수 있는 학생 계산
result = 0
# incoming + outgoing = N-1일 경우 가능함
for i in range(1, n+1):
    # incoming link 계산
    incoming = 0
    for x in range(1, n+1):
        if data[x][i] != INF:
            incoming += 1
    # outgoing link 계산
    outgoing = 0
    for x in range(1, n+1):
        if data[i][x] != INF:
            outgoing += 1
    # 순위 계산 체크
    if incoming + outgoing == n - 1:
        result += 1

print(result)
'''
# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

답안에서는 자기자신 cost를 0으로 초기화했다.
나는 0으로 초기화 안하고 -> a,b가 같은 경우를 제외하는 방식으로 구현했다.
'''