from base_function import BuildTree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 空tree
        if not root:
            return root

        # 當p為root or q為root時，那p or q必定為root
        if p == root or q == root:
            return root

        # 當找到時，返回上一層
        left_tree = self.lowestCommonAncestor(root.left, p, q)
        right_tree = self.lowestCommonAncestor(root.right, p, q)

        # 當2邊都找到時 -> 分別在左右不同子樹 -> 共同祖先的必定為root
        if left_tree and right_tree:
            return root
        else:
            # 當只有一邊時 -> 那肯定pq都是在同一邊子樹 -> 那就是看哪邊的子樹找到就是哪邊
            if left_tree:
                return left_tree
            else:
                return right_tree


if __name__ == '__main__':
    solution = Solution()
    buildTree = BuildTree()
    # root = buildTree.deserialize([1,2,"N","N",3,"N","N"])
    # p = buildTree.deserialize([2,"N","N"])
    # q = buildTree.deserialize([3,"N","N"])
    root, p, q = TreeNode(1), TreeNode(2), TreeNode(3)
    root.left = p
    root.right = q
    result = solution.lowestCommonAncestor(root= root, p= p, q= q)
    print(result)
