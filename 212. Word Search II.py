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
    # This is more complex but still can understand
    # Please review the note and vedio
    # https://www.youtube.com/watch?v=asbcE9mZz_U
    # This approach will encounter TLE but this method is very important
    def findWords(self, board: [[str]], words: [str]) -> [str]:
        root = TireNode()

        # 做出Treenode
        for w in words:
            root.addWord(w)

        rows, cols = len(board), len(board[0])

        # prevent duplicate
        ret, visit = set(), set()

        def dfs(r, c, node, word):
            # --base case--
            # top and down border
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] not in node.children or (r, c) in visit:
                return

            # left and right border
            if c < 0 or c >= cols:
                return

            # if the element not in node
            if board[r][c] not in node.children:
                return

            # if the element already visited
            if (r, c) in visit:
                return

            # --prepare into the next layer--
            # record the visit element and prepare into next layer
            visit.add((r, c))

            # update node -> prepare to in next layer
            node = node.children[board[r][c]]

            # update word -> prepare to in next layer
            word = word + board[r][c]

            # base case, if the node is the end layer
            if node.isWord:
                ret.add(word)

            # --into the next layer--
            # top dfs
            dfs(r - 1, c, node, word)

            # down dfs
            dfs(r + 1, c, node, word)

            # left dfs
            dfs(r, c - 1, node, word)

            # right dfs
            dfs(r, c + 1, node, word)

            # back to the previous layer and need to remove the visited element
            visit.remove((r, c))

        # trval all element and using the depth-first search
        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root, "")

        print(list(ret))
        return list(ret)


if __name__ == '__main__':
    solution = Solution()
    solution.findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"])