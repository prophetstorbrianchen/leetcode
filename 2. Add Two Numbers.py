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










    def addTwoNumbers_2(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        # 這種bit的加法核心概念 -> 餘數和carry位
        # 因為link list的特性 -> 要防長短不一
        # 因為link list的特性 -> 當原本link list一樣長時，但有carry位 -> 產生新的一個位數
        # 每次位數加總完的結果，都會產生一個node來串接，形成新的一個list

        dummy = ListNode()
        tail = dummy

        carry = 0
        # while判斷加carry -> 當只有多carry位時的情況
        while l1 or l2 or carry:
            # 防長短不一
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0

            # 開始做加法
            new_val = (val_1 + val_2 + carry) % 10
            carry = (val_1 + val_2 + carry) // 10
            node = ListNode(new_val)
            tail.next = node

            # 更新位址，大家都向後進一位
            # 必須要防長短不一
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            tail = tail.next

        return dummy.next


if __name__ == '__main__':
    solution = Solution()
    build_link_list = build_link_list()
    l1 = build_link_list.build([2, 4, 3])
    l2 = build_link_list.build([5, 6, 4])
    solution.addTwoNumbers(l1 = l1, l2 = l2)