class Solution:
    # hint
    # 看筆記
    # 這題是odd和even都需要一起輪過，然後再取最大值
    # 不能odd和even各自帶字串分開處理，同樣的字串要用odd和even的方法各自處理一次
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(s, start, end):
            while (0 <= start and end < len(s) and s[start] == s[end]):
                start = start - 1
                end = end + 1

            # print(s[start+1:end])
            return s[start + 1:end]

        # always update the ans is the longest Palindrome
        odd_ans = ""
        even_ans = ""
        for i in range(len(s)):
            # process "aba" situation
            tmp_ans = is_palindrome(s, i, i)
            if len(tmp_ans) > len(odd_ans):
                odd_ans = tmp_ans

            # process "aa" situation
            tmp_ans = is_palindrome(s, i, i + 1)
            if len(tmp_ans) > len(even_ans):
                even_ans = tmp_ans

        if len(odd_ans) >= len(even_ans):
            ans = odd_ans
        else:
            ans = even_ans

        return ans


if __name__ == '__main__':
    solution = Solution()
    solution.longestPalindrome(s = "babad")