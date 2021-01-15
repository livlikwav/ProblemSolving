'''
40분짜리 문제를 20분내로 풀려니까,
변수명 잘못 짓고,
pass 해야하는데 continue하는 등의 실수가 많았다.
실제로 코딩테스트 풀때도 시간을 여유롭게 풀 수 있도록,
첫 문제부터 속도감있게 풀기.

이 문제 핵심
1. matrix 90도 회전 방법 알고 있기 i,j --> j, n-1-i
2. N이 20밖에 안되므로, 공간복잡도 최대한 활용 --> lock 3배로 키워서 그냥 key 더하기
3. N이 20밖에 안되므로, 문제 그대로 이동,회전 다 하는 완전 탐색으로 풀기. (이 코드는 O(N^4)이다)
'''

# key = [[0,0,0], [1,0,0], [0,1,1]]
# lock = [[1,1,1], [1,1,0], [1,0,1]]
# result --> true

def rotate_90_degree_of_matrix(graph, m):
    tmp = [[0] * m for _ in range(m)]  
    for i in range(m):
        for j in range(m):
            tmp[j][m - 1 - i] = graph[i][j]
    return tmp

def check_big_lock(big_lock, n):
    for i in range(n, 2*n):
        for j in range(n, 2*n):
            if big_lock[i][j] == 1:
                pass
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
    # print(big_lock)
        
    # Solution
    rotated = key
    for k in range(4):
        if k != 0:
            rotated = rotate_90_degree_of_matrix(rotated, m)
        # print(rotated)

        for i in range(0, 2*n):
            for j in range(0, 2*n):
                # 끼워보기
                for x in range(m):
                    for y in range(m):
                        big_lock[i+x][j+y] += rotated[x][y]
                if check_big_lock(big_lock, n):
                    return True
                # 원상복구
                for x in range(m):
                    for y in range(m):
                        big_lock[i+x][j+y] -= rotated[x][y]
                # print(big_lock)
    return False

# print(solution(key, lock))

'''
<Answer>
def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    result = [[0] * n for _ in range(m)] # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - 1 -i] = a[i][j]
    return result

# 자물쇠 중간 부분이 모두 1인가 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    retrun True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기준으로 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key) # 열쇠 회전
        for x in range(n * 2):
            for y in range( n * 2):
                # 자물쇠에 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False
'''