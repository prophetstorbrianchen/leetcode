class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            # edge case, 當p為q的子樹時 or 當q為p的子樹時
            if root.val == p.val or root.val == q.val:
                print(root)
                return root

            if p.val < root.val and q.val < root.val:
                # pq同為左子樹
                root = root.left
            elif p.val > root.val and q.val > root.val:
                # pq同為右子樹
                root = root.right
            else:
                # pq為不同邊的子樹
                print(root)
                return root


if __name__ == '__main__':
    solution = Solution()
    root_p, node2_p, node3_p, node4_p, node5_p, node6_p, node7_p = TreeNode(6), TreeNode(2), TreeNode(8), TreeNode(0), TreeNode(4), TreeNode(7), TreeNode(9)
    root_p.left = node2_p
    root_p.right = node3_p
    node2_p.left = node4_p
    node2_p.right = node5_p
    node3_p.left = node6_p
    node3_p.right = node7_p

    solution.lowestCommonAncestor(root = root_p, p = node2_p, q = node3_p)

