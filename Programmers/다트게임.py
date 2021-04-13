'''
21분 소요. 또 경계값 놓쳐서 3분정도 더 걸림. 하마터면 다시 짜야할 수도 있었다.
0, 10을 체크 했어야 했다. 늘 문제 풀기전에 경계값부터 확인하기.
'''
def solution(dartResult):
    score = [0] # 0번째 원소는 삭제 예정

    bonus = {
        "S" : 1,
        "D" : 2,
        "T" : 3
    }
    isFirstNum = True
    for ch in dartResult:
        if ch.isnumeric():
            if isFirstNum:
                score.append(int(ch))
                isFirstNum = False # 두 자리수도 입력받기 위해 표시
            else:
                score[-1] = 10 # 두 자리수는 10밖에 없다.
        elif ch.isalpha():
            delta = score[-1]
            for _ in range(1, bonus[ch]):
                score[-1] *= delta
            isFirstNum = True # 새로운 수를 입력받기 위해 표시
        else:
            # 스타상
            if ch == "*":
                score[-1] *= 2
                score[-2] *= 2
            # 아차상
            if ch == "#":
                score[-1] = -score[-1]
    
    answer = sum(score[1:])
    # print(score)
    return answer