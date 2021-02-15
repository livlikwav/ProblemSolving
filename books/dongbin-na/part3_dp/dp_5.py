'''
<dp 풀이 인사이트>
dp를 1차원 arr를 채워가는 것이라고 생각하면,
어려운 dp를 풀기 어렵다.
이전 문제인 LIS(Longest Increasing Sequence, 매번 반복 비교하며 갱신),
다음 문제인 편집 거리(Edit distance, 2차원 dp 배열) 등
부분 문제를 재활용하는 것에 집중하되, 1차원 배열 풀이 방식에 사로잡혀있으면 안된다.

<풀이 메모>
dp는 결국 최적 부분 구조 문제에 유용한 풀이 패러다임이고,
한번 푼 문제를 반복해서 풀지 않도록 기억하며 푸는 문제이다.

따라서, 이 문제에서는 결국 못생긴 수 끼리만 곱해야하고,
제일 작은 못생긴 수 부터 차례로 2, 3, 5를 곱하면 된다.

결론적으로 dp table은 이전 못생긴 수를 다시 계산하지 않도록 쌓는 table이다.

<메모>
Dynamic programming의 이름의 유래가 뭔지 또 다시 찾아봤다.
하지만 Dynamic과 Programming이라는 단어의, 일반적인 컴퓨터 과학에서의 의미와는 전혀 달랐다.
이는 1940년에 만든 사람의 특수한 상황에서 지어진 이름이기 때문이다.

오히려 다음과 같이 기억하는 것이 훨씬 편하다.
1. 기억하며 풀기
2. 한번 푼 문제 다시 풀지 않기
3. 부분 문제 결과 재활용하기

부분 문제 반복과 최적 부분 구조를 가지고 있는 문제에 적합한 문제해결 패러다임이다.
'''
n = int(input())

dp = [0] * 1000
dp[0] = 1

i2 = 0
i3 = 0
i5 = 0

val = 1

next_i2 = dp[i2] * 2
next_i3 = dp[i3] * 3
next_i5 = dp[i5] * 5

for i in range(1, n):
    val = min(next_i2, next_i3, next_i5)
    dp[i] = val

    # 이렇게 if-elif-elif가 아닌 if-if-if로 선언함으로써 중복을 방지한다
    # 만약 2*3, 3*2 같이 6을 가르키는 값이 두개여도 넣는거는 하나뿐.
    if val == next_i2:
        i2 += 1
        next_i2 = dp[i2] * 2
    if val == next_i3:
        i3 += 1
        next_i3 = dp[i3] * 3
    if val == next_i5:
        i5 += 1
        next_i5 = dp[i5] * 5

print(dp[n-1])