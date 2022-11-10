class Solution:
    # 學會dfs + cache -> 可以使暴力法dfs更有效率 -> DP
    # https://www.youtube.com/watch?v=wCc_nd-GiEc
    def longestIncreasingPath(self, matrix: [[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        # (r, c) -> LIP
        dp = {}

        def dfs(r, c, prevVal):
            # 超出邊界或是value你要比的那個值 -> matrix[r][c]就是指到上下左右的那格，大於matrix[r][c]才能往下走，反之就停止
            if (r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prevVal):
                return 0

            # 為DP cache，走過就不用再走了
            if (r, c) in dp:
                return dp[(r, c)]

            # 要馬就是自己一格 -> 1; 若是往下一格 -> 那就要 +1
            # 取Max
            res = 1
            # 上
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            # 下
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            # 左
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            # 右
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))

            # 把每次更新結果存起來 -> 下面哪一種都對，原因是他每個點就只會記一次，不會重複記，去蓋掉舊的
            dp[(r, c)] = res
            # if (r, c) not in dp:
            #     dp[(r, c)] = res
            return res

        # 每個點都走訪，但和暴力法不同 -> 這個有DP cache，所以少走重複的路
        for r in range(ROWS):
            for c in range(COLS):
                # 因為最少都可以走一格，也就是自己本身那格，而那格最小為0 -> 永遠都要能過自己那格
                # 當然給float("-inf")一樣也可以
                dfs(r, c, -1)

        # 因為是找最長路徑
        # print(max(dp.values()))
        return max(dp.values())


if __name__ == '__main__':
    solution = Solution()
    solution.longestIncreasingPath(matrix = [[9,9,4],[6,6,8],[2,1,1]])