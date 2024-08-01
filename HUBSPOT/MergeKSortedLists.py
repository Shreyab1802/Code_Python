from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        sortedKLists = ListNode()
        head = sortedKLists

        for each in lists:
            while each is not None:
                nodes.append(each.val)
                each = each.next

        for each in sorted(nodes):
            head.next = ListNode(each)
            head = head.next

        curr = sortedKLists.next
        #Print
        while curr:
            print(curr.val)
            curr = curr.next

        return sortedKLists.next


def build_linked_lists(lists: List[List[int]]) -> List[Optional[ListNode]]:
    result = []
    for lst in lists:
        dummy = ListNode()
        current = dummy
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        result.append(dummy.next)
    return result


s = Solution()
linked_lists = build_linked_lists([[1, 4, 5], [1, 3, 4], [2, 6]])
s.mergeKLists(linked_lists)