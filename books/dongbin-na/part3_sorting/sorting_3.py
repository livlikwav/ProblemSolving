'''
<실수 줄이기 메모>
소요 시간 30분(권장 20분 문제)

초기화 하는 과정(누산) 알고리즘을 잘 못 짜서 헤맸다.
쉬운 문제일수록, 집중해서 정확히 한번에 풀고 끝내자 ㅜㅜ!

<답안 꿀팁>
1) python list.count(<<특정 값>>)
시간 복잡도 O(N)

근데 사실 내가 짠 코드가 한번 loop로 끝이니 더 빠르긴함.
다만 여유로우니 위 built-in 사용하면 코드가 깔끔함.

2) stages 1부터 차례로 실패율을 계산하면서, 전체 사람수를 줄여나감
fail = count / length
length -= count
이렇게 하면 더 코드가 훨씬 간결하긴 함.
이런 걸 다음에는 바로 떠올려보자 !


<답안 메모>
문제 정의 따라 실수 없이 구현을 잘해주면 된다.
따라서 구현 문제로도 분류할 수 있지만, 
문제 해결 과정에서 정렬 라이브러리가 효과적으로 사용되므로 정렬 문제로 분류함

전체 스테이지 개수가 200,000 이하이기 때문에,
O(NlogN) 기본 정렬 라이브러리로 충분히 수행 가능함.
'''
def solution(N, stages):
    # 순차탐색하면서 count 초기화
    count = [0] * (N+2) # 0 ~ N+1 idx
    for i in range(len(stages)):
        count[stages[i]] += 1
    # print(count) # debug

    # count 바탕으로 data 배열 생성 (각 스테이지 별 지나간 수)
    data = [0] * (N+1) # 0 ~ N idx
    for i in range(N, 0, -1): 
        if i == N: # 맨 처음 값의 경우 다 깬 애들꺼 더해서 초기화
            data[i] = count[i] + count[i+1]
        else:
            data[i] = count[i] # count 값으로 자기 값부터 초기화
            data[i] += data[i+1] # 누산
    # print(data) # debug

    # 실패율 계산
    medium = []
    for i in range(1, N+1):
        # 도달한 사람이 없으면 실패율은 0
        if data[i] == 0:
            failure = 0
        # 실패율 = 현재 머무는 사람 / 총 도달한 사람(지나간 사람 포함)
        else:
            failure = count[i]/data[i]

        # 중간 배열에 더함
        medium.append([-failure, i])
    
    medium.sort()

    # 결과 배열 생성
    answer = []
    for val in medium:
        answer.append(val[1]) # val = -실패율, 번호

    return answer

'''
<Answer>
# 프로그래머스 실패율

def solution(N, stages):
    answer = []
    length = len(stages)

    # 스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1, N+1):
        # 해당 스테이지에 머물러 있는 사람의 수 계산
        count = stages.count()

        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length
        
        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count
    
    # 실패율을 기준으로 각 스테이지를 내림차순 정렬
    answer = sorted(answer, key=lambda t: t[1], reverse=True)

    # 정렬된 스테이지 번호 출력
    answer = [i[0] for i in answer]
    return answer
'''