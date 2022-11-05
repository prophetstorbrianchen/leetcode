class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        # method 1 -> 最直觀的解法
        """
        new_matrix = []
        for m in matrix:
            new_matrix = new_matrix + m

        print(new_matrix)

        l = 0
        r = len(new_matrix) - 1

        while l <= r:
            m = (l + r) // 2

            # 要找最接近答案的那個，所以這個res在整個while沒跑完前會一直更新
            # 因為並非找固定某個值，而是timestamp_prev <= timestamp就可以
            if new_matrix[m] == target:
                print(True)
                return True

            # 向右找
            if new_matrix[m] < target:
                l = m + 1
            else:
                # 向左找
                r = m - 1

        print(False)
        return False
        """

        # method 2 -> neetcode解法 -> 2次的binary search
        top = 0
        bot = len(matrix) - 1

        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        # 因為跳出來有2種可能
        # 1. 找到row
        # 2. 因為bot > top 而跳出
        if not (top <= bot):
            return False

        row = (top + bot) // 2
        l = 0
        r = len(matrix[0]) - 1

        while l <= r:
            m = (l + r) // 2

            if target == matrix[row][m]:
                print(True)
                return True

            if target > matrix[row][m]:
                l = m + 1
            else:
                r = m - 1

        print(False)
        return False


if __name__ == '__main__':
    solution = Solution()
    solution.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)