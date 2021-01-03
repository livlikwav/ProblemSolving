def solution(s):
    
    def check(step: int) -> int:
        '''
        step은 압축 단위
        해당 압축 단위의 문자열 갯수 리턴
        '''
        result = 0
        length = len(s)
        # set first
        old = ''.join(s[0:step])
        count = 1
        # loop
        max = length // step
        for i in range(1,max):
            new = ''.join(s[i*step:2*i*step])
            if old == new:
                count += 1
            else:
                if count == 1:
                    result += step
                    count = 1
                else:
                    result += (step + 1)
                    count = 1
            old = new
        # save last i
        if count == 1:
            result += step
            count = 1
        else:
            result += (step + 1)
            count = 1
        # save remain chrs
        result += len(''.join(s[(length // step)*step:-1]))
        return result
    
    # Solution
    answer = 1001
    for i in range(1, len(s)):
        answer = min(answer, check(i))
    
    return answer