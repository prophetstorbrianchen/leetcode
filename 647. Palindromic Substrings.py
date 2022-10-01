class Solution:
    # hint
    # 是leetcode 5的簡單版本，只需要懂LC 5的原理
    def countSubstrings(self, s: str) -> int:
        self.ans = 0

        def is_palindrome(s, start, end):
            while (0 <= start and end < len(s) and s[start] == s[end]):
                start = start - 1
                end = end + 1
                self.ans = self.ans + 1

        # always update the ans is the longest Palindrome
        for i in range(len(s)):
            # process "aba" situation
            # process odd
            is_palindrome(s, i, i)

            # process "aa" situation
            # process even
            is_palindrome(s, i, i + 1)

        print(self.ans)
        return self.ans


if __name__ == '__main__':
    solution = Solution()
    solution.countSubstrings(s = "a")

