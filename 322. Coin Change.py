class Solution:
    # hint
    # 看筆記
    def coinChange(self, coins: [int], amount: int) -> int:
        # set list
        # 初始值設成無限大
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i - coin] + 1, dp[i])

        # 如果等同於初始值，表示根本沒辦法用coin組出amount
        if dp[amount] == float("inf"):
            print(-1)
            return -1
        else:
            print(dp[amount])
            return dp[amount]


if __name__ == '__main__':
    solution = Solution()
    solution.coinChange(coins = [3,5], amount = 4)