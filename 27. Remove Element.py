class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        count = 0
        for i, n in enumerate(nums):
            if n == val:
                nums[i] = -1
                continue
            else:
                count = count + 1

        nums.sort()
        nums.reverse()
        return count


if __name__ == '__main__':
    solution = Solution()
    solution.removeElement(nums = [3,2,2,3], val = 3)