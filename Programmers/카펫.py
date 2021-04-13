'''
19분 소요
sqrt() 사용하지 않고, 더 간단하게 풀었어도 됐을 문제!
2e6 O(N) 완전탐색이므로!
'''
def solution(brown, yellow):

    for i in range(yellow, 0, -1):
        row = i
        
        # row * col == yellow 인 경우에만 체크
        if yellow % row != 0:
            continue
        col = yellow // row

        # row은 col보다 크거나 같다
        if row < col:
            break

        # 주어진 brown을 만족하는 경우 정답
        if brown == (2 * row + 2 * col + 4):
            answer = [row + 2, col + 2]
            return answer

    answer = [] # invalid input
    return answer