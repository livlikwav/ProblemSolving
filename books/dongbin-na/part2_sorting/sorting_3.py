'''
5 3
1 2 5 4 3
5 5 6 6 5
'''

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# debug
# print(N, K)
# print(A)
# print(B)

A.sort()
B.sort(reverse=True)

print(A)
print(B)

for i in range(N):
    if i == K: # 0 ~ K-1
        break

    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break

sum = 0
for val in A:
    sum += val
print(sum)

'''
<Lesson Learned>
* 최대 횟수 K 같은거 if문으로 거를때 조심해야함!
이번에도 i가 0부터 시작하기때문에 i == K면 break해야함!!
실수할 뻔 했다

* 이 문제는 그냥 range(k)로 해도 됐다!!
<Answer>
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))
'''