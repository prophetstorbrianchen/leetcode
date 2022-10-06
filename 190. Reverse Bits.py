class Solution:
    def reverseBits(self, n: int) -> int:
        # print(bin(n)[2:].zfill(32)[::-1])
        result = bin(n)[2:].zfill(32)[::-1]

        # 二進制轉10進制
        # print(int(result, 2))

        return int(result, 2)


if __name__ == '__main__':
    solution = Solution()
    solution.reverseBits(n = 0b00000010100101000001111010011100)
