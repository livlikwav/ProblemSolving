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