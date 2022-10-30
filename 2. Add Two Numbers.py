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
    # hint
    # https://www.youtube.com/watch?v=wgFPrzTjm7s
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        dummy = ListNode()
        tail = dummy

        # 進位
        carry = 0

        # while 加了 carry 是因為 edge case: 8 + 7
        while l1 or l2 or carry:
            # --防l1, l2長短不一--
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # --new digit--
            val = v1 + v2 + carry
            # ex: val = 15 -> carry = 1, val = 5
            carry = val // 10
            val = val % 10
            # 建新node
            new_node = ListNode(val)
            tail.next = new_node

            # --update tail, l1 and l2--
            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


if __name__ == '__main__':
    solution = Solution()
    build_link_list = build_link_list()
    l1 = build_link_list.build([2, 4, 3])
    l2 = build_link_list.build([5, 6, 4])
    solution.addTwoNumbers(l1 = l1, l2 = l2)