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
    def oddEvenList(self, head: [ListNode]) -> [ListNode]:
        index = 0
        dummy = ListNode()
        tail = dummy
        dummy_l2 = ListNode()
        tail_l2 = dummy_l2

        # 使用index來區分odd or even，並用來create node和連接
        while head:
            if (index % 2) == 0:
                node = ListNode(head.val)
                tail.next = node
                tail = tail.next
            else:
                node = ListNode(head.val)
                tail_l2.next = node
                tail_l2 = tail_l2.next
            index = index + 1
            head = head.next

        tail.next = dummy_l2.next

        return dummy.next


if __name__ == '__main__':
    solution = Solution()
    buildLinkList = build_link_list()
    a = buildLinkList.build([1,2,3,4])

    solution.oddEvenList(head=a)
