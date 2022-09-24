class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: [ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        s = head
        f = head.next

        # 找斷點
        # 快慢指針
        # 我也寫不出來
        while f and f.next:
            s = s.next
            f = f.next.next

        # reverse
        list2 = s.next

        # 要特別注意address會相互影相結果
        prev = s.next = None
        while list2:
            temp = list2.next
            list2.next = prev
            prev = list2
            list2 = temp

        head1 = head
        head2 = prev

        # merge
        # 我完全寫不出來，先理解模仿怎麼做的
        while head2:
            temp1, temp2 = head1.next, head2.next
            head1.next = head2
            head2.next = temp1
            head1, head2 = temp1, temp2

        print(head)


if __name__ == '__main__':
    solution = Solution()
    list_1_node, list_2_node, list_3_node, list_4_node, list_5_node = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    list_1_node.next = list_2_node
    list_2_node.next = list_3_node
    list_3_node.next = list_4_node
    list_4_node.next = list_5_node

    solution.reorderList(head=list_1_node)
