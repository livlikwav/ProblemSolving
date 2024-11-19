class Sort:
    def __init__(self):
        array = [(3, 4), (2, 2), (3, 3), (1, 2), (1, -1)]
        print(array)

    def Normal(self):
        array = [(3, 4), (2, 2), (3, 3), (1, 2), (1, -1)]

        array.sort()
        # same with array.sort(key=lambda x: (x[0], x[1]))
        print(array)

    def ByOnlyFirst(self):
        array = [(3, 4), (2, 2), (3, 3), (1, 2), (1, -1)]

        array.sort(key=lambda x: x[0])
        print(array)

    def Reverse(self):
        array = [(3, 4), (2, 2), (3, 3), (1, 2), (1, -1)]

        array.sort(reverse=True)
        print(array)

    def ReverseByOnlyFirst(self):
        array = [(3, 4), (2, 2), (3, 3), (1, 2), (1, -1)]

        array.sort(key=lambda x: -x[0])
        array.sort(key=lambda x: x[0], reverse=True)
        print(array)

    def Diverse(self):
        array = [(3, 4), (2, 2), (3, 3), (1, 2), (1, -1)]

        array.sort(key=lambda x: (-x[0], x[1]))
        print(array)


sort = Sort()
sort.Normal()
sort.ByOnlyFirst()
sort.Reverse()
sort.ReverseByOnlyFirst()
sort.Diverse()
