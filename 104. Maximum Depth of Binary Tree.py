class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: [TreeNode]) -> [TreeNode]:
        def dfs(r, d, max_d):
            if not r:
                return

            max_d[0] = max(max_d[0], d)

            dfs(r.left, d + 1, max_d)
            dfs(r.right, d + 1, max_d)
            return

        if not root:
            return 0

        max_depth = [0]
        depth = 1
        dfs(root, depth, max_depth)

        print(max_depth[0])
        return max_depth[0]


if __name__ == '__main__':
    solution = Solution()
    root, node2, node3,  = TreeNode(2), TreeNode(1), TreeNode(3)
    root.left = node2
    node2.left = node3
    solution.maxDepth(root=root)
