//메모장 챌린지
import java.util.*;
import java.io.*;

public class Main{ //BOJ1978
    public static void main(String[] args) throws IOException{

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    //INPUT
    int N = Integer.parseInt(br.readLine());
    
    int[] nums = new int[N];
    StringTokenizer st = new StringTokenizer(br.readLine());
    for(int i = 0; i < N; i++){
        nums[i] = Integer.parseInt(st.nextToken());    
    }

    // eratosthenes
    eratosthenes(nums);

    br.close();

    }

    // nums <= 1000, natural num
    public static void eratosthenes(int[] nums){
        boolean[] sieve = new boolean[1001];

        //init boolean[]
        for(int i = 0; i < 1001; i++){
            sieve[i] = true;

        }
        sieve[0] = false;
        sieve[1] = false;

        //just do picking up
        for(int k = 2; (int)Math.pow(k, 2) <= 1000; k++){
            if(sieve[k] == true){
                for(int i = 2; i*k <= 1000; i++){
                    sieve[i*k] = false;
                }
            }
        }

        //count prime numbers
        int count = 0;

        for(int i = 0; i < nums.length; i++){
            if(sieve[nums[i]] == true){
                count++;
            }
        }

        //print count
        System.out.println(count);


    }

}