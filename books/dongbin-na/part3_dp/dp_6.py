A = input()
B = input()

lenx = len(A) + 1
leny = len(B) + 1

dp = [[0] * leny for _ in range(lenx)]

for i in range(1, lenx):
    dp[i][0] = i
for i in range(1, leny):
    dp[0][i] = i

# debug
# print(A, B)
# print(dp)
# print(A[1], B[1])

for i in range(1, lenx):
    for j in range(1, leny):
        val = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

        if A[i-1] == B[j-1]: # 같은 글자이면
            dp[i][j] = val
        else:
            dp[i][j] = val + 1

# debug
# for line in dp:
    # print(line)

print(dp[lenx-1][leny-1])