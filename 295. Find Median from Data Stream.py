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


if __name__ == '__main__':
    medianFinder = MedianFinder()
    medianFinder.addNum(3)
    medianFinder.addNum(2)
    medianFinder.addNum(7)
    medianFinder.addNum(4)