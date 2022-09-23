class Solution:
    # hint
    # 我這題使用list去做會超出界，r = r+1時
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        longest_lenght = 0
        hash_table = {}

        while r < len(s):
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



if __name__ == '__main__':
    solution = Solution()
    solution.characterReplacement(s = "AABABBA", k = 1)