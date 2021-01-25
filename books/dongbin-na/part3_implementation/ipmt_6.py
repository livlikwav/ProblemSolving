'''
<또 실수할 뻔 한점>
== 문제 이해를 제대로 했음에도, 틀리게 품

data 2d list에 단순 대입하면,
같은 index에 2개의 구조물 들어갈 수 없음!
그래서 answer와 3개 열짜리 list로만 수행해야함 문제.

<문제 포인트 정리>
추측1: 문제, 조건, 문제 조건이 복잡할 수록 -> 단순 완전 탐색일 경우가 높다(내피셜)
추측2: 5초... 무작정 마니 돌려도 되겠는데
추측3: 단순히 탐색하는 법... 무엇이 까다롭고 단순히 하기 힘들지?
기둥과 보 설치나 삭제하는게 괜찮은지 검사하는게 까다롭다.
특히 삭제시 해당 위치 주변의 구조물을 일일히 검사해야하는게 분기가 많고 까다롭다.
-> 그럼 현재 구조물 그냥 싹다 괜찮은지 검사하자! -> 단순!
O(n)을 분석해보자 해도될지.
전체 명령 개수 총 1,000개 이하이다.
시간제한이 5초 이므로 O(M^3)으로 해결해도 시간 초과 안된다!
따라서 그냥 싹다 전수조사하자!
'''
def solution(n, build_frame):
    answer = []
    
    def check():
        # 현재 모든 구조물에 대해서
        for val in answer:
            x, y, a = val
            if a == 0: # 기둥
                if y == 0: # 바닥위
                    continue
                elif [x, y, 1] in answer: # 보의 위
                    continue
                elif [x-1, y, 1] in answer: # 보의 위
                    continue
                elif [x, y-1, 0] in answer: # 기둥 위
                    continue
                else:
                    return False # 다 만족하지 않으면 Invalid
            elif a == 1: # 보
                if [x, y-1, 0] in answer: # 기둥 위
                    continue
                elif [x+1, y-1, 0] in answer: # 기둥 위
                    continue
                elif [x-1, y, 1] in answer and [x+1, y, 1] in answer: # 양쪽 끝이 보
                    continue
                else:
                    return False # 다 만족하지 않으면 Invalid

        # 모든 구조물이 조건을 만족하면 Valid
        return True

    # 모든 명령 수행
    for cmd in build_frame:
        x, y, a, b = cmd
        if b == 0: # 삭제
            # 일단 삭제
            answer.remove([x, y, a])
            
            if not check():
                # 다시 삽입
                answer.append([x, y, a])
        elif b == 1: # 삽입
            # 일단 삽입
            answer.append([x, y, a])
            
            if not check():
                # 다시 삭제
                answer.remove([x, y, a])

    answer.sort()
    return answer

# n = 5
# build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
# print(solution(n, build_frame))

# n = 5
# build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
# print(solution(n, build_frame))
'''
<Answer>
# 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 설치된 것이 '기둥'인 경우
            # '바닥 위' 혹은 '보의 한쪽 끝부분 위' 혹은 '다른 기둥 위'라면 정상
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False # 아니라면 거짓(False) 반환
        elif stuff == 1: # 설치된 것이 '보'인 경우
            # '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False # 아니라면 거짓(False) 반환
        return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame: # 작업의 개수는 최대 1,000개
        x, y, stuff, operate = frame
        if operate == 0: # 삭제하는 경우
            answer.remove([x, y, stuff]) # 일단 삭제를 해본 뒤에
            if not possible(answer): # 가능한 구조물인지 확인
                answer.append([x, y, stuff]) # 가능한 구조물이 아니라면 다시 설치
        if operate == 1: # 설치하는 경우
            answer.append([x, y, stuff]) # 일단 설치를 해본 뒤에
            if not possible(answer): # 가능한 구조물인지 확인
                answer.remove([x, y, stuff]) # 가능한 구조물이 아니라면 다시 제거
    return sorted(answer) # 정렬된 결과를 반환
'''