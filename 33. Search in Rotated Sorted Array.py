class Solution:
    # hint
    # 要熟記三種情況，有一種情況特別難想
    # 注意三種情況等號的部分
    def search(self, nums: [int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2

            if target == nums[m]:
                print(m)
                return m

            # 已經排好
            if nums[l] < nums[r]:
                if target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # 沒排好
            else:
                if nums[l] <= nums[m] < target or nums[m] < target < nums[l] or target < nums[l] <= nums[m]:
                    l = m + 1
                else:
                    r = m - 1

        print(-1)
        return -1


if __name__ == '__main__':
    solution = Solution()
    solution.search(nums = [3,1], target = 1)


