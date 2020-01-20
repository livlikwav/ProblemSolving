import java.io.*;
import java.util.*;

public class Main { //BOJ16771
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		ArrayList<Integer> fir = new ArrayList<Integer>();
		ArrayList<Integer> sec = new ArrayList<Integer>();
		HashSet<Integer> answerSet = new HashSet<Integer>();
		
		//input first barn
		String s = br.readLine();
		StringTokenizer st = new StringTokenizer(s);
		for (int i = 0; i < 10; i++) {
			fir.add(Integer.parseInt(st.nextToken()));
		}
		//input second barn
		s = br.readLine();
		st = new StringTokenizer(s);
		for (int i = 0; i < 10; i++) {
			sec.add(Integer.parseInt(st.nextToken()));
		}
        
		//CHECK INPUT
		/*
        Iterator<Integer> firIter = fir.iterator();
        Iterator<Integer> secIter = sec.iterator();
        
        while(firIter.hasNext()) {
        	bw.write(Integer.toString(firIter.next())+" ");
        }
        bw.write("\n");;
        while(secIter.hasNext()) {
        	bw.write(Integer.toString(secIter.next())+" ");
        }
        bw.write("\n");;

        bw.write(Integer.toString(fir.size())+" ");
        bw.write(Integer.toString(sec.size())+"\n");
        
		bw.flush();
        */
		
		for(int i = 0; i < 10; i++) {
			for(int j = 0; j< 11; j++) {
				for (int k = 0; k < 10; k++) {
					for (int m = 0; m < 11; m++) {
						//System.out.println(getAns(fir,sec,i,j,k,m));
						answerSet.add(getAns(fir,sec,i,j,k,m));
					}
				}	
			}
		}
		//CHECK ANSWER SET
		/*
		Iterator<Integer> ansIter = answerSet.iterator();
        while(ansIter.hasNext()) {
        	bw.write(Integer.toString(ansIter.next())+" ");
        }
        bw.write("\n");
		*/
		
		bw.write(Integer.toString(answerSet.size()));
        
        bw.close();
		br.close();
	}
	
	static int getAns(ArrayList<Integer> fir, ArrayList<Integer> sec, int i, int j, int k, int m) {
		int ans = 1000;
		
		ArrayList<Integer> tmpFir = new ArrayList<Integer>();
		ArrayList<Integer> tmpSec = new ArrayList<Integer>();
		tmpFir.addAll(fir);
		tmpSec.addAll(sec);
		/*
        Iterator<Integer> firIter = fir.iterator();
        Iterator<Integer> secIter = sec.iterator();
        
        while(firIter.hasNext()) {
        	System.out.print(Integer.toString(firIter.next())+" ");
        }
        System.out.println();
        while(secIter.hasNext()) {
        	System.out.print(Integer.toString(secIter.next())+" ");
        }
        System.out.println();
        System.out.println(fir.size());
        System.out.println(fir.size());
        */
		
		//first
		ans = ans - tmpFir.get(i);
		tmpSec.add(tmpFir.remove(i));
		//second
		ans = ans + tmpSec.get(j);
		tmpFir.add(tmpSec.remove(j));
		//third
		ans = ans - tmpFir.get(k);
		tmpSec.add(tmpFir.remove(k));
		//fourth
		ans = ans + tmpSec.get(m);
		
		return ans;
	}
}