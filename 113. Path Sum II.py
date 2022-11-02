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
    def pathSum(self, root: [TreeNode], targetSum: int) -> [[int]]:
        def dfs(r, target, path):
            # base case
            if not r:
                return

            # 使用差值 -> 直到0才保留
            next_target = target - r.val
            next_path = path + [r.val]

            # 記住一定要from root to leaf，所以必須要有not r.left and not r.right的條件
            if next_target == 0 and not r.left and not r.right:
                res.append(next_path)
                return

            # 這個為另一種case -> [1,2] 找target=1時，這題的答案是[](原因如上)。 但我這個答案會是1 -> 因為是只要有符合target的結果我就紀錄
            # 但這種寫法別題會用到，在此記一下
            """
            if next_target == 0:
                res.append(next_path)
                return
            """

            dfs(r.left, next_target, next_path)
            dfs(r.right, next_target, next_path)

        res = []
        dfs(root, targetSum, [])

        print(res)
        return res


if __name__ == '__main__':
    solution = Solution()
    buildTree = BuildTree()
    root = buildTree.deserialize([1,2,"N","N",2,"N","N"])
    solution.pathSum(root= root, targetSum= 3)