import java.io.*;
import java.util.*;

public class Main { //programmers hash #1
	
	public static void main(String[] args) throws IOException{
		
		Scanner sc = new Scanner(System.in);

		String[] part = {"mislav", "stanko", "mislav", "ana"};
		String[] com = {"stanko", "ana", "mislav"};
		
		Map<String, Integer> map = new HashMap<String, Integer>();
		
		for(int i = 0; i < part.length; i++) {
			String st = part[i];
			if(!map.containsKey(st)) {
				map.put(st, 1);
			}else {
				int tmp = map.get(st);
				map.put(st, tmp+1);
			}
		}
		
		for(int i = 0; i < com.length; i++) {
			String st = com[i];
			if(map.containsKey(st)) {
				int tmp = map.get(st);
				map.put(st, tmp - 1);
			}
		}
		
		Iterator<String> iter = map.keySet().iterator();
		while(iter.hasNext()) {
			String st = iter.next();
			int tmp = map.get(st);
			if(tmp > 0) {
				map.put(st, tmp - 1);
				System.out.println(st);
			}
		}
		
		sc.close();
	}
}