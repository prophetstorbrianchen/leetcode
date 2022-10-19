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
        # right list
        right_node = head
        for _ in range(right - 1):
            right_node = right_node.next

        new_right_node = right_node.next
        right_node.next = None

        # middle list
        middle_node = head
        for _ in range(left - 2):
            middle_node = middle_node.next

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
        pointer = prev
        while pointer:
            if pointer.next is None:
                pointer.next = new_right_node
                break
            pointer = pointer.next

        # left list
        # left list -> middle list -> right list
        new_left_node = head
        header_pointer = new_left_node
        while header_pointer:
            if header_pointer.next is None:
                if prev:
                    header_pointer.next = prev
                else:
                    header_pointer.next = new_right_node
                break
            header_pointer = header_pointer.next

        return head


if __name__ == '__main__':
    solution = Solution()
    buildLinkList = build_link_list()
    a = buildLinkList.build([1,2,3,4,5])

    solution.reverseBetween(head = a, left = 1, right = 5)
