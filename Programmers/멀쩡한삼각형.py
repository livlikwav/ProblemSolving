import math

def solution(w,h):
    grad = h/w
    
    def get_y(x: int) -> int:
        return math.ceil(grad * x)
    
    data = [0] * (w+1)
    for i in range(1, w+1): # w==8이면 1부터 8까지, 0빼고
        new = get_y(i)
        old = get_y(i-1)
        delta = new - old
        data[i] = delta + 1

        
    return (w*h) - sum(data)