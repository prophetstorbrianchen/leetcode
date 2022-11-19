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
        # dfs -> 不能用
        """
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
        """
        # bfs
        # 每個node都有編號，這個編號是full binary tree
        q = [(root, 1)]
        max_width = 0
        while q:
            max_width = max(max_width, q[-1][1] - q[0][1] + 1)
            new_q = []
            for node, pos in q:
                # 判断左右子树
                if node.left:
                    # 到下一層時，左邊的node編號*2
                    new_q.append((node.left, pos * 2))
                if node.right:
                    # 到下一層時，右邊的node編號*2 + 1
                    new_q.append((node.right, pos * 2 + 1))

            # 记得将旧的队列替换成新的队列
            q = new_q
        # 最后return想要返回的东西
        print(max_width)
        return max_width









    def widthOfBinaryTree_2(self, root: [TreeNode]) -> int:
        # 因為這題要用滿樹去看才會知道最大的寬度 -> BFS + Math
        # 假設root編號為1
        # 左leaf -> 2 -> (1*2), 右leaf -> 2 -> (1*2 + 1)
        # 寬度為同一queue中，最後面的編號扣掉最前面的編號 -> q[-1][1] - q[0][1]

        q = [(root, 1)]
        max_width = 0
        while q:
            max_width = max(max_width, q[-1][1] - q[0][1] + 1)
            new_q = []
            for node, index in q:
                # left tree
                if node.left:
                    new_q.append((node.left, index * 2))

                # right tree
                if node.right:
                    new_q.append((node.right, index * 2 + 1))

            q = new_q

        print(max_width)
        return max_width


if __name__ == '__main__':
    solution = Solution()
    buildTree = BuildTree()
    root = buildTree.deserialize([1,3,5,"N","N","N",2,"N","N"])
    solution.widthOfBinaryTree(root= root)

