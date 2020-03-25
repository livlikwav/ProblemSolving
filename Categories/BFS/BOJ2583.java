import java.io.*;
import java.util.*;
// 다음번에는 map matrix를 1차원 배열 아닌, 2차원 배열이나 Class로 풀어보기
// 다음에는 UP DOWN LEFT RIGHT 할때 제대로 그냥 다 분기하기
public class Main {//BOJ2583
	static int M;
	static int N;
	static int K;
	static int[] map;
	static boolean[] visited;
    public static void main(String[] agrs) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        //input first line
        M = Integer.parseInt(st.nextToken()); //row
        N = Integer.parseInt(st.nextToken()); //col
        K = Integer.parseInt(st.nextToken());
        //init map
        map = new int[(M)*(N)];
        for(int i = 0; i <N*M; i++ ) {
        	map[i] = 0; // 0: empty, 1: filled
        }
       visited = new boolean[(M)*(N)];
        for(int i = 0; i <N*M; i++ ) {
        	visited[i] = false;
        }

        //input each rect
        //printVisited();	
        
        
        for(int i = 0; i < K; i++) {
        	st = new StringTokenizer(br.readLine());
        	int ln = Integer.parseInt(st.nextToken());
        	int lm = Integer.parseInt(st.nextToken());
        	int rn = Integer.parseInt(st.nextToken());
        	int rm = Integer.parseInt(st.nextToken());
        	
        	//set map
        	for(int k = lm; k < rm; k++) {
        		for(int m = ln; m < rn; m++) {
        			map[getIdx(k,m)] = 1;
        			visited[getIdx(k,m)] = true;
        		}
        	}
        }

		//printVisited();
		
		
        int cnt = 0;
        ArrayList<Integer> size = new ArrayList<Integer>(){
        	@Override
    		public String toString() {
    			Iterator<Integer> iter = this.iterator();
    			StringBuilder sb = new StringBuilder();
    			while(iter.hasNext()) {
    				sb.append(iter.next());
    				sb.append(" ");
    			}
    			return sb.toString();
    		}
        };

        
        //DO BFS
        
        for(int i = 0; i < M; i++) {
        	for(int j = 0; j < N; j++) {
        		if(!visited[getIdx(i,j)] && map[getIdx(i,j)] == 0) {
        			cnt++;
        			size.add(BFS(i, j));
        		}
        	}
        }
        
        
        //print answer
        System.out.println(cnt);
        Collections.sort(size);
        System.out.println(size.toString());
        
    }
    
    static int BFS(int i, int j) {
    	//System.out.println("New BFS");
    	int size = 0;
    	Stack<Integer> stack = new Stack<Integer>();

		stack.add(getIdx(i,j));
		int[] dir = {+N, -N, +1, -1};
		
		while(!stack.isEmpty()) {
			/*
			Iterator<Integer> iter = stack.iterator();
			while(iter.hasNext()) {
				System.out.print(iter.next() + " ");
			}
			System.out.println();
			*/
			int idx = stack.pop();
			if(visited[idx] || map[idx] == 1) {
				continue;
			}
			visited[idx] = true;
			size++;
			//printVisited();
			
			//go BFS
			for(int x = 0; x < 4; x++) {
				if(x == 3) {
					if(idx % N == 0) {
						continue;
					}
				}
				if(x == 2) {
					if(idx % N == N-1) {
						continue;
					}
				}
				int newidx = idx + dir[x];
				if((0 <= newidx) && (newidx < N*M)) {// be in map
					if(!visited[newidx] && map[newidx] == 0) { 
						stack.add(newidx);
					}
				}
			}
		}
    	
    	return size;
    }
    
    static int getIdx(int row, int col) {
    	return row*N + col;
    }
    
    static void printMap() {
		System.out.println();
    	for(int i = M-1; i>= 0; i--) {
    		for(int j = 0; j < N; j++) {
    			System.out.print(map[getIdx(i, j)]+ " ");
    		}
    		System.out.println();
    	}
    }
    static void printVisited() {
		System.out.println();
    	for(int i = M-1; i>= 0; i--) {
    		for(int j = 0; j < N; j++) {
    			if(visited[getIdx(i, j)]) {
    				System.out.print("1 ");
    			}else{
    				System.out.print("0 ");
    			}
    		}
    		System.out.println();
    	}
    }
    
}

