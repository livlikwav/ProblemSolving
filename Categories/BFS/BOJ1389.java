import java.io.*;
import java.util.*;

public class Main { //BOJ1389
	
	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		ArrayList<ArrayList<Integer>> adj = new ArrayList<ArrayList<Integer>>();
		
		for(int i = 0; i < N; i++) {
			adj.add(new ArrayList<Integer>());
		}
		
		for(int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken()) - 1; //people number 1~5 > 0~4
			int y = Integer.parseInt(st.nextToken()) - 1;
			//undirected graph
			adj.get(x).add(y);
			adj.get(y).add(x);
		}
		
		//INPUT DEBUG
        /*
		for(int i = 0; i < N; i++) {
			System.out.print(i + " : ");
			Iterator<Integer> iter = adj.get(i).iterator();
			while(iter.hasNext()) {
				System.out.print(iter.next()+" ");
			}
			System.out.println();
		}
		*/
		
		//DEBUG
		//System.out.println("util : " + BFSutil(adj, 2, 0));
		//System.out.println("util : " + BFSutil(adj, 2, 1));
		//System.out.println("util : " + BFSutil(adj, 2, 3));
		//System.out.println("util : " + BFSutil(adj, 2, 4));
		
		//select person who has min #
		int min = 100000; //pseudo max # of sum
		int min_idx = 0;
		
		for(int i = 0; i < N; i++) {
			int sum = 0;
			
			for(int j = 0; j < N; j++) {
				if(i == j) {
					continue;
				}
				int tmp = BFSutil(adj, i, j);
				sum += tmp;
			}
			if(sum < min) {
				min = sum;
				min_idx = i;
			}
		}
		System.out.println((min_idx + 1));
		
		br.close();
	}
	
	static public int BFSutil(ArrayList<ArrayList<Integer>> adj, int start, int target) {
		LinkedList<Integer> queue = new LinkedList<Integer>();
		boolean[] visited = new boolean[adj.size()];
		int[] distance = new int[adj.size()];
		for(int i = 0; i < adj.size(); i++) {
			visited[i] = false; //init by false
			distance[i] = -1;
		}
		
		queue.add(start);
		distance[start] = 0;
		
		while(!queue.isEmpty()) {
			
			int k = queue.poll();
			
			if(k == target) {
				return distance[k];
			}
			
			visited[k] = true;
			//System.out.println(k);
			
			Iterator<Integer> iter = adj.get(k).iterator();
            while(iter.hasNext()) {
            	int tmp = iter.next();
            	
            	if(!visited[tmp]) {
            		queue.add(tmp);
            		visited[tmp] = true;
            		distance[tmp] = distance[k] + 1;
            	}
            }
		}
		
		return -1; //never happen that there is no friends
	}
}