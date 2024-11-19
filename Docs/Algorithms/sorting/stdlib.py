"""
파이썬의 기본 정렬 라이브러리는 merge sort 를 기반으로 만들어졌다.
merge sort 는 일반적으로 quick sort 보다 느리지만, 최악의 경우에도 O(NlogN) 을 보장한다.
"""

array = [('banana', 2), ('apple', 5), ('carrot', 3)]


def setting(data):
    return data[1]


# sorted() 나 sort() 를 이용할 때 key 매개변수를 입력으로 받을 수 있다.
# key 값으로는 하나의 함수가 들어가야 하며 이는 정렬 기준이 된다. 혹은 Lambda 함수를 사용할 수도 있다.
result = sorted(array, key=setting)
print(result)

array = [1, 3, 4, 5, 2]
array.sort(reverse=True)  # 이렇게 넣으면 내림차순 정렬
