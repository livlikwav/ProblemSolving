'''
<Python heap 라이브러리 사용법 까먹지마..>
까먹어서 못 풀뻔.. 그럼 직접 구현했어야하나 ㅋㅋㅋ
힙 자료구조 원리.. 다시 숙지해둘것
import heapq
heap = []
heapq.heappush(heap, value)
heapq.heappop(heap)

<답안 메모>
무조건 가장 작은 두 카드 묶음을 합치면 된다는 점에서,
그리디 알고리즘으로도 분류할 수 있다.
다만 정렬 개념을 활용해야해서 정렬로 분류했다.

이렇게 항상 가장 작은 두 묶음을 알아내기 위해
가장 효과적인 자료구조는 바로 우선순위 큐이다.
따라서 heapq를 사용하면 된다.
우선순위 큐는 원소를 push, pop할때마다 정렬이 되기 때문.
'''
import heapq

n = int(input())
heap = [] # 파이썬 최소힙
for _ in range(n):
    heapq.heappush(heap, int(input()))

# Solution
result = 0

for _ in range(n-1):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    
    result += a + b

    heapq.heappush(heap, a+b)

print(result)
'''
<Answer>
import heapq

n = int(input())

# 힙에 초기 카드 묶음을 모두 삽입
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

# 힙에 원소가 1개 남을 때까지
while len(heap) != 1:
    # 가장 작은 2개의 카드 묶음 꺼내기
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    # 카드 묶음을 합쳐서 다시 삽입
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)
'''