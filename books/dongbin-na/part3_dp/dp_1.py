'''
답안과 동일한 방법으로 풀었다.
DP 문제푸는 요령을 익힌듯 하다.

반복되는 부분문제를 생각해야한다.
쉽게 생각하는 방법은 점화식이 두 항, 또는 n 항 간의 관계임을 기억하고,
f(N)을 만들기 위한 f(N - 1)이 경우가 딱 나뉘어 떨어지는지 본다.
그리고 max(), min()이 잘 사용됨을 기억

<실수한 부분>
2중 for문에서 한 행마다 loop하는 것이 아니라,
한 열마다 loop하는 경우에
for j in range(m):
    for i in range(n):
이렇게 해야함!
'''
t = int(input())
# print(t)

def dp():
    n, m = map(int, input().split())
    data = [[0] * m for _ in range(n)]

    line = list(map(int, input().split()))
    for i in range(n):
        for j in range(m):
            data[i][j] = line[i*m + j]
    
    # print(n, m)
    # print(data)

    dp_table = [[0] * m for _ in range(n)]

    # print(dp_table)

    for j in range(m):
        for i in range(n):
            if j == 0: # 첫번째 열일 경우
                dp_table[i][j] = data[i][j]
            else: # 그 외에는 점화식 적용
                # 그대로 옆으로 가는건 무조건 가능
                max_val = dp_table[i][j - 1]
                if (i - 1) >= 0:
                    max_val = max(max_val, dp_table[i-1][j-1])
                if (i + 1) < n:
                    max_val = max(max_val, dp_table[i+1][j-1])
                # 최대값과 현재 위치값 더하면 곧, 현재 위치의 최대값
                dp_table[i][j] = data[i][j] + max_val
    
    # 마지막 열에서 최대값을 찾는다
    result = dp_table[0][m - 1] # 첫번째 값으로 초기화
    for i in range(1, n):
        result = max(result, dp_table[i][m - 1])
    print('답', result)

    # debug
    # for i in range(n):
    #     print(dp_table[i])
# Solution
for _ in range(t):
    dp()

'''
답안과 완전 동일한 아이디어로 풀었다.
2차원 테이블을 이용한 다이나믹 프로그래밍으로 해결

금광의 모든 위치에 대하여, 3가지 경우만 존재한다.
각 위치마다 가장 많은 금 값을 저장하면서 bottom-up

점화식
dp[i][j] = array[i][j] + max(dp[i - 1][j - 1] + dp[i][j - 1] + dp[i + 1][j - 1])

단, dp 테이블에 접근할 때마다 리스트의 범위를 벗어나지 않는지 체크할 필요가 있다.

Trick
이 문제의 경우에는 array, dp 별도로 선언하지 않고,
array에다가 그대로 업데이트해도 된다.


<Answer>
# 테스트 케이스 Test Case 입력
for tc in range(int(input())):
    # 금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m
    
    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result)
'''