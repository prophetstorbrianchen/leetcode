import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: [TreeNode]) -> [[int]]:
        def dfs(r, d, res):
            if not r:
                return

            if d not in res:
                res[d] = []

            res[d].append(r.val)

            dfs(r.left, d + 1, res)
            dfs(r.right, d + 1, res)

            return

        # edge case
        if not root:
            return []

        # 使用dict去紀錄list
        res = {}
        depth = 0
        dfs(root, depth, res)

        # 把dict的東西loop出來
        result = []
        for d, node_list in res.items():
            result.append(node_list)

        print(result)
        return result

    def levelOrder_2(self, root: [TreeNode]) -> [[int]]:
        def dfs(r, d, res_dict):
            if not r:
                return

            if d not in res_dict:
                res_dict[d] = []

            res_dict[d].append(r.val)
            dfs(r.left, d + 1, res_dict)
            dfs(r.right, d + 1, res_dict)

        # edge case
        if root is None:
            return []

        res = {}
        dfs(root, 0, res)

        result = []
        for _, depth_list in res.items():
            result.append(depth_list)

        return result

    def levelOrder_dfs(self, root: [TreeNode]) -> [[int]]:
        def dfs(r, d):
            if not r:
                return

            val = r.val
            hash_dict[d].append(val)

            dfs(r.left, d + 1)
            dfs(r.right, d + 1)

        hash_dict = collections.defaultdict(list)
        depth = 0
        dfs(root, depth)
        # print(list(hash_dict.values()))
        return list(hash_dict.values())

    def levelOrder_bfs(self, root: [TreeNode]) -> [[int]]:
        q = collections.deque()
        q.append(root)

        result = []
        while q:
            new_q = []
            tmp = []
            for node in q:
                q.popleft()
                tmp.append(node.val)

                if node.left:
                    new_q.append(node.left)

                if node.right:
                    new_q.append(node.right)

            result.append(tmp)
            q = new_q
        # print(result)
        return result


if __name__ == '__main__':
    solution = Solution()
    root_p, node2_p, node3_p, node4_p, node5_p = TreeNode(3), TreeNode(9), TreeNode(20), TreeNode(15), TreeNode(7)
    root_p.left = node2_p
    root_p.right = node3_p
    node3_p.left = node4_p
    node3_p.right = node5_p

    # solution.levelOrder(root = root_p)
    # solution.levelOrder_2(root=root_p)
    # solution.levelOrder_dfs(root=root_p)
    solution.levelOrder_bfs(root=root_p)
