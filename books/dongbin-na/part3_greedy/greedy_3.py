'''
0001100
(2,1)
00011100110110110
(5,4)
0111111111010100100101
(6,6)
'''

data = input()

zero = 0
one = 0

if data[0] == '1':
    one += 1
else: # '0'
    zero += 1

def count(char: str) -> None: 
    global zero
    global one

    if char == '1':
        one += 1
    else: # '0'
        zero += 1

for i in range(1, len(data)):
    old = data[i-1]
    new = data[i]

    if new == old:
        # dont count
        pass
    else:
        count(new)

print(min(zero, one))
'''
주석 작성하기! 채점자도 배려하자

좀 더 간단하게 풀 수 있었다!
바뀌는 다음 수가 1이면, 0을 카운트하고
바뀌는 다음 수가 0이면, 1을 카운트하면됨.
<Answer>
data = input()
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

# 첫 번째 원소에 대해서 처리
if data[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data) - 1):
    if data[i] != data[i+1]:
        # 다음 수에서 1로 바뀌는 경우
        if data[i+1] == '1':
            count0 += 1
        else:
            count1 += 1
            
print(min(count0, count1))
'''