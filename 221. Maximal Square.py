class Solution:
    # hint
    # neetcode使用dfs去做
    # 這題也可以用DP去做
    def maximalSquare(self, matrix: [[str]]) -> int:
        # DP: 由下往上
        # 遞迴: 由上往下

        ROWS, COLS = len(matrix), len(matrix[0])
        # 要cache位置，不重複做 -> (r, c) -> 可得出最大的square
        cache = {}

        def helper(r, c):
            # edge case
            if r >= ROWS or r < 0 or c >= COLS or c < 0:
                return 0

            if (r, c) not in cache:
                # 下
                down = helper(r + 1, c)

                # 右下
                right_down = helper(r + 1, c + 1)

                # 右
                right = helper(r, c + 1)

                # 設定起始位置是0 -> 如果剛好為0就為0，如果不為0那也是要看他的右/右下/下來決定大小
                cache[(r, c)] = 0
                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(down, right_down, right)

            return cache[(r, c)]

        helper(0, 0)
        return max(cache.values()) ** 2


if __name__ == '__main__':
    solution = Solution()
    solution.maximalSquare( matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])