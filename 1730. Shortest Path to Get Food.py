import collections


class Solution:
    # hint
    # BFS標準題型
    # https://www.youtube.com/watch?v=F0VC47KVnFI
    # 下次可以使用set()，來記錄你走過的路徑 -> 就是之前做的那種BFS標準題型
    def getFood(self, grid: [[str]]) -> int:
        row = -1
        col = -1
        found = False

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "*":
                    row = r
                    col = c
                    # 要變成無法走
                    # 而found是為了提早結束迴圈
                    grid[r][c] = "X"
                    found = True
                    break
            if found:
                break

        q = collections.deque()
        q.append((row, col, 0))
        while q:
            r, c, p = q.popleft()
            # 上
            if 0 <= r - 1 < len(grid) and 0 <= c < len(grid[0]) and grid[r - 1][c] != "X":
                if grid[r-1][c] == "#":
                    print(p + 1)
                    return p + 1
                else:
                    q.append((r-1, c, p + 1))
                    grid[r - 1][c] = "X"
            # 下
            if 0 <= r + 1 < len(grid) and 0 <= c < len(grid[0]) and grid[r + 1][c] != "X":
                if grid[r + 1][c] == "#":
                    print(p + 1)
                    return p + 1
                else:
                    q.append((r + 1, c, p + 1))
                    grid[r + 1][c] = "X"
            # 左
            if 0 <= r < len(grid) and 0 <= c - 1 < len(grid[0]) and grid[r][c - 1] != "X":
                if grid[r][c - 1] == "#":
                    print(p + 1)
                    return p + 1
                else:
                    q.append((r, c - 1, p + 1))
                    grid[r][c - 1] = "X"
            # 右
            if 0 <= r < len(grid) and 0 <= c + 1 < len(grid[0]) and grid[r][c + 1] != "X":
                if grid[r][c + 1] == "#":
                    print(p + 1)
                    return p + 1
                else:
                    q.append((r, c + 1, p + 1))
                    grid[r][c + 1] = "X"
        print(-1)
        return -1


if __name__ == '__main__':
    solution = Solution()
    solution.getFood(grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]])
