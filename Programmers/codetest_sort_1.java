import java.io.*;
import java.util.*;

public class Main { //Programmers Kth num
	public static void main(String[] args) throws IOException{
		
		int[][] commands = {{2, 5, 3}, {4, 4, 1}, {1, 7, 3}};
		int[] array = {1, 5, 2, 6, 3, 7, 4};
		
		System.out.println(Arrays.toString(solution(array, commands)));
	}
	
	static int[] solution(int[] array, int[][] commands) {
		int num = commands.length;
        int[] answer = new int[num];
        
        for(int x = 0; x < num; x++){
            int i = commands[x][0];
            int j = commands[x][1];
	        int k = commands[x][2];
	           
            int[] tmp = Arrays.copyOfRange(array, i-1, j);
            Arrays.sort(tmp);
	        answer[x] = tmp[k-1];
	    }
	    return answer;
	}
}