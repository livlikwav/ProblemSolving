'''
1시간 45분 동안해서 틀림 ㅎㅎ. 왜 붙잡고 있었는지 ㅎㅎ
'''
def solution(gems):
    # print(gems)

    length = len(gems)
    
    dp = [0] * length
    dp[-1] = (1, 1, [length-1, length-1]) # kind, count, list

    for i in range(length - 2, -1, -1):
        dp[i] = dp[i+1]
        last_kind = dp[i+1][0]
        last_count = dp[i+1][1]
        # 포함
        if gems[i] in set(gems[dp[i+1][2][0]:dp[i+1][2][1]+1]):
            for j in range(last_kind-1, last_count): # kind-1~ count-1
                kind = len(set(gems[i:i+j+1]))
                count = len(gems[i:i+j+1])

                if last_kind == kind:
                    dp[i] = (kind, count, [i, i+j])
                    break
        # 불포함
        else:
            kind = last_kind + 1
            last_idx = dp[i+1][2][1]
            count = last_idx - i + 1
            dp[i] = (kind, count, [i, last_idx])

    # print(dp)

    answer = [dp[0][2][0]+1, dp[0][2][1]+1]
    return answer


# print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# print(solution(["AA", "AB", "AC", "AA", "AC"]))
# print(solution(["XYZ", "XYZ", "XYZ"]))
# print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))