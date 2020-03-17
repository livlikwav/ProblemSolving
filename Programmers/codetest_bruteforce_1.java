import java.io.*;
import java.util.*;

public class Main {	//Programmers bruteforce #1
	static int cnt = 0;
    public static void main(String[] agrs) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //StringTokenizer st = new StringTokenizer(br.readLine());
       // String a = st.nextToken();

        int[] answers = {1, 2, 3, 4, 5};
        System.out.println(Arrays.toString(solution(answers)));

    }
    
    static int[] solution(int[] answers) {
    	StringBuilder sb;
    	
    	sb = new StringBuilder();
    	for(int i = 0; i < 10000/5; i++) {
    		sb.append("12345");
    	}
    	String[] A = sb.toString().split("");
    	
    	sb = new StringBuilder();
    	for(int i = 0; i < 10000/8; i++) {
    		sb.append("21232425");
    	}
    	String[] B = sb.toString().split("");
    	
    	sb = new StringBuilder();
    	for(int i = 0; i < 10000/10; i++) {
    		sb.append("3311224455");
    	}
    	String[] C = sb.toString().split("");
    	
    	String str = Arrays.toString(answers);
    	str = str.substring(1, str.length() - 1).replace(", ", "");
    	if(str.length() < 10000) {
    		sb = new StringBuilder(str);
    		for(int i = 0; i < 10000-str.length(); i++) {
    			sb.append("-");
    		}
    		str = sb.toString();
    	}
    	String[] X = str.split("");
    	
    	int[] cnt = new int[3];
    	for(int i = 0; i < 10000; i++) {
    		String x = X[i];
    		if(x.equals(A[i])) {
    			cnt[0]++;
    		}
    		if(x.equals(B[i])) {
    			cnt[1]++;
    		}
    		if(x.equals(C[i])) {
    			cnt[2]++;
    		}
    	}
    	
    	LinkedList<Integer> ans = new LinkedList<Integer>();
    	int max = cnt[0];
    	for(int i = 0; i < 3; i++) {
    		if(max == cnt[i]) {
    			ans.add(i);
    		}else if(max < cnt[i]){
    			ans.clear();
    			ans.add(i);
    			max = cnt[i];
    		}
    	}
    	int size = ans.size();
    	int[] answer = new int[size];
    	
    	for(int i = 0; i < size; i++) {
    		answer[i] = ans.pop() + 1;
    	}
    	return answer;
    }
}
/*
better code : i % a.length to make loop
for(int i=0; i<answer.length; i++) {
            if(answer[i] == a[i%a.length]) {score[0]++;}
            if(answer[i] == b[i%b.length]) {score[1]++;}
            if(answer[i] == c[i%c.length]) {score[2]++;}
        }
        int maxScore = Math.max(score[0], Math.max(score[1], score[2]));
        ArrayList<Integer> list = new ArrayList<>();
        if(maxScore == score[0]) {list.add(1);}
        if(maxScore == score[1]) {list.add(2);}
        if(maxScore == score[2]) {list.add(3);}
*/




