from base_function import BuildTree
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: [TreeNode]) -> [int]:
        # method 1: dfs
        """
        def dfs(r, d):
            if not r:
                return

            if d not in res:
                res[d] = []
            res[d].append(r.val)

            dfs(r.left, d + 1)
            dfs(r.right, d + 1)
            return

        res = {}
        depth = 0
        dfs(root, depth)

        result = []
        for key, value in res.items():
            result.append(value[-1])

        return result
        """
        # method 2 -> bfs
        if not root:
            return
        q = [root]
        depth = 0
        res = []
        while q:
            # 每次都會更新q，當有左右子樹的情況
            # 因為是bfs，所以q[-1]，一定是樹的最右邊
            res.append(q[-1].val)
            depth = depth + 1
            new_q = []
            for node in q:
                # do somethins with this layer nodes...
                # 判断左右子树
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            # 记得将旧的队列替换成新的队列
            q = new_q
        # 最后return想要返回的东西
        print(res)
        return res



if __name__ == '__main__':
    solution = Solution()
    buildTree = BuildTree()
    root = buildTree.deserialize([1,2,"N",5,"N","N",3,"N",4,"N","N"])
    solution.rightSideView(root= root)

