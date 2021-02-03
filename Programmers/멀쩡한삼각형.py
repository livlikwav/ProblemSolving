'''
<풀이 방법 메모>
사실 저번에 풀어서 최대공약수라는 키워드를 기억하고 있었음.
이게 주요한 정답 이유이긴 했지만...

나름의 시도 방법
1) 주어진 예제 그림에서 반복되는 패턴에 주목함
2) case study를 끊임없이 수행함
그림을 여러번 그려서, 가설을 세우고, 다시 그려서 증명해나감.
(w, h가 다를때 왜 nw + nh - 1 인지는 증명하지 못했음)

<이해함>
w = 8이고, h = 12일때, h = (3/2) * w 가 대각선 직선의 방정식이다.
이 직선의 방정식의 (정수, 정수)해가 grid의 꼭짓점을 지난다.
그리고 꼭짓점을 지날때 마다 패턴이 반복된다.

위 예시에서는,
w가 2의 배수이고, h가 3의 배수일 때 점을 지난다.
x: (2, 4, 6, 8), y: (3, 6, 9, 12)
패턴이 반복되는 경우가 최대 공약수인 4개인 것이다.

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
'''
<참고 링크>
https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%A9%80%EC%A9%A1%ED%95%9C-%EC%82%AC%EA%B0%81%ED%98%95-in-python
'''