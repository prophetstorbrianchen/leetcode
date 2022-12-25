import collections


class Solution:
    # hint
    # https://www.youtube.com/watch?v=EYeR-_1NRlQ
    # N-sum都可以這樣做
    # 4sum -> 3sum -> 2sum => 可以拆解成子問題
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        nums.sort()
        res, quad = [], []

        def kSum(k, start, target):
            # target會隨著每往下一層而改變
            if k != 2:
                # **最難的在於為什麼要len(nums) - k + 1**
                # k能到最後的index -> 最後一定要留l和r的位置
                for i in range(start, len(nums) - k + 1):
                    # 防重複
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return

            # base case
            # two sum II
            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l = l + 1
                elif nums[l] + nums[r] > target:
                    r = r - 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l = l + 1
                    # 2sum or 3sum 時的重點
                    while l < r and nums[l] == nums[l - 1]:
                        l = l + 1

        kSum(4, 0, target)
        return res


if __name__ == '__main__':
    solution = Solution()
    solution.fourSum(nums = [1,0,-1,0,-2,2], target = 0)