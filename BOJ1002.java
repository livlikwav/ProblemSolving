import java.util.Scanner;
import java.util.StringTokenizer;
// 계속 틀렸던 포인트 : 원의 존재할 수 있는 Case를 다 분석하지 못함
// 원의 중점이 같지만 반지름이 다른 경우 : 교점 0개
public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int loop;
		String line;
		double x1, y1, r1, x2, y2, r2;
		double dist;
		int[] ansArray;
		
		loop = sc.nextInt();
		sc.nextLine();
		ansArray = new int[loop];
		
		for(int i = 0; i < loop; i++) {
			line = sc.nextLine();
			StringTokenizer st = new StringTokenizer(line);
			//x1, y1, r1, x2, y2, r2
			x1 = Integer.parseInt(st.nextToken());
			y1 = Integer.parseInt(st.nextToken());
			r1 = Double.parseDouble(st.nextToken());
			x2 = Integer.parseInt(st.nextToken());
			y2 = Integer.parseInt(st.nextToken());
			r2 = Double.parseDouble(st.nextToken());
			// dist = root((x1-x2)^2 + (y1-y2)^2)
			dist = Math.sqrt(Math.pow(x1-x2, 2) + Math.pow(y1-y2, 2));
			
			//원 2개를 그려서 교점을 구함, 교점 = 예상되는 위치
			if((x1==x2)&&(y1==y2)) {
				if(r1==r2) {// 원이 동일한 원이라면 교점 -1개 (무한대)
					ansArray[i] = -1;
				}
				else { //원의 중점이 동일하지만 반지름이 다르면 교점 0개
					ansArray[i] = 0;
				}
			}
			else {
				if(dist > r1 + r2) {// dist > r1+ r2 이면 교점 0개
					ansArray[i] = 0;
				}
				else if(dist == r1 + r2) {// dist = r1+ r2 이면 교점 1개
					ansArray[i] = 1;
				}
				else {// dist < r1 + r2 이면 교점 2개
					if(Math.abs(r2 - r1) == dist) { //원 내부에 포함하지만 접점 1개
						ansArray[i] = 1;
					}
					else if(Math.abs(r2 - r1) > dist) { //원 내부에 포함하지만 교점 없음
						ansArray[i] = 0;
					}
					else { // 별개의 원 2개
						ansArray[i] = 2;
					}
				}
			}
		}
		
		sc.close();
		
		for(int i = 0; i < loop; i++) {
			System.out.println(ansArray[i]);
		}
	}

}
