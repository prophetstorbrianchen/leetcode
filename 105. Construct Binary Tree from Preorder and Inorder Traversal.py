class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # hint
    def buildTree(self, preorder: [int], inorder: [int]) -> [TreeNode]:
        if not preorder or not inorder:
            return None

        # 用preorder決定順序
        root = TreeNode(preorder[0])

        # 用inorder決定左右子樹
        inorder_index = inorder.index(preorder[0])

        # 決定出preoder,inorder各自的左右子樹
        inorder_left = inorder[:inorder_index]
        inorder_right = inorder[inorder_index + 1:]

        # method 1 -> 直接用長度來推導
        preorder_left = preorder[1:len(inorder_left) + 1]
        preorder_right = preorder[len(inorder_right) * -1:]

        # method ->  因為inorder_index和preorder的長度一樣，所以可以使用inorder的root來判斷preorder的各自左右子樹list
        # preorder_left = preorder[1:inorder_index + 1]
        # preorder_right = preorder[inorder_index + 1:]

        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root

    def buildTree_2(self, preorder: [int], inorder: [int]) -> [TreeNode]:
        if not preorder and not inorder:
            return None

        val = preorder[0]
        root = TreeNode(val)
        root_inorder_index = inorder.index(val)

        left_preorder = preorder[1: root_inorder_index + 1]
        right_preorder = preorder[1 + root_inorder_index:]
        left_inorder = inorder[:root_inorder_index]
        right_inorder = inorder[root_inorder_index + 1:]

        root.left = self.buildTree_2(left_preorder, left_inorder)
        root.right = self.buildTree_2(right_preorder, right_inorder)

        return root


if __name__ == '__main__':
    solution = Solution()
    solution.buildTree_2(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])