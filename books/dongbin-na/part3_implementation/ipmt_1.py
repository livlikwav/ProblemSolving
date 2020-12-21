import time

data = list(map(int, input()))

start_time = time.time()

mid_index: int = len(data) // 2

left = data[:mid_index]
right = data[mid_index:]

if sum(left) == sum(right):
    print('LUCKY')
else:
    print('READY')

end_time = time.time()
print("time:", end_time - start_time)

# print(data)
# print(mid_index)
# print(left)
# print(right)

'''
<Lesson Learned>
알고리즘 시간 측정 코드 까먹지 말기!
import time
start_time = time.time()
end_time = time.time()
print('time:', end_time - start_time)

또 debug 안하면 실수할 뻔 함.
input시에 붙어있는 문자열인지, 공백문자가 있는 문자열인지 잘 확인해서
입력받을 것!
<Answer>
n = input()
length = len(n)
summary = 0

for i in range(length // 2):
    summary += int(n[i])

for i in range(length // 2, length):
    summary -= int(n[i])

if summary == 0:
    print('LUCKY')
else:
    print('READY')

'''