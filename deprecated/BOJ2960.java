import java.io.*;
import java.util.*;

public class Main {//BOJ2960
	
    public static void main(String[] agrs) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] nums = new int[N+1];
        for(int i = 0; i <= N; i++) {
        	nums[i] = 1;
        }
        nums[0] = 0;
        nums[1] = 0;

        //TEST
        //System.out.println(Arrays.toString(nums));
        
        int cnt = 0;
        
        for(int i = 2; i <= N; i++) {
        	for(int j = 1; j <= N/i; j++) {
        		if(nums[i*j] == 1) {
            		cnt++;
            		nums[i*j] = 0;
            		//System.out.println(i*j);
            		if(cnt == K) {
            			System.out.println(i*j);
            		}
            	}
        	}
        }

    }
}