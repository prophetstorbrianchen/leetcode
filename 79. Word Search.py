class TireNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TireNode()
            cur = cur.children[c]
        cur.isWord = True


class Solution:
    # hint
    # use Word Search II
    def exist(self, board: [[str]], word: str) -> bool:
        root = TireNode()
        list_word = [word]

        for c in list_word:
            root.addWord(c)

        rows, cols = len(board), len(board[0])
        ret, visit = set(), set()

        def dfs(r, c, node, w):
            # --base case--
            if r < 0 or r >= rows:
                return

            if c < 0 or c >= cols:
                return

            if (r, c) in visit:
                return

            # 這個case要記得
            if board[r][c] not in node.children:
                return

            # --設定向下層的參數--
            # 走過的點要記下，避免往回走
            visit.add((r, c))

            w = w + board[r][c]

            node = node.children[board[r][c]]

            # base case, if the node is the end layer
            if node.isWord:
                ret.add(w)

            # --走向下一層--
            # 走上
            dfs(r - 1, c, node, w)

            # 走下
            dfs(r + 1, c, node, w)

            # 走左
            dfs(r, c - 1, node, w)

            # 走右
            dfs(r, c + 1, node, w)

            # 回上層就要釋放走訪過的點
            visit.remove((r, c))

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root, "")

        print(list(ret))
        string_result = "".join(ret)
        if string_result == word:
            return True

        return False

    def exist_2(self, board: [[str]], word: str) -> bool:
        # only use dfs and not use tried
        # TLE -> 測資改大了
        def dfs(r, c, path):
            # base
            if path == word:
                return True

            # 上
            if 0 <= r - 1 and r - 1 < rows and 0 <= c and c < cols and (r - 1, c) not in visited and path in word:
                visited.add((r - 1, c))
                top = dfs(r - 1, c, path + board[r - 1][c])
                visited.remove((r - 1, c))
            else:
                top = False

            # 下
            if 0 <= r + 1 and r + 1 < rows and 0 <= c and c < cols and (r + 1, c) not in visited and path in word:
                visited.add((r + 1, c))
                down = dfs(r + 1, c, path + board[r + 1][c])
                visited.remove((r + 1, c))
            else:
                down = False

            # 左
            if 0 <= r and r < rows and 0 <= c - 1 and c - 1 < cols and (r, c - 1) not in visited and path in word:
                visited.add((r, c - 1))
                left = dfs(r, c - 1, path + board[r][c - 1])
                visited.remove((r, c - 1))
            else:
                left = False

            # 右
            if 0 <= r and r < rows and 0 <= c + 1 and c + 1 < cols and (r, c + 1) not in visited and path in word:
                visited.add((r, c + 1))
                right = dfs(r, c + 1, path + board[r][c + 1])
                visited.remove((r, c + 1))
            else:
                right = False

            if top or down or left or right:
                return True
            else:
                return False

        rows = len(board)
        cols = len(board[0])

        visited = set()
        for row in range(rows):
            for col in range(cols):
                string = board[row][col]
                visited.add((row, col))
                if dfs(row, col, string):
                    # print(True)
                    return True
                visited.remove((row, col))

        # print(False)
        return False


if __name__ == '__main__':
    solution = Solution()
    solution.exist_2(board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]], word = "BAAAAAAAAAAAAAA")