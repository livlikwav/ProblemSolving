N = int(input())
data = set(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

for target in targets:
    if target in data:
        print('yes')
    else:
        print('no')