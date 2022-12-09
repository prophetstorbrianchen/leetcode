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

    def lowestCommonAncestor_2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            # 若一剛開始，p或q就是在root的位置
            if root.val == p.val:
                return p
            elif root.val == q.val:
                return q
            else:
                pass

            # p和q在同一邊
            if (p.val < root.val and q.val < root.val) or (p.val > root.val and q.val > root.val):
                # p和q同在左子樹
                if p.val < root.val and q.val < root.val:
                    root = root.left
                else:
                    # p和q同在右子樹
                    root = root.right
            else:
                # p和q在不同一邊
                return root

    def lowestCommonAncestor_3(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p == root or q == root:
                return root

            if (p.val > root.val and q.val < root.val) or (p.val < root.val and q.val > root.val):
                return root
            else:
                if p.val < root.val and q.val < root.val:
                    root = root.left
                elif p.val > root.val and q.val > root.val:
                    root = root.right
                else:
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
    solution.lowestCommonAncestor_2(root=root_p, p=node2_p, q=node3_p)
    solution.lowestCommonAncestor_3(root=root_p, p=node2_p, q=node3_p)

