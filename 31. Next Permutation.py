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
        # 從倒數第二個開始遍歷
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


if __name__ == '__main__':
    solution = Solution()
    solution.nextPermutation(nums = [1,2,3])