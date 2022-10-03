import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # --DP--
        # 做出2維陣列
        """
        dp = []
        for row in range(m):
            tmp = []
            for col in range(n):
                tmp.append(1)
            dp.append(tmp)
        """

        # 做出2維陣列的高級技巧
        dp = [[1] * n for _ in range(m)]

        # 因為所有格子都預先給1了，所以只要update就可以了
        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    continue
                else:
                    dp[row][col] = dp[row][col - 1] + dp[row - 1][col]

        print(dp)
        return dp[m - 1][n - 1]

        """
        # --math--
        # 使用階層函數
        ans = math.factorial(m + n - 2) // (math.factorial(n - 1) * math.factorial(m - 1))
        print(ans)

        return ans
        """


if __name__ == '__main__':
    solution = Solution()
    solution.uniquePaths(m = 3, n = 7)