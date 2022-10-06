class Solution:
    # hint
    # 可以用string的方法解
    # 這邊我用XOR去解，XOR的特性很重要
    # 3 XOR 3 -> 0, 0 XOR 3 -> 3
    # XOR特性
    # 0 xor 0 = 0
    # 0 xor 1 = 1
    # 1 xor 0 = 1
    # 1 xor 1 = 0
    def missingNumber(self, nums: [int]) -> int:
        # 列出整個數列
        full_nums = [i for i in range(len(nums) + 1)]

        res = 0
        # 3 ^ 4 ^ 3 -> 4, 3 ^ 3 ^ 0 -> 3
        # [1, 2, 3] ^ [1, 3] -> 2
        for n in nums:
            res = res ^ n

        for n in full_nums:
            res = res ^ n

        print(res)
        return res


if __name__ == '__main__':
    solution = Solution()
    solution.missingNumber(nums = [9,6,4,2,3,5,7,0,1])