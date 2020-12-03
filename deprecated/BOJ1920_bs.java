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
			if(binarySearch(nums, 0, nums.length - 1, x[i]) == 1) {
				bw.write("1\n");
			}
			else {
				bw.write("0\n");
			}
		}

		br.close();
        bw.close();
	}
	
	static int binarySearch(int[] array, int from, int to, int target) {//parameter : sorted array
		int mid = (from + to) / 2;
		
		if(from <= to) {
			if(array[mid] == target) {
				return 1; //there is an answer
			}else if(array[mid] < target){ //go right
				return binarySearch(array, mid + 1, to,target);
			}else {//go left
				return binarySearch(array, from, mid - 1,target);
			}
		}else {
			return 0; //there is no answer
		}
	}
}
