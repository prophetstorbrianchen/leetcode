class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # hint
    # 不是很好理解，需要多看幾次筆記
    # 工具題
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        dummy = ListNode()
        # 因為這邊是看address, tail所移動的路徑，其實就是dummy的整個list結果
        tail = dummy

        # 其中一個到底就要停止
        # 不太會merge，先理解模仿怎麼寫的
        while list1 or list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            # 往後接
            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next


if __name__ == '__main__':
    solution = Solution()
    list1_1_node, list1_2_node, list1_3_node = ListNode(1), ListNode(2), ListNode(4)
    list1_1_node.next = list1_2_node
    list1_2_node.next = list1_3_node

    list2_1_node, list2_2_node, list2_3_node = ListNode(1), ListNode(3), ListNode(4)
    list2_1_node.next = list2_2_node
    list2_2_node.next = list2_3_node

    solution.mergeTwoLists(list1=list1_1_node, list2=list2_1_node)
