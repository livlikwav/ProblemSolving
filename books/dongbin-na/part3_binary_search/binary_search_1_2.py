'''
7 2
1 1 2 2 2 2 3
>> 4

7 4
1 1 2 2 2 2 3
>> -1

7 1
1 1 2 2 2 2 3
>> 2
'''
def bs_first(data, target):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2

        # if (mid == 0 or data[mid - 1] < target) and data[mid] == target:
        #     return mid
        if data[mid] == target:
            if mid == 0 or data[mid - 1] < target:
                return mid
            else: # go left
                end = mid - 1
        elif data[mid] < target: # go right
            start = mid + 1
        else: # go left
            end = mid - 1

def bs_last(data, target):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        # if (mid == len(data) - 1 or data[mid + 1] > target) and data[mid] == target:
        #     return mid
        if data[mid] == target:
            if (mid == len(data) - 1 or data[mid + 1] > target):
                return mid
            else: # go right
                start = mid + 1
        elif data[mid] < target: # go right
            start = mid + 1
        else: # go left
            end = mid - 1

n, x = map(int, input().split())
data = list(map(int, input().split()))

first = bs_first(data, x)
last = bs_last(data, x)

# print(first)
# print(last)
if first == None:
    print(-1)
else:
    print(last - first + 1)