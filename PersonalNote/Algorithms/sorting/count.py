"""
계수 정렬 Count sort
데이터 갯수 1,000만개 미만일 때 사용하자.
최악의 경우에도 TC O(N + K) 를 보장한다. 데이터 개수 N, 데이터 중 최댓값 K
비교 기반의 정렬 알고리즘이 아니다(비교 기반 = quick, selection, insertion...)
SC O(N + K)
기수 정렬 Radix Sort 와 더불어 가장 빠르다고 볼 수 있다.
데이터의 특성을 파악하기 어렵다면 퀵 정렬을 이용하는 것이 유리하다.
"""
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
