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
    def rotateRight(self, head: [ListNode], k: int) -> [ListNode]:
        # method 1 -> 可以這樣解，但會TLE，因為用到2個loop
        """
        if not head or not head.next:
            return head

        for _ in range(k):
            s = head
            f = head.next

            while f and f.next:
                s = s.next
                f = f.next

            new_node = s.next
            s.next = None
            new_node.next = head
            head = new_node

        return head
        """
        # method 2 -> 用餘數來解，我寫太醜
        # edge case
        if not head or not head.next:
            return head

        # method 2 -> 使用餘數來解
        # 先算head總長
        p = head
        count = 0
        while p:
            p = p.next
            count = count + 1

        # 得到總數 if count = 3, k = 4 -> 走到最後一位
        # 因為到著算，所以count要先扣，才會正著算
        new_k = count - (k % count)

        s = head
        # 因為會過頭，要new_k - 1
        for _ in range(new_k - 1):
            s = s.next

        new_node = s.next
        s.next = None

        # 如果s走到底 -> k是能夠被%成0 -> 不會有任何rotate
        if not new_node:
            return head

        # 要把new_node的指針指到最後面
        t = new_node
        while new_node:
            if not t.next:
                break
            else:
                t = t.next

        # 合併，連接起來
        t.next = head

        print(new_node)
        return new_node


if __name__ == '__main__':
    solution = Solution()
    build_link_list = build_link_list()
    head = build_link_list.build([1,2,3,4,5])
    solution.rotateRight(head = head, k = 0)