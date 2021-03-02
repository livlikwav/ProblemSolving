'''
또 틀렸다. 1시간 24분을 풀었는데.. 햄보칼수가없어... 구현, 그리디가 제일 어렵다.
이건 그리디라기보다는 나에게는 구현 문제이다. 구현을 계속 digging하자... 포기하지말자 ㅜㅜ

Lesson Learned
변수명 previous
heap이 담는 값이 list나 tuple일 경우 역시 순서가 중요함을 기억.
음식이 무조건 하나씩 빠지므로 length -= 1
(k - sum_value) % length <-- 사용했었지만 확신을 가지지못해 바꿨다.
'''
import heapq

def solution(food_times, k):
    # 섭취해야할 음식이 없다면 -1를 반환한다.
    if k > sum(food_times):
        return -1

    heap = []
    for i in range(len(food_times)):
        heapq.heappush(heap, [food_times[i], i]) 

    sum_val = 0
    old = 0

    while heap:
        count = len(heap)
        val, idx = heapq.heappop(heap)
        # 아직 음식이 남아있는 경우
        if old < val:
            remains = k - sum_val
            plus_val = (val - old) * count
            old = val

            # K를 넘기는 경우 다시 하나하나 세야함
            if plus_val > remains:
                heapq.heappush(heap, [val, idx])
                heap.sort(key = lambda x: x[1])

                for i in range(count):
                    heap[i][0] -= 1
                    remains -= 1

                    if remains == -1:
                        return heap[i][1] + 1

            elif plus_val == remains:
                heap.sort(key = lambda x: x[1])
                _, result = heap[0]

                return result + 1
            else:
                sum_val += plus_val
                
                continue
'''
import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1
    
    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호)형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i))

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간

    length = len(food_times) # 남은 음식의 개수

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key = lambda x: x[1]) # 음식 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]
'''