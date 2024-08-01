from typing import Optional, List


class ListNode:
    def __init__(self, value =0, next = None):
        self.val = value
        self.next = next

class Solution:

    def merge2sortedLinkedLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1

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
        if not list1:
            tail.next = list2
        if not list2:
            tail.next = list1

        ## Print
        curr = dummy.next
        while curr:
            print(curr.val)
            curr = curr.next
        ######

        return dummy.next

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
input1 = s.build_linked_lists([1, 2, 4])
input2 = s.build_linked_lists([0, 3, 9])

print(s.merge2sortedLinkedLists(input1,input2))