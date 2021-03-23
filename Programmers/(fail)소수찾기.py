import math
from itertools import permutations

def solution(numbers):
    primes = prime_list(int(1e7))
    
    numbers = list(map(int, numbers))
    
    permu = set(permutations(numbers, len(numbers)))
    cand = {}
    for val in permu:
        
    
    answer = 0
    return answer

def prime_list(num: int) -> list:
    arr = [True] * num
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if arr[i] == True:
            for j in range(i+i, num, i):
                arr[j] = False
    
    return [i for i in range(2, num) if arr[i] == True]

    