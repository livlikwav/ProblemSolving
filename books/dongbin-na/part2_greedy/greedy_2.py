import sys

def my_input():
    return sys.stdin.readline()

# input
N, M = map(int, my_input().split())
data = [sorted(list(map(int, my_input().split()))) for _ in range(N)]
# compute
max_val = 0
for i in range(N):
    max_val = max(max_val, data[i][0])
print(max_val)

'''
<Lesson learned>
python min(list), min(int, int)
파이썬에서는 min 함수에 list 그대로 넣을 수 있다

if문 대신 min(), max() 활용하자

max, min 변수 사용하면 내장함수 max(), min() 오류난다

<Answer>
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
print(result)
'''