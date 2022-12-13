class Solution:
    # hint
    # Netskope考過
    # 因為要找first和last的index -> 必須分2次做binary search -> [3,5,8,8,8,10]
    # 要找左邊的一定要一直像左找
    # 要找右邊的一定要一直像右找
    def searchRange(self, nums: [int], target: int) -> [int]:

        res = []
        left_index = self.searchLeft(nums, target)
        right_index = self.searchRight(nums, target)

        res.append(left_index)
        res.append(right_index)

        print(res)
        return res

    # 因為要往左找，有可能l==r的情況 -> 這情況是允許的
    def searchLeft(self, nums, target):
        l = 0
        r = len(nums) - 1

        index = float("inf")
        while l <= r:
            m = (l + r) // 2

            # 這3種都是要一起判斷的 -> 使用if/elif/else
            # 等於/大於/小於的情況
            if nums[m] == target:
                index = min(index, m)
                # 要一直往左搜 -> 才能找到最小的
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        if index == float("inf"):
            return -1
        else:
            return index

    def searchRight(self, nums, target):
        l = 0
        r = len(nums) - 1

        index = float("-inf")
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                index = max(index, m)
                # 要一直往右搜 -> 才能找到最大的
                l = m + 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        if index == float("-inf"):
            return -1
        else:
            return index


if __name__ == '__main__':
    solution = Solution()
    solution.searchRange(nums = [8,8,8,8,8,8], target = 8)