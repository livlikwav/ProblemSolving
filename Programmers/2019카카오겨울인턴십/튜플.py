'''
36분 걸림 ㅜㅜ
엣지 케이스인 '20', '113' 등을 걸러내게 미리 짰어야하는데,
또 바로 짜고 디버깅때 발견해서 고침
'''
def solution(s):
    # 파서 만들기
    def parsor(s: str) -> list: 
        '''
        결과값 : [(길이, 집합), (길이, 집합) ... ]
        '''
        # 전처리: 양 끝 {} 삭제
        s = s[1:-1]

        # 파싱 시작
        result = []
        temp = ''

        for i in range(len(s)):
            ch = s[i]

            # 괄호 시작 시 집합 초기화
            if ch == '{':
                temp = ''
            # 괄호 종료 시 임시 문자열을 가공하여 result에 반영
            elif ch == '}':
                # , 구분자로 split하여 문자열 배열 만듬
                temp = temp.split(',')

                # result 추가용 임시 집합 만듬
                temp_set = set()
                for val in temp:
                    temp_set.add(int(val))

                result.append((len(temp_set), temp_set))

            # {} 사이에는 하나의 임시 문자열로 다룸
            else:
                temp += ch

        return result
                

    # 주어진 문자열 파싱하여 data 만듬
    data = parsor(s)
    data.sort()
    # 최종 답 만들기
    answer = []

    # 맨 처음 값은 바로 추가
    for x in data[0][1]:
        answer.append(x)

    for i in range(1, len(data)):
        # 집합 간 차집합으로 원소 구함
        val = data[i][1] - data[i-1][1]
        for x in val:
            answer.append(x)

    return answer
