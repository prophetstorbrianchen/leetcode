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
    def sortList(self, head: [ListNode]) -> [ListNode]:
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next

        sorted_val_list = sorted(val_list)
        buildLinkList = build_link_list()
        sorted_head = buildLinkList.build(sorted_val_list)

        return sorted_head

    # hint
    # 這題完全是工具題，一定要熟練
    # 可以看筆記
    # https://www.youtube.com/watch?v=TGveA1oFhrc
    def sortList_2(self, head: [ListNode]) -> [ListNode]:
        if not head or not head.next:
            return head

        # 切割list
        left = head
        # 如何從中間切斷 -> 這也是工具題
        right = self.getmid(left)
        tmp = right.next

        # 截斷之後，left會從原本整個head的list變成到right之前 -> 重要的技巧
        right.next = None
        right = tmp

        # 使用recursive一直分割下去
        left = self.sortList_2(left)
        right = self.sortList_2(right)
        # 如何合併 -> 這也是工具提
        return self.merged(left, right)

    def getmid(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merged(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next

    def sortList_3(self, head: [ListNode]) -> [ListNode]:
        # **因為是遞迴，所以要有base case**
        if not head or not head.next:
            return head

        left = head
        right = self.getmid_3(left)

        tmp = right.next
        # **當right.next = None時，已經切分出left和right**
        right.next = None
        right = tmp

        # 繼續切left和right
        self.sortList_3(left)
        self.sortList_3(right)

        # 合併
        return self.merged_3(left, right)

    def getmid_3(self, head):
        # **一定要熟練**
        s = head
        f = head.next
        while f and f.next:
            s = s.next
            f = f.next.next

        return s

    def merged_3(self, list1, list2):
        # **一定要熟練**
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next


if __name__ == '__main__':
    solution = Solution()
    buildLinkList = build_link_list()
    head = buildLinkList.build([4,2,1,3])

    solution.sortList_3(head = head)