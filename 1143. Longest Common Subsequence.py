class Solution:
    # hint
    # 可以畫圖硬背硬解，但max(dp[i-1][j], dp[i][j-1])不是很懂
    # https://www.youtube.com/embed/Ua0GhsJSlWM
    # https://leetcode.com/problems/longest-common-subsequence/discuss/389782/Simon%E2%80%99s-Note-Python3
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        print(dp)
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    # solution.longestCommonSubsequence(text1 = "psnw", text2 = "vozsh")
    solution.longestCommonSubsequence(text1 = "bcde", text2 = "ace" )