'''
띠용하지만 수학 문제.
나름의 생각은, 아직 이런 유형이 더 어려운 듯 하다.
최대공약수라는 아이디어를 찾지 못하면 틀리는 문제.

실력이 늘때까지의 접근 전략은,
1)이런 문제 빼고 다맞추기.
2)그래도 직사각형에 대각선 그었을때 최대공약수 쓰는구나~ 알았다
3)예제에서 패턴이 반복되는 것을 체크해보는 것도 좋구나~ 싶었다.

배운점: 반올림, 올림, 내림, 최대공약수
import math
math.round(n) # 두번째 인자 비면 소수 첫째자리에서 반올림
math.round(n, 2) # 소수 셋째 자리에서 반올림! 주의!
math.ceil(n) # 올림
math.floor(n) # 내림
math.gcd(x, y) # x와 y의 최대 공약수 구해줌
'''
import math

def solution(w,h):
    grad = h/w

    ceils = [0] * (w+1)
    floors = [0] * (w+1)
    
    for i in range(w+1):
        tmp = grad * i
        ceils[i] = math.ceil(tmp)
        floors[i] = math.floor(tmp)
    
    result = 0
    # data = [0] * (w+1)
    for i in range(1, w+1): # w==8이면 1부터 8까지, 0빼고
        new = ceils[i]
        old = floors[i-1]
        # new = math.ceil(get_y(i))
        # old = math.floor(get_y(i-1))
        # data[i] = new - old
        result += new - old
        
    return (w*h) - result