class Solution:
    # hint
    # 抓到為0的位置，並記錄
    # 針對為0位置的直行橫列全部設成0，把所有為0的位置都loop過一次
    # 可以看筆記
    def setZeroes(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        # 得到value為0的位置
        zero_location = []
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    zero_location.append((row, col))

        # 把value為0位置的直行橫列全部改成0
        for row, col in zero_location:
            # process col
            for i in range(cols):
                matrix[row][i] = 0

            # process row
            for i in range(rows):
                matrix[i][col] = 0


if __name__ == '__main__':
    solution = Solution()
    solution.setZeroes(matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]])