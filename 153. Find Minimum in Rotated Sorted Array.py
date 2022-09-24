class Solution:
    def findMin(self, nums: [int]) -> int:
        l = 0
        r = len(nums) - 1
        min_res = float('inf')

        while l <= r:
            # 紀錄m值
            m = (l + r) // 2
            min_res = min(min_res, nums[m])

            if nums[l] <= nums[r]:
                # 如果已經是排序完的情況，那肯定L必定最小
                min_res = min(min_res, nums[l])
                print(min_res)
                return min_res

            # 注意向左向右找的情況，可以看筆記
            if nums[l] <= nums[m]:
                # 向右找
                l = m + 1
            else:
                # 向左找
                r = m - 1


if __name__ == '__main__':
    solution = Solution()
    solution.findMin(nums = [4,5,6,7,0,1,2])


