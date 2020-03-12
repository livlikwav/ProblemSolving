import java.io.*;
import java.util.*;

public class Main { //Programmers sort #2
	public static void main(String[] args) throws IOException{
		
		int[] numbers = {3, 30, 34, 5, 9};
		
		System.out.println(solution(numbers));
	}
	
	static String makefour(String str) {
		if(str.equals("0")){
			return str;
		}
		
		StringBuilder sb = new StringBuilder(str);
		switch(str.length()) {
		case 1:
			sb.append(str);sb.append(str);sb.append(str);
			str = sb.toString();
			break;
		case 2:
			sb.append(str);
			str = sb.toString();
			break;
		case 3:
			sb.append(str.substring(0, 1));
			str = sb.toString();
			break;
		default: //4
			str = sb.toString();
			break;
		}
		return str;
	}
	
	static String solution(int[] numbers) {

		int limit = numbers.length;

		String[] str = new String[limit];
		for(int i = 0; i < limit; i++) {
			str[i] = Integer.toString(numbers[i]);
		}
		
		Arrays.sort(str, new Comparator<String>() {
			@Override
			public int compare(String s1, String s2) {
				String t1 = makefour(s1);
				String t2 = makefour(s2);
				return (t2).compareTo(t1);
			}
		});
		
		StringBuilder sb = new StringBuilder();
		for(int i = 0; i < str.length; i++) {
			if(i == 0 && str[i].equals("0")) {
				return "0";
			}
			sb.append(str[i]);
		}
		String answer = sb.toString();
		
		
		return answer;
	}
}
