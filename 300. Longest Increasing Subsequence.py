class Solution:
    # hint
    # 這個DP是從DFS with cache來的
    # 需要看筆記
    # DP的buttom-up
    def lengthOfLIS(self, nums: [int]) -> int:
        dp = [1] * len(nums)

        # 這個loop要很熟練
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        print(max(dp))
        return max(dp)


if __name__ == '__main__':
    solution = Solution()
    solution.lengthOfLIS(nums = [1, 2, 4, 3])