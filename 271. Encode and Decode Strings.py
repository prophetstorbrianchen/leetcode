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

    def encode_2(self, strs: list):
        # 用#當中間隔開
        encode = ""
        for string in strs:
            encode = encode + str(len(string)) + "#" + string

        print(encode)
        return encode

    def decode_2(self, strs: str):
        res = []
        l = 0
        r = 0

        while r < len(strs):
            if strs[r] == "#":
                # 得出數字
                num = int(strs[l: r + 1])

                # 得出字串位置
                string = strs[r + 1: r + 1 + num]

                # 更新l和r的位置
                l = r + 1 + num
                r = l

                res.append(string)
            else:
                r = r + 1

        print(res)
        return res


if __name__ == '__main__':
    solution = Solution()
    encode = solution.encode(["10#a#########b", "2#op"])
    decode = solution.decode(encode)

    encode_2 = solution.encode_2(["10#a#########b", "2#op"])
    decode_2 = solution.decode(encode_2)