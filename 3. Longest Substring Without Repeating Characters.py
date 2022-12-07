class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # get longest substring
        cur_list = []
        max_length = 0
        r = 0
        while r < len(s):
            if s[r] not in cur_list:
                cur_list.append(s[r])
                r = r + 1
                max_length = max(max_length, len(cur_list))
            else:
                # 得到重複的char
                # 看是哪個當前的list char得到重複的char，要從重複的字元的後一個開始重新記算
                duplicate_char_index = cur_list.index(s[r])
                cur_list = cur_list[duplicate_char_index + 1:]
                cur_list.append(s[r])
                r = r + 1

        print(max_length)
        return max_length

    def lengthOfLongestSubstring_2(self, s: str) -> int:
        r = 0

        max_len = 0.
        # **要記錄每次更新的string**
        cur_string = ""
        while r < len(s):
            if s[r] not in cur_string:
                cur_string = cur_string + s[r]
                max_len = max(max_len, len(cur_string))
            else:
                # **從重複的後面一個開始算**
                duplica_index = cur_string.index(s[r])

                # 更新cur_string
                cur_string = cur_string[duplica_index + 1:] + s[r]

            r = r + 1
        print(max_len)
        return max_len

    def lengthOfLongestSubstring_3(self, s: str) -> int:
        max_string = ""
        string = ""
        for i, c in enumerate(s):
            if c not in string:
                string = string + c
                if len(max_string) <= len(string):
                    max_string = string
            else:
                duplicate_index = string.index(c)
                string = string[duplicate_index + 1:] + c

        # print(max_string)
        return len(max_string)


if __name__ == '__main__':
    solution = Solution()
    solution.lengthOfLongestSubstring_3(s = "pwwkew")
    # solution.lengthOfLongestSubstring_2(s = " ")