# dongbin-na

이것이 코딩테스트다 파이썬 - 나동빈 저

- [dongbin-na](#dongbin-na)
  - [Python syntax](#python-syntax)
    - [input 개선](#input-개선)
    - [input 개선 2](#input-개선-2)
    - [for-loop](#for-loop)
    - [sort](#sort)
    - [operators](#operators)
    - [Data-type & built-in funcs](#data-type--built-in-funcs)

## Python syntax

### input 개선

```python
# input example
# 1 2 3 4 5

# int 객체 입력받을 때
import sys
n = int(sys.stdin.readline())

# 한 줄에 여러가지 입력이 필요할 때
import sys
n = sys.stdin.readline().split() # ["1", "2," ...]

# python map(function, iterable) 함수 사용
import sys
n = list(map(int, sys.stdin.readline().split())) # [1, 2, 3, 4, 5]
# map()은 map 객체를 반환한다
# 따라서 list()로 다시 list로 형변환

# sys.stdout.write 출력
import sys
print(1)
sys.stdout.write(str(1) + '\n')
# stdout 주의할 점
# 1) str로 꼭 변환해줘야한다
# 2) 개행문자를 사용해서 개행해야한다. print()와 다름
```

### input 개선 2

[참고 링크](https://itcrowd2016.tistory.com/81)

input이 들어가있는 txt 파일을 저장하고,  
표준 입력으로 읽어 사용

```python
import sys
sys.stdin = open("input.txt", "r")
```

python input best practices

```python
# 1
N = int(input())
print(N)

# 2
print(input().split()) # string list

# 3
# 내가 입력받을 데이터 갯수 정해져있을 때만 사용
N, M = map(int, input().split()) # int list
print(N, M) # 1 2

# 4
# 데이터 갯수 안 정해져 있을때
arr = list(map(int, input().split()))  # 그냥 list 자체로 받아옴
print(arr)

# 5
# 공백문자 없는 숫자 리스트
print(input()) # 한 줄을 그냥 string으로 받아옴
# 12345

print(list(input())) # string 한 줄에 list 씌우면
# ['1', '2', ...]

# 6
# 공백문자 없는 숫자를 int list로 입력받기
arr = list(map(int, input()))
print(arr)
# [1, 2, ...]

# 7
# N행으로 이루어진 2차원 배열 입력받기
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
# list comprehension을 통해 편리하게 list 작성
```

- 알게된 점
  - input()
    - 무조건 한 줄을 string으로 다 읽어온다.
  - Python String
    - 그대로 map(function, iterable)에 넣을 수 있다
    - 근데 python에 char 타입은 없음에 유의
  - list comprehension(리스트 내포)

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
