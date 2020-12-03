import java.io.*;
import java.util.*;

public class Main {//programmers heap #1
	
    public static void main(String[] agrs) throws IOException{
        //BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //StringTokenizer st = new StringTokenizer(br.readLine());
        
        /*
        {1, 2, 3, 9, 10, 12}
        7
        
        */
        
        int[] scoville = {1, 2, 3, 9, 10, 12};
        int K = 7;

        solution(scoville, K);
    }
    
    static int solution(int[] scoville, int K) {
    	
    	PriorityQueue<Integer> heap = new PriorityQueue<Integer>();
    	for(int i = 0; i < scoville.length; i++) {
    		heap.offer(scoville[i]);
    	}
    	
    	int answer = 0;
    	
    	while(heap.peek() < K) {
    		//DEBUG
    		/*
    		Iterator<Integer> iter = heap.iterator();
    		while(iter.hasNext()) {
    			System.out.print(iter.next()+ " ");
    		}
    		System.out.println();
    		*/
    		if(heap.size() == 1) {
    			answer = -1;
    			break;
    		}
    		
    		int n = heap.poll();
    		int m = heap.poll();
    		heap.offer(n + m * 2);
    		answer++;
    	}
    	//DEBUG
    	/*
		Iterator<Integer> iter = heap.iterator();
		while(iter.hasNext()) {
			System.out.print(iter.next()+ " ");
		}
		System.out.println();
		*/
    	return answer;
    }
}

