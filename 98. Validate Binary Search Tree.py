class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: [TreeNode]) -> bool:
        def dfs(r, u, l):
            if not r:
                return True

            val = r.val
            if (val >= u) or (val <= l):
                return False

            # 每次都要調整上下邊界
            # 進左子樹就要l以lower當底邊的邊界
            # 進右子樹就要u以upper當底邊的邊界
            if dfs(r.left, val, l) and dfs(r.right, u, val):
                return True

        # set upper and lower
        upper = float("inf")
        lower = float("-inf")
        return dfs(root, upper, lower)


if __name__ == '__main__':
    solution = Solution()
    root_p, node2_p, node3_p,  = TreeNode(2), TreeNode(1), TreeNode(3)
    root_p.left = node2_p
    root_p.right = node3_p

    root_q, node2_q, node3_q, = TreeNode(1), TreeNode(2), TreeNode(3)
    root_q.left = node2_q
    root_q.right = node3_q

    solution.isValidBST(root = root_p)
