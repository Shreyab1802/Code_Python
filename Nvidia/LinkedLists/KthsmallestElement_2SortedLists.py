from typing import Optional, List


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoSortedLinkedLists(self, list1:Optional[ListNode], list2:Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        curr = head

        if not list1:
            return list2
        if not list2:
            return list1

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if not list2:
            curr.next = list1
        if not list1:
            curr.next = list2

        return head.next

    def kthsmallest(self, node : Optional[ListNode], k :int) -> int:

        n = 0 #node counter
        if not node:
            return None

        curr = node
        while curr:
            n += 1
            if n == k:
                return curr.val

            curr = curr.next

    def build_linked_lists(self, vals: List[int]) -> Optional[ListNode]:
        if not vals:
            return None

        head = ListNode(vals[0])
        curr = head
        for vals in vals[1:]:
            curr.next = ListNode(vals)
            curr = curr.next
        return head


s = Solution()
list1 = s.build_linked_lists([1,2,4])
list2 = s.build_linked_lists([0,3,9])
output = s.mergeTwoSortedLinkedLists(list1, list2)
print(output)
print(s.kthsmallest(output,5))



