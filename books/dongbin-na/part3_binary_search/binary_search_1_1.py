'''
7 2
1 1 2 2 2 2 3
>> 4

7 4
1 1 2 2 2 2 3
>> -1
'''
from bisect import bisect_left, bisect_right

def count_by_range(l, a, b):
    """
    만약 원소가 없다면 0을 반환한다.
    왜냐하면 리스트 최솟값 보다 작다면 둘다 0을 반환하고,
    최대값보다 크다면 length값을 반환하기 때문이다.
    """
    left_idx = bisect_left(l, a)
    right_idx = bisect_right(l, b)
    result = right_idx - left_idx
    if result <= 0:
        return -1
    else:
        return result
    

n, x = map(int, input().split())
data = list(map(int, input().split()))

print(count_by_range(data, x, x))

'''
<Answer>
동일하다.
'''