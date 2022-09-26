class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: [TreeNode]) -> int:
        res = [float("-inf")]

        def dfs(r, result):
            if not r:
                return 0

            # 拿左子數值
            # max是為了防負數，若有負數直接不拿左子數值
            left_val = dfs(r.left, result)
            left_val = max(left_val, 0)

            # 拿右子樹值
            # max是為了防負數，若有負數直接不拿右子數值
            right_val = dfs(r.right, result)
            right_val = max(right_val, 0)

            # 先算本樹的值，更新res
            cur_val = r.val + left_val + right_val
            result[0] = max(result[0], cur_val)

            # 再算要return回去給上層的值
            return r.val + max(left_val, right_val)

        dfs(root, res)
        print(res)
        return int(res[0])


if __name__ == '__main__':
    solution = Solution()
    root_p, node2_p, node3_p, node4_p, node5_p = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
    root_p.left = node2_p
    root_p.right = node3_p
    node3_p.left = node4_p
    node3_p.right = node5_p

    solution.maxPathSum(root = root_p)
