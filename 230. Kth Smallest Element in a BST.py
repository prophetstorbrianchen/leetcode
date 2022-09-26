class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # hint
    def kthSmallest(self, root: [TreeNode], k: int) -> int:
        def dfs(r, res):
            if not r:
                return

            # inorder的模板
            dfs(r.left, res)
            res.append(r.val)
            dfs(r.right, res)

            """
            # preorder的模板
            res.append(r.val)
            dfs(r.left, res)
            dfs(r.right, res)

            # postorder的模板
            dfs(r.left, res)
            dfs(r.right, res)
            res.append(r.val)
            """

        res_list = []
        dfs(root, res_list)
        print(res_list)
        return res_list[k - 1]


if __name__ == '__main__':
    solution = Solution()
    root_p, node2_p, node3_p, node4_p, node5_p, node6_p = TreeNode(5), TreeNode(3), TreeNode(6), TreeNode(2), TreeNode(4), TreeNode(1)
    root_p.left = node2_p
    root_p.right = node3_p
    node2_p.left = node4_p
    node2_p.right = node5_p
    node4_p.left = node6_p
    solution.kthSmallest(root = root_p, k = 3)