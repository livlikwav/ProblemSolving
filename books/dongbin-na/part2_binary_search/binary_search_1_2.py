N = int(input())
array = [0] * (int(1e6) + 1)
data = list(map(int, input().split()))
for val in data:
    array[val] = 1

M = int(input())
targets = list(map(int, input().split()))

# Solution
for target in targets:
    if array[target] == 1:
        print('yes')
    else:
        print('no')