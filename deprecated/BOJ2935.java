import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {	//BOJ2935
	static int cnt = 0;
    public static void main(String[] agrs) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String a = st.nextToken();
        
        st = new StringTokenizer(br.readLine());
        String s = st.nextToken();
        
        st = new StringTokenizer(br.readLine());
        String b = st.nextToken();
        
        StringBuilder sb = new StringBuilder();
        if(s.equals("*")) {
        	sb.append(a);
        	sb.append(b.substring(1, b.length()));
        }else if(s.equals("+")) {
        	if(a.equals(b)) {
        		sb.append("2");
        		sb.append(a.substring(1, a.length()));
        	}else{
        		int max = Math.max(a.length(), b.length());
        		int min = Math.min(a.length(), b.length());
        		for(int i = max; i > 0; i--) {
        			if(i == max || i == min) {
        				sb.append("1");
        				continue;
        			}
        			sb.append("0");
        		}
        	}
        }
        System.out.println(sb.toString());
    }
}





