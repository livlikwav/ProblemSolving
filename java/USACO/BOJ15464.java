import java.io.*;
import java.util.*;

public class Main { //BOJ15464
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(br.readLine());
        List<String> origin = new ArrayList<>(Arrays.asList(br.readLine().split(" ")));
        List<String> ID = new ArrayList<>(Arrays.asList(br.readLine().split(" ")));
    	
    	for(int t = 0; t < 3; t++) {
    		List<String> tmp = new ArrayList<>();
    		tmp.addAll(ID);
    		for(int i = 0; i < T; i++) {
    			ID.set(i, tmp.get(Integer.parseInt(origin.get(i))-1));
    		}
    	}
    	Iterator<String> itr = ID.iterator();
        while(itr.hasNext()) {
        	bw.write(itr.next());
        	bw.write("\n");
        }
    	
		bw.close();
		br.close();
	}
}