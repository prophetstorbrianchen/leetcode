class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_palindrome(string, left, right):
            while (0 <= left and right < len(string)):
                if string[left] != string[right]:
                    return False
                left = left - 1
                right = right + 1

            return True

        lowercaseletter = ["a", "b", "c", "d", "e", "f", "g", "h", "i",  "j",  "k",  "l",  "m", "n", "o", "p",  "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        # process string to lowercase letters and non-alphanumeric characters.
        lowercase_s = s.lower()
        new_lower_string = ""
        for c in lowercase_s:
            if c in lowercaseletter:
                new_lower_string = new_lower_string + c
        print(new_lower_string)

        # process odd
        if len(new_lower_string) % 2 == 1:
            l = int((len(new_lower_string) - 1) / 2)
            r = l
            res = is_palindrome(new_lower_string, l, r)
        # process even
        else:
            r = int(len(new_lower_string) / 2)
            l = r - 1
            res = is_palindrome(new_lower_string, l, r)

        print(res)
        return res


if __name__ == '__main__':
    solution = Solution()
    solution.isPalindrome(s = " ")