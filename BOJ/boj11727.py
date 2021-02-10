'''
자꾸 dp에서 index error를 겪는다.
빨리 풀려다보니..
경곗값 테스트를 잘하자!!!
'''
n = int(input())

dp = [0] * n
if n == 1:
    print(1)
else:
    dp[0] = 1
    dp[1] = 3

    for i in range(2, n):
        dp[i] = dp[i-2]*2 + dp[i-1]

    print(dp[n-1] % 10007)