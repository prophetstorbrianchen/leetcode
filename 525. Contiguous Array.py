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

    def findMaxLength_2(self, nums: [int]) -> int:
        # 使用prefix sum和hash table
        # 0 -> -1; 1 -> +1
        # 小技巧，必須多使用一個0在前面; {num: index}
        # nums:            [0 ,1 ,0]
        # prefix_sum: [0, -1, 0, -1]
        prefix_hash_table = {0: 0}

        init_prefix_sum = 0
        max_length = 0
        for i, n in enumerate(nums):
            if n == 0:
                init_prefix_sum = init_prefix_sum - 1
            else:
                init_prefix_sum = init_prefix_sum + 1

            if init_prefix_sum not in prefix_hash_table:
                prefix_hash_table[init_prefix_sum] = i + 1
            else:
                origin_index = prefix_hash_table[init_prefix_sum]
                new_index = i + 1
                max_length = max(max_length, new_index - origin_index)

        print(max_length)
        return max_length


if __name__ == '__main__':
    solution = Solution()
    solution.findMaxLength_2(nums = [1,0,1,0,0,1])



