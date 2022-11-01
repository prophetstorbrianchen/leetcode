from base_function import BuildTree


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


if __name__ == '__main__':
    solution = Solution()
    buildTree = BuildTree()
    root = buildTree.deserialize([3,9,"N","N",20, 15,"N","N",7,"N","N"])
    solution.zigzagLevelOrder(root= root)

