from collections import deque


class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 雙端佇列
        # append(): 新增元素於佇列右側
        # appendleft(): 新增元素於佇列左側
        # pop(): 刪除最右側元素
        # popleft(): 刪除最左側元素
        self.q = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0


if __name__ == '__main__':
    mystack = MyStack()
    mystack.push(1)
    mystack.push(2)
    mystack.push(3)