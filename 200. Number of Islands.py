import collections


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

    def numIslands_3(self, grid: [[str]]) -> int:
        # BFS寫法
        # 殭屍擴散的方法，使用q.appendleft
        # 分別給為1的island，不同的號碼
        # 因為一直擴散出去，所以相互連通的會是同一組號碼，不相互連通的會有不同的號碼
        # 最後只要看有幾個不同的號碼就可以了

        rows = len(grid)
        cols = len(grid[0])

        # 給定號碼
        q = collections.deque()
        seen = set()
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "0":
                    seen.add((r, c))
                    continue
                else:
                    q.append((r, c, count))
                count = count + 1

        island_count = set()

        # BFS
        while q:
            r, c, index = q.popleft()
            # 被擴散出去的絕對會在seen中，而獨立的必定不再seen中
            # 用此可以在island_count中得到不同的號碼 -> 有幾種不同的號碼就表示有幾個不連通的島嶼
            if (r, c) not in seen:
                seen.add((r, c))
                island_count.add(index)

            # 上
            if 0 <= r - 1 < rows and 0 <= c < cols and (r - 1, c) not in seen:
                island_count.add(index)
                # 如果使用append就會跑到後面，那index就不會被蓋掉了 -> appendleft是殭屍擴散法的精隨
                q.appendleft((r - 1, c, index))
                seen.add((r - 1, c))

            # 下
            if 0 <= r + 1 < rows and 0 <= c < cols and (r + 1, c) not in seen:
                island_count.add(index)
                q.appendleft((r + 1, c, index))
                seen.add((r + 1, c))

            # 左
            if 0 <= r < rows and 0 <= c - 1 < cols and (r, c - 1) not in seen:
                island_count.add(index)
                q.appendleft((r, c - 1, index))
                seen.add((r, c - 1))

            # 右
            if 0 <= r < rows and 0 <= c + 1 < cols and (r, c + 1) not in seen:
                island_count.add(index)
                q.appendleft((r, c + 1, index))
                seen.add((r, c + 1))

        print(len(island_count))
        return len(island_count)

    def numIslands_4(self, grid: [[str]]) -> int:
        # BFS寫法
        # 看是使用了幾次BFS，count就要加+1
        # 跟DFS方法是一樣的
        pass


if __name__ == '__main__':
    solution = Solution()
    solution.numIslands_3(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])