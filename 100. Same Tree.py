class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: [TreeNode], q: [TreeNode]) -> bool:
        def dfs(root_p, root_q):
            if not root_p and not root_q:
                return True

            if not root_p or not root_q:
                return False

            if root_p.val == root_q.val and dfs(root_p.left, root_q.left) and dfs(root_p.right, root_q.right):
                return True

        # print(dfs(p, q))
        return dfs(p, q)

    def isSameTree_2(self, p: [TreeNode], q: [TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val == q.val and self.isSameTree_2(p.left, q.left) and self.isSameTree_2(p.right, q.right):
            return True


if __name__ == '__main__':
    solution = Solution()
    root_p, node2_p, node3_p,  = TreeNode(1), TreeNode(2), TreeNode(3)
    root_p.left = node2_p
    root_p.right = node3_p

    root_q, node2_q, node3_q, = TreeNode(1), TreeNode(2), TreeNode(3)
    root_q.left = node2_q
    root_q.right = node3_q

    solution.isSameTree(p = root_p, q = root_q)
    solution.isSameTree_2(p=root_p, q=root_q)
