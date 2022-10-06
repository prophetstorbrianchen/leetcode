class Solution:
    def hammingWeight(self, n: int) -> int:
        # 轉成2進制
        print(bin(n))

        # 去除0b
        print(bin(n)[2:])

        # 補成32位元，前面的位數會補成0
        print(bin(n)[2:].zfill(32))

        count = 0
        # 用處理string的方式處理2進制問題
        for i in bin(n)[2:].zfill(32):
            if i == "1":
                count = count + 1
        print(count)
        return count


if __name__ == '__main__':
    solution = Solution()
    solution.hammingWeight(n = 0b00000000000000000000000000001011)
