'''
boj11404

<풀이 메모>
문제를 풀면서 플로이드 워셜 알고리즘에 대해서 의문이 들었다.
하나의 Vertex K에 대해서, K를 지나가는 서로다른 A,B 쌍에 대해서 갱신하는 것이다.
그런데 이 K와 A, B 를 정하는 순서에 따라서 최적이 아닌 값으로 갱신될 수 있지 않나? 가 의문이었다.

이건 내가 Floyd-Warshall Algorithm을 잘못 이해하고 있었기 때문이다.
모든 Edge를 체크하기 때문에 성립한다 -> X
모든 Edge의 경우인 A, B에 대해서 임의의 K를 거쳐가는 경우를 체크한다 -> X
1~ N까지 모든 Vertex를 경유지로 하는 Edge의 경우를 체크한다 -> X

핵심은
1) 플로이드 워셜은 DP 알고리즘이다. Greedy가 아니다.
2) Shortest_Path(u, v, k)는 1부터 k까지의 순차적인 Vertex를 경유하는 경우 중 최단거리를 의미한다. 딱 k만을 경유하는 최단거리가 아니다.

따라서,
Shortest_Path(u, v, 0) = w(u, v) 이다. 아무 Vertex도 경유하지 않는 거리이므로.

그래서 구현 방법이 1부터 k까지 차례로 검사하는 것이 아니라,
공집합 -> {1} -> {1, 2} -> {1, 2, 3} -> ... -> {1 ~ k} 까지 검사하는 것이고,
이는 subproblems을 반복적으로 수행하며, 쌓아가는 형태이므로 DP이다!

또한, 같은 이유로
1)
for k -> for a -> for b 의 순서가 중요하고
2)
k는 for i in {1, 2, 3, ... N}으로 순서가 중요하지만,
a나 b는 순서가 중요하지 않다 for a in V 와 같이.
3)
그리고 자기 자신으로 가는 비용이 0으로 초기화 되어 있어야
k -> a -> b에서 그대로 돌려도 잘못 초기화되지 않는다.
또는 a와 b가 다른 경우만 처리하도록 구현해야한다.

INF로 초기화되어 있으면 a==b, k인 경우에 a->b = INF, a->k + k->b = !INF 일 수 있으므로 잘못 계산될 수 있다.

두 링크가 도움이 됐다.
https://www.youtube.com/watch?v=NzgFUwOaoIw&ab_channel=MITOpenCourseWare (mit 강의)
https://ko.wikipedia.org/wiki/%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%9B%8C%EC%85%9C_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98 (위키피디아)
'''

n = int(input())
m = int(input())

INF = int(1e9)
data = [[INF] * (n + 1) for _ in range(n+1)] # 나중에 출력시에는 1,1 부터 출력하기

for _ in range(m):
    start, end, cost = map(int, input().split())
    data[start][end] = min(data[start][end], cost)

# debug
# print(n, m)
# for i in range(1, n+1):
#     print(data[i][1:])

# d_ab = min(d_ab, d_ak + d_kb)
for a in range(1, n+1):
    for b in range(1, n+1):
        for k in range(1, n+1):
            if a != b:
                data[a][b] = min(data[a][b], data[a][k] + data[k][b])

# INF 값 0으로 변환
for i in range(1, n+1):
    for j in range(1, n+1):
        if data[i][j] == INF:
            data[i][j] = 0

# 결과 출력
for i in range(1, n+1):
    print(' '.join(list(map(str, data[i][1:]))))
    # print(data[i][1:])
