'''
N은1이상 1,000,000이하이다.
자리수를 더한 값이 최고 54이다.
999,999 -> 9 * 6 = 54
'''

n = int(input())

# debug
# print(n)

def compute(x):
    sum = x
    
    while x != 0:
        sum += x % 10
        x = x // 10

    return sum

flag = False
for x in range(n-60, n):
    val = compute(x)

    # debug
    # print(x, val)

    if val == n:
        print(x)
        flag = True
        break

if not flag:
    print(0)
