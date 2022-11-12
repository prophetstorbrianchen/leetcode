class Solution:
    # hint
    # 跟硬幣DP的思路很像
    # 之後可以用dfs+cache的方式解看看 -> 如何cache是要學的
    # https://www.youtube.com/watch?v=dw2nMCxG0ik
    def combinationSum4(self, nums: [int], target: int) -> int:
        # method 1 -> DP解
        # base case
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1, 1):
            for n in nums:
                if i - n < 0:
                    continue
                else:
                    dp[i] = dp[i] + dp[i - n]

        print(dp)
        print(dp[target])
        return dp[target]


if __name__ == '__main__':
    solution = Solution()
    solution.combinationSum4(nums = [1,2,3], target = 4)