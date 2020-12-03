import java.io.*;
import java.util.*;

public class Main { //BOJ1920
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		//INPUT N nums
		int N = Integer.parseInt(br.readLine());
		String s = br.readLine();
		StringTokenizer st = new StringTokenizer(s);
		int[] nums = new int[N];
		for (int i = 0; i < N; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}
		// INPUT M nums
		int M = Integer.parseInt(br.readLine());
		s = br.readLine();
		st = new StringTokenizer(s);
		int[] x = new int[M];
		for (int i = 0; i < M; i++) {
			x[i] = Integer.parseInt(st.nextToken());
		}
		
		//CHECK INPUT
		/*
		System.out.println("N= " + Integer.toString(N));
		for (int i = 0; i < N; i++) {
			System.out.print(Integer.toString(nums[i])+" ");
		}
		System.out.println("M= " + Integer.toString(M));
		for (int i = 0; i < M; i++) {
			System.out.print(Integer.toString(x[i])+" ");
		}
		*/
		
		//GET ANS
		Arrays.sort(nums);
		
		for(int i = 0; i < M; i++) { //x
			int flag = 0;
			
			for(int j = 0; j < N; j++) { //nums loop
				if(nums[j] > x[i]) {
					break;
				}
				else if(nums[j] == x[i]) {
					flag = 1;
					break;
				}
				else {
					//CONTINUE
				}
			}
			
			if(flag == 1) {
				bw.write("1\n");
			}
			else {
				bw.write("0\n");
			}
		}
        
        bw.close();
		br.close();
	}
}
