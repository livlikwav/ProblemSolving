'''
답안 잘 확인하기 -> 나는 자료구조로 풀었지만, 그리디하게 풀지 못했다.
그리디 = 현재 상태에서 매번 가장 좋아 보이는 것만을 선택하는 알고리즘
현재 상태 = 1부터 target-1까지의 모든 금액을 만들 수 있는 상태
이때, 매번 target도 만들 수 있는지 체크해보기.

이해함.
이게 가능한 것은
1 ~ (target - 1)까지가 가능하기 때문에
target이 가능하면
1 ~ (x + target - 1) 까지는 가능한 거자나
그래서 다음 타겟을 x + target으로 잡는 것이다.

당연하게도 현재 x 를 체크하기 이전의
1 ~ target -1 이 다 가능한 이유는
Greedy하게 매번 상태를 체크하면서 넘어왔기 때문이다.

주의할 점!!
1) Set은 append가 아닌 add
2) iteration 중에 Set 변경되면 오류남
5
3 2 1 1 9
>> 8

3
3 5 7
>> 1
'''
import time
n = int(input())
data = list(map(int, input().split()))

# n = 1000
# data = [3, 2, 1, 1, 9] * 200

start_time = time.time()
s = set()
for a in data:
    # check others
    array = []
    for b in s:
        array.append(a+b)
    for x in array: # RuntimeError: Set changed size during iteration
        s.add(x)
    # add itself
    s.add(a)

max = int(1e6)
for i in range(1, max):
    if i not in s:
        print(i)
        break
end_time = time.time()
print(f'time: {end_time-start_time}')
'''
<Answer>
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

# 만들 수 없는 금액 출력
print(target)

'''