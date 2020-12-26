'''
틀린 답.
greedy 근거에 대한 검증이 모자랐다

26에 경우 -1, //5, //5가 최선
지금은 /3, -1, /3, /3 ... 이런식으로 풀게 된다.
'''

x = int(input())
d = [0] * (30000 + 1)
# d[1] = 0, d[0] = 0

# debug
# print(x)
# print(len(d))

for i in range(2, x+1): # 2 ~ x
    if i % 5 == 0:
        d[i] = d[i//5] + 1
    elif i % 3 == 0:
        d[i] = d[i//3] + 1
    elif i % 2 == 0:
        d[i] = d[i//2] + 1
    else: # finally
        d[i] = d[i-1] + 1

# Solution
print(d[x])