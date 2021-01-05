'''
<나만의 팁 만들기 : list step따라 slicing하기>
step loop에서
iteration = len(list) // step
remain_index_start = (len(list) // step) * step

aabbaccc
ababcdcdababcdcd
xxxxxxxxxxyyy
'''
def solution(s):
    
    N = len(s)
    answer = 1001
    
    for step in range(1, N+1):
        tmp = ''
        iteration = N // step
        # init first step
        old = ''
        count = 0
        # iteration
        for i in range(1, iteration + 1):
            new = s[(i-1)*step: i*step]
            
            if new == old:
                count += 1
            else:
                if count == 1:
                    tmp += old
                elif count > 1:
                    tmp += str(count) + old
                count = 1
            
            old = new
        # save last step
        if count == 1:
            tmp += old
        elif count > 1:
            tmp += str(count) + old
        # save remain chars
        idx = (N // step) * step
        if idx < N:
            tmp += s[idx:]
        else:
            pass
        # debug
        # print(tmp)
        # check min val
        answer = min(answer, len(tmp))
    
    return answer

print(solution(input()))
'''
<Answer>
def solution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1
        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, lne(s), step):
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 다시 상태 초기화
                count = 1
    # 남아 있는 문자열에 대해서 처리
    compressed += str(count) + prev if count >= 2 else prev
    # 만들어지는 압축 문자열이 가장 짧은 것이 정답
    answer = min(answer, len(compressed))
return answer
''' 