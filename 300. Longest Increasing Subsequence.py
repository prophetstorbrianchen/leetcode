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

    def lengthOfLIS_2(self, nums: [int]) -> int:
        # setting
        dp = [1] * len(nums)

        # algo - button up
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                continue
            else:
                for j in range(len(nums) - 1, i, -1):
                    if nums[i] < nums[j]:
                        dp[i] = max(dp[i], dp[j] + 1)

        print(dp)
        return max(dp)


if __name__ == '__main__':
    solution = Solution()
    solution.lengthOfLIS_2(nums = [0,1,0,3,2,3])