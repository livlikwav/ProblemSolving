import java.io.*;
import java.util.*;

public class Main {//BOJ1037
	
    public static void main(String[] agrs) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] nums = new int[N];
        for(int i = 0; i < N; i++) {
        	nums[i] = Integer.parseInt(st.nextToken());
        }
        //System.out.println(N);
        //System.out.println(Arrays.toString(nums));

        Arrays.sort(nums);
        if(N == 1) {
        	System.out.println(nums[0] * nums[0]);
        }else {
        	System.out.println(nums[0] * nums[N-1]);
        }
    }
}