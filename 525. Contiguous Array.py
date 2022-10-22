class Solution:
    # hint
    # prefix_sun
    # hash table
    # https://maxming0.github.io/2020/04/26/Contiguous-Array/
    def findMaxLength(self, nums: [int]) -> int:
        # 使用prefix的和得到一數列，碰到0扣1，碰到1加1
        sum = 0

        # 因為使用了prefix來做 -> 看筆記
        prefix = [0]
        for n in nums:
            if n == 0:
                sum = sum - 1
            else:
                sum = sum + 1

            prefix.append(sum)
        print(prefix)

        # 使用hash table去紀錄prefix值，碰到重複的就去比，紀錄max的那個
        hash_table = {}
        max_length = 0

        for i, item in enumerate(prefix):
            if item not in hash_table:
                hash_table.update({item: i})
            else:
                origin_index = hash_table[item]
                equal_index = origin_index + 1
                max_length = max(max_length, (i - equal_index) + 1)

        print(max_length)
        return max_length


if __name__ == '__main__':
    solution = Solution()
    solution.findMaxLength(nums = [1,0,1])



