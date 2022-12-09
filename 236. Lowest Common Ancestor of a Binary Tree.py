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

    def lowestCommonAncestor_2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 此題要找最小祖先，會有下列幾種case
        # 1.root即為p or q -> 那p or q即是最小祖先
        # 2.p和q分別在左右子樹 -> p和q的root為共同最小祖先 -> 能在同時找到p和q在不同子樹
        # 3.p和q分別在同一子樹 -> 那就是看p or q誰在上面，在上面的即是最小祖先 -> 只能在一子樹找到p or q，另一子樹為None

        # edge case -> 防空樹
        if not root:
            return root

        if root == p or root == q:
            return root

        left_tree = self.lowestCommonAncestor_2(root.left, p, q)
        right_tree = self.lowestCommonAncestor_2(root.right, p, q)

        if left_tree and right_tree:
            return root
        elif left_tree:
            return left_tree
        else:
            return right_tree

    def lowestCommonAncestor_3(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(r):
            if not r:
                return None

            if r == p or r == q:
                return r

            left = dfs(r.left)
            right = dfs(r.right)

            if left and right:
                return r
            else:
                if left:
                    return left
                else:
                    return right

        return dfs(root)


if __name__ == '__main__':
    solution = Solution()
    buildTree = BuildTree()
    # root = buildTree.deserialize([1,2,"N","N",3,"N","N"])
    # p = buildTree.deserialize([2,"N","N"])
    # q = buildTree.deserialize([3,"N","N"])
    root, p, q = TreeNode(1), TreeNode(2), TreeNode(3)
    root.left = p
    root.right = q
    result = solution.lowestCommonAncestor_3(root= root, p= p, q= q)
    print(result)
