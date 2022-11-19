from base_function import BuildTree
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # hint
    # 可用dfs，但主要應該是要用bfs
    def zigzagLevelOrder(self, root: [TreeNode]) -> [[int]]:
        # method 1 -> dfs
        """
        def dfs(r, d):
            if not r:
                return

            if d not in res:
                res[d] = []
            res[d].append(r.val)

            dfs(r.left, d + 1)
            dfs(r.right, d + 1)

        res = {}
        depth = 0
        dfs(root, depth)

        result = []
        for i, (key, value) in enumerate(res.items()):
            if i % 2 == 1:
                result.append(value[::-1])
            else:
                result.append(value)
        return result
        """
        # method 2 -> bfs
        if not root:
            return
        q = deque([root])
        depth = 0
        result = []
        while q:
            depth = depth + 1
            new_q = []
            tmp = []
            for _ in range(len(q)):
                # do somethins with this layer nodes...
                node = q.pop()
                tmp.append(node.val)
                # 一層要換一層不用換
                if depth % 2 == 1:
                    if node.left:
                        new_q.append(node.left)
                    if node.right:
                        new_q.append(node.right)
                else:
                    if node.right:
                        new_q.append(node.right)
                    if node.left:
                        new_q.append(node.left)
            # 记得将旧的队列替换成新的队列
            q = new_q
            result.append(tmp)
        # 最后return想要返回的东西
        print(result)
        return result

    def zigzagLevelOrder_2(self, root: [TreeNode]) -> [[int]]:
        # **使用BFS，要非常熟練這個模板 -> q.pop()/if node.left/if node.right**
        # 第一層是左右
        # 第二層是右左
        # 第三層是左右

        # **edge case**
        if not root:
            return

        res = []
        q = [root]
        depth = 0
        while q:
            depth = depth + 1
            tmp = []
            new_q = []
            # 使用_ in range(len(q)) and pop的方式是為了要倒敘放入queue
            # 使用node in q -> 正序放入queue
            for _ in range(len(q)):
                node = q.pop()
                val = node.val
                tmp.append(val)

                # count % 2 == 0 -> 先左在右
                if depth % 2 == 1:
                    if node.left:
                        new_q.append(node.left)
                    if node.right:
                        new_q.append(node.right)
                else:
                    if node.right:
                        new_q.append(node.right)
                    if node.left:
                        new_q.append(node.left)

            res.append(tmp)
            q = new_q
        print(res)
        return res


if __name__ == '__main__':
    solution = Solution()
    buildTree = BuildTree()
    root = buildTree.deserialize([3,9,"N","N",20, 15,"N","N",7,"N","N"])
    solution.zigzagLevelOrder_2(root= root)

