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
            # 最後一個不看
            if i == len(nums) - 1:
                continue
            else:
                for j in range(len(nums) - 1, i, -1):
                    if nums[i] < nums[j]:
                        dp[i] = max(dp[i], dp[j] + 1)

        print(dp)
        return max(dp)

    def lengthOfLIS_3(self, nums: [int]) -> int:
        dp = [1] * len(nums)

        for n in range(len(nums) - 1, -1, -1):
            # 因為最後一個的dp必定為1 -> dp[-1] = 1
            if n == 0:
                break
            for i in range(len(nums) - 1, n - 1, -1):
                if nums[n - 1] < nums[i]:
                    dp[n - 1] = max(dp[n - 1], dp[i] + 1)

        print(dp)
        return max(dp)


if __name__ == '__main__':
    solution = Solution()
    solution.lengthOfLIS_3(nums = [1,2,4,3])