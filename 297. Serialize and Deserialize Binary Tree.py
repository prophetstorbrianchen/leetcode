class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 這個版本的為string版本
class Codec:
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
        # print(res)
        string_result = ",".join(res)
        return string_result

    def deserialize(self, data):
        # 因為我們已經完整的使用N來表示所有空的節點，所以不需要使用preorder+inorder來製造tree
        # 運用指標，去往後指list的index
        self.index = 0

        def dfs():
            if root_list[self.index] == "N":
                self.index = self.index + 1
                return None

            # 這也是preorder的模板(中左右)
            node = TreeNode(root_list[self.index])
            self.index = self.index + 1

            node.left = dfs()
            node.right = dfs()

            return node

        # 先轉成list
        root_list = data.split(",")
        root = dfs()
        return root

    def serialize_2(self, root):
        def dfs(r):
            if not r:
                res.append("N")
                return

            # 使用preorder來排序
            res.append(str(r.val))
            dfs(r.left)
            dfs(r.right)

        res = []
        dfs(root)

        # **這個技巧很容易忘記**
        string = ",".join(res)
        print(string)
        return string

    def deserialize_2(self, data):
        # 使用index向右進的方式，去組成tree
        def dfs():
            if self.data_list[self.i] == "N":
                self.i = self.i + 1
                return None

            root = TreeNode(self.data_list[self.i])
            self.i = self.i + 1
            root.left = dfs()
            root.right = dfs()

            return root

        # 先解掉string改成list
        self.data_list = data.split(",")
        self.i = 0

        return dfs()


# 這個版本的為list版本,可以用在任何Tree的題目，以方便建tree
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


if __name__ == '__main__':
    root_p, node2_p, node3_p, node4_p, node5_p, node6_p = TreeNode(5), TreeNode(3), TreeNode(6), TreeNode(2), TreeNode(4), TreeNode(1)
    root_p.left = node2_p
    root_p.right = node3_p
    node2_p.left = node4_p
    node2_p.right = node5_p
    node4_p.left = node6_p

    ser = Codec()
    root_string = ser.serialize(root_p)
    root = ser.deserialize(root_string)
    root_string = ser.serialize_2(root_p)
    root = ser.deserialize(root_string)
