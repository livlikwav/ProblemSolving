immutable = 1
mutable = [1, 1, 1]

# locals, globals 실험

def print1():
    print('print1', immutable)
    print('print1', mutable)
    print('locals', locals())
    print('globals', globals())

def print2():
    immutable = 2
    mutable = [2, 2, 2]
    print('print2', immutable)
    print('print2', mutable)
    print('locals', locals())
    print('globals', globals())

def print3():
    global immutable
    global mutable
    immutable = 3
    mutable = [3, 3, 3]
    print('print3', immutable)
    print('print3', mutable)
    print('locals', locals())
    print('globals', globals())

# call by reference 실험

def print4(immutable, mutable):
    print('print4', immutable)
    print('print4', mutable)
    print('locals', locals())
    print('globals', globals())

def print5(immutable, mutable):
    immutable = 2
    mutable = [2, 2, 2]
    print('print5', immutable)
    print('print5', mutable)
    print('locals', locals())
    print('globals', globals())

def print5_2(immutable, mutable):
    immutable = 2
    mutable[0] = 2
    print('print5_2', immutable)
    print('print5_2', mutable)
    print('locals', locals())
    print('globals', globals())

def print5_3():
    immutable = 2
    mutable[0] = 2
    print('print5_3', immutable)
    print('print5_3', mutable)
    print('locals', locals())
    print('globals', globals())

def print6(immutable, mutable):
    # global immutable # "immutable" is assigned before global declarationPylance
    # global mutable # "mutable" is assigned before global declarationPylance
    # SyntaxError: name 'immutable' is parameter and global
    # SyntaxError: name 'mutable' is parameter and global
    immutable = 3
    mutable = [3, 3, 3]
    print('print6', immutable)
    print('print6', mutable)
    print('locals', locals())
    print('globals', globals())

# global 2-d list 실험
def print7():
    mutable2 = [1, 1, 1]
    print('print7', mutable2)
    print('locals', locals())
    print('globals', globals())

def print8():
    mutable2[0][0] = 2
    print('print8', mutable2)
    print('locals', locals())
    print('globals', globals())

def print9():
    global mutable2
    mutable2[0][0] = 2
    print('print9', mutable2)
    print('locals', locals())
    print('globals', globals())

def print10(mutable2):
    mutable2 = [1, 1, 1]
    print('print10', mutable2)
    print('locals', locals())
    print('globals', globals())

def print11(mutable2):
    mutable2[0][0] = 2
    print('print11', mutable2)
    print('locals', locals())
    print('globals', globals())

def print12(mutable2):
    mutable2[0][0] = 3
    print('print12', mutable2)
    print('locals', locals())
    print('globals', globals())
    mutable2 = [3, 3, 3]
    print('print12', mutable2)
    print('locals', locals())
    print('globals', globals())
    mutable2[0] = 7
    print('print12', mutable2)
    print('locals', locals())
    print('globals', globals())

def print13(mutable2):
    print('mutable2_print13_id', id(mutable2))
    mutable2[0][0] = 3
    print('mutable2_print13_id', id(mutable2))
    print('print13', mutable2)
    print('locals', locals())
    print('globals', globals())
    mutable2 = [3, 3, 3]
    print('mutable2_print13_id', id(mutable2))
    print('print13', mutable2)
    print('locals', locals())
    print('globals', globals())

# locals, globals 실험
print1()
print2()
print3()
# call by reference 실험
# 초기화
immutable = 1
mutable = [1, 1, 1]
# 시작
print4(immutable, mutable)
print5(immutable, mutable)
print5_2(immutable, mutable)
print5_3()
# print6(immutable, mutable)

# global 2-d list 실험
# 초기화
mutable2 = [[1, 1], [1, 1], [1, 1]]
# 시작
print7()
print8()
print9()
# 초기화
mutable2 = [[1, 1], [1, 1], [1, 1]]
# 시작
print10(mutable2)
print11(mutable2)
print12(mutable2)
print('mutable2_global_past_id', id(mutable2))
print13(mutable2)
print('mutable2_global_future_id', id(mutable2))

# mutable 실험

list1 = [1, 2]
list2 = [1, 2]
list3 = list1

print(id(list1))
print(id(list2))
print(id(list3))

# 같은 객체 가리키고 변화를 줘도 달라지지 않음
list3[0] = 3
print(id(list1))
print(id(list3))

# immutable 실험

int1 = 1
int2 = 1
print(id(int1))
print(id(int2))
# 같은 객체 가리킴 (immutable)

# mutable 과 함수 실험

mut1 = [1, 2, 3]

def get_mut1(mut1):
    print(id(mut1))

def get_mut2(mut1):
    print(id(mut1))

print(id(mut1))
get_mut1(mut1)
get_mut1(mut1)
get_mut2(mut1)

# immutable 과 함수 실험

immut1 = 1

def get_immut1(immut1):
    print(id(immut1))

print(id(immut1))
get_immut1(immut1)