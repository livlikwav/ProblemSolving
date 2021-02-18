'''
Python 답안을 좀 보니까,
sys.stdin.readline() 사용해서 입력 시간을 줄이더라.
나는 그냥 Pypy3로 풀었다 ㅋㅋ

radix sort로 풀었던건 틀렸다.
입력이 양수가 아니라 정수도 있어서 ㅋㅋ
'''
n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))
data.sort()
for x in data:
    print(x)