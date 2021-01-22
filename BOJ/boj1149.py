'''
O(3N)
3000번 정도?
0.5초 무조건 가능

3
26 40 83
49 60 57
13 89 99
>> 96
'''
n = int(input())
dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))

# debug
# print(n, dp)

for i in range(1, n):
    # RED
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]
    # BLUE
    dp[i][1] = min(dp[i-1][2], dp[i-1][0]) + dp[i][1]
    # GREEN
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + dp[i][2]

print(min(dp[n-1]))




'''
그냥 바로 dp 테이블 갱신

마지막 RGB에 각각
최소값을 갱신한다고 생각해보면

R은
R은 min( n-1의 G와 B 중에서)랑 + R

이런식으로 RGB 각각 갱신해서
마지막 줄 min값 출력한다.
'''