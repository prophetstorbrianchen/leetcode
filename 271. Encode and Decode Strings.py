class Solution:
    def encode(self, strs: list):
        res = ""
        for string in strs:
            res = res + str(len(string)) + "#" + string

        print(res)
        return res

    def decode(self, strs: str):
        res = []
        l = 0
        r = 0

        while l < len(strs):
            if strs[r] == "#":
                # 解析字串
                length = int(strs[l:r])
                string = strs[r + 1: r + length + 1]
                res.append(string)

                # 變更左右指標位置
                l = r + length + 1
                r = l
            else:
                r = r + 1

        print(res)
        return res


if __name__ == '__main__':
    solution = Solution()
    encode = solution.encode(["10#a#########b", "2#op"])
    decode = solution.decode(encode)
