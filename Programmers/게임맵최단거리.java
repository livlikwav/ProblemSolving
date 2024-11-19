// DFS, BFS
package Programmers;

import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int[] dx = { 1, -1, 0, 0 };
        int[] dy = { 0, 0, 1, -1 };

        boolean[][] visited = new boolean[maps.length][maps[0].length];

        Queue<int[]> q = new LinkedList<>();
        visited[0][0] = true;
        // 이거 dis 처음에 0 으로 넣었다가 헤맸다.
        // print 찍으면서 문제가 원하는 답 뭔지 예시로 감잡기. 이거는 시작 지점도 +1 해야하는 문제였다.
        q.add(new int[] { 0, 0, 1 }); // x, y, dis

        while (!q.isEmpty()) {
            int[] item = q.poll();

            int x = item[0];
            int y = item[1];
            int dis = item[2];

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx >= 0 && nx < maps.length && ny >= 0 && ny < maps[0].length) {
                    // 많이 푼 답안을 보니, target 도달했는지를 앞으로 빼서 loop 돌기 전에 현재 dis 에서 return 하더라.
                    // 근데 그럼 해당 답 찾기까지 다른 item poll 다 빠지는거 기다리긴 해야함.
                    if (!visited[nx][ny] && maps[nx][ny] == 1) {
                        if (nx == maps.length - 1 && ny == maps[0].length - 1) {
                            return dis + 1;
                        }

                        q.add(new int[] { nx, ny, dis + 1 });
                        visited[nx][ny] = true;
                    }
                }
            }
        }

        return -1;
    }
}

/*
 * 되게 무난하다. 2차원 matrix 에서 특정 점까지 최단 거리 구하는 문제
 * 기억해보자. DFS 는 depth-first, BFS 는 breadth-first
 * DFS recursion 또는 stack(func call stack 처럼) 으로 구현하고
 * BFS 는 queue 로 구현한다.
 * BFS 는 level 별로 모두 탐색하므로 최단거리를 제일 빨리 구할 수 있고,
 * DFS 는 ... 머드라. 풀고 찾아보자.
 * 
 * BFS 할 때는 동서남북 편하니까 i, j 뽑을 array 2개 만들어두고 item 4 loop 만들면 되고
 * 매번 queue 에 담고 뽑아서 이동하면 된다.
 * 이동했을 때 i,j 가 target 이랑 동일하면 return
 * queue 가 empty 되면 -1 return
 * 
 * constraints 를 보면 n, m 은 1 이상 100 이하 = 10000
 * BFS 라 이거는 크게 상관없음 (최단거리를 제일 빨리 찾으니까)
 */