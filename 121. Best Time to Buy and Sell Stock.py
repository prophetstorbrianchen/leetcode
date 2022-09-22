class Solution:
    def maxProfit(self, prices: [int]) -> int:
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


if __name__ == '__main__':
    solution = Solution()
    solution.maxProfit(prices = [7,1,5,3,6,4])