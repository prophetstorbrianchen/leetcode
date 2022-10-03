class Solution:
    # hint
    # 使用DP，然後看筆記
    def maxSubArray(self, nums: [int]) -> int:
        # set dp list and define dp[0] = nums[0]
        dp = [nums[0]] * len(nums)

        # update dp[1] ~ dp[i]
        for i in range(1, len(nums)):
            dp[i] = max((dp[i - 1] + nums[i]), nums[i])

        print(dp)
        return max(dp)


if __name__ == '__main__':
    solution = Solution()
    solution.maxSubArray(nums = [1])