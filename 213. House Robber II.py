class Solution:
    # hint
    # 為house robber I的變形題，仍然使用house robber I來解
    # 因為頭尾不能同時搶，所以要分成2種case，然後取最大值
    def rob(self, nums: [int]) -> int:
        def rob_I(nums):
            # set list
            dp = [-1] * len(nums)

            # edge case and define base dp value
            if len(nums) == 1:
                return nums[0]
            elif len(nums) == 2:
                return max(nums[0], nums[1])
            else:
                dp[0] = nums[0]
                # 再只有2個房子時，只能搶最大的 -> 這個要注意
                dp[1] = max(nums[0], nums[1])

            # update list
            # 因為不能連續搶劫
            for n in range(2, len(nums)):
                dp[n] = max(dp[n - 1], dp[n - 2] + nums[n])

            return dp[-1]

        # edge case
        if len(nums) == 1:
            # print(nums[0])
            return nums[0]

        # 去頭和去尾的處理，因為沒辦法同時搶頭尾
        remove_first_nums = nums[1:]
        remove_last_nums = nums[:-1]
        # print(max(rob_I(remove_first_nums), rob_I(remove_last_nums)))
        return max(rob_I(remove_first_nums), rob_I(remove_last_nums))


if __name__ == '__main__':
    solution = Solution()
    solution.rob(nums = [1])