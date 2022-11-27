class Solution:
    # hint
    # 看筆記，多做幾次
    # https://www.youtube.com/watch?v=U-fW7MEJPLs
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        up = 0
        down = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        res = []
        while left <= right and up <= down:
            # from left to right
            for i in range(left, right + 1):
                res.append(matrix[up][i])
            up = up + 1

            # from top to down
            for i in range(up, down + 1):
                res.append(matrix[i][right])
            right = right - 1

            # from right to left
            # 必須要特別注意上邊是否小於等於下邊
            # **要記得是up <= down，當由右到左的時候**
            if up <= down:
                for i in range(right, left - 1, -1):
                    res.append(matrix[down][i])
                down = down - 1

            # from down to top
            # 必須要特別注意左邊是否小於等於右邊
            # **要記得是left <= right，當由下到上的時候**
            if left <= right:
                for i in range(down, up - 1, -1):
                    res.append(matrix[i][left])
                left = left + 1

        print(res)
        return res


if __name__ == '__main__':
    solution = Solution()
    solution.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]])