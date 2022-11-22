class Solution:
    def maxProfit(self, prices: [int]) -> int:
        """
        min_buy = float("inf")
        max_profit = float("-inf")

        for price in prices:
            # 負數時要給0
            profit = price - min_buy if price - min_buy >= 0 else 0
            max_profit = max(max_profit, profit)
            # 買入時，當然要買比較小的那個stock，這樣才會賺
            min_buy = min(min_buy, price)

        print(max_profit)
        return max_profit
        """

        # method 2
        # 使用雙指針和slide window
        prices.append(float("-inf"))
        max_profit = 0
        l, r = 0, 0
        while r < len(prices) - 1:
            if l == r:
                r = r + 1

            if prices[r] - prices[l] >= 0:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
                r = r + 1
            else:
                l = l + 1

        print(max_profit)
        return max_profit

    def maxProfit_2(self, prices: [int]) -> int:
        # 使用two pointer
        # 使用貪婪演算法
        # 當prices[l] == price[r] -> r向右1格
        # 當prices[l] < price[r] -> 此時股票必定為正，計算價格差。比較最大值，r向右1格
        # 當prices[l] > price[r] -> 此時股票必定為負，計算價格差。l向右1格
        # 所以r無論如何必定會走到最底
        # 因為這個規則在[5,4,3,2,1] -> 必定out of index -> 需要偷吃步 -> 方法在下面

        l = 0
        r = 0

        # 偷吃步
        right_bound = float("-inf")
        prices.append(right_bound)

        max_pricce = 0
        while r < len(prices) - 1:
            if prices[l] == prices[r]:
                r = r + 1

            if prices[l] < prices[r]:
                tmp_price = prices[r] - prices[l]
                max_pricce = max(max_pricce, tmp_price)
                r = r + 1
            else:
                l = l + 1

        print(max_pricce)
        return max_pricce


if __name__ == '__main__':
    solution = Solution()
    solution.maxProfit_2(prices = [7,6,4,3,1])