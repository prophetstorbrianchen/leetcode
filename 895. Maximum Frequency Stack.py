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

class FreqStack_2:
    def __init__(self):
        self.cnt = {}
        self.maxCnt = 0
        self.stacks = {}

    def push(self, val: int) -> None:
        # 需要做2張表，一個self.maxCnt
        # self.cnt -> 計算每個num的當前總數 -> {5: 3, 7: 2, 4: 1}
        # self.stacks -> 分成好幾階，在為count n的時候，有哪幾個數字在裡面 -> {1: [5,7,4], 2: [5,7], 3: [5]}
        # self.maxCnt -> 用來記當前最多num的個數 -> 這個可以利用self.stacks來反查是哪個num(很厲害的)

        # 做self.cnt這張表
        if val not in self.cnt:
            self.cnt[val] = 0
        self.cnt[val] = self.cnt[val] + 1

        # 每次進來的數字，都會有當前的個數
        valCnt = self.cnt[val]

        # 更新self.stack這張表
        if valCnt > self.maxCnt:
            # 每次更新最大值 -> 要隨時記著最多次 -> 可以用self.stacks反推最多次的是哪個數字 -> self.stacks[self.maxCnt]
            self.maxCnt = valCnt
            if valCnt not in self.stacks:
                self.stacks[valCnt] = []
        self.stacks[valCnt].append(val)

    def pop(self) -> int:
        # {1: [5,7,4], 2: [5,7], 3: [5]} -> res is 5
        res = self.stacks[self.maxCnt].pop()
        # 更新maxCnt和2個table
        self.cnt[res] = self.cnt[res] - 1
        if not self.stacks[self.maxCnt]:
            # 若為空，表示maxCnt就要降一街 -> {1: [5,7,4], 2: [5,7], 3: []} -> 3為空
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
