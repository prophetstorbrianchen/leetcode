import collections


class Solution:
    # hint
    # 第一種方法為BFS -> 從四周向內擴散 -> 記住被擴散的位置為"O"
    # 第二種方法為DFS -> 從四周向內擴散 -> 記住被擴散的位置為"O"
    def solve(self, board: [[str]]) -> None:
        # 從4周向內擴散，被擴散到的絕對不會變X

        rows = len(board)
        cols = len(board[0])

        q = collections.deque()
        for row in range(rows):
            for col in range(cols):
                if (row == 0 or row == rows - 1 or col == 0 or col == cols - 1) and board[row][col] == "O":
                    q.append((row, col))

        # bfs
        seen = set()    # seen -> "O"的位置
        while q:
            r, c = q.popleft()
            seen.add((r, c))
            # 上
            if 0 <= r - 1 < rows and 0 <= c < cols and (r - 1, c) not in seen and board[r - 1][c] == "O":
                q.append((r - 1, c))
                seen.add((r - 1, c))

            # 下
            if 0 <= r + 1 < rows and 0 <= c < cols and (r + 1, c) not in seen and board[r + 1][c] == "O":
                q.append((r + 1, c))
                seen.add((r + 1, c))

            # 左
            if 0 <= r < rows and 0 <= c - 1 < cols and (r, c - 1) not in seen and board[r][c - 1] == "O":
                q.append((r, c - 1))
                seen.add((r, c - 1))

            # 右
            if 0 <= r < rows and 0 <= c + 1 < cols and (r, c + 1) not in seen and board[r][c + 1] == "O":
                q.append((r, c + 1))
                seen.add((r, c + 1))

        # 保持seen的位置為"O"，其他位置為"X"
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in seen and board[row][col] == "O":
                    board[row][col] = "X"

        # print(board)

    def solve_dfs(self, board: [[str]]) -> None:
        pass


if __name__ == '__main__':
    solution = Solution()
    solution.solve(board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])