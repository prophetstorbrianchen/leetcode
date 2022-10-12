class Solution:
    # hint
    # 走過就要轉為0，之後才不會重複算
    # 這是一種題型，另一種題型是走訪過，回上層還需要release的，這後面會碰到
    # 這題是用dfs把所有的"1"歷變成0之後，才算一個島嶼 -> 經典題
    def numIslands(self, grid: [[str]]) -> int:
        def dfs(r, c):
            # --base case--
            if r < 0 or r >= rows:
                return

            if c < 0 or c >= cols:
                return

            if grid[r][c] == "0":
                return

            # --表示已經找到是1的點--
            # 走過要改為0，之後才不會重複走
            grid[r][c] = "0"

            # --上下左右走訪--
            dfs(r - 1, c)

            dfs(r + 1, c)

            dfs(r, c - 1)

            dfs(r, c + 1)

            return

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        # 歷遍所有點
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    islands = islands + 1

        print(islands)
        return islands

    def numIslands_2(self, grid: [[str]]) -> int:
        def dfs(r, c):
            # base case
            if r < 0 or r >= rows:
                return

            if c < 0 or c >= cols:
                return

            if grid[r][c] == "0":
                return

            # 為進入下層做準備
            # **走過的改成0**
            grid[r][c] = "0"

            # **防止往回走**
            visit.add((r, c))

            # 進入下層 -> 上下左右
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

            visit.remove((r, c))

            return

        rows = len(grid)
        cols = len(grid[0])
        count = 0
        visit = set()
        for row in range(rows):
            for col in range(cols):
                # 歷遍所有點
                if grid[row][col] == "1":
                    dfs(row, col)
                    count = count + 1

        print(count)
        return count



if __name__ == '__main__':
    solution = Solution()
    solution.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])