import java.io.*;
import java.util.*;
//틀린이유 : 또 조건 생각안함. 0 <= N <= 12, N=0일때 처리, 0! = 1
//for문을 쓰지 않고 재귀함수를 해야한다
//내 생각 : if i == 1을 이용해서 1까지 가면 재귀 안하고 그대로 출력하는 식으로 빠져나가게 해둬야함.
public class Main { //BOJ10872
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		if(0 <= N || N <= 12) {
			System.out.println(factorial(N));
		}
	}
	// f(N) > f(N-1) * N > f(N-2) * N-1 * N > 1 * 2 * 3... N-1 * N
	static int factorial(int n) {
		if (n == 1 || n == 0) {
			return 1;
		}
		else {
			return n * factorial(n - 1);
		}
	}
}