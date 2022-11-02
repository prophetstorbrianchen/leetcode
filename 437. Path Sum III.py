from base_function import BuildTree
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # hint
    # 使用combination sum的概念來做
    def pathSum(self, root: [TreeNode], targetSum: int) -> int:
        def dfs(r, target, path):
            # base case
            if not r:
                return

            # 使用差值 -> 直到0才保留
            if target - r.val < 0:
                next_target = target
                next_path = path
            else:
                next_target = target - r.val
                next_path = path + [r.val]

            if next_target == 0:
                res.append(next_path)
                return

            dfs(r.left, next_target, next_path)
            dfs(r.right, next_target, next_path)

        res = []
        dfs(root, targetSum, [])

        print(res)
        return len(res)


if __name__ == '__main__':
    solution = Solution()
    buildTree = BuildTree()
    root = buildTree.deserialize([1,2,"N","N",2,"N","N"])
    solution.pathSum(root= root, targetSum = 8)