class Solution:
    # hint
    # 在考sort
    def sortColors(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # --method 1--
        # 氣泡排序
        n = len(nums)

        # 遍历所有数组元素
        for i in range(n):
            # Last i elements are already in place
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        print(nums)
        return nums

        """
        # 使用list
        red = []
        white = []
        blue = []
        for n in nums:
            if n == 0:
                red.append(n)
            elif n == 1:
                white.append(n)
            else:
                blue.append(n)

        # nums[:] -> 複製list的意思
        nums[:] = red + white + blue
        return nums
        """


if __name__ == '__main__':
    solution = Solution()
    solution.sortColors(nums = [2,0,2,1,1,0])