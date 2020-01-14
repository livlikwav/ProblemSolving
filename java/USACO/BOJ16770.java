import java.io.*;
import java.util.*;

public class Main { //BOJ16770
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		
		int[] time = new int[1000]; // 0 =< si - 1, ti - 1 < 1000
		int T = Integer.parseInt(br.readLine());
		
    	for(int i = 0; i < T; i++) {
    		int si = 0;
    		int ti = 0;
    		int bi = 0;
    		String s = br.readLine();
    		StringTokenizer st = new StringTokenizer(s);
    		si = Integer.parseInt(st.nextToken()) - 1;
    		ti = Integer.parseInt(st.nextToken()) - 1;
    		bi = Integer.parseInt(st.nextToken());
    		//INPUT ARRAY
    		for(int j = si; j <= ti; j++) {
    			time[j] = time[j] + bi;
    		}
    	}
    	//CHECK ARRAY
    	/*
	    for(int i = 0; i < 1000; i++) {
	    	bw.write(Integer.toString(time[i])+" ");
	    	if(i % 100 == 0 && i != 0) {
	    		bw.write("\n");
	    	}
	    }
	    bw.write("\n");
	    */
	    //FIND MAX
	    Arrays.sort(time);
	    bw.write(Integer.toString(time[time.length - 1]));

		bw.close();
		br.close();
	}
}