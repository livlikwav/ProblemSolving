import java.io.*;
import java.util.*;

public class Main {//BOJ1085
	//문제 잘 읽기. 서쪽 남쪽으로도 가능 
    public static void main(String[] agrs) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());
        
        System.out.println(Math.min(Math.min(w-x, h-y), Math.min(x, y)));
        
        
    }
}