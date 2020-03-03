import java.util.*;
import java.io.*;

public class Main{ //BOJ6588, check > 6 = 3 + 3
    public static void main(String[] args) throws IOException{

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    boolean[] primes = eratosthenes(1000000);
    
    for(int N = Integer.parseInt(br.readLine()); N != 0; N = Integer.parseInt(br.readLine())) {
    	goldbach(primes, N);
    }
    
    br.close();
    }

    // nums <= 1000, natural num
    public static boolean[] eratosthenes(int num){
        boolean[] sieve = new boolean[num + 1];

        //init boolean[]
        for(int i = 0; i < num + 1; i++){
            sieve[i] = true;

        }
        sieve[0] = false;
        sieve[1] = false;

        //just do picking up
        for(int k = 2; (int)Math.pow(k, 2) <= num; k++){
            if(sieve[k] == true){
                for(int i = 2; i*k <= num; i++){
                    sieve[i*k] = false;
                }
            }
        }
        
        //leave only odd prime nums
        sieve[2] = false;
        
        return sieve;
    }
    
    public static void goldbach(boolean[] primes, int N) {
    	for(int i = 0; i <= (N/2); i++) { // until a < num/2
    		if(primes[i] == true) { // if a is prime
    			if(primes[N - i] == true) { // if b is prime too
    				System.out.println(N + " = " + i + " + " + (N-i));
    				return;
    			}
    		}
    	}
    	// there is no correct a+b
    	System.out.println("Goldbach's conjecture is wrong.");
    }

}