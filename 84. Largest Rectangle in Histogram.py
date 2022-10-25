class Solution:
    # hint
    # 這題很難，要多看幾次
    # 看筆記和影片
    # https://www.youtube.com/watch?v=zx5Sw9130L0
    def largestRectangleArea(self, heights: [int]) -> int:
        maxArea = 0
        stack = []  # (index, height)

        for i, h in enumerate(heights):
            start = i
            # 如果stack不為空，而且stack的最上面的height是大於h時 -> pop stack -> 因為已經不能向右走了
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # 算出Area並和maxArea比，保留大的
                maxArea = max(maxArea, height * (i - index))
                # start要回到pop的index -> [2, 1] -> 2被pop了，但1要從index 0開始start
                start = index
            # 2被pop了，要把1 push進去
            stack.append((start, h))

        # 處理剩下沒有被pop的stack，算出Area去更新maxArea
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea


if __name__ == '__main__':
    solution = Solution()
    solution.largestRectangleArea(heights = [2,1,5,6,2,3])