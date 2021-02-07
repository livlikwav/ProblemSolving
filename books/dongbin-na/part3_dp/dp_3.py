n = int(input())
t = [0]
p = [0]
for _ in range(n):
    line = list(map(int, input().split()))
    t.append(line[0])
    p.append(line[1])

# print(n)
# print(t)
# print(p)

dp = [0] * (n + 1)
max_val = 0
for i in range(n, 0, -1):
    # 딱 맞게 끝난다면
    if (i + t[i] - 1) == n:
        dp[i] = max(max_val, p[i])
        max_val = dp[i]
    # i 위치에서 상담이 가능하다면
    elif (i + t[i] - 1) < n:
        dp[i] = max(max_val, p[i] + dp[i + t[i]])
        max_val = dp[i]
    # 불가능 하다면
    else:
        dp[i] = max_val

# print(dp)
print(dp[1])
'''
<답안과 다른점>
분명 아예 동일한 접근 방법이었는데, 왜 if문 분기에서 계속 해맸을까?
답에서 time이 n이면 index error 나지 않나? -> 채점해보니 그러지 않았다.

이 차이는 나는 3개의 배열을 모두 n+1 길이로 초기화했고,
얘는 dp만 n+1, t와p는 n으로 했기 때문이다.
<Answer>
n = int(input())
t = []
p = []
dp = [0] * (n + 1)
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n - 1, -1, -1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)
'''