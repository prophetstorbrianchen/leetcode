class Solution:
    # https://ithelp.ithome.com.tw/articles/10278644 -> quick sort
    # https://ithelp.ithome.com.tw/articles/10278179 -> merge sort
    def bubble_sort(self, nums: [int]):
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        #print(nums)

    def merge_sort(self, nums: [int]):
        def merge(left, right):
            result = []
            # 當左右都有的時候 -> 跟linklist的merge非常像
            while left and right:
                if left[0] < right[0]:
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))

            # 防止一長一短的情況
            if left:
                result = result + left
            else:
                result = result + right

            return result

        # edge case
        if len(nums) < 2:
            return nums

        # 切中間分成左右2半
        mid = len(nums) // 2
        leftArray = nums[:mid]
        rightArray = nums[mid:]

        return merge(self.merge_sort(leftArray), self.merge_sort(rightArray))


if __name__ == '__main__':
    solution = Solution()
    solution.bubble_sort(nums = [1,5,6,2,3])
    solution.merge_sort(nums = [6,2])