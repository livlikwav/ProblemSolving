def solution(n, computers):
    # 컴퓨터의 갯수가 n개
    # i -> j 가 컴퓨터가 연결되어있다는 뜻이다.
    
    visited = [False] * n
    result = [0] * n
    cnt = 0
    
    def dfs(i):
        # 방문처리 + 네트워크 처리
        visited[i] = True
        result[i] = cnt
        
        for idx in range(n):                
            # 연결되어 있을때
            if computers[i][idx] == 1:
                # 방문하지 않았고 == 아직 네트워크 포함안되어있을때
                if not visited[idx]:
                    dfs(idx) # recursive
    
    # dfs를 모든 컴퓨터에 대해서 적용한다.
    for i in range(n):
        # 방문안한 컴퓨터만 새로운 네트워크로 시작함
        if not visited[i]:
            cnt += 1 # 새 네트워크 체크
            dfs(i)
                    
    return cnt