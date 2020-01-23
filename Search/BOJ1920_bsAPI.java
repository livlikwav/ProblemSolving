import java.io.*;
import java.util.*;

public class Main { //BOJ1920
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		//INPUT
		int N = Integer.parseInt(br.readLine());
		int[] nums = new int[N];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}
		
		int M = Integer.parseInt(br.readLine());
		int[] x = new int[M];
		
		st = new StringTokenizer(br.readLine());
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
		
		//DO BINARY SEARCH
		Arrays.sort(nums);
		
		for(int i = 0; i < M; i++) { //x
			if(Arrays.binarySearch(nums, x[i]) >= 0) {
				bw.write("1\n");
			}
			else {
				bw.write("0\n");
			}
		}

		br.close();
		bw.flush();
        bw.close();
	}
}
