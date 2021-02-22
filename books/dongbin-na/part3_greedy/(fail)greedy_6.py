'''
<풀이 메모>
답안을 확인해보니, 접근 방법까지는 캐치했으나,
아직까지 쉽게 구현하는 노하우가 부족하다.
heapq를 사용해서 한 음식씩 줄여나갈 수 있다는 걸 깨닫지 못했다.

<답안 메모>
시간이 적게 걸리는 음식부터 확인하는 탐욕적 접근 방식
모든 음식을 시간을 기준으로 정렬한 뒤, 시간이 적게 걸리는 음식부터 제거해 나가는 방식
우선순위 큐를 이용하여 구현
'''
def solution(food_times, k):
    
    N = len(food_times)
    
    k_cnt = k # 총 먹는 시간
    food_cnt = N # 남은 음식 갯수
    food_remaining = list(range(0, N)) # 남은 음식 index

    while k_cnt > food_cnt:
        # 먹어야할 시간이 남아있으나 먹을 음식이 없다면 break
        if food_cnt == 0:
            return -1
        
        val = k_cnt // food_cnt
        
        for i in range(N):
            # 남아있는 음식의 경우
            if food_times[i] > 0:
                # 음식이 뺄 양보다 많을 때
                if food_times[i] > val:
                    k_cnt -= val
                    food_times[i] -= val
                # 음식을 다 먹었을 때
                else:
                    k_cnt -= food_times[i]
                    food_times[i] = 0
                    food_cnt -= 1 # 남아있는 음식 개수 감소
                    food_remaining.remove(i)

        # 1개씩 차례로 먹는다
        while k_cnt >= 0:
            for idx in food_remaining:
                if food_times[idx] > 0:
                    k_cnt -= 1
                    food_times[idx] -= 1

                    # 종료 조건
                    if k_cnt == -1:
                        return (idx + 1) # 음식 번호는 1부터 시작하므로
                else:
                    food_remaining.remove(idx)

food_times = [3, 1, 2]
k = 5

print(solution(food_times, k))
'''
<Answer>

import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1
    
    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))
    
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
    result = sorted(q, key = lambda x: x[1]) # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]
'''