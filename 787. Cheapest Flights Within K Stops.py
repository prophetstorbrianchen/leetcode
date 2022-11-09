class Solution:
    # hint
    # 這題是Bellman-Ford Algo -> 需要多加熟記與練習，剛開始一定不習慣這code的寫法
    # 只要有source/destination/edge這種的，都可以try一下這種方式
    # https://www.youtube.com/watch?v=5eIK3zUdYmE
    def findCheapestPrice(self, n: int, flights: [[int]], src: int, dst: int, k: int) -> int:
        # 設定初始值 -> 如同我們筆記寫的
        prices = [float("inf")] * n
        prices[src] = 0

        # 因為我們的筆記是算步，而題目的K是算stop的city有幾個，所以會差一
        # Bellman-Ford的模板，一步一步更新destination
        for i in range(k + 1):
            # 必須複製上一次的結果再作計算
            tmpPrices = prices.copy()

            # s -> source, d -> destination, p -> price
            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue

                # 如果路徑小於原本的路徑 -> 更新成比較短的那條路徑
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p

            prices = tmpPrices

        print(prices[dst] if prices[dst] != float("inf") else -1)
        return prices[dst] if prices[dst] != float("inf") else -1


if __name__ == '__main__':
    solution = Solution()
    solution.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1)