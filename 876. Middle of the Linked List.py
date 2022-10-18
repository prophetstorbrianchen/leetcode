class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class build_link_list:
    def build(self, lists: [int]) -> [ListNode]:
        dummy = ListNode()
        tail = dummy

        for n in lists:
            node = ListNode(n)
            tail.next = node
            tail = tail.next

        return dummy.next


class Solution:
    # hint
    # 工具題，必著眼睛都要會
    # 可以看筆記
    def middleNode(self, head: [ListNode]) -> [ListNode]:

        print(len(head))
        s = head
        f = head.next

        dummy = ListNode()
        tail = dummy

        while f and f.next:
            s = s.next
            f = f.next.next

        if f:
            tail.next = s.next
        else:
            tail.next = s

        return dummy.next


if __name__ == '__main__':
    solution = Solution()
    buildLinkList = build_link_list()
    head = buildLinkList.build([1, 2, 3, 4, 5])
    solution.middleNode(head=head)
