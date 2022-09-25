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
    # https://www.youtube.com/watch?v=q5a5OiGbT6Q
    def mergeKLists(self, lists: [[ListNode]]) -> [ListNode]:
        # method 1
        # 答案正確，但是TLE
        """
        def merged_fun(list1, list2):
            if list1 and list2:
                pass
            else:
                if list1:
                    return list1
                elif list2:
                    return list2
                else:
                    return None

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

        if not lists:
            return None

        merged_list = None
        for item in lists:
            merged_list = merged_fun(merged_list, item)

        return merged_list
        """
        # method 2
        def mergeList(l1, l2):
            dummy = ListNode()
            tail = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            if l1:
                tail.next = l1
            if l2:
                tail.next = l2
            return dummy.next

        if not lists or len(lists) == 0:
            return None

        # 這個技巧要學會,這個技巧很重要
        # 為實現22 merge的方法
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # 注意bound的條件
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(mergeList(l1, l2))
            # 重新把22merge後的結果在assign給lists
            lists = mergedLists
        return lists[0]


if __name__ == '__main__':
    solution = Solution()
    buildLinkList = build_link_list()
    head1 = buildLinkList.build([1, 4, 5])
    head2 = buildLinkList.build([1, 3, 4])
    head3 = buildLinkList.build([2, 6])

    solution.mergeKLists(lists=[head1, head2, head3])