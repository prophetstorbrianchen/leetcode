import heapq


class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, num * -1)

        # 比值大小
        if self.small or self.large and self.small[0] * -1 > self.large[0]:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, val * -1)

        # 比list中的數量
        # 注意+1的位置
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, val * -1)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, val * -1)

    def findMedian(self) -> float:
        # 要用數量的大小判斷而非奇偶數
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        if len(self.large) > len(self.small):
            return self.large[0]
        if len(self.small) == len(self.large):
            return (self.small[0] * -1 + self.large[0]) / 2

    def addNum_2(self, num: int) -> None:
        # 對self.small使用heap來排序，default的heap是min heap，乘上-1會是max heap
        heapq.heappush(self.small, -1 * num)

        # 大小
        if self.small and self.large and self.small[0] * -1 > self.large[0]:
            pop_item = heapq.heappop(self.small)
            heapq.heappush(self.large, pop_item * -1)

        # 個數
        # large多了
        if len(self.small) + 1 < len(self.large):
            pop_item = heapq.heappop(self.large)
            heapq.heappush(self.small, pop_item * -1)

        # small多了
        if len(self.large) + 1 < len(self.small):
            pop_item = heapq.heappop(self.small)
            heapq.heappush(self.large, pop_item * -1)

    def findMedian_2(self) -> float:
        # **不能用pop，因為還有後面的findMedian需要使用前面add的數字**
        # large比較多
        if len(self.large) > len(self.small):
            return self.large[0]
        elif len(self.small) > len(self.large):
            # small比較多
            return self.small[0] * -1
        else:
            # small和large一樣多
            return (self.large[0] + self.small[0] * -1) / 2


if __name__ == '__main__':
    medianFinder = MedianFinder()
    medianFinder.addNum(3)
    medianFinder.addNum(2)
    medianFinder.addNum(7)
    medianFinder.addNum(4)