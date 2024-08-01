from typing import Optional, List


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def mergeKSortedLinkedLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0,len(lists),2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(self.merge2SortedLists(list1,list2))
            lists = mergedLists
        return lists[0]


    def merge2SortedLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

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

        return dummy.next

def build_linked_lists(input: List[List[int]]) -> Optional[List[ListNode]]:
    result = []
    for each in input:
        head = ListNode(each[0])
        curr = head
        for i in each:
            curr.next = ListNode(i)
            curr = curr.next
        result.append(head)
    return result

s = Solution()
input = build_linked_lists([[1, 4, 5], [1, 3, 4], [2, 6]])


