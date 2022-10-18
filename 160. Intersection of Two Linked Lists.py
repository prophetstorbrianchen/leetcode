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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> [ListNode]:
        # a的個數
        tail_a = headA
        count_a = 0
        while tail_a:
            tail_a = tail_a.next
            count_a = count_a + 1

        # b的個數
        tail_b = headB
        count_b = 0
        while tail_b:
            tail_b = tail_b.next
            count_b = count_b + 1

        while headA and headB:
            if count_a > count_b:
                headA = headA.next
                count_a = count_a - 1
            elif count_a < count_b:
                headB = headB.next
                count_b = count_b - 1
            else:
                if headA == headB:
                    return headA
                elif headA.next == headB.next:
                    return headA.next
                else:
                    headA = headA.next
                    headB = headB.next
                    count_a = count_a - 1
                    count_b = count_b - 1
        return None


if __name__ == '__main__':
    solution = Solution()
    buildLinkList = build_link_list()
    a = buildLinkList.build([4,1])
    b = buildLinkList.build([5,6,1])
    c = buildLinkList.build([8,4,5])

    a.next.next = c
    b.next.next.next = c
    solution.getIntersectionNode(headA=a, headB=b)
