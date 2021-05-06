'''
28분 걸림
오랜만에 해서 좀 verbose한 답이긴 함
'''

def solution(board, moves):
    # 행렬의 높이를 저장한다
    height = len(board)

    # 가로 인덱스 값 기반으로 행렬에서 맨 위의 값을 뽑아온다
    def pop_vertically(row_idx: int):
        for i in range(0, height):
            val = board[i][row_idx]

            # 0이 아닌 값을 찾으면
            if val != 0:
                # 그 자리를 0으로 채우고
                board[i][row_idx] = 0
                # 그 값을 가져온다
                return val

    # 결과 바구니
    result = []
    # 터진 인형 갯수 (+2씩 됨)
    answer = 0

    # 바구니에 채운다
    def push_result(val: int):
        answer = 0

        # debug
        # print('start', result, val)
        
        # 빈 바구니가 아니면
        if len(result) != 0:
            # 바구니 맨 위랑 겹치나 확인
            if val == result[-1]:

                # 겹치면 넣지않고, 이미 있는걸 뺀다
                result.pop()


                # 터진 인형 갯수 +2
                answer = 2
            # 안 겹치면
            else:
                # 바로 넣는다
                result.append(val)
        # 빈 바구니면
        else:
            # 바로 넣는다
            result.append(val)
        
        # debug
        # print('end', result, val)

        return answer
        

    # moves 따라 실행함
    for move in moves:
        # debug
        # print('move:', move)

        val = pop_vertically(move - 1) # 인덱스 1부터 시작하니까
        if val != None:
            answer += push_result(val)

    return answer