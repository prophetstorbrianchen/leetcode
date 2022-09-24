class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # hint
    # 快慢指針
    # dummy/tail/dummy.next
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        s = head
        f = head

        # f要比s快幾步
        for _ in range(n):
            f = f.next

        # 找出n的那個點，並記錄走幾步
        count = 0
        while f:
            count = count + 1
            s = s.next
            f = f.next

        # dummy的起手式子(模板)
        dummy = ListNode()
        dummy.next = head
        tail = dummy

        # tail向後走幾步
        for _ in range(count):
            tail = tail.next

        # 連在一起就等同於把n拿掉
        tail.next = s.next
        return dummy.next


if __name__ == '__main__':
    solution = Solution()
    list_1_node, list_2_node, list_3_node, list_4_node, list_5_node = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    list_1_node.next = list_2_node
    list_2_node.next = list_3_node
    list_3_node.next = list_4_node
    list_4_node.next = list_5_node

    solution.removeNthFromEnd(head=list_1_node, n=2)