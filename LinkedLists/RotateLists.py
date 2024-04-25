# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return head

        length_LinkedList, tail = 1, head

        while tail.next:
            tail = tail.next
            length_LinkedList += 1
        print(length_LinkedList)

        k = k % length_LinkedList
        if k == 0:
            return head
        print(k)

        current = head
        for i in range(length_LinkedList - k - 1):
            current = current.next

        new_pos = current.next
        current.next = None
        tail.next = head

        return new_pos
