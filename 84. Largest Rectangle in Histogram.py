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

    def largestRectangleArea_2(self, heights: [int]) -> int:
        # 需要使用stack來適時的pop和push
        # pop的時機: 當新進來的高度比stack最上面的那個小時(stack[-1])，那就要pop出來，直到stack裡面的element都完全符合條件 -> while loop
        # push的時機: 每回合都要做這件事情 -> for loop
        # 當pop出來時需要算面積 -> 使用pop出來的index和當走到的index去算 -> height * (i - index), 跟原始的max_area比，保留大的
        # 而被append進去的index，必須被改成最後被pop出來那個element的index -> 因為他會從pop出來那個element的index開始算面積，這個要看筆記 -> start = index 在while loop結束之後
        # 最後要計算剩餘在stack -> 因為剩餘的stack中，都是可以重頭跑到尾的 -> 算面積時，就從後面的index當底，計算和每個element的index差值即可

        stack = []
        max_area = 0
        # 標準Monotone Stack模板
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                # pop, 算面積
                index, height = stack.pop()
                tmp_area = height * (i - index)
                max_area = max(max_area, tmp_area)

                # **從pop出來那個element的index開始算面積**
                start = index

            # **從pop出來那個element的index開始算面積**
            stack.append((start, h))

        # 算剩餘面積
        for i, h in stack:
            tmp_area = h * (len(heights) - i)
            max_area = max(max_area, tmp_area)

        print(max_area)
        return max_area


if __name__ == '__main__':
    solution = Solution()
    solution.largestRectangleArea_2(heights = [2,1,5,6,2,3])