def rotate_90_degree_of_matrix(graph, n):
    x = len(graph)
    tmp = [[0] * x for _ in range(x)]  
    for i in range(x):
        for j in range(x):
            tmp[j][n - 1 - i] = graph[i][j]
    return tmp

def check_big_lock(big_lock, n):
    for i in range(n, 2*n):
        for j in range(n, 2*n):
            if big_lock[i][j] == 1:
                continue
            else:
                return False
    return True

def solution(key, lock):
    
    m = len(key)
    n = len(lock)
    big_lock = [[0] * (3 * n) for _ in range(3 * n)]
    for i in range(n, 2*n):
        for j in range(n, 2*n):
            big_lock[i][j] = lock[i - n][j - n]
        
    # Solution
    rotated = key
    for k in range(4):
        if k != 0:
            rotated = rotate_90_degree_of_matrix(key, n)
        for i in range(0, 2*n):
            for j in range(0, 2*n):
                # 끼워보기
                for x in range(m):
                    for y in range(m):
                        big_lock[i][j] += rotated[x][y]
                if check_big_lock(big_lock, n):
                    return True
                # 원상복구
                for x in range(m):
                    for y in range(m):
                        big_lock[i][j] -= rotated[x][y]
    return False
