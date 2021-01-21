'''
<핵심 아이디어>
제한시간 5초에, 명령 수 최대 1000이면
딱 O(N^3)이 가능할 것 같고 + 구현 문제면
앞으로는 일단 전수조사로 구현 후 나중에 생각해도 될 것 같다!

내 계산 상으로는 Python 1s가 2e^7라면
5s는 1e^8로 N^3인 1e^9에는 못미쳐서 안될 것 같았는데,
충분하댄다. 위와 같은 어림짐작은 어림짐작일 뿐인가봄.
너무 클 경우에만 Big O 최적화를 생각하기.

<실수한 점>
문제 이해를 잘못한게,
data를 업데이트하고 조사하지말고, answer만 조사하면 됐다.

또한 x,y 에 0, 1
즉 기둥과 보 둘다 존재 가능한데,
그게 안되도록 구현했기 때문에 무조건 틀림



다 풀었을때 시간도 제한시간 50분 훨씬 넘은,
거의 1시간 20분 수준이었다.
또한, 프로그래머스 실행에서는 성공하였으나,
문제 제출했더니 싹 다 틀림...
구현.. 멀고 험하구나..
'''

# build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
# n = 5

# n = 5
# build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1],
#                 [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0],
#                 [1, 1, 1, 0], [2, 2, 0, 1]]

def solution(n, build_frame):
    # 0은 기둥, 1은 보, -1는 빈자리
    # 0은 삭제, 1은 설치
    # 겹치는 구조물 설치나 없는 구조물 삭제인 경우는 없다


    # data map 초기화
    # 다 빈자리, 즉 -1로 초기화한다.
    data = [[-1] * (n+1) for _ in range(n+1)]


    # 결과값
    result = []

    # 해당 좌표가 맵 안인지 파악
    def check_in_map(x, y):
        if 0 <= x <= n and 0 <= y <= n:
            return True
        else:
            return False

    def check_bo(x, y):
        # 지어도 괜찮은 경우
        if check_in_map(x, y-1):
            if data[x][y-1] == 0: # 밑이 기둥이라면
                return True

        if check_in_map(x+1, y-1):
            if data[x+1][y-1] == 0: # 옆에 밑이 기둥이라면
                return True

        if check_in_map(x+1, y) and check_in_map(x-1, y):
            if data[x+1][y] == 1 and data[x-1][y] == 1: # 양 옆이 보라면
                return True
        
        return False

    def check_gidung(x, y):
        # 지어도 괜찮은 경우
        if check_in_map(x, y):
            if y == 0: # 빈 땅이라면
                return True

        if check_in_map(x, y-1):
            if data[x][y-1] == 0: # 밑에가 기둥이라면
                return True

        if check_in_map(x - 1, y):
            if data[x-1][y] == 1: # 옆에가 보 라면
                return True
        
        return False

    # 보를 설치하려는 경우
    def add_bo(x, y):

        if check_bo(x, y):
            data[x][y] = 1 # 보를 설치한다
            result.append([x, y, 1])
        else:
            pass

    # 기둥을 설치
    def add_gidung(x, y):
        if check_gidung(x, y):
            data[x][y] = 0 # 기둥을 설치한다
            result.append([x, y, 0])
        else:
            pass

    # 보를 삭제하려는 경우
    def del_bo(x, y):
        
        # 일단 보를 삭제한다
        data[x][y] = -1

        b1 = check_gidung(x+1, y)
        b2 = check_bo(x-1, y)
        b3 = check_bo(x+1, y)
        if b1 and b2 and b3:
            # 결과값에서도 삭제한다
            result.remove([x, y, 1])
        else:
            # 보를 원상복구 시킨다
            data[x][y] = 1
    
    # 기둥을 삭제하려는 경우
    def del_gidung(x, y):

        # 일단 기둥 삭제
        data[x][y] = -1

        b1 = check_gidung(x, y+1)
        b2 = check_bo(x, y+1)
        b3 = check_bo(x-1, y+1)

        if b1 and b2 and b3:
            # 결과값에서도 삭제한다
            result.remove([x, y, 0])
        else:
            # 기둥 원상복구
            data[x][y] = 0



    # 입력값에 대해서 순차적으로 함수 실행
    for array in build_frame:
        x, y, a, b = array
        if a == 0: # 기둥이면
            if b == 0: # 삭제면
                del_gidung(x, y)
            elif b == 1: # 설치면
                add_gidung(x, y)
        elif a == 1: # 보 면
            if b == 0: # 삭제면
                del_bo(x, y)
            elif b == 1: # 설치면
                add_bo(x, y)
        
        # debug
        # print(result)

    result.sort(key=lambda x: (x[0], x[1], -x[2]))

    return result

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