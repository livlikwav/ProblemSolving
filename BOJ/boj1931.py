'''
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
'''

n = int(input())
data = []
for _ in range(n):
    line = list(map(int, input().split()))
    data.append(line)
data.sort()

# debug
# print(n)
# print(data)

x = -1
y = -1
nx = -1
ny = -1
cnt = 0
for i in range(n):
    nx, ny = data[i]
    
    if nx > y:
        cnt += 1
        x = nx
        y = ny
    else:
        if ny < y:
            x = nx
            y = ny
        else:
            pass

print(cnt)
