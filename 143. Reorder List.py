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

    def reorderList_2(self, head: [ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # **f起始要比s快一步**
        s = head
        f = head.next

        # **f一次走2步s一次走一步，注意while的條件**
        while f and f.next:
            s = s.next
            f = f.next.next

        # **設定list2來做reverse**
        list2 = s.next

        # **須得到list1，是使用s1.next = none -> 這樣head就會是前半段，再assign給list1，list1 = head**
        s.next = None

        # **對list2做reverse -> 工具必會**
        prev = None
        while list2:
            tmp = list2.next
            list2.next = prev
            prev = list2
            list2 = tmp

        # **對head1和head2做merge，我這邊使用dummy，比較簡單一些**
        head1 = head
        head2 = prev

        dummy = ListNode()
        tail = dummy

        # **先接head1的一個node再接head2的一個node -> 工具**
        while head1 and head2:
            tail.next = head1
            head1 = head1.next
            tail = tail.next

            tail.next = head2
            head2 = head2.next
            tail = tail.next

        if head1:
            tail.next = head1
        else:
            tail.next = head2

        # print(dummy.next)
        head = dummy.next

    def reorderList_3(self, head: [ListNode]) -> None:
        # 切中間
        # 後半部reverse
        # merge

        # --mid--
        s = head
        f = head.next
        while f and f.next:
            s = s.next
            f = f.next.next

        # head 分成前後2段
        list2 = s.next
        s.next = None
        list1 = head

        # --針對list2做reverse -> prev為reverse的結果--
        prev = None

        while list2:
            temp = list2.next
            list2.next = prev
            prev = list2
            list2 = temp

        reverse_list2 = prev

        # --做merge--
        dummy = ListNode()
        tail = dummy

        while list1 and reverse_list2:
            tail.next = list1
            list1 = list1.next
            tail = tail.next

            tail.next = reverse_list2
            reverse_list2 = reverse_list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = reverse_list2

        print(dummy.next)
        head = dummy.next


if __name__ == '__main__':
    solution = Solution()
    list_1_node, list_2_node, list_3_node, list_4_node, list_5_node = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    list_1_node.next = list_2_node
    list_2_node.next = list_3_node
    list_3_node.next = list_4_node
    list_4_node.next = list_5_node

    solution.reorderList(head=list_1_node)
    solution.reorderList_2(head=list_1_node)
    solution.reorderList_3(head=list_1_node)
