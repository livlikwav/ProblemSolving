'''
나는 바보였다. 빨리 풀 생각에 눈이 멀어서
dict로 했다.
dict로 하면 앞에 있는거나, 뒤에 있는거나 순서 붙어있게 체크된다.
'''
def solution(s):
    
    def check(step: int) -> int:
        '''
        step은 압축 단위
        :Return: 해당 step의 압축 후 문자열 길이
        '''
        result = 0
        i = 0
        d = {}
        while (i + 1) * step <= len(s):
            val = ''.join(s[i*step:(i+1)*step])
            if val in d:
                d[val] += 1
            else:
                d[val] = 1
            i += 1
        # count remain chs
        result += len(s) - (i * step)
        # print(result)
        print(d)
        # count d
        for x in d.values():
            if x > 1:
                result += (step + 1)
            else:
                result += step
        print(result)
        return result
    
    
    answer = 1001
    for i in range(1, len(s)):
        answer = min(answer, check(i))
    return answer

print(solution(input()))