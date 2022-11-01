from base_function import BuildTree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: [TreeNode]) -> [int]:
        # method 1: dfs
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


if __name__ == '__main__':
    solution = Solution()
    buildTree = BuildTree()
    root = buildTree.deserialize([1,2,"N",5,"N","N",3,"N",4,"N","N"])
    solution.rightSideView(root= root)

