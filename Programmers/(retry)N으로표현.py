'''
1시간 넘게 소요됨. 답 확인하고 다시 풀음. 다음에 다시 풀 필요가 있다. retry -> fin
작은 부분 문제의 답을 저장해놓고, 반복해서 사용하는 것이 dp라고 할 수 있다.
달랐던 점은, 모든 경우의 수의 set을 담는다는 것이다.

점화식을 캐치하기 위한 포인트는 1) 사칙연산, 2) N을 연달아 붙여서 쓰는 것. 2개로 n번째 set이 결정된다는 것이다.
'''
def solution(N, number):
    dp = [{}, {N}, {int(str(N)*2), N*N, N//N, N+N}] # 0은 빼고 넣는다
    
    if number in dp[1]:
        return 1
    if number in dp[2]:
        return 2

    for i in range(3, 9): # 최솟값 8까지만 체크함
        # N을 i번 연달아 붙인 것부터 넣어둠
        data = set()
        data.add(int(str(N)*i))

        # dp[n]은 1 연산 n-1, 2 연산 n-2 ... n-1 연산 1 다 해본거
        for j in range(1, i):
            left = j
            right = i-j

            for x in dp[left]:
                for y in dp[right]:
                    data.add(x + y)
                    data.add(x - y)
                    data.add(x * y)
                    data.add(x // y)
        
        print(data)

        # 현재 배열에 number(답)이 존재하는 경우 바로 return
        if number in data:
            return i
        # dp 배열에 추가 후 continue
        else:
            data.remove(0) # 0은 빼준다
            dp.append(data)

    # N을 9개 이상 사용한 경우 -1 return
    answer = -1
    return answer