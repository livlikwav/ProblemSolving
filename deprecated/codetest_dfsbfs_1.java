import java.io.*;
import java.util.*;

public class Main { //Programmers DFS, BFS #1
	static int cnt = 0;
	static int lvl = 0;
	public static void main(String[] args) throws IOException{
		

		int[] numbers = {1, 1, 1, 1, 1, 1};
		int target = 2;
		
		solution(numbers, target);
	}
	
	static int solution(int[] numbers, int target) {
		int answer = 0;
		
		lvl = numbers.length;
		DFS(numbers, 0, 0, 0, target);
		
		System.out.println(cnt);
		
		return answer;
	}
	
	static void DFS(int[] numbers, int x, int idx, int depth, int target) {
		
		if(depth < lvl) {
			int tmp1 = x + numbers[idx];
			int tmp2 = x - numbers[idx];
			idx++;
			depth++;
			//System.out.println(tmp1 + " " + tmp2 + " " + idx + " " + depth + " " + target);
			DFS(numbers, tmp1, idx, depth, target);
			DFS(numbers, tmp2, idx, depth, target);
		}else {
			if(x == target) {
				cnt++;
			}
		}
	}
}