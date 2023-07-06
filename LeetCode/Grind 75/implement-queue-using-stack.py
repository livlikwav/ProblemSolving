class MyQueueVoted1:
    """
    Voted #1 내 방법보다 훨씬 낫네. 어짜피 out order 는 정해져있으니까, 한번 out stack 으로 all pop 해서 넘기면 그대로 뽑아쓰면 된다.
    그리고 out stack 비어있을때만 채워주면, order 섞일 이유도 없다.
    그래서 문제에서 제시한 조건인 amortized O(1) 이 딱 이 뜻이구나. out_stk 비었을 때 in_stk 한번 가져오는 연산만 오래 걸리니까.

    그리고 python if 문에서 iterable 그대로 써서 emtpy 인지 확인하는 연산도 참 좋네.
    """

    def __init__(self):
        self.in_stk = []
        self.out_stk = []

    # Push element x to the back of queue...
    def push(self, x):
        self.in_stk.append(x)

    # Remove the element from the front of the queue and returns it...
    def pop(self):
        self.peek()
        return self.out_stk.pop()

    # Get the front element...
    def peek(self):
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())
        return self.out_stk[-1]

    # Return whether the queue is empty...
    def empty(self):
        return not self.in_stk and not self.out_stk

    """
    Voted #2 는 확인했는데 별로다. 내가 시도하지 않은 마지막 방법임. 임시 옆 스택에 넣어뒀다가, 다시 오리지널 스택에 담아주는 방식이다.
    거기다가 peek 도 pop 과 동일하게 이 방식을 사용해서 TC 가 더 많이 소요된다.

    나머지 방법들도 별로 볼 필요 없는듯. Voted #1 가 가장 brilliant 한 방법이다. 진정한 amortized O(1)
    """


class MySolQueue:
    """
    MY SOLUTION, 42min elapsed (딴 짓 많이해서 실제론 한 30분 걸린듯, 이것도 오래걸리긴 함 ㅋㅋㅋ)
    처음에 잘못 구현했으나, 다시 수정했다. slicing 을 이용해서 더 깔끔하게 구현했다.
    flag 를 쓰는게 slicing 연산 2번만 하면 되어서 낫더라. 하나의 list 에만 유지하려면 다시 돌아오는데 1번 더 slicing 해야한다.
    """

    def __init__(self):
        self.plus = []
        self.minus = []
        self.flag = True

    def push(self, x: int) -> None:  # O(1)
        if self.flag:
            self.plus.append(x)
        else:
            self.minus.append(x)
        # print(self.plus, self.minus, self.flag)

    def pop(self) -> int:  # O(N)
        if self.flag:
            self.minus = self.plus[1:]
            self.plus = self.plus[:1]
            self.flag = not self.flag
            return self.plus.pop()
            # n = len(self.plus)
            # for i in range(n):
            #     x = self.plus.pop()
            #     self.minus.append(x)

            # self.flag = not self.flag
            # print(self.plus, self.minus, self.flag)
            # return self.minus.pop()
        else:
            self.plus = self.minus[1:]
            self.minus = self.minus[:1]
            self.flag = not self.flag
            return self.minus.pop()
            # n = len(self.minus)
            # for i in range(n):
            #     x = self.minus.pop()
            #     self.plus.append(x)

            # self.flag = not self.flag
            # print(self.plus, self.minus, self.flag)
            return self.plus.pop()

    def peek(self) -> int:  # O(1)
        if self.flag:
            return self.plus[0]
        else:
            return self.minus[0]

    def empty(self) -> bool:  # O(1)
        if self.flag:
            return len(self.plus) == 0
        else:
            return len(self.minus) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
