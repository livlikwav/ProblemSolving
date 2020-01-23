import java.io.*;
import java.util.*;

public class Main { //BOJ16769
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int[] milk = new int[3];
		int[] cap = new int[3];
		
    	for(int i = 0; i < 3; i++) {
    		String s = br.readLine();
    		StringTokenizer st = new StringTokenizer(s);
    		cap[i] = Integer.parseInt(st.nextToken());
    		milk[i] = Integer.parseInt(st.nextToken());
    	}
    	/*
	    for(int i = 0; i < 3; i++) {
	    	bw.write(Integer.toString(milk[i])+" ");
	    }
	    bw.write("\n");
	    for(int i = 0; i < 3; i++) {
	    	bw.write(Integer.toString(cap[i])+" ");
	    }
	    bw.write("\n");
	    */
    	//INPUT COMPLETE
	    
	    int loop = 0;
	    while(loop < 100) {
	    	int sum = 0;
    		sum = milk[loop % 3] + milk[(loop + 1)% 3];
    		if(sum <= cap[(loop + 1)% 3]) {
    			milk[loop % 3] = 0;
    			milk[(loop + 1)% 3] = sum;
    		}
    		else {
    			milk[loop % 3] = sum - cap[(loop + 1)% 3];
    			milk[(loop + 1)% 3] = cap[(loop + 1)% 3];
    		}
	    	
	    	//DEBUG
	    	/*
			bw.write("loop=" + Integer.toString(loop + 1)+" ");
			bw.write(Integer.toString(milk[0])+" ");
			bw.write(Integer.toString(milk[1])+" ");
			bw.write(Integer.toString(milk[2])+"\n");
			*/
	    	loop = loop + 1;
	    }

		bw.write(Integer.toString(milk[0])+"\n");
		bw.write(Integer.toString(milk[1])+"\n");
		bw.write(Integer.toString(milk[2])+"\n");
		
		bw.close();
		br.close();
	}
}