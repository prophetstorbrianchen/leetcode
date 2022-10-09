class Solution:
    # hint
    # 我這題使用list去做會超出界，r = r + 1 時 -> 其實也不用r = r + 1 去做，因為r每步都在更新
    # 只要在l向右時，注意count要減一
    # window的長度是以len(s[l:r])來算
    def characterReplacement(self, s: str, k: int) -> int:
        """
        # method 1
        l, r = 0, 0
        longest_lenght = 0
        hash_table = {}

        while r <= len(s):
            if not hash_table:
                max_len = 0
            else:
                max_len = max(hash_table.values())

            if len(s[l:r]) - max_len <= k:
                longest_lenght = max(longest_lenght, len(s[l:r]))
                prev_r = r
                r = r + 1
                if s[prev_r:r] not in hash_table:
                    hash_table[s[prev_r:r]] = 0
                hash_table[s[prev_r:r]] = hash_table[s[prev_r:r]] + 1
            else:
                prev_l = l
                l = l + 1
                hash_table[s[prev_l:l]] = hash_table[s[prev_l:l]] - 1

        print(longest_lenght)
        return longest_lenght
        """

        # method 2
        l, r = 0, 0
        longest_length = 0
        hash_table = {}

        while r < len(s):
            if s[r] not in hash_table:
                hash_table[s[r]] = 0
            hash_table[s[r]] = hash_table[s[r]] + 1

            if not hash_table:
                max_len = 0
            else:
                max_len = max(hash_table.values())

            if (r - l) + 1 - max_len <= k:
                pass
            else:
                # l需要向右，向右之後table要繼續更新
                hash_table[s[l]] = hash_table[s[l]] - 1
                l = l + 1

            longest_length = max(longest_length, (r - l) + 1)

            # 因為每個步驟r都會向右走1
            r = r + 1

        print(longest_length)
        return longest_length

    def characterReplacement_2(self, s: str, k: int) -> int:
        l = 0
        longest_len = 0
        count_table = {}
        for r in range(len(s)):
            # 做表，算最多字元的各數
            if s[r] not in count_table:
                count_table[s[r]] = 0
            count_table[s[r]] = count_table[s[r]] + 1

            # 得到最多字元的長度
            max_len = max(count_table.values())

            # window_len - max <= k
            window_len = r - l + 1
            if window_len - max_len <= k:
                longest_len = max(longest_len, window_len)
            else:
                # 向右移之後，前面的那個char不能被算在更新count_table，必須被扣掉
                pre_char = s[l]

                # 更新count_table
                count_table[pre_char] = count_table[pre_char] - 1

                # L要向右移1格
                l = l + 1

        print(longest_len)
        return longest_len


if __name__ == '__main__':
    solution = Solution()
    solution.characterReplacement(s = "AABABBA", k = 1)
    solution.characterReplacement_2(s = "ABAB", k = 2)