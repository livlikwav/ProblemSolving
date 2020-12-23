'''
5
8 3 7 9 2
3 
5 7 9
'''
import sys
import time

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
data = list(map(int, input().split()))
M = int(input())
target = list(map(int, input().split()))

data.sort()


# debug
# print(N)
# print(data)
# print(M)
# print(target)

def binary_search(data, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if data[mid] == target:
        return mid
    elif data[mid] < target: # right
        return binary_search(data, target, mid + 1, end)
    else: # left
        return binary_search(data, target, start, mid - 1)

start_time = time.time()

# Solution
for i in target:
    if binary_search(data, i, 0, N-1): # Not None
        print('yes')
    else:
        print('no')

end_time = time.time()
print('time: ', end_time-start_time)