class Solution:
    # hint
    # https://leetcode.com/problems/find-the-duplicate-number/solution/
    def findDuplicate(self, nums: [int]) -> int:
        # do not meet the constant extra space
        """
        nums.sort()
        for i, n in enumerate(nums):
            if i + 1 < len(nums):
                if nums[i + 1] == nums[i]:
                    print(nums[i])
                    return nums[i]

        print(0)
        return 0
        """

        # Approach 4.2: Array as HashMap (Iterative)
        # 這方法很神
        while nums[0] != nums[nums[0]]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
        return nums[0]


if __name__ == '__main__':
    solution = Solution()
    solution.findDuplicate(nums = [3])