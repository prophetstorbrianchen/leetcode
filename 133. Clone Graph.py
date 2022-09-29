# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    # hint
    # 值藥一樣但位址要不同
    # 這題要多看幾次，很特殊的資料結構
    # https://www.youtube.com/embed/mQeF6bN8hMk
    def cloneGraph(self, node: Node) -> Node:
        oldToNew = {}

        def dfs(node):
            # 表示所有的node都已經歷遍，因為都記錄在hash map上
            if node in oldToNew:
                return oldToNew[node]

            # 建立cop node
            copy = Node(node.val)

            # 沒在hash map中，就紀錄
            oldToNew[node] = copy

            # 這用法很不習慣
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None


if __name__ == '__main__':
    solution = Solution()
    node1, node2, node3, node4 = Node(1), Node(2), Node(3), Node(4)
    node1.neighbors.append(node2)
    node1.neighbors.append(node4)

    node2.neighbors.append(node3)
    node2.neighbors.append(node1)

    node3.neighbors.append(node4)
    node3.neighbors.append(node2)

    node4.neighbors.append(node1)
    node4.neighbors.append(node3)

    clone_node = solution.cloneGraph(node = node1)
    print(clone_node)