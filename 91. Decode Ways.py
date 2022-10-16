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

    # 這思路可以回去想想
    # https://yuihuang.com/leetcode-91/
    # https://www.796t.com/p/521105.html
    # 1. s[i-2]和s[i-1] 兩個字元是10----26之間但不包括10和20這兩個數時,有兩種編碼方式,比如23------>[“BC”,“W”],所以dp[i] = dp[i-1]+dp[i-2]
    # 2. s[i-2]和s[i-1] 兩個字元10或20這兩個數時,有一種編碼方式,比如10------>[“J”], 所以dp[i] = dp[i-2]
    # 3. s[i-2]和s[i-1] 兩個字元不在上述兩種範圍時,編碼方式為零,比如27,比如01,所以dp[i] = dp[i-1]
    def numDecodings_2(self, s: str) -> int:
        # edge case
        if s == "" or s[0] == '0':
            return 0

        # **預先設定此值**
        dp = [1, 1]
        for i in range(2, len(s) + 1):
            if 10 <= int(s[i - 2:i]) <= 26 and s[i - 1] != '0':  # 編碼方式為2
                dp.append(dp[i - 1] + dp[i - 2])
            elif int(s[i - 2:i]) == 10 or int(s[i - 2:i]) == 20:  # 編碼方式為1
                dp.append(dp[i - 2])
            elif s[i - 1] != '0':  # 編碼方式為0
                dp.append(dp[i - 1])
            else:
                return 0

        print(dp[-1])
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    solution.numDecodings_2(s = "226")