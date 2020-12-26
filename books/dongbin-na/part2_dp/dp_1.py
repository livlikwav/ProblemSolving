'''
도중에 또 틀린 이유는 
if elif elif else가 아니라
if if if if 로 했어야했기 때문이다...

또 이런 단순 if문 분기 실수로 틀렸다...
'''

x = int(input())
d = [0] * (30000 + 1)
# d[1] = 0, d[0] = 0

# debug
# print(x)
# print(len(d))

for i in range(2, x+1): # 2 ~ x
    array = []
    if i % 5 == 0:
        array.append(d[i//5])
    if i % 3 == 0:
        array.append(d[i//3])
    if i % 2 == 0:
        array.append(d[i//2])
    # finally
    array.append(d[i-1])

    d[i] = min(array) + 1

# Solution
# print(d[:x+1])

print(d[x])

'''
<Answer>
x = int(input())
d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])
'''