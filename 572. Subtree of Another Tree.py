class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: [TreeNode], subRoot: [TreeNode]) -> bool:
        def dfs(root_p, root_q):
            if not root_p and not root_q:
                return True

            if not root_p or not root_q:
                return False

            if root_p.val == root_q.val and dfs(root_p.left, root_q.left) and dfs(root_p.right, root_q.right):
                return True

        # root本身為root的子樹
        # 下面就如同dfs中的判斷
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        return dfs(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSubtree_2(self, root: [TreeNode], subRoot: [TreeNode]) -> bool:
        def dfs(r, sub_r):
            if not r and not sub_r:
                return True

            if not r or not sub_r:
                return False

            if r.val == sub_r.val and dfs(r.left, sub_r.left) and dfs(r.right, sub_r.right):
                return True

        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        # **記得是or，只要一個對就對了**
        if dfs(root, subRoot) or self.isSubtree_2(root.left, subRoot) or self.isSubtree_2(root.right, subRoot):
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    root_p, node2_p, node3_p, node4_p, node5_p = TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(1), TreeNode(2)
    root_p.left = node2_p
    root_p.right = node3_p
    node2_p.left = node4_p
    node2_p.right = node5_p

    root_q, node2_q, node3_q, = TreeNode(4), TreeNode(1), TreeNode(2)
    root_q.left = node2_q
    root_q.right = node3_q
    solution.isSubtree(root = root_p, subRoot = root_q)

