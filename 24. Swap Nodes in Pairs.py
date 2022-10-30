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
    # 多看幾次，看筆記
    # https://www.youtube.com/watch?v=o811TZLAWOo
    def swapPairs(self, head: [ListNode]) -> [ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head

        while curr and curr.next:
            # save ptrs
            nxtPair = curr.next.next
            second = curr.next

            # reverse this pair
            second.next = curr
            curr.next = nxtPair
            prev.next = second

            # update ptrs
            prev = curr
            curr = nxtPair

        return dummy.next


if __name__ == '__main__':
    solution = Solution()
    build_link_list = build_link_list()
    head = build_link_list.build([1, 2, 3, 4])
    solution.swapPairs(head = head)
