class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # hint
    # 工具題，需要非常熟練，必須是反射動作
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        prev = None
        root = head

        while root:
            temp = root.next
            root.next = prev
            prev = root
            root = temp

        return prev


if __name__ == '__main__':
    solution = Solution()
    list_1_node, list_2_node, list_3_node = ListNode(1), ListNode(2), ListNode(3)
    list_1_node.next = list_2_node
    list_2_node.next = list_3_node

    solution.reverseList(head=list_1_node)
