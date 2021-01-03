'''
핵심: data.sort(key=(lambda x: (-x[1], x[2], -x[3], x[0])))

sort()의 key option func은
해당 list의 데이터 자체를 바꾸진 않는다.
(내부적으로 sorting할때 compare할때만 사용하는 듯.)
'''

N = int(input())
data = []
for _ in range(N):
    line = input().split()
    data.append((line[0], int(line[1]), int(line[2]), int(line[3])))

# debug
# print(N)
# print(data)

# Solution
data.sort(key=(lambda x: (-x[1], x[2], -x[3], x[0])))

for x in data:
    print(x[0])

'''
<Answer>
이 문제를 기억한다면,
특정한 기준으로 정렬하는 대부분의 문제를 해결할 수 있다.

Python에서 tuple을 원소로 갖는 list의 경우,
해당 리스트를 정렬하면 기본적으로 각 튜플을 구성하는 원소의 순서에 맞게 정렬된다는
특징이 있다.

sort() 함수의 key 속성에 값을 대입하여
내가 원하는 조건에 맞게 튜플을 정렬시킬 수 있다는 점을 기억.
'''