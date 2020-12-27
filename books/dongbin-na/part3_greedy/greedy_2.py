data = list(map(int, input())) # 붙어있는 문자열

# debug
# print(data)

# Solution
sum = data[0]
for i in range(1, len(data)): # 1 ~ N-1
    right = data[i]
    

    if 2 <= sum and 2 <= right <= 9:
        sum = sum * right
    else:
        sum = sum + right

print(sum)

'''
<Answer>
data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
'''