import java.io.*;
import java.util.*;

public class Main { //BOJ2798
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		String s = br.readLine();
		StringTokenizer st = new StringTokenizer(s);
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		s = br.readLine();
		st = new StringTokenizer(s);
		int[] cards = new int[N];
		for (int i = 0; i < N; i++) {
			cards[i] = Integer.parseInt(st.nextToken());
		}
		
		//CHECK INPUT
		/*
		System.out.println("N= " + Integer.toString(N));
		System.out.println("M= " + Integer.toString(M));
		for (int i = 0; i < N; i++) {
			System.out.print(Integer.toString(cards[i])+" ");
		}
		*/
		
		int max = 0;
		
		for(int i = 0; i < N-2; i++) {
			for(int j = i+1; j < N-1; j++) {
				for(int m = j+1; m < N; m++) {
					int tmp = cards[i] + cards[j] + cards[m];
			    	if(max < tmp && tmp <= M) {
				    	max = tmp;
				    }
				}
			}
		}
		
		bw.write(Integer.toString(max));
		
        bw.close();
		br.close();
	}
}

