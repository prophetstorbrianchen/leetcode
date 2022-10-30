class Solution:
    # hint
    def findAnagrams(self, s: str, p: str) -> [int]:
        # 先對p做個table
        p_dict = {}
        windows_dict = {}
        for c in p:
            if c not in p_dict:
                p_dict[c] = 0
                windows_dict[c] = 0
            p_dict[c] = p_dict[c] + 1

        res = []
        # 針對slide windows做table
        for i, c in enumerate(s):
            # 前P位是要塞入dict，要先滿足window size
            if i < len(p):
                pass
            else:
                # 因為是從P位開始，所以windows再動的時候要從前P位開始扣
                prev_c = s[i - len(p)]
                if prev_c in windows_dict:
                    windows_dict[prev_c] = windows_dict[prev_c] - 1

            if c in windows_dict:
                windows_dict[c] = windows_dict[c] + 1

            if p_dict == windows_dict:
                # 因為指針是從第P-1位開始算，所以要往回扣
                # 因為又是從0開始，所以要再扣1
                i = i - (len(p) - 1)
                res.append(i)

        return res


if __name__ == '__main__':
    solution = Solution()
    solution.findAnagrams(s = "cbaebabacd", p = "abc")