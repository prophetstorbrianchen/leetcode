class Solution:
    # hint
    # 這是對一串數字，找出比他大一級的方法
    # 1.找升序
    # 2.找比升序大的數字，然後交換
    # 3.對升序之後的位置做reverse
    # https://maxming0.github.io/2021/01/31/Next-Permutation/
    # 這動畫完全表現出這個algo
    # https://leetcode.cn/problems/next-permutation/solution/xia-yi-ge-pai-lie-by-leetcode-solution/
    def nextPermutation(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # 從倒數第二個開始遍歷 -> 因為由後向前，如果從倒數第一個開始會out of range
        i = n - 2
        while i >= 0:
            # 判斷是否生序
            if nums[i] >= nums[i + 1]:
                # 不是升序，就繼續由後向前找
                i = i - 1
            else:
                # 是升序
                for j in range(n - 1, i, -1):
                    # 再從後向前找，找到比nums[i]還大的數，進行交換
                    if nums[j] > nums[i]:
                        # 交換
                        nums[i], nums[j] = nums[j], nums[i]
                        # 對i後面的數做排序 -> 即可得到最終的結果
                        nums[i + 1:] = sorted(nums[i + 1:])
                        return

        # 若沒有升序，表示此為最大排序，直接reverse即可
        nums.reverse()

    def nextPermutation_2(self, nums: [int]) -> None:
        # 找到升序 -> 交換
        # 交換是從後面開始看，第一個比i大的就交換
        # 對升序後面的list做reverse

        i = len(nums) - 2

        while i >= 0:
            # 找升序
            if nums[i] < nums[i + 1]:
                # **從最後一個開始招，找到必須找第一個比i大的，然後交換 -> 而非左又交換，這差很多**
                # 只要到第i個就可以
                for j in range(len(nums) - 1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        # 做reverse
                        nums[i+1:] = sorted(nums[i+1:])
                        print(nums)
                        return nums
            else:
                i = i - 1

        print(nums)
        return nums.reverse()


if __name__ == '__main__':
    solution = Solution()
    solution.nextPermutation_2(nums = [2,3,1])