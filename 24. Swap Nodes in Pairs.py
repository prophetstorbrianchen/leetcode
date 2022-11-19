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

    # 是否可以用切割，做reverse，再merge的方式
    def swapPairs_2(self, head: [ListNode]) -> [ListNode]:
        # 1 -> 2 -> 3 -> 4
        # 因為是22一組，所以一定要先區分出這次的pair和下一個pair(nxtPair)
        # 設立dummy來輔助
        # cur做next和next.next時，沒有assign的狀況，連結就不會切斷
        # dummy->1->2->3->4, cur是從head, tail是從dummy開始
        # cur可以先劃分出1->2一組,3->4一組
        # 先針對1->2這組進行反轉 -> 2接到1,1接到3,tail在接到2
        # 更新tail和cur到3->4這組的位置
        # 一直往下走

        dummy = ListNode(0)
        dummy.next = head
        tail, curr = dummy, head

        while curr and curr.next:
            # 劃分位置
            second = curr.next
            nxtPair = curr.next.next

            # 改變位置連接
            second.next = curr # 連結斷了(指向別人)
            curr.next = nxtPair
            tail.next = second

            # 更新位置
            tail = curr
            curr = nxtPair


if __name__ == '__main__':
    solution = Solution()
    build_link_list = build_link_list()
    head = build_link_list.build([1, 2, 3, 4])
    solution.swapPairs(head = head)
