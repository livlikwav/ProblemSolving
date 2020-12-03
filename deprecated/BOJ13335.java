import java.io.*;
import java.util.*;

public class Main { //BOJ13335
	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine());
		int num = Integer.parseInt(st.nextToken());
		int width = Integer.parseInt(st.nextToken());
		int weightLimit = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(br.readLine());
		int[] trucks = new int[num];
		for(int i = 0; i < num; i++) {
			trucks[i] = Integer.parseInt(st.nextToken());
		}
		
		Queue<Truck> bridge = new LinkedList<Truck>();
		int currTruck = 0;
		int currWeight = 0;
		int cnt = 0;
		
		currWeight = trucks[currTruck];
		bridge.offer(new Truck(trucks[currTruck], width));
		currTruck++;
		//System.out.println(bridge.toString());
		
		while(!bridge.isEmpty()) {
			
			//one cnt
			cnt++;
			Iterator<Truck> iter = bridge.iterator();
			while(iter.hasNext()) {
				iter.next().dis--;
			}
			//check to pop
			if(bridge.peek().dis == 0) {
				currWeight = currWeight - bridge.poll().weight;
			}
			
			if(currTruck < num) {
				if(currWeight + trucks[currTruck] <= weightLimit) {
					//one more truck
					currWeight = currWeight + trucks[currTruck];
					bridge.offer(new Truck(trucks[currTruck], width));
					currTruck++;
				}
			}
			//System.out.println(bridge.toString());
		}
		
		System.out.println(cnt + 1);
	}
}

class Truck{
	public int weight;
	public int dis;
	Truck(int weight, int dis){
		this.weight = weight;
		this.dis = dis;
	}
	
	@Override
	public String toString() {
		return "weight= " + weight + ", dis= " + dis;
	}
}
