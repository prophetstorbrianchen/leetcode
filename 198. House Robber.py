class Solution:
    def rob(self, nums: [int]) -> int:
        # set list
        dp = [-1] * len(nums)

        # edge case and define base dp value
        if len(nums) == 1:
            print(nums[0])
            return nums[0]
        elif len(nums) == 2:
            print(max(nums[0], nums[1]))
            return max(nums[0], nums[1])
        else:
            dp[0] = nums[0]
            # 再只有2個房子時，只能搶最大的 -> 這個要注意
            dp[1] = max(nums[0], nums[1])

        # update list
        # 因為不能連續搶劫
        for n in range(2, len(nums)):
            dp[n] = max(dp[n - 1], dp[n - 2] + nums[n])

        print(dp[-1])
        return dp[-1]

    # dp[n] = max(dp[n-2] + nums[n], dp[n-1])
    def rob_2(self, nums: [int]) -> int:
        # define dp base
        dp = [-1] * len(nums)

        # edge case
        # 當只有1棟房子
        if len(nums) == 1:
            return nums[0]
        # 當只有2棟房子
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

        # algo
        for n in range(2, len(nums)):
            dp[n] = max(dp[n - 2] + nums[n], dp[n - 1])

        return dp[-1]

    def rob_3(self, nums: [int]) -> int:
        dp = [-1] * len(nums)

        # base case
        if len(nums) == 1:
            dp[0] = nums[0]
        if len(nums) >= 2:
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        # print(dp)
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    solution.rob(nums = [2,1,1,2])