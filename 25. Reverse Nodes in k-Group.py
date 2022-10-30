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
    # 這題有點複雜要再看過
    # https://www.youtube.com/watch?v=1UOPsfP85V4
    def reverseKGroup(self, head: [ListNode], k: int) -> [ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # reverse group
            # 原本prev是給None去接，但是在目前情況是可以把None換成kth.next
            prev = kth.next
            curr = groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k = k - 1
        return curr



if __name__ == '__main__':
    solution = Solution()
    build_link_list = build_link_list()
    head = build_link_list.build([1, 2, 3, 4, 5])
    solution.reverseKGroup(head=head, k=2)