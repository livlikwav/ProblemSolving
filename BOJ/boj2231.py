n = int(input())

def compute(x):
    sum = x

    while x > 0:
        sum += x % 10
        x = x // 10

    return sum

# debug
# print(compute(n))

isValid = False
if n < 60:
    for i in range(1, n):
        val = compute(i)

        if val == n:
            isValid = True
            print(i)
            break
else:
    for i in range(n - 60, n):
        val = compute(i)

        if val == n:
            isValid = True
            print(i)
            break

if not isValid:
    print(0)
