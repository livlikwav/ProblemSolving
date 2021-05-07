'''
54분 동안 풀었음.
왜 제대로 안도는지 도저히 모르겠다. 도움을 청하자 ㅜㅜ
'''
answer = int(1e9)

def solution(board):

    width = len(board)
    target = (width-1, width-1)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def dfs(visited: list, direction: int, cost: int, pos: tuple) -> None:
        global answer
        # print(visited, pos, cost)

        if cost > answer:
            return

        if pos == target:
            answer = min(answer, cost)
            return

        for i in range(4):
            x, y = pos
            nx, ny = x + dx[i], y + dy[i]
            
            # check out of map
            if not (0 <= nx <= width-1 and 0 <= ny <= width-1):
                continue
            # check wall
            if board[nx][ny] == 1:
                continue
            # check visited
            if (nx, ny) in visited:
                continue

            # if start -> no corner
            if pos == (0, 0):
                dfs(visited + [(nx, ny)], i, cost + 100, (nx, ny))
            # same direction -> no corner
            elif i == direction:
                dfs(visited + [(nx, ny)], i, cost + 100, (nx, ny))
            else:
                dfs(visited + [(nx, ny)], i, cost + 600, (nx, ny))
                
    dfs([], 0, 0, (0,0))
    
    return answer

# print(solution([[0,0,0],[0,0,0],[0,0,0]]))
# print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
# print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
# print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))