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

    # 原理要記得，需要常翻筆記
    def maxProduct_2(self, nums: [int]) -> int:
        # set cur_max and cur_min
        cur_min = 1
        cur_max = 1

        max_result = float("-inf")
        for n in nums:
            # edge case
            # 因為是連續計算，所以只要碰到0，就要重新計算了，不管是cur_max or cur_min
            if n == 0:
                cur_max = 1
                cur_min = 1

            # cur_max會被改掉，所以要temp起來
            # 這邊會計算每次的最大最小值
            temp = cur_max
            cur_max = max(cur_max * n, cur_min * n, n)
            cur_min = min(temp * n, cur_min * n, n)

            max_result = max(max_result, cur_max)

        print(max_result)
        return max_result


if __name__ == '__main__':
    solution = Solution()
    solution.maxProduct(nums = [2,0,3,4])