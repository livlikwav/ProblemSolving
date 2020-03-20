import java.io.*;
import java.util.*;

public class Main {//BOJ16282
	
    public static void main(String[] agrs) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long N = Long.parseLong(br.readLine());
        //System.out.println(N);

        for(long i = 1; i <= 64; i++) {
        	long tmp = (i + 1) * ((long)Math.pow(2, i+1) - 1) + i;
        	if(N <= tmp) {
        		System.out.println(i);
        		break;
        	}
        }
    }
}