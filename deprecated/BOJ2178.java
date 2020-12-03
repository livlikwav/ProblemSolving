import java.io.*;
import java.util.*;

public class Main { //BOJ2178
	static int N = 0;
	static int M = 0;
	
	public static void main(String[] args) throws IOException{
		
		Scanner sc = new Scanner(System.in);

		StringTokenizer st = new StringTokenizer(sc.nextLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		ArrayList<Integer> adj = new ArrayList<Integer>();

		for(int i = 0; i < N; i++) {
			String s = sc.nextLine();
			String[] S = s.split("");
			for(int j = 0; j < M; j++) {
				adj.add(Integer.parseInt(S[j]));
			}
		}
		
		//INPUT DEBUG
        /*
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				System.out.print(adj.get(getPos(i, j)) + " ");
			}
			System.out.println();
		}
		*/
		
		
		System.out.println(BFS(adj));
		
		sc.close();
	}
	// FIX : start (0,0) end (N, M)
	public static int BFS(ArrayList<Integer> adj) {
		LinkedList<Integer> queue = new LinkedList<Integer>();
		boolean[] visited = new boolean[adj.size()];
		int[] distance = new int[adj.size()];
		
		for(int i = 0; i < adj.size(); i++) {
			visited[i] = false;
			distance[i] = 1;
		}
		
		queue.add(getPos(0,0));
		
		while(!queue.isEmpty()) {
			
			int k = queue.poll();
			
        	//System.out.println(k);
			
			if(visited[k]) {
				continue;
			}
			
			visited[k] = true;
			
			
			//UP pos(i-1,j) = pos - M
			if(k - M > 0) { // is it out of map?
				int tmp_val = adj.get(k - M);
				int tmp_pos = k - M;
				if(tmp_val == 1) { //ok to go
					if(!visited[tmp_pos]) {
						distance[tmp_pos] = distance[k] + 1;
		            	queue.add(tmp_pos);
					}
	            }
			}
			
			//DOWN pos(i+1,j) = pos + M
			if(k + M < N*M) { // is it out of map?
				int tmp_val = adj.get(k + M);
				int tmp_pos = k + M;
				if(tmp_val == 1) { //ok to go
					if(!visited[tmp_pos]) {
						distance[tmp_pos] = distance[k] + 1;
		            	queue.add(tmp_pos);
					}
	            }
			}
			//LEFT pos(i,j-1)
			if((k % M) > 0) { // is it out of map?
				int tmp_val = adj.get(k - 1);
				int tmp_pos = k - 1;
				if(tmp_val == 1) { //ok to go
					if(!visited[tmp_pos]) {
						distance[tmp_pos] = distance[k] + 1;
		            	queue.add(tmp_pos);
					}
				}
			}
			
			//RIGHT pos(i,j+1)
			if((k % M) < M - 1) { // is it out of map?
				int tmp_val = adj.get(k + 1);
				int tmp_pos = k + 1;
				if(tmp_val == 1) { //ok to go
					if(!visited[tmp_pos]) {
						distance[tmp_pos] = distance[k] + 1;
		            	queue.add(tmp_pos);
					}
				}
			}
		}
		
		return distance[getPos(N-1,M-1)];
	}
	
	public static int getPos(int i, int j) {
		// adjacency matrix
		// start from (0,0) to (N-1, M-1)
		
		return i * M + j;
	}
}