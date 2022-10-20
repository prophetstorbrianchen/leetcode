import heapq
import copy


class MinStack:

    # method 1
    # TLE
    """
    def __init__(self):
        self.q = []

    def push(self, val: int) -> None:
        self.q.append(val)

    def pop(self) -> None:
        self.q.pop()

    def top(self) -> int:
        return self.q[-1]

    def getMin(self) -> int:
        copy_q = copy.deepcopy(self.q)
        heapq.heapify(copy_q)
        print(copy_q[0])
        return copy_q[0]
    """

    def __init__(self):
        self.q = []
        self.min_q = []

    def push(self, val: int) -> None:
        # 必須維持2個stack，一個是普通的stack，一個是min stack
        self.q.append(val)
        if not self.q or val <= self.min_q[-1]:
            self.min_q.append(val)

    def pop(self) -> None:
        if self.q[-1] == self.min_q[-1]:
            # 2個一起pop，維持一致性
            self.q.pop()
            self.min_q.pop()
        else:
            # 表示min_q裡沒有self.q要pop的東西
            self.q.pop()

    def top(self) -> int:
        return self.q[-1]

    def getMin(self) -> int:
        return self.min_q[-1]


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.getMin() # return -3
    minStack.pop()
    minStack.top() # return 0
    minStack.getMin() # return -2

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()