import java.io.*;
import java.util.*;

public class Main { //BOJ2493
	
	public static long[] heights;
			
	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		Stack<Tower> tower = new Stack<Tower>();
		
		for(int i = 0; i < N; i++) {
			int a = Integer.parseInt(st.nextToken());
			
			while(!tower.isEmpty()) {
			    if(tower.peek().height >= a) {
			    	System.out.print(tower.peek().pos + " ");
			    	break;
			    }
			    tower.pop();
			}
			if(tower.isEmpty()) {
				System.out.print("0 ");
			}
			tower.push(new Tower(a, i + 1));
		}
	}
}

class Tower{
	public int height;
	public int pos;
	public Tower(int height, int pos) {
		this.height = height;
		this.pos = pos;
	}
}