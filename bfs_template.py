# https://www.jianshu.com/p/453c3850a9d2
'''
树的遍历
對於所有node的歷遍，无需分层遍历
'''
from collections import deque
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def level_order_tree(root, result):
    if not root:
        return
    # 这里借助python的双向队列实现队列
    # 避免使用list.pop(0)出站的时间复杂度为O(n)
    queue = deque([root])
    while queue:
        node = queue.popleft()
        # do somethings
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print(result)
    return result

'''
图的遍历
對於所有node的歷遍，无需分层遍历
'''
def bsf_graph(root):
    if not root:
        return
    # queue和seen为一对好基友，同时出现
    queue = deque([root])
    # seen避免图遍历过程中重复访问的情况，导致无法跳出循环
    seen = set([root])
    while queue:
        head = queue.popleft()
        # do somethings with the head node
        # 将head的邻居都添加进来
        for neighbor in head.neighbors:
            if neighbor not in seen:
                queue.append(neighbor)
                seen.add(neighbor)
    return True

'''
树的遍历
對於所有node的歷遍，确定当前遍历到了哪一层
'''
# 最淺的depth
def level_order_tree_1(root):
    if not root:
        return
    q = [root]
    depth = 0
    min_depth = float("inf")
    while q:
        depth = depth + 1
        new_q = []
        for node in q:
            # do somethins with this layer nodes...
            if not node.left and not node.right:
                min_depth = min(min_depth, depth)
            # do somethins with this layer nodes...
            # 判断左右子树
            if node.left:
                new_q.append(node.left)
            if node.right:
                new_q.append(node.right)
        # 记得将旧的队列替换成新的队列
        q = new_q
    # 最后return想要返回的东西
    print(min_depth)
    return min_depth

# 最深的depth
def level_order_tree_2(root):
    if not root:
        return
    q = [root]
    depth = 0
    max_depth = float("-inf")
    while q:
        depth = depth + 1
        new_q = []
        for node in q:
            # do somethins with this layer nodes...
            if not node.left or not node.right:
                max_depth = max(max_depth, depth)
            # do somethins with this layer nodes...
            # 判断左右子树
            if node.left:
                new_q.append(node.left)
            if node.right:
                new_q.append(node.right)
        # 记得将旧的队列替换成新的队列
        q = new_q
    # 最后return想要返回的东西
    print(max_depth)
    return max_depth
'''
图的遍历
對於所有node的歷遍，确定当前遍历到了哪一层
'''
def bsf_graph_1(root):
    if not root:
        return
    queue = [root]
    seen = set([root])
    while queue:
        new_queue = []
        for node in queue:
            # do somethins with the node
            for neighbor in node.neighbors:
                if neighbor not in seen:
                    new_queue.append(neighbor)
                    seen.add(neighbor)
    return True


if __name__ == "__main__":
    tree = TreeNode(4)
    tree.left = TreeNode(9)
    tree.right = TreeNode(0)
    tree.left.left = TreeNode(5)
    tree.left.right = TreeNode(1)

    level_order_tree(tree, [])
    level_order_tree_1(tree)
    level_order_tree_2(tree)