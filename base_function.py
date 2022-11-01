class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BuildTree:
    def serialize(self, root):
        def dfs(r, result):
            if not r:
                result.append("N")
                return

            # 我們用的是preorder的模板(中左右)
            result.append(str(r.val))
            dfs(r.left, result)
            dfs(r.right, result)

        res = []
        dfs(root, res)
        return res

    def deserialize(self, data):
        # 因為我們已經完整的使用N來表示所有空的節點，所以不需要使用preorder+inorder來製造tree
        # 運用指標，去往後指list的index
        self.index = 0

        def dfs():
            if data[self.index] == "N":
                self.index = self.index + 1
                return None

            # 這也是preorder的模板(中左右)
            node = TreeNode(data[self.index])
            self.index = self.index + 1

            node.left = dfs()
            node.right = dfs()

            return node

        root = dfs()
        return root