from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        My solution with BFS
        영어 문제를 잘 읽자 ㅋㅋㅋ 같은 색깔의 4방향 인접 셀만 칠해야한다.
        """
        n = len(image)
        m = len(image[0])

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        q = deque([(sr, sc)])

        while q:
            x, y = q.pop()
            if image[x][y] == color:
                continue

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and image[x][y] == image[nx][ny]:
                    q.append((nx, ny))

            image[x][y] = color

        return image
        """
        Most voted solution with DFS recursion
        """
        start_color = image[sr][sc]

        def flood_fill(x, y):
            if x < 0 or x >= len(image):
                return
            if y < 0 or y >= len(image[0]):
                return

            if image[x][y] == color:
                return
            if image[x][y] != start_color:
                return  # 함수 내 선언한 지역 함수라, 상위 namespace 변수 접근 가능

            image[x][y] = color
            flood_fill(x-1, y)
            flood_fill(x+1, y)
            flood_fill(x, y+1)
            flood_fill(x, y-1)

        flood_fill(sr, sc)
        return image
