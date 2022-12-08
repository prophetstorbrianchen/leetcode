class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # hint
    # 快慢指針
    # dummy/tail/dummy.next
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        s = head
        f = head

        # f要比s快幾步
        for _ in range(n):
            f = f.next

        # 找出n的那個點，並記錄走幾步
        count = 0
        while f:
            count = count + 1
            s = s.next
            f = f.next

        # dummy的起手式子(模板)
        dummy = ListNode()
        dummy.next = head
        tail = dummy

        # tail向後走幾步
        for _ in range(count):
            tail = tail.next

        # 連在一起就等同於把n拿掉
        tail.next = s.next
        return dummy.next

    def removeNthFromEnd_2(self, head: [ListNode], n: int) -> [ListNode]:
        s = head
        f = head

        for _ in range(n):
            f = f.next

        count = 0
        # **注意while條件，因為前面f的設定並沒有f = head.next這樣的設定，這邊都是一次跳一步而已**
        while f:
            s = s.next
            f = f.next
            count = count + 1

        # 設定dummy，記得起手式
        dummy = ListNode()
        dummy.next = head
        tail = dummy

        for _ in range(count):
            tail = tail.next

        # s的next就是我們要的
        tail.next = s.next

        return dummy.next

    def removeNthFromEnd_3(self, head: [ListNode], n: int) -> [ListNode]:
        # 此方法跟上面不同，不過使用快慢指針應該才是對的
        # 看總長多長
        # 使用扣的，算出要停在哪邊

        f = head
        count = 0
        while f:
            count = count + 1
            f = f.next

        # **link list的題目使用dummy可以避免不必要的麻煩***
        dummy = ListNode()
        dummy.next = head
        tail = dummy
        for _ in range(count - n):
            tail = tail.next

        tail.next = tail.next.next

        # print(head)
        return dummy.next


if __name__ == '__main__':
    solution = Solution()
    list_1_node, list_2_node, list_3_node, list_4_node, list_5_node = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    list_1_node.next = list_2_node
    list_2_node.next = list_3_node
    list_3_node.next = list_4_node
    list_4_node.next = list_5_node

    #solution.removeNthFromEnd(head=list_1_node, n=2)
    #solution.removeNthFromEnd_2(head=list_1_node, n=2)
    solution.removeNthFromEnd_3(head=list_1_node, n=5)