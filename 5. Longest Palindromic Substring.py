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

    def longestPalindrome_2(self, s: str) -> str:
        # 先定義回文的function
        def palindrome(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l = l - 1
                r = r + 1

            # 回傳此次最大可能的回文string
            return s[l + 1: r]

        # 同一串文字必須走過odd和even
        max_odd = ""
        max_even = ""
        for i in range(len(s)):
            # **要記得是整串string都要進來做，但是每次index都要換(從0開始)，才能每個可能的回文都能找到**
            temp_odd_max = palindrome(s, i, i)
            if len(max_odd) < len(temp_odd_max):
                max_odd = temp_odd_max

            temp_even_max = palindrome(s, i, i + 1)
            if len(max_even) < len(temp_even_max):
                max_even = temp_even_max

        # 對odd和even分別的max再取max
        if len(max_odd) < len(max_even):
            longest_palindrome = max_even
        else:
            longest_palindrome = max_odd

        print(longest_palindrome)
        return longest_palindrome

    def longestPalindrome_3(self, s: str) -> str:
        # two pointer
        # 判斷回文的function，並每次回傳最長得出來
        # 要分成odd/even來判斷

        def isPalindrome(string, l, r):
            # keep the max Palindrome length
            max_palindrome = ""
            while 0 <= l and r < len(string) and string[l] == string[r]:
                tmp = string[l:r + 1]
                if len(tmp) > len(max_palindrome):
                    max_palindrome = tmp
                l = l - 1
                r = r + 1

            # return s[l + 1: r] -> 這個會比較快
            return max_palindrome

        # odd case
        odd_max = ""
        for i in range(len(s)):
            tmp_palindrome = isPalindrome(s, i, i)
            if len(tmp_palindrome) > len(odd_max):
                odd_max = tmp_palindrome

        # even case
        even_max = ""
        for i in range(len(s)):
            tmp_palindrome = isPalindrome(s, i, i + 1)
            if len(tmp_palindrome) > len(even_max):
                even_max = tmp_palindrome

        # get the max palindrome
        if len(odd_max) > len(even_max):
            return odd_max
        else:
            return even_max


if __name__ == '__main__':
    solution = Solution()
    solution.longestPalindrome_3(s = "cbbs")