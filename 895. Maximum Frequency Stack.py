class FreqStack:
    # hint
    # https://www.youtube.com/watch?v=Z6idIicFDOE
    def __init__(self):
        self.cnt = {}
        self.maxCnt = 0
        self.stacks = {}

    def push(self, val: int) -> None:
        # valCnt = 1 + self.cnt.get(val, 0)
        # self.cnt[val] = valCnt

        # 做self.cnt這張表
        if val not in self.cnt:
            self.cnt[val] = 0
        self.cnt[val] = self.cnt[val] + 1

        # 每次進來的數字，都會有當前的個數
        valCnt = self.cnt[val]

        # 更新self.maxCnt和self.stacks，因為當有個number的個數超過1時，那就是要進到count 2 -> 看筆記
        # 這邊的見表比較不常見，需要多練習
        if valCnt > self.maxCnt:
            self.maxCnt = valCnt
            self.stacks[valCnt] = []
        self.stacks[valCnt].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxCnt].pop()
        self.cnt[res] = self.cnt[res] - 1
        if not self.stacks[self.maxCnt]:
            self.maxCnt = self.maxCnt - 1
        return res


if __name__ == '__main__':
    freqStack = FreqStack()
    freqStack.push(5)   # The stack is [5]
    freqStack.push(7)   # The stack is [5,7]
    freqStack.push(5)   # The stack is [5,7,5]
    freqStack.push(7)   # The stack is [5,7,5,7]
    freqStack.push(4)   # The stack is [5,7,5,7,4]
    freqStack.push(5)   # The stack is [5,7,5,7,4,5]
    freqStack.pop()     # return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4]
    freqStack.pop()     # return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4]
    freqStack.pop()     # return 5, as 5 is the most frequent. The stack becomes [5,7,4]
    freqStack.pop()     # return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7]
