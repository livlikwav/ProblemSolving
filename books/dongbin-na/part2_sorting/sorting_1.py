N = int(input())
data = [int(input()) for _ in range(N)]

# print(N)
# print(data)

data.sort()
data.reverse()

for i in data:
    print(i, end=' ')

'''
<Lesson learned>
print(i, end=' ') 
> 이렇게 해야 \n가 없이 한 줄에 입력이 됨!
<Answer>
n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
    print(i, end='')
'''