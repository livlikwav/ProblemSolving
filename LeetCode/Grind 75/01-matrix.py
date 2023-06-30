from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # THIRD SOLUTION: BFS from first nodes list of all 0 nodes
        # SUCCESS!!! 38min elapsed
        # Key: Backtracking 밖에 안 보이는데, 매 노드는 확인하지 않을 것 같고 ... 0 만 먼저 쫙 넣으면 ...?
        # TC O(10^4 * 2) SC O(10^4 * 2)
        m = len(mat)
        n = len(mat[0])

        result = [[0] * n for _ in range(m)]
        visited = [[False] * n for _ in range(m)]

        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        q = deque([])

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    visited[i][j] = True

        while q:
            x, y, dis = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                if visited[nx][ny] == True:
                    continue

                visited[nx][ny] = True
                result[nx][ny] = dis + 1
                q.append((nx, ny, dis + 1))

        return result

        # Rated #2: Python DP with white board explanation EASY
        # 이걸 DP 로도 생각할 수 있구나 ㄷㄷ 오히려 다른 답변은 DP 가 더 많았던게 신기하다!
        # for loop 를 돌면서 체크하는 방향에 따라서 이전 dp 값에 거리를 더해준다. 0 이면 그냥 0 으로 둔다.
        # TC O(10^4 * 2) SC O(1) mat 는 인자라서 안친다고 할 경우에;;
        rows = len(mat)
        cols = len(mat[0])
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] != 0:
                    top = mat[i - 1][j] if i > 0 else float("inf")
                    left = mat[i][j - 1] if i > 0 else float("inf")
                    mat[i][j] = min(top, right) + 1
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if mat[i][j] != 0:
                    right = mat[i][j + 1] if j < cols - 1 else float("inf")
                    down = mat[i + 1][j] if i < rows - 1 else float("inf")
                    mat[i][j] = min(mat[i][j], min(left, down) + 1)
        return mat

        # Rated #1: 나와 동일한 아이디어
        # mat 리스트를 재활용해서 SC 측면에서는 더 효율적이다.
        Row, Col = len(mat), len(mat[0])
        queue = []
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for i in range(Row):
            for j in range(Col):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = "*"

        for r, c in queue:
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                if 0 <= row < Row and 0 <= col < Col and mat[row][col] == "*":
                    mat[row][col] = mat[r][c] + 1
                    queue.append((row, col))
        return mat

        # SECOND SOLUTION: BFS for all node: TIME EXCEEDED
        # TC O(10^4^(10^4)) BFS 가 노드 갯수만큼 이니까 10^4 인데, 이거를 모든 노드 갯수만큼 반복
        # 이걸 10^8 이라고 잘못 생각해서, 이 방법대로 푸느라 시간을 더 소비했다. 경계조건 생각부터 잘 하기
        # SC O(10^4 * 2) result, visited

        # m = len(mat)
        # n = len(mat[0])

        # result = [[0] * n for _ in range(m)]

        # dx = [0, 0, -1, 1]
        # dy = [-1, 1, 0, 0]

        # def bfs(x, y) -> int:
        #     if mat[x][y] == 0:
        #         return 0

        #     visited = [[False] * n for _ in range(m)]

        #     q = deque([(x, y, 0)])

        #     while q:
        #         ix, iy, dis = q.popleft()

        #         for i in range(4):
        #             nx = ix + dx[i]
        #             ny = iy + dy[i]
        #             if nx < 0 or ny < 0 or nx >= m or ny >= n:
        #                 continue
        #             if visited[nx][ny] == True:
        #                 continue

        #             if mat[nx][ny] == 0: # Find
        #                 return dis + 1

        #             visited[nx][ny] = True
        #             q.append((nx, ny, dis + 1))

        #     return -1 # ERR

        # for i in range(m):
        #     for j in range(n):
        #         result[i][j] = bfs(i,j)
        # return result

        # FIRST SOLUTION: GREEDY: FAILED BECAUSE IS INVALID
        # MISSED #1: 첫 노드가 0 이 아닐 수 있다
        # MISSED #2: 멀리 떨어진 두 0 사이의 거리가 잘못 계산된다.
        # m = len(mat)
        # n = len(mat[0])

        # visited = [[False] * n for _ in range(m)]
        # result = [[0] * n for _ in range(m)]

        # result[0][0] = 0
        # visited[0][0] = True
        # q = deque([(0,0)])

        # while q:
        #     x, y = q.popleft()

        #     for i in range(4):
        #         nx = x + dx[i]
        #         ny = y + dy[i]

        #         if visited[nx][ny] == False:
        #             next_dis = result[x][y] + 1
        #             if mat[nx][ny] == 0:
        #                 next_dis = 0

        #             result[nx][ny] = next_dis
        #             visited[nx][ny] = True
        #             q.append((nx, ny))

        # return result
