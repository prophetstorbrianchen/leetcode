class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        hash_table = {}
        nums.sort()

        for n in nums:
            if n not in hash_table:
                hash_table[n] = 0

            hash_table[n] = hash_table[n] + 1
            if hash_table[n] >= 2:
                print(True)
                return True

        print(False)
        return False


if __name__ == '__main__':
    solution = Solution()
    solution.containsDuplicate(nums = [1,2,3,4])