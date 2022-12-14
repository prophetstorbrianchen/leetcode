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
    def reverseBetween(self, head: [ListNode], left: int, right: int) -> [ListNode]:
        dummy = ListNode()
        dummy.next = head

        # right list
        right_node = head
        for _ in range(right - 1):
            right_node = right_node.next

        # 區分出(左+中)、右
        new_right_node = right_node.next
        right_node.next = None

        # 一定要用dummy去做，不然會無法處理left為1的情況
        middle_node = dummy
        for _ in range(left - 1):
            middle_node = middle_node.next

        # 區分出左、中
        new_middle_node = middle_node.next
        middle_node.next = None

        # middle list reverse
        prev = None
        while new_middle_node:
            tmp = new_middle_node.next
            new_middle_node.next = prev
            prev = new_middle_node
            new_middle_node = tmp

        # middle list -> right list
        # 中連接右
        pointer = prev
        while pointer:
            if pointer.next is None:
                pointer.next = new_right_node
                break
            pointer = pointer.next

        # left list
        # left list -> middle list -> right list
        # 左連接中
        new_left_node = dummy
        header_pointer = new_left_node
        while header_pointer:
            if header_pointer.next is None:
                if prev:
                    header_pointer.next = prev
                else:
                    header_pointer.next = new_right_node
                break
            header_pointer = header_pointer.next

        return dummy.next









    def reverseBetween_2(self, head: [ListNode], left: int, right: int) -> [ListNode]:
        # **基本工具題**
        def reverse(list):
            prev = None
            while list:
                tmp = list.next
                list.next = prev
                prev = list
                list = tmp

            return prev

        # **基本工具題**
        def merge(list1, list2):
            tail = list1
            while tail:
                if tail.next is None:
                    break
                else:
                    tail = tail.next

            tail.next = list2

        s = head
        for _ in range(right - 1):
            s = s.next

        # 切出(左+中)和右
        tmp = s.next
        s.next = None
        right = tmp

        dummy = ListNode()
        dummy.next = head
        tail = dummy

        # 切出(左+中)
        for _ in range(left - 1):
            tail = tail.next

        tmp = tail.next
        tail.next = None
        mid = tmp
        # **要熟練這個地方 -> 防left = 1**
        left = dummy

        # reverse
        reverse_mid = reverse(mid)

        # merge
        merge(left, reverse_mid)
        merge(left, right)

        print(dummy)
        return dummy.next





if __name__ == '__main__':
    solution = Solution()
    buildLinkList = build_link_list()
    # a = buildLinkList.build([3, 5])
    a = buildLinkList.build([1, 2, 3, 4, 5])

    solution.reverseBetween_2(head = a, left = 2, right = 4)
