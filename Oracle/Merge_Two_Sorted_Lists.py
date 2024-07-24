# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        if not list1:
            return list2
        if not list2:
            return list1

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            elif list1.val > list2.val:
                list2 = list2.next
                tail.next = list2
            tail = tail.next

        if not list1:
            tail.next = list2

        if not list2:
            tail.next = list1

        return dummy.next