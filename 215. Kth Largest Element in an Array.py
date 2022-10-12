class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        sorted_nums = sorted(nums)
        print(sorted_nums[k * -1])
        return sorted_nums[k * -1]


if __name__ == '__main__':
    solution = Solution()
    solution.findKthLargest(nums = [3,2,1,5,6,4], k = 2)