class Solution:
    # hint
    # 此題是用DP去做
    # https://www.youtube.com/watch?v=Sx9NNgInc3A
    # must follow dp[i] = dp[i + len(w)] rule -> is word break
    # 也可以使用trie去做 -> 下次試試
    # 小小福讲Leetcode -> 這個的DP方法比較簡單好懂
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        # --neetcode--
        """
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                print(i + len(w), s[i: i + len(w)])
                if i == 3:
                    print(3)
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        print(dp[0])
        return dp[0]
        """

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)):
            # dp[i]是True，才能繼續往下拼接 -> key point
            if dp[i] is True:
                for word in wordDict:
                    # 剛好符合wordDict中的word，
                    if s[i: i + len(word)] == word:
                        dp[i + len(word)] = True

        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    solution.wordBreak(s = "leetcode", wordDict = ["code", "leet"])