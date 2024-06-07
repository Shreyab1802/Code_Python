from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def printAlternateNodes(self, head: Optional[ListNode]) -> List[int]:
        lists = []
        tail = head
        collect = True
        while tail:
            if collect:
                lists.append(tail.val)
            collect = not collect
            tail = tail.next

        return lists

def createLinkedList(vals: List[int]) -> Optional[ListNode]:
        if not vals:
            return None
        head = ListNode(vals[0])
        current = head
        for val in vals[1:]:
            current.next = ListNode(val)
            current = current.next
        return head


s = Solution()
head = createLinkedList([1,2,3,4,5])

print(s.printAlternateNodes(head))


#############Using Recursion################

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def printAlternateNodes(self, head: Optional[ListNode]) -> List[int]:
        def helper(node: Optional[ListNode], collect: bool) -> List[int]:
            if not node:
                return []
            if collect:
                return [node.val] + helper(node.next, not collect)
            else:
                return helper(node.next, not collect)

        return helper(head, True)


def createLinkedList(vals: List[int]) -> Optional[ListNode]:
    if not vals:
        return None
    head = ListNode(vals[0])
    current = head
    for val in vals[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Example usage
s = Solution()
head = createLinkedList([1, 2, 3, 4, 5])
print(s.printAlternateNodes(head))  # Output: [1, 3, 5]
