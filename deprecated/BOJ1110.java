import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {	//BOJ1110
	static int cnt = 0;
    public static void main(String[] agrs) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        
        //TEST
       // System.out.println(N);
       // System.out.println("ans : " + cycle(55));
        int tmp = N;
        do {
        	tmp = cycle(tmp);
        	cnt++;
        }while(tmp != N);
        
        System.out.println(cnt);
        
    }
    
    static int cycle(int N) {
    	int ans = 0;

    	StringBuilder sb = new StringBuilder();
		String[] S;
    	if(N < 10) {
    		S = new String[2];
    		S[0] = "0";
    		S[1] = Integer.toString(N);
    	}else {
        	S = Integer.toString(N).split("");
    	}
    	
        sb.append(S[1]);
        sb.append(Integer.toString((Integer.parseInt(S[0]) + Integer.parseInt(S[1])) % 10));
        ans = Integer.parseInt(sb.toString());
        
    	return ans;
    }
}





