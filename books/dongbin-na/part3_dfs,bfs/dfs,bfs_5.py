'''
<실수 줄이기! 메모!>
1. 문제 예제 보면서 답안 체크 잘하기
(특히 제출 기회 1번뿐인 카카오 같은 코테라면)
최대, 최소 print해야하는데 반대로 해서 틀릴 뻔함.

2. 문제 구현 사항 하라는대로 그냥 구현하기 (안 복잡하면)
python //도 C++14처럼 음수를 양수로 변환해서 계산후 다시 음수 변환할 줄 알았는데,
아니었나봄. 해당 부분 구현하니 바로 맞았다.

<답안 배울점>
나처럼 굳이 list쓰지 않고, 바로바로 sum 구하고,
count 배열 넘기지 않고, 
더했다가 dfs 보내고 다시 빼는 식(원상복구)
이게 더 구현 간단하긴 하다.

<답안 메모>
이 문제는 각 사칙연산 중복해서 사용할 수도 있기 때문에,
중복순열 계산하는 python itertools.product 사용해 찾을 수도 있다.
--> 하지만 단순 갱신이므로 그냥 dfs로 완전 탐색하는 것이 편하다.

from itertools import product
n = 4
print(list(product(['+', '-', '*', '/'], repeat = (n - 1))))
'''
import copy
n = int(input())
data = list(map(int, input().split()))
ops_count = list(map(int, input().split()))
# idx 0 : +
# idx 1 : -
# idx 2 : *
# idx 3 : //

# print(n)
# print(data)
# print(ops_count)

def compute(ordered_ops: list) -> int:
    # dfs 를 통해 연산자들이 순서대로 리스트에 담겨서 온다

    # 숫자배열의 첫 인덱스 값으로 초기화
    val = data[0]
    for i in range(n-1): # 0 ~ n-2
        # 각 연산자에 대해 알맞은 연산을 누산함
        if ordered_ops[i] == 0: # +
            val += data[i+1]
        elif ordered_ops[i] == 1: # -
            val -= data[i+1]
        elif ordered_ops[i] == 2: # *
            val *= data[i+1]
        elif ordered_ops[i] == 3: # //
            # 음수인 경우 C++14 규칙을 따름
            if val < 0:
                val = -((-val) // data[i+1])
            else:
                val //= data[i+1]
    
    return val
# -10억보다 크거나 같고, 10억보다 작거나 같다
min_val = int(1e9)
max_val = -int(1e9)

def dfs(ordered_ops: list, count: list, step: int) -> None:
    global min_val
    global max_val

    # 마지막 연산자를 추가했을 경우에 (마지막 level 도착)
    if step == n - 1:
        val = compute(ordered_ops)
        # 최소 최대 갱신
        min_val = min(min_val, val)
        max_val = max(max_val, val)
        # debug
        # print(ordered_ops)
        # print(val)

    # 아직 모든 연산자를 추가하지 않았을 때
    elif step < n - 1:

        for i in range(4): # + - * // 순서

            if count[i] > 0: # 아직 그 연산자가 남아있으면
                # 먼저 list 복제
                tmp_ops = copy.deepcopy(ordered_ops)
                tmp_count = copy.deepcopy(count)
                # step 수행
                tmp_ops.append(i) # result 배열에 연산자 추가하고
                tmp_count[i] -= 1 # 연산자 카운트 감소시키고

                dfs(tmp_ops, tmp_count, step + 1) # step수 올려서 dfs 뻗어나감.

# Solution
dfs([], ops_count, 0)

print(max_val)
print(min_val)
'''
<Answer>
n = int(input())
# 연산을 수행하고자 하는 수 리스트
data = list(map(int, input().split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int, input().split())

# 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9

# dfs 메서드
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 갱신
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i])) # 나눌 때는 나머지를 제거
            div += 1
# dfs 메서드 호출
dfs(1, data[0])

# 최댓값과 최솟값 차례대로 출력
print(max_value)
print(min_value)
'''