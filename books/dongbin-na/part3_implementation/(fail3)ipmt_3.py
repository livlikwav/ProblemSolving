'''
결론: 오히려 문제대로 문자열 만들어서 풀었으면 바로 맞았음
문자열 만들지 않고 임의로 int 값 더해서 구하다가 틀림
(count 10이상일때도 +1만 되도록 코드가 짜여져 있는것 외에도 문제가 많은듯)

이 코드 고쳐서 해결함
(개선1: count 10, 100, 100 제대로 출력)
(개선2: len(s) // 2 + 1에서 "a"가 제대로 안되므로 다시 len(s)로 회귀)

이 폴더 README.md 참고

PYTHON의 이해 안가는 널널한 검사
list slicing에서 list[a:b]에서
b가 len(list)를 한참 초과해도
오류가 나지 않고 마지막 값까지만 slicing 해준다
예를 들어, 
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr[8:100]
>> [9, 10]

또한 a가 초과해도 오류가 나지 않고,
빈 list를 반환한다
ex,
arr[100:1]
>> []
'''
def solution(s):
    
    def check(step: int) -> int:
        '''
        :Param: 문자열 압축 단위
        :Return: 해당 step의 문자열 길이
        '''
        start = 0
        end = 0
        result = 0
        count = 0
        old = ''
        while start + step <= len(s):
            end = start + step
            new = ''.join(s[start:end])
            if old != new:
                # count past word
                if count == 1:
                    result += step
                elif 10 > count > 1:
                    result += (step + 1)
                elif 100 > count > 1:
                    result += (step + 2)
                elif 1000 > count > 1:
                    result += (step + 3)
                elif count == 1000:
                    result += (step + 4)
                count = 1
                old = new
            else:
                count += 1
            # set next start
            start = end
        # count last word
        if count == 1:
            result += step
        elif 10 > count > 1:
            result += (step + 1)
        elif 100 > count > 1:
            result += (step + 2)
        elif 1000 > count > 1:
            result += (step + 3)
        elif count == 1000:
            result += (step + 4)
        # count remain characters
        result += (len(s) - start)
        return result
    
    # Solution
    answer = 1001
    for i in range(1, len(s)+1):
        answer = min(answer, check(i))
        print(f'{i}, {answer}')
    return answer

print(solution(input()))

'''
<Answer>
def solution(s):
    answer = len(s)
    # 1개 단위 step부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step] # 앞에서부터 step 만큼의 문자열 추출
        count = 1
        # 단위 step 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수 (count) 증가
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step] # 다시 상태 초기화
                count = 1
        # 남아 있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    return answer
'''