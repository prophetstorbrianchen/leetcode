from base_function import BuildTree
from collections import deque
from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> [int]:
        # 樹轉圖的方法，要記熟
        # 因為是變成圖，所以要記相連的點 -> 父節點，左右子節點
        # 使用DFS建圖
        def build_graph(node, parent):
            if not node:
                return

            if parent:
                if node.val not in self.graph:
                    self.graph[node.val] = []
                self.graph[node.val].append(parent.val)

            if node.left:
                if node.val not in self.graph:
                    self.graph[node.val] = []
                self.graph[node.val].append(node.left.val)
                build_graph(node.left, node)

            if node.right:
                if node.val not in self.graph:
                    self.graph[node.val] = []
                self.graph[node.val].append(node.right.val)
                build_graph(node.right, node)

        # defaultdict(list) -> 這個方法可以學一下，dict帶list
        # self.graph = defaultdict(list)
        self.graph = {}

        # root本來就沒有parent所以給None
        build_graph(root, None)
        res = []
        seen = set()
        queue = deque()

        # 從此點開始為初始點，向外擴張，初始層設為0
        queue.append([target.val, 0])

        # 非常類似BFS
        while len(queue) != 0:
            print(queue)
            # FIFO
            node, level = queue.popleft()
            if node in seen:
                continue
            seen.add(node)
            print(node)

            # 如果找到K那就append
            if level == k:
                res.append(node)
            else:
                # 美往外一層就要+1
                for connected in self.graph[node]:
                    queue.append([connected, level + 1])

        print(res)
        return res


if __name__ == '__main__':
    solution = Solution()
    buildTree = BuildTree()
    #root = buildTree.deserialize([3, 5, 6, "N", "N", 2, 7, "N", "N", 4, "N", "N", 1, 0, "N", "N", 8, "N", "N"])
    node1, node2, node3, node4, node5, node6, node7, node8, node9 = TreeNode(3), TreeNode(5), TreeNode(1), TreeNode(6), TreeNode(2), TreeNode(7), TreeNode(4), TreeNode(0), TreeNode(8)
    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    node5.left, node5.right = node6, node7
    node3.left, node3.right = node8, node9

    solution.distanceK(root=node1, target = node2, k = 2)