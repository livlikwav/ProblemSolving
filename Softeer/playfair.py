import sys

plaintext = sys.stdin.readline().strip()
# print(plaintext)

key = sys.stdin.readline().strip()
# print(key)

# init matrix
alphabets = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # exclude J
d = {}
oneline = ""

for c in key:
    if c not in d:
        d[c] = 1
        oneline += c

for c in alphabets:
    if c not in d:
        oneline += c

# print(oneline)
matrix = []
tmp = []
for i in range(len(oneline)):
    if i % 5 == 4:
        tmp.append(oneline[i])
        matrix.append(tmp)
        tmp = []
    else:
        tmp.append(oneline[i])

# print(matrix)

# prepare plaintext
prepared = ""
for c in plaintext:
    if len(prepared) % 2 == 0:
        prepared += c
        continue

    if not prepared or prepared[-1] != c:
        prepared += c
    elif prepared[-1] == "X":
        prepared += "Q" + c
    else:
        prepared += "X" + c

if len(prepared) % 2 != 0:
    prepared += "X"

# for i in range(0,len(prepared), 2):
#     print(prepared[i:i+2])

### ENCRYPT
result = ""
for i in range(0, len(prepared), 2):  # O(1000 + a) = O(1)
    a, b = prepared[i], prepared[i + 1]

    # find a, b 2-d index
    ax, ay, bx, by = -1, -1, -1, -1
    for x in range(5):
        for y in range(5):  # O(25) = O(1)
            if matrix[x][y] == a:
                ax, ay = x, y
            if matrix[x][y] == b:
                bx, by = x, y

            if ax != -1 and ay != -1 and bx != -1 and by != -1:
                break
    # check each case O(1)
    if ax == bx:
        ay += 1
        if ay > 4:
            ay = 0
        by += 1
        if by > 4:
            by = 0

        result += matrix[ax][ay]
        result += matrix[bx][by]
    elif ay == by:
        ax += 1
        if ax > 4:
            ax = 0
        bx += 1
        if bx > 4:
            bx = 0

        result += matrix[ax][ay]
        result += matrix[bx][by]
    else:
        result += matrix[ax][by]
        result += matrix[bx][ay]

print(result)
