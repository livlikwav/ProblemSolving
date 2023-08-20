"""
하면서 Python 관련 궁금했던거 찾아봄
string literal 선언 시 작은따옴표(')와 큰따옴표(")사이에 차이는 없다.
하지만, 문자열의 시작과 끝에 같은 종류의 따옴표를 사용해야 한다.
"""
import sys

### input
M, N, K = map(int, sys.stdin.readline().strip().split())

hidden = list(map(int, sys.stdin.readline().strip().split()))

user_input = list(map(int, sys.stdin.readline().strip().split()))

# print(M, N, K)
# print(hidden)
# print(user_input)

### solution
# hidden is subarray of user input array ? secret : normal
isSecret = False

if M <= N:
    for i in range(N):
        if user_input[i] == hidden[0]:
            j = i + M - 1
            if j < N and user_input[i : j + 1] == hidden:
                isSecret = True
                break

if isSecret:
    print("secret")
else:
    print("normal")
