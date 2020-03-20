import java.io.*;
import java.util.*;

public class Main {//BOJ1912 better to use DP
	
    public static void main(String[] agrs) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int tmp = Integer.parseInt(st.nextToken());
        int max = tmp;
        
        while(st.hasMoreTokens()) {
        	int i = Integer.parseInt(st.nextToken());

        	if(tmp + i >= 0) {
        		if(tmp >= 0) {
            		tmp = tmp + i;
        		}else {
        			tmp = i;
        		}
        	}else {
        		tmp = i;
        	}
        	
        	if(max < tmp) {
        		max = tmp;
        	}
        }
        System.out.println(max);

    }
}