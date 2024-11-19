package docs.Algorithms.backtracking;

import java.util.*;

public class bfs {
    public static void adjencyList(List<List<Integer>> adj, int s) {
        // ref:
        // https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
        Queue<Integer> q = new LinkedList<Integer>();

        boolean[] visited = new boolean[adj.size()];

        visited[s] = true;
        q.add(s);

        while (!q.isEmpty()) {
            int curr = q.poll();
            System.out.print(curr + " ");

            for (int x : adj.get(curr)) {
                if (!visited[x]) {
                    visited[x] = true;
                    q.add(x);
                }
            }
        }
    }

    static void addEdgeList(List<List<Integer>> adj, int u, int v) {
        adj.get(u).add(v);
        adj.get(v).add(u);
    }

    static class Graph {
        // ref:
        // https://www.geeksforgeeks.org/implementation-of-bfs-using-adjacency-matrix/
        int v; // vertex
        int e; // edge
        int[][] adj;

        Graph(int v, int e) {
            this.v = v;
            this.e = e;
            adj = new int[v][v];
            for (int row = 0; row < v; row++) {
                Arrays.fill(adj[row], 0); // 0 으로 초기화 안해주면?
            }
        }

        void addEdgeMatrix(int start, int e) {
            adj[start][e] = 1;
            adj[e][start] = 1;
        }

        void BFS(int start) {
            boolean[] visited = new boolean[v];
            Arrays.fill(visited, false);

            List<Integer> q = new ArrayList<>();
            q.add(start);
            visited[start] = true;

            int vis;
            while (!q.isEmpty()) {
                vis = q.get(0);

                System.out.print(vis + " ");
                q.remove(q.get(0));

                for (int i = 0; i < v; i++) {
                    if (adj[vis][i] == 1 && (!visited[i])) {
                        q.add(i);
                        visited[i] = true;
                    }
                }
            }
        }
    }

    public static void main(String[] args) {
        // AdjencyList
        int V = 5;

        List<List<Integer>> adj = new ArrayList<>(V);
        for (int i = 0; i < V; i++) {
            adj.add(new ArrayList<>());
        }

        addEdgeList(adj, 0, 1);
        addEdgeList(adj, 0, 2);
        addEdgeList(adj, 1, 3);
        addEdgeList(adj, 1, 4);
        addEdgeList(adj, 2, 4);

        System.out.println("BFS adjencyList from 0:");
        adjencyList(adj, 0);

        // AdjencyMatrix
        int vv = 5, ee = 4;

        Graph G = new Graph(vv, ee);

        G.addEdgeMatrix(0, 1);
        G.addEdgeMatrix(0, 2);
        G.addEdgeMatrix(1, 3);

        G.BFS(0);
    }
}
