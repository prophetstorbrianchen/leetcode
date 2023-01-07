class Solution:
    # hint
    # sliding windows
    def strStr(self, haystack: str, needle: str) -> int:
        string_length = len(needle)

        tmp_string = ""
        for i, s in enumerate(haystack):
            if len(tmp_string) != string_length:
                tmp_string = tmp_string + s
            else:
                tmp_string = tmp_string[1:] + s

            if needle == tmp_string:
                # print(i - string_length + 1)
                return i - string_length + 1

        # print(-1)
        return -1


if __name__ == '__main__':
    solution = Solution()
    solution.strStr(haystack = "sadbutsad", needle = "sad")