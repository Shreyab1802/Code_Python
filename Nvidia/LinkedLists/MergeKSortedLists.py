# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
        return sortedKLists.next