# dongbin-na

이것이 코딩테스트다 파이썬 - 나동빈 저

- [dongbin-na](#dongbin-na)
  - [중요한 Python 테크닉](#중요한-python-테크닉)
    - [input()](#input)
    - [sys.stdin.readline()](#sysstdinreadline)
    - [functions](#functions)
  - [문제별 테크닉](#문제별-테크닉)
    - [N, M 2차원 행렬맵](#n-m-2차원-행렬맵)
  - [공부 팁](#공부-팁)
    - [파일로 표준 입력받기](#파일로-표준-입력받기)
  - [Python 기초](#python-기초)
    - [중요](#중요)
    - [for-loop](#for-loop)
    - [sort](#sort)
    - [operators](#operators)
    - [Data-type & built-in funcs](#data-type--built-in-funcs)

## 중요한 Python 테크닉

### input()

```python
# int 1
n = int(input())

# 2-d string list (sparse)
# 2-d string list (dense)
data = [input() for _ in range(row)]

# 2-d int list (sparse)
data = [list(map(int, input().split())) for _ in range(row)]

# 2-d in list (dense) **
data = []
for i in range(row):
  graph.append(list(map(int, input())))
```

### sys.stdin.readline()

```python
# sys.stdin.readline이 input()보다 더 빠르다
import sys
n = int(sys.stdin.readline())
```

### functions

```python
# List summation
l = [1, 2, 3, 4, 5]
print(sum(l))
```

## 문제별 테크닉

### N, M 2차원 행렬맵

```python
# 상하좌우 검사
x = 0
y = 0
dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]

for i in range(4):
  nx = x + dx[i]
  ny = y + dy[i]
```

## 공부 팁

### 파일로 표준 입력받기

[참고 링크](https://itcrowd2016.tistory.com/81)

input이 들어가있는 txt 파일을 저장하고,  
표준 입력으로 읽어 사용

```python
import sys
sys.stdin = open("input.txt", "r")
```

## Python 기초

### 중요

- input()은 한 줄을 String으로 읽어온다
- String은 index를 통해 값 변경 불가능
  - replace()는 있는데, 이건 문자열 매칭 후 변경
- Python에 char 타입은 없다

### for-loop

[ref](https://wiki.python.org/moin/ForLoop)

```python
# ex 1
for i in range(0, 6):
  print(f'{i}')

# ex 2
while True:
  print('infinite loop')

# For ... Else
# Strings as an iterable
# Lists as an iterable
# Loop over lists of lists
```

### sort

[ref](https://docs.python.org/ko/3/howto/sorting.html)

list 정렬 내장 함수  

```python
list.sort() -> None
sorted(iterables) -> list
# list.sort()는 해당 list 변수 자체를 변경
# sorted()는 해당 list는 놔두고 새로운 list 반환
```

list 역순으로 뒤집기

```python
list.reverse() -> None
# list.reverse()는 해당 list 변수 자체를 변경
```

### operators

```python
# 나머지 연산
int(A / B)
A // B
```

### Data-type & built-in funcs

```python

# iterables 길이
lis = [1, 2, 3]
len(lis)
>> 3

# list + list 는 각 요소의 합이 아니다. 리스트 확정
A = [1, 2]
B = [2, 1]
A + B
>> [1, 2, 2, 1]
# list 각 요소의 합은, list comprehension을 사용하면 편함
[A[i] + B[i] for i in range(len(A))]

# 파이썬의 and, or, not > 그냥 영어로 쓰기. || 같은거 아님
x = True or True
x = True and False
x = not True

# python ord()
# The ord() function returns an integer representing the Unicode character.
# By the way, the ord() function is the inverse of the Python chr() function.
# 유니코드 문자 정수를 반환함.
# abcdef.. 에서 차이 갯수 세는지 등에 사용함
diff = int(ord(input_data[0])) - int(ord('a')) + 1
```
