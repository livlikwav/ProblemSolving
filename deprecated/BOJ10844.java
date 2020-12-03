import java.io.*;
import java.util.*;

public class Main {//BOJ10844
	static final int DIVISOR = 1000000000;
	
    public static void main(String[] agrs) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        //System.out.println(N);
        //Dynamic Programming - bottom up
        int[] nums = new int[1000];
        nums[0] = 0;
        nums[1] = 1;
        nums[2] = 1;
        nums[3] = 1;
        nums[4] = 1;
        nums[5] = 1;
        nums[6] = 1;
        nums[7] = 1;
        nums[8] = 1;
        nums[9] = 1;
        
        for(int i = 1; i <= (N-1); i++) {
        	nums[i*10 + 0] = nums[(i-1)*10 + 1] % DIVISOR;
        	nums[i*10 + 1] = (nums[(i-1)*10 + 0] + nums[(i-1)*10 + 2]) % DIVISOR;
        	nums[i*10 + 2] = (nums[(i-1)*10 + 1] + nums[(i-1)*10 + 3]) % DIVISOR;
        	nums[i*10 + 3] = (nums[(i-1)*10 + 2] + nums[(i-1)*10 + 4]) % DIVISOR;
        	nums[i*10 + 4] = (nums[(i-1)*10 + 3] + nums[(i-1)*10 + 5]) % DIVISOR;
        	nums[i*10 + 5] = (nums[(i-1)*10 + 4] + nums[(i-1)*10 + 6]) % DIVISOR;
        	nums[i*10 + 6] = (nums[(i-1)*10 + 5] + nums[(i-1)*10 + 7]) % DIVISOR;
        	nums[i*10 + 7] = (nums[(i-1)*10 + 6] + nums[(i-1)*10 + 8]) % DIVISOR;
        	nums[i*10 + 8] = (nums[(i-1)*10 + 7] + nums[(i-1)*10 + 9]) % DIVISOR;
        	nums[i*10 + 9] = (nums[(i-1)*10 + 8]) % DIVISOR;
        }
        
        int ans = 0;
        for(int i = 0; i <= 9; i++) {
        	ans += nums[(N-1)*10 + i];
        	ans = ans % DIVISOR;
        }
     
        System.out.println(ans);
        
    }
}