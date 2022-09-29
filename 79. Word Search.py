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


if __name__ == '__main__':
    solution = Solution()
    solution.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")