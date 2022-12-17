import collections

from base_function import BuildTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # hint
    # BFS -> 對的
    # DFS -> 目前是錯的，還需要再改 -> [1,2,2,2,null,2]
    def isSymmetric(self, root: [TreeNode]) -> bool:
        # dfs -> 分成左右子樹 -> 建出list
        def dfs(r, p):
            if not r:
                p.append("N")
                return

            dfs(r.left, p)
            val = r.val
            p.append(val)
            dfs(r.right, p)


        # root的左子樹
        if not root:
            return True
        else:
            if not root.left and not root.right:
                return True
            elif not root.left and root.right:
                return False
            elif root.left and not root.right:
                return False
            else:
                left_tree = root.left
                right_tree = root.right

                left_res = []
                right_res = []

                dfs(left_tree, left_res)
                dfs(right_tree, right_res)

                # 其中一個reverse就可以了
                right_res.reverse()

                if left_res == right_res:
                    print(True)
                    return True
                else:
                    print(False)
                    return False

    def isSymmetric_bfs(self, root: [TreeNode]) -> bool:
        q = collections.deque()

        # root的左子樹
        if not root:
            return True
        else:
            if not root.left and not root.right:
                return True
            elif not root.left and root.right:
                return False
            elif root.left and not root.right:
                return False
            else:
                q.append(root)

                while q:
                    tmp_q = []
                    left_res = []
                    right_res = []
                    for node in q:
                        if node.left:
                            # 看每一層的孩子的list，有就寫val，沒有就寫N
                            # 而tmp_q不append "N"
                            left_res.append(node.left.val)
                            tmp_q.append(node.left)
                        else:
                            left_res.append("N")

                        if node.right:
                            right_res.append(node.right.val)
                            tmp_q.append(node.right)
                        else:
                            right_res.append("N")

                    right_res.reverse()

                    # 當左柚子樹每層都互為reverse -> 表示就是symmetric tree
                    if left_res != right_res:
                        print(False)
                        return False

                    q = tmp_q

                print(True)
                return True


if __name__ == '__main__':
    solution = Solution()
    buildTree = BuildTree()
    root = buildTree.deserialize([1, 2, 3, "N", "N", 4, "N", "N",  2, 4, "N", "N", 3, "N", "N"])

    solution.isSymmetric_bfs(root = root)
