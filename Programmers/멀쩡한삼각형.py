'''
<풀이 방법 메모>
사실 저번에 풀어서 최대공약수라는 키워드를 기억하고 있었음.
이게 주요한 정답 이유이긴 했지만...

나름의 시도 방법
1) 주어진 예제 그림에서 반복되는 패턴에 주목함
2) case study를 끊임없이 수행함
그림을 여러번 그려서, 가설을 세우고, 다시 그려서 증명해나감.
(w, h가 다를때 왜 nw + nh - 1 인지는 증명하지 못했음)

'''
def solution(w,h):
    # 최대 공약수 구하기
    def get_gcd(x, y):
        gcd = 1
        for i in range(1, max(x, y)):
            # 둘다 나눠 떨어지면 갱신
            if (x % i == 0) and (y % i == 0):
                gcd = i
            else:
                pass
        # 마지막(제일 큰) 수가 gcd
        return gcd
    
    # 기존의 grid 갯수
    original = w * h
    # 반복 횟수 구하기
    iteration = get_gcd(w, h)
    
    # 반복되는 패턴의 최소 모양 구하기
    nw = w // iteration
    nh = h // iteration
    
    val = 0
    if nw == nh:
        val = nw
    else:
        val = nw + nh - 1
        
    return original - (iteration * val)
