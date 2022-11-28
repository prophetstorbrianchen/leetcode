class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class build_link_list:
    def build(self, lists: [[int]]) -> [ListNode]:
        dummy = ListNode()
        tail = dummy

        for n in lists:
            node = ListNode(n)
            tail.next = node
            tail = tail.next

        return dummy.next


class Solution:
    def deleteDuplicates(self, head: [ListNode]) -> [ListNode]:
        # find the duplicate node
        # connect to the next
        # list is in the range [0, 300]

        dummy = ListNode()
        dummy.next = head
        tail = head

        while tail and tail.next:
            if tail.val == tail.next.val:
                tail.next = tail.next.next
            else:
                tail = tail.next

        return dummy.next


if __name__ == '__main__':
    solution = Solution()
    build_link_list = build_link_list()
    l1 = build_link_list.build([0,0,0,0,0])
    solution.deleteDuplicates(head = l1)