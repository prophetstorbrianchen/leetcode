class Solution:
    # hint
    # 看筆記
    # 利用雙指針 -> 每回合r都會向右走 -> 裡面會有while會圈判斷l是否要向右走
    def minSubArrayLen(self, target: int, nums: [int]) -> int:
        # 利用雙指針 -> 當window的大小大於target時，l就要向右靠，不然平常r都要一直向右走
        # 這題method 1 就是正確的觀念，但是function的使用上會timeout(第一次就寫對了)

        # method 1 -> 使用sum做會TLE
        """
        l = 0
        r = 0
        min_window_len = float("inf")
        while r < len(nums) + 1:
            print(l, r, sum(nums[l:r]))
            wind_len = len(nums[l:r])

            if sum(nums[l:r]) >= target:
                min_window_len = min(min_window_len, wind_len)

            while sum(nums[l:r]) > target:
                l = l + 1
                print(l, r, sum(nums[l:r]))
                wind_len = len(nums[l:r])
                if sum(nums[l:r]) >= target:
                    min_window_len = min(min_window_len, wind_len)
            else:
                r = r + 1

        if min_window_len == float("inf"):
            print(0)
            return 0
        else:
            print(min_window_len)
            return min_window_len
        """

        # method 2 -> 使用len(nums[l:r + 1])會TLE
        """
        l = 0
        r = 0
        cur = 0
        min_window_len = float("inf")
        while r < len(nums):
            wind_len = len(nums[l:r + 1])
            cur = cur + nums[r]

            if cur >= target:
                min_window_len = min(min_window_len, wind_len)

            while cur > target:
                cur = cur - nums[l]
                l = l + 1

                wind_len = len(nums[l:r + 1])
                if cur >= target:
                    min_window_len = min(min_window_len, wind_len)
            else:
                r = r + 1

        if min_window_len == float("inf"):
            #print(0)
            return 0
        else:
            #print(min_window_len)
            return min_window_len
        """

        # method 3 -> 不能使用len(nums[l:r + 1])和sum(nums[l:r]) -> 會TLE
        l = 0
        r = 0
        cur = 0
        min_window_len = float("inf")
        while r < len(nums):
            wind_len = r - l + 1
            cur = cur + nums[r]

            # 找到了
            if cur >= target:
                min_window_len = min(min_window_len, wind_len)

            # 當大於target時，l要往右縮，看是否能找到更小的windows length
            while cur > target:
                cur = cur - nums[l]
                l = l + 1

                # 每做一次就要檢查一次
                wind_len = r - l + 1
                if cur >= target:
                    min_window_len = min(min_window_len, wind_len)
            else:
                r = r + 1

        if min_window_len == float("inf"):
            # print(0)
            return 0
        else:
            # print(min_window_len)
            return min_window_len


if __name__ == '__main__':
    solution = Solution()
    solution.minSubArrayLen(target = 15, nums = [5,1,3,5,10,7,4,9,2,8])