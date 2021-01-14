'''
블로그에 증명 과정을 정리해놨다.

직선 위에서,
다른 모든 점과의 거리의 합이 최소인 점은,
해당 직선의 중간값이다!
'''
n = int(input())
data = list(map(int, input().split()))
data.sort()

# print medium
print(data[(n - 1) // 2])