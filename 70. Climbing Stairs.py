class Solution:
    def climbStairs(self, n: int) -> int:
        # set list
        dp = [-1] * n

        # edge case
        if n == 1:
            return 1

        # define base dp value
        dp[0] = 1
        dp[1] = 2

        # update list
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        print(dp[-1])
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    solution.climbStairs(n = 3)