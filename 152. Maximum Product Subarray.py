class Solution:
    # hint
    # 要看筆記
    def maxProduct(self, nums: [int]) -> int:
        # the zero case -> [-1, 0, -2]
        max_result = max(nums)
        cur_max, cur_min = 1, 1

        for n in nums:
            # edge case, need to reset to 1
            if n == 0:
                cur_max, cur_min = 1, 1
                continue

            # cur_max會被換掉，就不是用舊的cur_max去得到cur_min
            # 舊的cur_max要先keep起來
            tmp = n * cur_max
            # the n is for this case [-1, 8] and [-1, -8] -> 這case很容易忘
            cur_max = max(n * cur_max, n * cur_min, n)
            cur_min = min(tmp, n * cur_min, n)

            max_result = max(max_result, cur_max)

        print(max_result)
        return max_result


if __name__ == '__main__':
    solution = Solution()
    solution.maxProduct(nums = [2,3,-2,4])