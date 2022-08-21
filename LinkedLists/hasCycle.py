# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# we will keep two pointers one is slow and the other one is fast,
# if any time they meet that means that linkedlists has cycle

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False