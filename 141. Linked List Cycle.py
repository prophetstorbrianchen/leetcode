class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # hint
    # 要注意while迴圈是要用and而非or
    def hasCycle(self, head: [ListNode]) -> bool:
        s = head
        f = head

        # 如果head不是一個迴圈 -> 就會跑出來 -> return False
        # 如果head是一個迴圈 -> s和f必定相交 -> return True
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                print(True)
                return True

        print(False)
        return False


if __name__ == '__main__':
    solution = Solution()
    list_1_node, list_2_node, list_3_node, list_4_node = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
    list_1_node.next = list_2_node
    list_2_node.next = list_3_node
    list_3_node.next = list_4_node
    list_4_node.next = list_2_node

    solution.hasCycle(head=list_1_node)