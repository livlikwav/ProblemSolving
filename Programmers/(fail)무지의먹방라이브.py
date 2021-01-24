'''
시간 49분 걸렸고
애초에 pseudo code 작성도 정교하게 완료하지 못하고,
구현에 들어가서 틀렸다.
시간 없다고 무작정 구현을 들어가면,
꼭 이렇게 틀리는 경우가 많은 것 같다...
애초에 알고리즘을 정확히 정의하지 않아서 당연했다.

이 문제의 point는,
1) 가장 적게 걸리는 음식부터 먹기 = greedy
2) 이걸 쉽게 하기위한 heapq 사용
3) 복잡한 알고리즘을 구현하기 위한 구현 능력

그리고, 
1) 남은 음식 중에서 몇번째 음식인지 확인하는 아이디어
2) k가 처음 length보다 크면 바로 -1 return 하는 아이디어
가 중요했던 것 같다.

lv4 이지만 무난히 풀어낼 수 있을 때 까지,
게을리하지말자 ㅜㅜ 화이팅!
'''
def solution(food_times, k):
    data = [[food_times[i], i] for i in range(len(food_times))]
    data.sort()

    length = len(data)
    while True:
        if not data:
            return -1

        min_val = data[0][0]

        if k <= length * min_val:
            break
        
        k -= length * min_val
        map(lambda x: [x[0] - min_val, x[1]], data)

        for i in range(len(data)):
            if data[i][0] == 0:
                data.pop(i)
            else:
                break
        
    data.sort(key=lambda x: [x[1], x[0]])
    while k >= 0:
        for i in range(len(data)):
            if data[i][0] > 0:
                if k == 0:
                    return i

                data[i][0] -= 1
                k -= i



    answer = 0
    return answer

print(solution([3, 1, 2], 5))
'''
<Answer>
# 이 코드는 다음 프로그래머스 사이트에서 테스트해야 정상 동작한다
# 무지의 먹방 라이브

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

    # sum_value + (현재의 음식 시간 - 이전의 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length ) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key = lambda x: x[1]) # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]
'''