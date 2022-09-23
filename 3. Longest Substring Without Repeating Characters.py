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


if __name__ == '__main__':
    solution = Solution()
    solution.lengthOfLongestSubstring(s = "abcabcbb")