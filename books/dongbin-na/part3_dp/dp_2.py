'''
[조심할 것]
2중 리스트가 정사각형이 아니라,
직각삼각형이라서 loop시 조심!

0 <= y < n이 아니라
0 <= y <= x - 1인게 포인트!

또한 이 문제는 dp 테이블 별도 선언하지 않아도 된다!
하지만, 늘 그런건 아니지 주의하자!
'''

n = int(input())
data = []

for i in range(n):
    data.append(list(map(int,input().split())))

# debug
# print(n)
# print(data)

for x in range(0, n):
    for y in range(0, x+1): #0,0 1,0 1,1 2,0 2,1 2,2 ...
        if x == 0:
            pass
        else: # until x == n-1
            tmp1 = -1
            nx = x - 1
            ny = y - 1
            if 0 <= nx < n and 0 <= ny <= x-1: # in map
                tmp1 = data[nx][ny]

            tmp2 = -1
            nx = x - 1
            ny = y
            if 0 <= nx < n and 0 <= ny <= x-1: # in map
                tmp2 = data[nx][ny]

            data[x][y] = data[x][y] + max(tmp1, tmp2)

print(max(data[n-1])) # 마지막 줄의 max값을 리턴한다
'''
답에서 참고할 점은!
나와 다르게 list 체크를 했다!

처음보는 사람이 보기에
좀더 의미가 잘 해석될 듯 하다.
참고하기!

<Answer>
n = int(input())
dp = [] # 다이나믹 프로그래밍을 위한 DP 테이블 초기화

for _ in range(n):
    dp.append(list(map(int, input().split())))

# 다이나믹 프로그래밍으로 두 번째 줄부터 내려가면서 확인
for i in range(1, n):
    for j in range(i + 1):
        # 왼쪽 위에서 내려오는 경우
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i-1][j-1]
        # 바로 위에서 내려오는 경우
        if j == i:
            up = 0
        else:
            up = dp[i-1][j]
        # 최대 합을 저장
        dp[i][j] = dp[i][j] + max(up_left, up)

print(max(dp[n - 1]))
'''