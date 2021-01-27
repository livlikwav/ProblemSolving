'''
<후기>
풀이 시간 20분이라고 했는데,
맞기 까지 36분 걸렸다...
pseudo code 작성하고 나니 21분이었는데
어떻게 더 시간을 줄일 수 있을까?
(모르겠다, 그냥 문제를 더 빨리 이해하는 수 밖에...)

그리고 또 idx 실수했다.
프린트 찍어보면서 고쳤다.
실수 줄이도록 하자.

<답안 정리>
엄밀히 말하면 이 문제는 DFS 문제는 아니다.
정확한 구현을 요구하고, 실수하기 쉬운 문제라는 점에서
구현 문제 유형으로 분류할수도 있다.
하지만 DFS 알고리즘 핵심이 되는 재귀 함수 구현을 요구한다는 점에서
DFS 연습 목적의 문제로 DFS/BFS 파트에서 다루고자 한다.

이 문제를 실수 없이 풀려면 소스코드를 최대한 단순화 하는 것이 좋다.
'''
def solution(p):

    # 올바른 괄호 문자열인지 체크 - 쌍이 맞다
    def check(s: str) -> bool:
        left, right = 0, 0
        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            elif s[i] == ")":
                right += 1
                # 만약 right가 많아지면 바로 실패
                if left < right:
                    return False
        # 마지막 검사
        if left == right:
            return True
        else: # 왼쪽 괄호만 더 많으면
            return False
    
    # v의 시작 위치 반환
    def get_atomic(s: str) -> int:
        count = 0
        for i in range(len(s)):
            if s[i] == "(":
                count += 1
            elif s[i] == ")":
                count -= 1
            # 바로 짝이 맞나 검사
            if count == 0:
                return i+1
        # 도중에 되어야 하는데 안되면 균형잡힌 문자열이 아닌거
        if count != 0:
            # print(s)
            # print(count)
            raise Exception

    # u 개선하는 함수
    def trim(s: str) -> str:
        if len(s) == 2:
            return ""
        else:
            # 양쪽 문자 제거
            s = s[1:-1]

            result = ""
            # 괄호 반대로 작업하기
            for ch in s:
                if ch == ")":
                    result += "("
                elif ch == "(":
                    result += ")"
            return result

    # 균형잡힌 문자열 올바른 문자열로 바꾸는 함수
    def change(s: str) -> str:
        # print(s)
        # 빈 문자열일 경우 바로 반환
        if len(s) == 0:
            return ""
        # u와 v로 분리
        idx = get_atomic(s)
        u, v = s[:idx], s[idx:]
        # print(u, v)
        # u가 올바른지 체크
        if check(u):
            return u + change(v)
        else:
            return "(" + change(v) + ")" + trim(u)
        

    # 바로 올바른 애면 반환
    if check(p):
        return p
    # 함수 수행
    answer = change(p)
    return answer

# p = "(()())()"
# p = ")("
p = "()))((()"
print(solution(p))

'''
<Answer>
# 프로그래머스 괄호 변형

# 균형잡힌 괄호 문자열의 인덱스 반환
def balanced_index(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

# 올바른 괄호 문자열인지 판단
def check_proper(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0: # 쌍이 맞지 않는 경우에 False 반환
                return False
            count -= 1
    return True # 쌍이 맞는 경우에 True 반환

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]
    # 올바른 괄호 문자열이면, v에 대해 함수를 수행한 결과를 붙여 반환
    if check_proper(u):
        answer = u + solution(v)
    # 올바른 괄호 문자열이 아니라면 아래의 과정을 수행
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1]) # 첫번째와 마지막 문자를 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer
'''