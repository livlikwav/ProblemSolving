'''
어려운 구현 문제일수록 문제 코드는 짧고 단순한 것 같다.

계속 도전하자. 계~~~속 풀면 잘하는 날이 오겠지. (잘하기 전까지 포기 안하는게 목표)

<답안 포인트>
일단 구현 로직 자체가 어려웠다.
친구의 모든 순열을 구해두고,
각 순열 되는지 체크하면서 또 참가한 친구의 수를 추가한다.
일단 추가하고 되면 체크하고 -> 완전 탐색에서 최소값을 계속 갱신해서 해결한다.

<답안 해석>
weak 리스트와 dist 리스트의 길이가 매우 작은 것을 볼 수 있다.
문제에서 찾고자 하는 값은 '투입해야하는 친구 수의 최솟값'이다.
따라서 모든 친구를 무작위로 나열하는 모든 Permutations의 개수를 계산해보면
8P8 == 8! == 40320으로 충분히 계산 가능한 경우의 수이다.

<원형으로 나열된 데이터를 처리하는 경우>
길이를 2배로 늘려서 원형을 일자로 만드는 작업을 해준다.
1 3 4 9 10 을
1 3 4 9 10 13 15 16 21 22 로 만들어서 수행한다.

'''

import copy
def solution(n, weak, dist):

    # 최대 거리 친구부터 검사하기 위함
    dist.sort()
    dist.reverse()

    def check(friends: int, start: int) -> bool:

        # 현재와 과거 취약지점 저장
        # 필요한 이동거리 계산 위함
        present = start
        old = start

        step_sum = 0

        # 현재 설정된 친구 수만큼만 검사해봄
        for i in range(friends): 
            # 친구의 잔여 걸음수 초기화
            last_step = dist[i] 
            
            while present < len(weak):
                present += 1

                # 마지막 걸음까지 왔다면
                if present == len(weak):
                    step = (n - weak[len(weak)-1]) + weak[0]
                    # 남은 걸음 수로 가능한 거리라면
                    if step <= last_step: 
                        return True
                    # 불가능한 거리라면 break
                    else:
                        # present 원상복구
                        present -= 1
                        break
                # 원 안에서만 했다면
                else:
                    print(present, old)
                    step = weak[present] - weak[old]
                    # 남은 걸음 수로 가능한 거리라면
                    if step <= last_step: 
                        # 남은 걸음 수 차감하고
                        last_step -= step 
                        # 이동한 거리 추가
                        step_sum += step
                    # 불가능한 거리라면 break
                    else:
                        # present 원상복구
                        present -= 1
                        break
                
                # 아직 더해야하면 old도 update
                old += 1

        # n 만큼의 거리 모두 이동했으면 성공
        if step_sum == n: 
            print(step_sum, friends, start, '이게 왜 돼')
            return True
        else:
            return False

    # Solution
    for friends in range(1, len(dist)+1):
        for start in range(len(weak)):
            if check(friends, start):
                return friends

    # 가능한 경우 없었으면 -1 반환
    return -1                

n, weak, dist = 12, [1, 5, 6, 10], [1, 2, 3, 4]
# n, weak, dist = 12, [1, 3, 4, 9, 10], [3, 5, 7]
print(solution(n, weak, dist))
'''
<Answer>
# 프로그래머스 외벽 점검

from itertools import permutations

def solution(n, weak, dist):
    # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1 # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1로 초기화
    # 0부터 length - 1 까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 투입할 친구의 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]
            # 시작점부터 모든 취약 지점을 확인
            for index in range(start, start + length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    count += 1 # 새로운 친구를 투입
                    if count > len(dist): # 더 투입이 불가능하다면 종료
                        break
                    position = weak[index] + friends[count - 1]
        answer = min(answer, count) # 최솟값 계산
    if answer > len(dist):
        return -1
    return answer
'''