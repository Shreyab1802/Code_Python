from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sortedLists = []
        mergedLinkedLists = ListNode()
        head = mergedLinkedLists

        for each in lists:
            while each is not None:
                sortedLists.append(each.val)
                each = each.next

        for each in sorted(sortedLists):
            head.next = ListNode(each)
            head = head.next

        return mergedLinkedLists.next

    def kth_smallest(self, head: Optional[ListNode], k: int) -> int:
        n = 0
        cur = head
        while cur:
            n += 1
            if n == k:
                return cur.val
            cur = cur.next
        return -1  # Return -1 or raise an exception if k is out of bounds


# Helper function to convert a list of lists into a list of ListNode objects
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
merged_head = s.mergeKLists(linked_lists)
k = 4  # Example k value
print(s.kth_smallest(merged_head, k))  # Output the k-th smallest element
