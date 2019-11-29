import java.io.*;
import java.util.*;
//BFS 기초 문제. 
//Queue를 다루는 것에 대해 시간걸림
//queue 출력. visited[]. stringTokenizer, 정규표현식 사용 등
public class Main { //BOJ11403

	public static void main(String[] args) throws IOException{
		Graph gp = new Graph();
		gp.BFS_all();

	}
}

//인접행렬을 이용한 방향성 있는 그래프 클래스
class Graph{
	private int T;//노드 개수
	private int[][] map;
	
	Graph() throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int t = Integer.parseInt(bf.readLine());
		T = t;
		map = new int[T][T];
		
		for (int i = 0; i < T; i++) {
			String line = bf.readLine();
			StringTokenizer st = new StringTokenizer(line);
			for (int j = 0; j < T; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		bf.close();
	}
	
	void BFS_all() {
		int node_num = 0;
		// 0~T-1 까지 모든 노드에 대해 실행함
		for(int i = 0; i < T; i++) {
			boolean visited[] = new boolean[T]; //초기값 false
			LinkedList<Integer> queue = new LinkedList<Integer>();
			
			//현재 노드 i를 방문한 것으로 표시하고 큐에 삽입(enqueue)
			queue.add(i);
			
			//queue가 빌 때까지 반복
			while(queue.size() != 0){
				//방문한 노드를 큐에서 추출하고 값을 출력
				node_num = queue.poll();

				//방문한 노드s와 인접한 모든 노드를 가져온다
				StringTokenizer st = new StringTokenizer(Arrays.toString(map[node_num]).replaceAll("[^0-9 ]","")); //re사용하여 숫자만 토큰으로 뽑음
				for (int j = 0; j < T; j++) {
					if(Integer.parseInt(st.nextToken()) == 1) {
						//방문하지 않은 노드이면 방문한 것으로 표시하고 큐에 삽입(enqueue)
						if(!visited[j]) {
							visited[j] = true;
							queue.add(j);
						}
					}
				}
			}
			//방문한 노드들 중에 true인것만 뽑음
			for(int k = 0; k < T; k++) {
				if(visited[k]) {
					System.out.print("1 ");
				}
				else {
					System.out.print("0 ");
				}
			}
			System.out.println();
		}
	}
}