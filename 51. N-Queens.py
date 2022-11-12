class Solution:
    # hint
    # 以row為主體時，使用col/posDiag/negDiag來記錄位置，使quuen不能互撞
    # neetcode這題講得很好，容易懂
    # https://www.youtube.com/watch?v=Ph95IHmRp5M
    def solveNQueens(self, n: int) -> [[str]]:
        # c
        col = set()
        # (r + c)
        posDiag = set()
        # (r - c)
        negDiag = set()

        res = []
        # 如果放入queen，就更新棋盤
        # 答案是board -> 但我不知道為什麼board0不行 -> 明明格式都一模一樣
        # https://blog.csdn.net/weixin_43303161/article/details/115683927
        # 因為[["."] * n] * n -> 永遠都是reference第一個list，所以一個改了，後面都會跟著改

        # board0 = [["."] * n] * n
        board = [["."] * n for i in range(n)]
        # print(board0)
        # print(board)
        # board0[0][0] = 1
        # board[0][0] = 1

        def dfs(r):
            # base case
            # 因為是以row為主體來看，row走到底意味著queen也放完了
            if r == n:
                # 因為答案要的是string
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            # backtracking
            for c in range(n):
                # 若在這些位置上，表示有quuen會attack，不能放
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                # 放過的queen的位置，都要被記載在col/posDiag/negDiag
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                dfs(r + 1)

                # 當回到上一層時，這些紀錄就要被remove調 -> dfs or backtracking基本的套路
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        dfs(0)
        print(res)
        return res


if __name__ == '__main__':
    solution = Solution()
    solution.solveNQueens(n = 4)