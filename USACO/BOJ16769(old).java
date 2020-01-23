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
	    	
	    	switch(loop % 3) {
	    	case 0:
	    		sum = milk[0] + milk[1];
	    		if(sum <= cap[1]) {
	    			milk[0] = 0;
	    			milk[1] = sum;
	    		}
	    		else {
	    			milk[0] = sum - cap[1];
	    			milk[1] = cap[1];
	    		}
	    		break;
	    	case 1:
	    		sum = milk[1] + milk[2];
	    		if(sum <= cap[2]) {
	    			milk[1] = 0;
	    			milk[2] = sum;
	    		}
	    		else {
	    			milk[1] = sum - cap[2];
	    			milk[2] = cap[2];
	    		}
	    		break;
	    	case 2:
	    		sum = milk[2] + milk[0];
	    		if(sum <= cap[0]) {
	    			milk[2] = 0;
	    			milk[0] = sum;
	    		}
	    		else {
	    			milk[2] = sum - cap[0];
	    			milk[0] = cap[0];
	    		}
	    		break;
	    	default:
	    		break;
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