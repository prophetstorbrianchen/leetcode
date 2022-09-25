class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: [TreeNode]) -> [TreeNode]:
        def dfs(r):
            if not r:
                return

            temp = r.left
            r.left = r.right
            r.right = temp

            dfs(r.left)
            dfs(r.right)
            return
        dfs(root)

        return root


if __name__ == '__main__':
    solution = Solution()
    root, node2, node3,  = TreeNode(2), TreeNode(1), TreeNode(3)
    root.left, root.right = node2, node3
    solution.invertTree(root=root)
