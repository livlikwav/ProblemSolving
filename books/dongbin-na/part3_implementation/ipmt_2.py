'''
중요! Python에서 문자열도 list내에서 정렬 가능!
(list: string).sort()

var.isalpha()
알파벳이면 True, 아니면 False

seperator_string.join(iterable)
iterable 객체를 편하게 string으로 만드는 함수
'''
data = input()

nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

strings = []
sum = 0

for i in range(len(data)): # 0 ~ N-1
    if data[i] in nums: # number
        sum += int(data[i])
    else: # string
        strings.append(data[i])

strings.sort()

for i in strings:
    print(i, end='') # no new line
print(sum) # finally print sum

'''
<Answer>
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))
'''