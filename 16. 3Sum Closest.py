class Solution:
    # hint
    # 3sum的延伸，但要使用雙指針 -> 比3sum還簡單
    # https://blog.csdn.net/fuxuemingzhu/article/details/83116781
    def threeSumClosest(self, nums: [int], target: int) -> int:
        # 先做sort
        nums = sorted(nums)

        # 此值是需要持續被更新的，當sum和target得差值越小時，就要更新sum值進去
        res = float("inf")

        # 使用雙指針，同3sum
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]

                # 當新的差值比原本的還小時，就更新
                if abs(target - sum) < abs(target - res):
                    res = sum

                # 因為排序過了，
                # 如果過大，那r就要向左移
                # 如果過小，那l就要像右移
                if sum == target:
                    return target
                elif sum > target:
                    r = r - 1
                else:
                    l = l + 1

        print(res)
        return res


if __name__ == '__main__':
    solution = Solution()
    solution.threeSumClosest(nums = [0,0,0], target = 1)