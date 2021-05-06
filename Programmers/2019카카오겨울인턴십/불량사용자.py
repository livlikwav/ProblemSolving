'''
1시간 5분 걸렸음.
dfs로 완전탐색하는 아이디어를 어떻게 깔끔하게 구현할지 고민하다가 좀 걸린듯. (dfs를 오랜만에 하기도 했고)
또 set(set)이나 set(list)는 불가능하다는 것을 알았음! TypeError: unhashable type: 'list'
'''
def solution(user_id, banned_id):

    # 문자열 패턴 매칭기
    def match(user: str, banned: str) -> bool:
        # 먼저 문자열 길이가 같아야함
        if len(user) != len(banned):
            return False
        
        # 문자 하나씩 순서대로 비교
        for i in range(len(banned)):
            ch = banned[i]
            if ch != '*':
                # 해당 문자 다를경우 바로 False
                if ch != user[i]:
                    return False
        # 모든 조건 만족시 True
        return True
    
    # 하나의 banned ID에 대해서 userID후보 list 만듬
    def get_cand(users: list, bans: list) -> list:
        result = []

        for banned in bans:
            temp = []

            for user in users:
                if match(user, banned):
                    temp.append(user)
            
            result.append((banned, temp))
            
        return result
    
    data = get_cand(user_id, banned_id)

    # 불량 아이디 갯수
    length = len(banned_id)

    # 각 후보 아이디 갯수 담은 배열 만들기
    num_of_cand = []
    for i in range(length):
        num_of_cand.append(len(data[i][1]))
    
    result = []

    def dfs(temp: list, level: int):
        if level == length:
            # 현재 temp 리스트를 set으로 변환
            temp = set(temp)
            # set의 길이가 불량 사용자 갯수와 맞는지 확인
            if len(temp) == len(banned_id):
                # 아마 중복되는 조합이 result에 있는지 확인
                if temp not in result:
                    result.append(temp)
            return
        
        for i in range(num_of_cand[level]):
            next = temp + [data[level][1][i]]
            dfs(next, level + 1)
        
    # dfs 수행
    start = 0
    for i in range(num_of_cand[start]):
        # 첫번째 원소의 각 경우의 수로 dfs를 시작함
        dfs([data[start][1][i]], 1)

    answer = len(result)
    return answer







# solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
# solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])
# solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
# solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "*****", "******"])