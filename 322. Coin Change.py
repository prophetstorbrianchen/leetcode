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

    def coinChange_2(self, coins: [int], amount: int) -> int:
        # define dp
        dp = [float("inf")] * (amount + 1)

        # base case
        dp[0] = 0

        # algo
        for n in range(1, amount + 1):
            for c in coins:
                # ** n等於或大於c才要減**
                # [1,3,4,7], amount=7
                # 當dp[2]時，也就是2塊的硬幣能怎麼換，只能換1塊，沒辦法換3/4/7塊
                # 怎麼換可以看筆記
                if n >= c:
                    dp[n] = min(dp[n], dp[n - c] + 1)

        if dp[amount] == [float("inf")]:
            print(dp[amount])
            return -1
        else:
            print(dp[amount])
            return dp[amount]


if __name__ == '__main__':
    solution = Solution()
    solution.coinChange_2(coins = [1,2,5], amount = 11)