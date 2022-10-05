class Solution:
    # hint
    # 因為要轉90度
    # 所以要先reverse，再對角線交換
    def rotate(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 定義row和col的數量
        rows = len(matrix)

        # reverse
        matrix.reverse()

        # 對角線交換
        for row in range(rows):
            for col in range(row):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        print(matrix)
        return matrix


if __name__ == '__main__':
    solution = Solution()
    solution.rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]])