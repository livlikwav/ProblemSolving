import java.io.*;
import java.util.*;

public class Main { //BOJ6603 by DFS
	public static int[] nums;
	
	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		while(true) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			
			// test case is ended by inputing 0
			if(N == 0) { 
				break;
			}
			
			nums = new int[N];
			for(int i = 0; i < N; i++) {
				nums[i] = Integer.parseInt(st.nextToken());
			}
			//Back Tracking
			for(int i = 0; i < N; i++) {
				DFS(i, "", 0);
			}
		    System.out.println(); //plus escape sequence
		}
		

		br.close();
	}
		
    public static void DFS(int start, String str, int depth) {
    	
    	str = str + nums[start] + " ";
    	depth++;
    	
    	if(depth == 6) {
    		System.out.println(str);
    		return;
    	}
    	
    	for(int i = start + 1; i < nums.length; i++) {
    		DFS(i, str, depth);
    	}
    }
}