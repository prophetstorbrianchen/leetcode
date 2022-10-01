class Solution:
    # hint
    # 這題要多看幾次
    def numDecodings(self, s: str) -> int:
        # 沒使用遞迴
        """
        n = len(s)
        dp0, dp1, dp2 = 0, 1, 0
        for i in range(1, n + 1):
            # dp2為每次新的紀算，所以要reset為0
            dp2 = 0
            if s[i - 1] != '0':
                dp2 = dp2 + dp1

            # 加完第一種(一位數的處理)在加上第二種(2位數的處理)
            if i > 1 and s[i - 2] != '0' and int(s[i - 2: i]) <= 26:
                dp2 = dp2 + dp0

            # 向前移動
            dp0, dp1 = dp1, dp2
        return dp2
        """
        n = len(s)
        dp = [0] * n + [1]
        for i in range(n):
            if s[i] != '0':
                dp[i] += dp[i - 1]
            if i > 0 and 1 <= int(s[i - 1:i + 1]) <= 26 and s[i - 1] != '0':
                dp[i] += dp[i - 2]
        return dp[n - 1]


if __name__ == '__main__':
    solution = Solution()
    solution.numDecodings(s = "226")