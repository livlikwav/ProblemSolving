'''
49분 걸림.
정규표현식 오랜만에 쓰느라 찾아보느라 좀 걸림. split 구분자 여러개 쓰는법 이번 기회에 확실히 함.
list deep copy 문제도 기억하기. 테스트케이스를 다 보여주니까 잘 고쳤는데, 없었으면 확실히 더 힘들었을 듯함.
'''
import re

def solution(expression):
    nums = list(map(int, re.split('[*+-]', expression)))
    opers = re.split('\d+', expression)[1:-1]

    # print(nums, opers)

    candidates = [
        ['+', '-', '*'],
        ['+', '*', '-'],
        ['-', '+', '*'],
        ['-', '*', '+'],
        ['*', '-', '+'],
        ['*', '+', '-']
    ]

    def compute(num1: int, num2: int, x: str) -> int:
        if x == '+':
            return num1 + num2
        elif x == '-':
            return num1 - num2
        else:
            return num1 * num2

    answer = 0

    for order in candidates:
        # print('order', order)
        temp_nums = [] ; temp_opers = []
        for x in nums:
            temp_nums.append(x)
        for x in opers:
            temp_opers.append(x)


        for oper in order:
            isUndone = True
            while isUndone:
                if len(temp_opers) == 0:
                    isUndone = False

                for i in range(len(temp_opers)):

                    if temp_opers[i] == oper:
                        val = compute(temp_nums[i], temp_nums[i+1], temp_opers[i])
                        del temp_nums[i] ; del temp_nums[i] ; del temp_opers[i]
                        temp_nums.insert(i, val)
                        # print(temp_opers, temp_nums, i)

                        break
                    else:
                        if i == len(temp_opers)-1:
                            isUndone = False

        answer = max(answer, abs(temp_nums[0]))

    return answer


# solution("100-200*300-500+20")
# solution("50*6-3*2")