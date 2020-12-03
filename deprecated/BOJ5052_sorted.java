import java.io.*;
import java.util.*;

public class Main { //BOJ5052
	
	public static void main(String[] args) throws IOException{
		
		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();
		sc.nextLine();
		
		ArrayList<String[]> book = new ArrayList<String[]>();
		for(int i = 0; i < t; i++) {
			int n = sc.nextInt();
			sc.nextLine();
			String[] str = new String[n];
			for(int j = 0; j < n; j++) {
				str[j] = sc.nextLine();
			}
			book.add(str);
		}
		
		Iterator<String[]> iter = book.iterator();
		while(iter.hasNext()) {
			
			String[] str = iter.next();
			Arrays.sort(str);
			int lng = str.length;
			boolean chk = false;
			
			for(int i = 0; i < lng - 1; i++) {
				int n = str[i].length();
				int m = str[i+1].length();
				int min = Math.min(n, m);
				if(str[i].substring(0, min).equals(str[i+1].substring(0, min))) {
					chk = true;
				}
			}
			
			if(chk) {
				System.out.println("NO");
			}else {
				System.out.println("YES");
			}
			
		}
	}
}