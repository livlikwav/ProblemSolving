import java.io.*;
import java.util.*;

public class Main { //BOJ1929
	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		//INPUT
		StringTokenizer st = new StringTokenizer(br.readLine());
		int M = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());
		br.close();
		
		Eratosthenes(M, N);
	}
	
	static public void Eratosthenes(int M, int N) {
		boolean[] sieve = new boolean[N+1];
		//init boolean[]
		for(int i = 0; i < N+1; i++) {
			sieve[i] = true;
		}
		
		if(N == 1) {
			return;
		}
		
		sieve[0] = false;
		sieve[1] = false;

		//Eratosthenes to 1~N
		for(int k = 2; (int)Math.pow(k, 2) <= N; k++) { // k^2 > N = stop
			if(sieve[k] == true) { // is prime number
				for(int j = 2; k * j <= N; j++) {
					sieve[k * j] = false; // k's multiple = k*2, k*3, ...
				}
			}
		}
		
		//print result
		for(int i = 0; i < N+1; i++) {
			//pick them out by M
			if(i < M) {
				continue;
			}
			if(sieve[i] == true) {
				System.out.println(i);
			}
		}
	}
}
