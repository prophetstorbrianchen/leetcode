from base_function import BuildTree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # hint
    # 這題不能用dfs
    # 要使用bfs + 數學
    def widthOfBinaryTree(self, root: [TreeNode]) -> int:
        #
        def dfs(r, d):
            if not r:
                if d not in res:
                    res[d] = []
                res[d].append("N")
                return

            if d not in res:
                res[d] = []
            res[d].append(r.val)

            dfs(r.left, d + 1)
            dfs(r.right, d + 1)

        res = {}
        depth = 0
        dfs(root, depth)

        max_width = 0
        for item_list in res.values():
            for _ in range(len(item_list)):
                if item_list[-1] == "N":
                    item_list.pop()
                else:
                    break
            max_width = max(max_width, len(item_list))

        return max_width




if __name__ == '__main__':
    solution = Solution()
    buildTree = BuildTree()
    root = buildTree.deserialize([1,3,5,"N","N","N",2,"N","N"])
    solution.widthOfBinaryTree(root= root)

